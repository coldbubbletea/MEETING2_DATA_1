#!/usr/bin/env python3
"""Reapply the handoff taxonomy to representatives in repositories with >100 stars."""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

import pyarrow.parquet as pq

from skill_domain_stars import OTHER, TAXONOMY, classify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, required=True, help="Pinned Parquet data directory")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repos = {}
    for path in sorted((args.data / "repos").glob("*.parquet")):
        for row in pq.read_table(path, columns=["full_name", "stars", "description"]).to_pylist():
            if row["full_name"] in repos:
                raise ValueError(f"Duplicate repository: {row['full_name']}")
            repos[row["full_name"]] = row
    counts, basis, groups = Counter(), Counter(), Counter()
    for path in sorted((args.data / "artifacts").glob("*.parquet")):
        parquet = pq.ParquetFile(path)
        for batch in parquet.iter_batches(columns=["dedup_primary", "repo_full_name", "name", "description"]):
            for row in batch.to_pylist():
                if row["dedup_primary"] != 1:
                    continue
                repo = repos.get(row["repo_full_name"], {})
                stars = repo.get("stars")
                group = "unknown" if stars is None else "gt100" if stars > 100 else "le100"
                groups[group] += 1
                if group == "gt100":
                    index, source = classify(row["name"] or "", row["description"] or "", repo.get("description") or "")
                    counts[TAXONOMY[index][0] if index >= 0 else OTHER] += 1
                    basis[source] += 1
    if sum(groups.values()) != 1877981 or groups["gt100"] != 128382 or groups["unknown"] != 787:
        raise ValueError(f"Counts differ from the pinned handoff: {dict(groups)}")
    if sum(counts.values()) != groups["gt100"]:
        raise ValueError("Domain counts do not match selected representatives")
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "skill_domains_gt100.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["domain", "distinct_skills", "share_selected"])
        writer.writeheader()
        for domain, count in counts.most_common():
            writer.writerow({"domain": domain, "distinct_skills": count, "share_selected": count / groups["gt100"]})
    summary = {
        "revision": "ebab17454a7c236f8f26b183567f1a126f42e3f8",
        "selection": "dedup_primary == 1 AND representative repository stars > 100",
        "groups": dict(groups),
        "basis_counts": dict(basis),
        "taxonomy": "skill_domain_stars.py; unchanged",
        "validation": "No independent audit of the selected subset; whole-corpus audit is not subset accuracy",
    }
    (args.output / "skill_domains_gt100_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
