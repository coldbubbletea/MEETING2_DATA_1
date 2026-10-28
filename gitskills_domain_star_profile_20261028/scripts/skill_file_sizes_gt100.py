#!/usr/bin/env python3
"""File sizes of GitSkills skills whose repository has more than 100 stars.

A skill is one distinct SKILL.md content, represented by its representative copy.
Its files are the SKILL.md itself plus every file in the same folder, recursively,
as listed in artifact_siblings (entry_type == "file").

Selections:
  A (primary): the representative's repository has more than 100 stars.
  B (alternate): any copy of the content lives in a repository with more than 100 stars.

Totals:
  per_skill_sum: sum of each skill's own folder. A folder that contains other skills
                 counts their files again.
  union:         each (repository, path) is counted once across the selected skills.
Folders with composition_truncated = 1 may be incomplete, so their totals are lower bounds.
Skills with composition_fetched = 0 have no folder listing; only their SKILL.md is counted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import multiprocessing as mp
import posixpath
import random
import statistics
from collections import defaultdict, namedtuple
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

WORKSPACE = Path(__file__).resolve().parents[1]
DATA = WORKSPACE / "data"
OUTPUT = WORKSPACE / "output"
THRESHOLD = 100

BIG: set[str] = set()
B_SHAS: set[str] = set()
CAND_KEYS: set[tuple[str, str]] = set()
Rec = namedtuple("Rec", "repo path sha n_bytes blob_ok len_ok content_sha_ok cf ct sc sb in_big")
BANDS = [("101-999", 101, 1000), ("1000-9999", 1000, 10000), (">=10000", 10000, float("inf"))]


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()


def pct(values: list, q: float):
    return values[min(len(values) - 1, round(q * (len(values) - 1)))]


def load_stars() -> dict:
    rows = pq.read_table(DATA / "repos" / "part-00000.parquet", columns=["full_name", "stars"]).to_pylist()
    stars = {row["full_name"]: row["stars"] for row in rows}
    assert len(stars) == len(rows), "duplicate repository names"
    return stars


def scan_big_repo_shas(path: str) -> set[str]:
    table = pq.read_table(path, columns=["repo_full_name", "file_sha"])
    mask = pc.is_in(table["repo_full_name"], value_set=pa.array(sorted(BIG)))
    return set(table.filter(mask)["file_sha"].to_pylist())


def scan_representatives(path: str) -> tuple[dict, list]:
    table = pq.read_table(path, columns=[
        "repo_full_name", "path", "file_sha", "dedup_primary", "content", "content_sha_ok",
        "composition_fetched", "composition_truncated", "sibling_count", "sibling_bytes",
    ])
    table = table.filter(pc.equal(table["dedup_primary"], 1))
    lengths = pc.binary_length(table["content"].cast(pa.binary())).to_pylist()
    ctx = defaultdict(int)
    ctx["representatives"] = table.num_rows
    for n, cf, ct, sb in zip(lengths, table["composition_fetched"].to_pylist(),
                             table["composition_truncated"].to_pylist(), table["sibling_bytes"].to_pylist()):
        if n is None:
            ctx["content_missing"] += 1
        else:
            ctx["skill_md_bytes"] += n
        if cf == 1:
            ctx["folder_bytes_recorded"] += sb or 0
            ctx["composition_truncated"] += int(ct == 1)
        else:
            ctx["composition_unfetched"] += 1

    mask = pc.is_in(table["file_sha"], value_set=pa.array(sorted(B_SHAS)))
    cand = table.filter(mask)
    cand_lengths = pc.binary_length(cand["content"].cast(pa.binary())).to_pylist()
    records = []
    rows = zip(cand["repo_full_name"].to_pylist(), cand["path"].to_pylist(), cand["file_sha"].to_pylist(),
               cand["content"].to_pylist(), cand["content_sha_ok"].to_pylist(),
               cand["composition_fetched"].to_pylist(), cand["composition_truncated"].to_pylist(),
               cand["sibling_count"].to_pylist(), cand["sibling_bytes"].to_pylist(), cand_lengths)
    for repo, p, sha, content, cok, cf, ct, sc, sb, arrow_len in rows:
        if content is None:
            n_bytes, blob_ok, len_ok = None, False, True
        else:
            data = content.encode("utf-8")
            n_bytes, blob_ok, len_ok = len(data), blob_sha1(data) == sha, len(data) == arrow_len
        records.append(Rec(repo, p, sha, n_bytes, blob_ok, len_ok, cok, cf, ct, sc, sb, repo in BIG))
    return dict(ctx), records


def scan_sibling_files(path: str) -> dict:
    table = pq.read_table(path, columns=["repo_full_name", "artifact_path", "entry_name", "entry_type", "entry_size"])
    table = table.filter(pc.equal(table["entry_type"], "file"))
    found: dict = defaultdict(list)
    for repo, p, name, size in zip(table["repo_full_name"].to_pylist(), table["artifact_path"].to_pylist(),
                                   table["entry_name"].to_pylist(), table["entry_size"].to_pylist()):
        if (repo, p) in CAND_KEYS:
            found[(repo, p)].append((name, size))
    return dict(found)


def check_sibling_sizes(path: str, sample: int, seed: int = 20261029) -> dict:
    table = pq.read_table(path, columns=["entry_type", "entry_name", "entry_size", "entry_sha", "content"])
    table = table.filter(pc.and_(pc.equal(table["entry_type"], "file"), pc.is_valid(table["content"])))
    picks = sorted(random.Random(seed).sample(range(table.num_rows), min(sample, table.num_rows)))
    rows = table.take(pa.array(picks)).to_pylist()
    size_ok = blob_ok = 0
    for row in rows:
        data = row["content"].encode("utf-8")
        size_ok += int(len(data) == row["entry_size"])
        blob_ok += int(blob_sha1(data) == row["entry_sha"])
    return {"file": Path(path).name, "sampled": len(rows),
            "size_matches_content": size_ok, "blob_sha_matches_content": blob_ok}


def folder_entries(rec: Rec, sibs: dict) -> tuple[dict, int]:
    folder = posixpath.dirname(rec.path)
    entries: dict[str, int] = {}
    conflicts = 0
    if rec.n_bytes is not None:
        entries[rec.path] = rec.n_bytes
    for name, size in sibs.get((rec.repo, rec.path), ()):
        full = posixpath.join(folder, name) if folder else name
        if full in entries:
            conflicts += int(entries[full] != (size or 0))
            continue
        entries[full] = size or 0
    return entries, conflicts


def summarise(label: str, recs: list, sibs: dict, stars: dict):
    union: dict[tuple[str, str], int] = {}
    union_conflicts = folder_conflicts = 0
    per_skill = []
    by_status: dict = defaultdict(lambda: {"skills": 0, "per_skill_bytes": 0, "files": 0})
    fetched_table = fetched_recorded = skill_md_unverified = 0
    for rec in recs:
        entries, conflicts = folder_entries(rec, sibs)
        folder_conflicts += conflicts
        for full, size in entries.items():
            key = (rec.repo, full)
            if key in union:
                union_conflicts += int(union[key] != size)
            else:
                union[key] = size
        total = sum(entries.values())
        status = ("composition_unfetched" if rec.cf != 1
                  else "composition_truncated" if rec.ct == 1 else "composition_complete")
        bucket = by_status[status]
        bucket["skills"] += 1
        bucket["per_skill_bytes"] += total
        bucket["files"] += len(entries)
        skill_md_unverified += int(rec.n_bytes is not None and not rec.blob_ok)
        if rec.cf == 1:
            fetched_table += total
            fetched_recorded += (rec.n_bytes or 0) + (rec.sb or 0)
        per_skill.append((rec.repo, rec.path, total, len(entries), status, stars.get(rec.repo)))

    totals = sorted(row[2] for row in per_skill)
    per_skill_sum = sum(totals)
    union_bytes = sum(union.values())
    summary = {
        "selection": label,
        "skills": len(recs),
        "skill_md_bytes": sum(rec.n_bytes or 0 for rec in recs),
        "skill_md_blob_unverified": skill_md_unverified,
        "per_skill_sum_bytes": per_skill_sum,
        "union_files": len(union),
        "union_bytes": union_bytes,
        "nested_overlap_bytes": per_skill_sum - union_bytes,
        "fetched_skills_table_bytes": fetched_table,
        "fetched_skills_recorded_bytes": fetched_recorded,
        "folder_conflicts": folder_conflicts,
        "union_conflicts": union_conflicts,
        "per_skill_median_bytes": statistics.median(totals) if totals else None,
        "per_skill_p90_bytes": pct(totals, 0.90) if totals else None,
        "per_skill_p99_bytes": pct(totals, 0.99) if totals else None,
        "per_skill_max_bytes": totals[-1] if totals else None,
        "by_status": {k: dict(v) for k, v in sorted(by_status.items())},
    }
    top = sorted(per_skill, key=lambda row: -row[2])[:20]
    return summary, top, per_skill


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--sample", type=int, default=5000)
    args = parser.parse_args()
    OUTPUT.mkdir(exist_ok=True)

    stars = load_stars()
    BIG.update(k for k, v in stars.items() if v is not None and v > THRESHOLD)
    art_files = [str(p) for p in sorted((DATA / "artifacts").glob("*.parquet"))]
    sib_files = [str(p) for p in sorted((DATA / "artifact_siblings").glob("*.parquet"))]
    pool_ctx = mp.get_context("fork")

    with pool_ctx.Pool(args.workers) as pool:
        for shas in pool.imap_unordered(scan_big_repo_shas, art_files):
            B_SHAS.update(shas)

    context: dict = defaultdict(int)
    recs: list[Rec] = []
    with pool_ctx.Pool(args.workers) as pool:
        for part_ctx, part_recs in pool.imap_unordered(scan_representatives, art_files):
            for key, value in part_ctx.items():
                context[key] += value
            recs.extend(part_recs)
    CAND_KEYS.update((r.repo, r.path) for r in recs)

    sibs: dict = {}
    with pool_ctx.Pool(args.workers) as pool:
        for part in pool.imap_unordered(scan_sibling_files, sib_files):
            for key, value in part.items():
                sibs.setdefault(key, []).extend(value)

    sample_check = check_sibling_sizes(sib_files[0], args.sample)
    a_recs = [r for r in recs if r.in_big]
    summary_a, top_a, rows_a = summarise("A_representative_repo_gt100", a_recs, sibs, stars)
    summary_b, _, _ = summarise("B_any_copy_gt100", recs, sibs, stars)

    band_rows = []
    for label, low, high in BANDS:
        selected = [row for row in rows_a if row[5] is not None and low <= row[5] < high]
        band_rows.append({
            "band_stars": label,
            "skills": len(selected),
            "per_skill_bytes": sum(row[2] for row in selected),
            "files": sum(row[3] for row in selected),
        })

    integrity = {
        "big_repositories": len(BIG),
        "b_shas": len(B_SHAS),
        "candidate_representatives": len(recs),
        "a_skills": len(a_recs),
        "candidate_length_mismatch": sum(not r.len_ok for r in recs),
        "candidate_content_missing": sum(r.n_bytes is None for r in recs),
        "sibling_sample_check": sample_check,
        "all_representatives": dict(context),
    }
    result = {"threshold_stars": THRESHOLD, "integrity": integrity,
              "A": summary_a, "B": summary_b, "A_bands": band_rows}
    (OUTPUT / "skill_file_sizes_gt100_summary.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (OUTPUT / "skill_file_sizes_gt100_top20.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["repo", "path", "bytes", "files", "status", "repo_stars"])
        for repo, path, total, files, status, repo_stars in top_a:
            writer.writerow([repo, path, total, files, status, "" if repo_stars is None else repo_stars])
    print(json.dumps(result, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
