#!/usr/bin/env python3
"""Classify the natural-language prose of the fixed >100-star representatives."""

import argparse
import csv
import gzip
import json
import multiprocessing as mp
import re
from collections import Counter
from functools import lru_cache
from importlib.metadata import version
from pathlib import Path

import pyarrow.compute as pc
import pyarrow.parquet as pq
from lingua import Language, LanguageDetectorBuilder


REVISION = "ebab17454a7c236f8f26b183567f1a126f42e3f8"
CATEGORIES = ("english", "chinese", "mixed", "other", "unknown")
MIN_LETTERS = 40
MIXED_SHARE = 0.20
ENGLISH_FUNCTION_WORDS = frozenset(
    "a an the and or to of in for with that this these those you your is are be as by from when if then not".split()
)
DETECTOR = None
STARS = {}


def prose_only(content):
    lines = content.replace("\r\n", "\n").splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() in ("---", "...")), None)
        if end is not None:
            lines = lines[end + 1:]
    prose = []
    fence = None
    for line in lines:
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None or line.startswith("    ") or line.startswith("\t"):
            continue
        if re.match(r"^\s*\[[^\]]+\]:\s*\S+", line):
            continue
        line = re.sub(r"`+[^`]*`+", " ", line)
        line = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
        line = re.sub(r"https?://\S+|<[^>]+>", " ", line)
        line = re.sub(r"(?<!\w)(?:[\w.-]+/)+[\w./-]+", " ", line)
        prose.append(line)
    return "\n".join(prose).strip()


def detector():
    global DETECTOR
    if DETECTOR is None:
        DETECTOR = (
            LanguageDetectorBuilder.from_all_languages()
            .with_low_accuracy_mode()
            .with_minimum_relative_distance(0.15)
            .build()
        )
    return DETECTOR


@lru_cache(maxsize=1024)
def classify_prose(text):
    letters = sum(char.isalpha() for char in text)
    if letters < MIN_LETTERS:
        return "unknown", (), letters
    weights = Counter()
    english_prose_words = 0
    for segment in detector().detect_multiple_languages_of(text):
        segment_text = text[segment.start_index:segment.end_index]
        weight = sum(char.isalpha() for char in segment_text)
        weights[segment.language.name.lower()] += weight
        if segment.language == Language.ENGLISH:
            english_prose_words += sum(
                word in ENGLISH_FUNCTION_WORDS for word in re.findall(r"[a-z]+", segment_text.lower())
            )
    recognised = sum(weights.values())
    if not recognised:
        return "unknown", (), letters
    english = weights["english"]
    chinese = weights["chinese"]
    if (
        english >= MIN_LETTERS
        and chinese >= MIN_LETTERS
        and english / letters >= MIXED_SHARE
        and chinese / letters >= MIXED_SHARE
        and (english + chinese) / letters >= 0.80
        and english_prose_words >= 3
    ):
        category = "mixed"
    else:
        language = detector().detect_language_of(text)
        category = (
            "unknown" if language is None
            else "english" if language == Language.ENGLISH
            else "chinese" if language == Language.CHINESE
            else "other"
        )
    return category, tuple(sorted(weights.items())), letters


def init_worker(stars):
    global STARS
    STARS = stars


def analyse_file(path):
    rows = []
    for batch in pq.ParquetFile(path).iter_batches(
        batch_size=256,
        columns=["dedup_primary", "repo_full_name", "path", "file_sha", "content", "content_fetched"],
    ):
        selected = batch.filter(pc.equal(batch.column("dedup_primary"), 1))
        for row in selected.to_pylist():
            stars = STARS.get(row["repo_full_name"])
            if stars is None or stars <= 100:
                continue
            if row["content_fetched"] != 1 or not isinstance(row["content"], str):
                raise ValueError(f"Selected content is unavailable: {row['repo_full_name']}:{row['path']}")
            category, weights, letters = classify_prose(prose_only(row["content"]))
            rows.append({
                "repo_full_name": row["repo_full_name"],
                "path": row["path"],
                "file_sha": row["file_sha"],
                "category": category,
                "prose_letters": letters,
                "language_letters": json.dumps(dict(weights), sort_keys=True),
            })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=6)
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    if version("lingua-language-detector") != "2.1.1":
        raise ValueError("Use the pinned requirements-language.txt for reproducible classification")
    stars = {}
    for path in sorted((args.data / "repos").glob("*.parquet")):
        for row in pq.read_table(path, columns=["full_name", "stars"]).to_pylist():
            if row["full_name"] in stars:
                raise ValueError(f"Duplicate repository: {row['full_name']}")
            stars[row["full_name"]] = row["stars"]
    paths = sorted((args.data / "artifacts").glob("*.parquet"))
    if not paths or len(stars) != 282200:
        raise ValueError("Input does not match the fixed GitSkills snapshot")
    rows = []
    with mp.Pool(args.workers, initializer=init_worker, initargs=(stars,)) as pool:
        for index, result in enumerate(pool.imap(analyse_file, paths), 1):
            rows.extend(result)
            print(f"{index}/{len(paths)} partitions; {len(rows)} selected Skills", flush=True)
    write_results(rows, args.output)


def write_results(rows, output):
    if len(rows) != 128382 or len({row["file_sha"] for row in rows}) != 128382:
        raise ValueError("Selected representatives differ from the fixed 128382-content cohort")
    rows.sort(key=lambda row: (row["repo_full_name"], row["path"]))
    counts = Counter(row["category"] for row in rows)
    summary = {
        "revision": REVISION,
        "selection": "dedup_primary == 1 AND representative repository stars > 100",
        "total": len(rows),
        "counts": {category: counts[category] for category in CATEGORIES},
        "method": {
            "detector": "lingua-language-detector",
            "version": "2.1.1",
            "mode": "all languages; low accuracy; minimum relative distance 0.15",
            "input": "SKILL.md prose, excluding front matter, code blocks, inline code, URLs and paths",
            "minimum_prose_letters": MIN_LETTERS,
            "mixed": "English and Chinese each >=40 letters and >=20% of all prose letters; combined >=80%; at least 3 English function words in English-detected spans",
            "english_function_words": sorted(ENGLISH_FUNCTION_WORDS),
            "other": "A detected dominant language other than English or Chinese",
            "unknown": "Too little prose or no confident dominant language; remains in denominator",
        },
        "limitations": [
            "Automatic text classification, not an independent human language audit.",
            "Language refers to SKILL.md prose, not repository programming language or bundled files.",
            "Quoted examples and multilingual instructions can affect automatic labels.",
        ],
    }
    output.mkdir(parents=True, exist_ok=True)
    with gzip.open(output / "skill_languages_gt100_items.csv.gz", "wt", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    with (output / "skill_languages_gt100.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["category", "skills", "share_selected"])
        writer.writeheader()
        for category in CATEGORIES:
            writer.writerow({"category": category, "skills": counts[category], "share_selected": counts[category] / len(rows)})
    (output / "skill_languages_gt100_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
