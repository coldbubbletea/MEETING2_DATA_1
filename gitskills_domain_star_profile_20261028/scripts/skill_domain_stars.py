#!/usr/bin/env python3
"""Domain and star-count profile of the GitSkills SKILL.md representatives.

Each distinct content (dedup_primary == 1) is labelled by a keyword taxonomy
over its name (weight 2) and description (weight 1). If neither matches, the
repository description is used with weight 1. Stars are those of the
representative's repository.
"""

from __future__ import annotations

import argparse
import csv
import json
import multiprocessing as mp
import random
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

WORKSPACE = Path(__file__).resolve().parents[1]
DATA = WORKSPACE / "data"
OUTPUT = WORKSPACE / "output"
OTHER = "其他/未归类"
REPOS: dict[str, dict] = {}

# Earlier entries win ties, so more specific domains come first.
TAXONOMY: list[tuple[str, str]] = [
    ("安全与审计", r"security|vulnerab\w*|pentest\w*|penetration test\w*|owasp|exploit\w*|malware|threat model\w*|\bcves?\b|\bctf\b|forensic\w*|intrusion|secret scan\w*|credentials?|\bxss\b|\bcsrf\b|sql injection|reverse engineering|incident response|安全|漏洞|渗透"),
    ("测试与QA", r"\btest(?:s|ing|ed)?\b|\btdd\b|\bbdd\b|\bqa\b|quality assurance|coverage|\be2e\b|end-to-end|unit tests?|integration tests?|pytest|jest|vitest|mocha|cypress|playwright|junit|xunit|\bpest\b|phpunit|\bmocks?\b|fixtures?|regression|测试"),
    ("代码审查与质量", r"\breview\w*|\blint\w*|refactor\w*|code quality|code smells?|critique|static analysis|code health|clean code|technical debt|code style|formatting|代码审查|代码质量|重构"),
    ("前端与UI", r"front-?end|\breact\w*|\bvue\w*|angular\w*|svelte\w*|next\.?js|\bnuxt\b|tailwind\w*|\bcss\b|\bhtml\b|\bui\b|\bux\b|components?|landing pages?|web ?pages?|responsive|shadcn|storybook|accessibility|\ba11y\b|\bdom\b|\bjsx\b|\btsx\b|前端|界面|组件"),
    ("后端与API", r"back-?end|\bapis?\b|\brest(?:ful)?\b|graphql|endpoints?|microservices?|\bexpress\b|fastapi|django|\bflask\b|\bspring\w*|nestjs|\bgrpc\b|webhooks?|middleware|后端|接口"),
    ("数据库与数据工程", r"databases?|\bsql\w*|postgres\w*|\bmysql\b|sqlite|mongo\w*|\bredis\b|nosql|\borm\b|database schemas?|\betl\b|data pipelines?|\bspark\b|\bdbt\b|data warehouses?|bigquery|snowflake|bigtable|dynamodb|supabase|firebase|db migrations?|query optimi\w*|数据库|数据仓库"),
    ("数据分析与可视化", r"data analy\w*|data science|data scientists?|analytics|statistic\w*|\bpandas\b|\bnumpy\b|dataframes?|visuali[sz]\w*|\bcharts?\b|dashboards?|\bkpis?\b|\bcsv\b|jupyter|notebooks?|exploratory|数据分析|可视化|统计"),
    ("AI与机器学习", r"machine learning|deep learning|neural net\w*|\bpytorch\b|tensorflow|\bkeras\b|scikit\w*|\btransformers?\b|\bllms?\b|large language models?|\brag\b|embeddings?|vector (?:database|db|store|search)|fine-?tun\w*|prompt engineering|prompt (?:design|writing|optimi[sz]\w*|templates?)|hugging ?face|\bopenai\b|\banthropic\b|claude api|langchain|llamaindex|model training|diffusion model\w*|\bevals?\b|大模型|机器学习|深度学习"),
    ("Agent与Skill工具链", r"agent[ -]skills?|skills?[ -](?:creator|authoring|builder|manager|writer|loader|development)|(?:create|write|build|edit|improve|author)[ -](?:a[ -]|an[ -]|new[ -]|the[ -])?skills?|claude code|claude\.md|agents\.md|\bcodex\b|cursor (?:rules?|ide|editor)|windsurf|copilot|\bmcp\b|model context protocol|claude plugins?|plugin manifests?|slash commands?|subagents?|sub-agents?|agent orchestrat\w*|multi-agent|agentic|\bgsd\b|get shit done|智能体|技能"),
    ("DevOps与云", r"devops|\bdocker\w*|kubernetes|\bk8s\b|\bhelm\b|terraform|ansible|\bci/cd\b|\bcicd\b|github actions|\bdeploy\w*|\bcloud\b|\baws\b|\bazure\b|\bgcp\b|google cloud|serverless|\blambda\b|cloudflare|vercel|netlify|\bnginx\b|\blinux\b|infrastructure|observability|monitoring|prometheus|grafana|networking|network (?:configuration|protocols?|engineering|troubleshooting)|\bdns\b|\bvpn\b|firewalls?|\bradius\b|\bwi-?fi\b|sysadmin|system administration|部署|云"),
    ("文档与办公", r"documentation|\bdocs?\b|\breadme\b|changelog|release notes?|\bpdfs?\b|\bdocx\b|word documents?|\bpptx\b|powerpoint|slides?|presentations?|\bexcel\b|\bxlsx\b|spreadsheets?|\boffice\b|\bmarkdown\b|\blatex\b|google docs|confluence|\bnotion\b|文档|表格|幻灯片|演示文稿"),
    ("写作与营销", r"writing|\bwriters?\b|\bblogs?\b|\barticles?\b|copywriting|copywriter|copy editing|content (?:creation|marketing|strategy)|newsletters?|social media|\bseo\b|marketing|brand voice|linkedin|twitter|\btweets?\b|email campaigns?|storytelling|editorial|translation|localization|写作|营销|文案"),
    ("软件架构与规划", r"architect\w*|system design|software design|\bplans?\b|planning|roadmaps?|\bspecs?\b|specifications?|requirements?|\bprds?\b|product (?:management|requirements|strategy|discovery)|brainstorm\w*|decision records?|\badrs?\b|estimation|task breakdown|\bbacklogs?\b|\bepics?\b|user stories|project management|需求|架构|规划|计划"),
    ("设计与多媒体", r"\bdesign\w*|figma|\bimages?\b|\bphotos?\b|illustrations?|\blogos?\b|\bsvg\b|\bcanvas\b|animations?|\bvideos?\b|ffmpeg|\baudio\b|\bmusic\b|\b3d\b|blender|three\.?js|graphics?|posters?|\bicons?\b|\bfonts?\b|diagrams?|mermaid|设计|图片|图像|视频|音频|动画"),
    ("版本控制与协作", r"\bgit\b|github|gitlab|\bcommits?\b|\bbranch(?:es|ing)?\b|\bmerges?\b|worktrees?|rebase|pull requests?|\bprs?\b|\bissues?\b|triage|\bjira\b|\blinear\b|kanban|\bsprints?\b|\bslack\b|\bdiscord\b|collaborat\w*|版本控制|协作"),
    ("游戏", r"\bgames?\b|gaming|\bunity\b|unreal|godot|pygame|minecraft|roblox|game dev\w*|游戏"),
    ("编程语言与框架", r"\bpython\b|typescript|javascript|node\.js|\brust\b|golang|\bgo (?:language|lang|code|best)|\bjava\b|kotlin|\bswift(?:ui)?\b|dotnet|\.net\b|\bc#|csharp|\bphp\b|laravel|\bruby\b|\brails\b|\bscala\b|elixir|c\+\+|\bflutter\b|react native|\bexpo\b|\bios\b|\bandroid\b|\bmobile\b|移动端|安卓|编程语言"),
    ("法律与合规", r"\blegal\b|\blaw\b|\blaws\b|lawyers?|attorney|regulat\w*|compliance|\bgdpr\b|\bhipaa\b|contract (?:drafting|review|law)|litigation|statutes?|\bcourts?\b|patents?|trademarks?|\bprivacy\b|\bsox\b|\bkyc\b|\baml\b|法律|合规|合同|法规"),
    ("金融与会计", r"finance|financial|accounting|accountants?|\btax(?:es|ation)?\b|\binvoices?\b|bookkeeping|\bbanking\b|stock market|stock trading|trading|investment\w*|crypto\w*|blockchain|\bpayments?\b|stripe|budgets?|insurance|revenue|财务|会计|金融|税"),
    ("医疗健康", r"medical|medicine|clinical|\bhealth\b|healthcare|patients?|pharma\w*|diagnos\w*|nursing|nutrition|fitness|wellness|therap\w*|医疗|健康|患者"),
    ("教育与培训", r"education\w*|teach\w*|teachers?|students?|courses?|lessons?|curriculum|quiz\w*|tutor\w*|\bexams?\b|assessments?|training|onboarding|classroom|教育|教学|学生|课程"),
    ("科研与学术", r"research\w*|\bpapers?\b|academic\w*|scientific|\bscience\b|literature review|\barxiv\b|citations?|bibliograph\w*|journals?|hypothes\w*|bioinformatics|chemistr\w*|physics|biology|mathematic\w*|\bmath\b|theorem\w*|科研|论文|学术"),
    ("商业与电商", r"e-?commerce|shopify|woocommerce|\bcrm\b|\berp\b|\bsales\b|customer (?:support|service|success)|helpdesk|\bhr\b|recruit\w*|hiring|resumes?|real estate|restaurants?|hotels?|logistics|supply chain|marketplace|电商|销售|客户|招聘"),
    ("个人效率与生活", r"\btodos?\b|calendars?|\bemails?\b|\binbox\b|\bnotes?\b|obsidian|journal\w*|\bdiary\b|habits?|personal|recipes?|cooking|meal\w*|shopping|reminders?|\bmeetings?\b|productivity|travel|itinerar\w*|旅行|日程|笔记|个人"),
    ("自动化与爬虫", r"automation|automate\w*|\bscrap\w*|\bcrawl\w*|browser automation|puppeteer|selenium|\brpa\b|zapier|\bn8n\b|\bcron\b|scheduled tasks?|workflow automation|自动化|爬虫"),
]

GROUP_RE = re.compile(
    "|".join(f"(?P<g{i}>(?:{pattern}))" for i, (_, pattern) in enumerate(TAXONOMY))
)


def add_scores(text: str, weight: int, totals: dict[int, int]) -> None:
    matched: dict[int, set[str]] = defaultdict(set)
    for match in GROUP_RE.finditer(text):
        matched[int(match.lastgroup[1:])].add(match.group(0))
    for index, words in matched.items():
        totals[index] = totals.get(index, 0) + weight * len(words)


def best_domain(totals: dict[int, int]) -> int | None:
    if not totals:
        return None
    return max(totals, key=lambda i: (totals[i], -i))


def classify(name: str, description: str, repo_description: str) -> tuple[int, str]:
    totals: dict[int, int] = {}
    add_scores(name.lower(), 2, totals)
    add_scores(description.lower(), 1, totals)
    index = best_domain(totals)
    if index is not None:
        return index, "skill_text"
    fallback: dict[int, int] = {}
    add_scores(repo_description.lower(), 1, fallback)
    index = best_domain(fallback)
    if index is not None:
        return index, "repo_description"
    return -1, "none"


def classify_shard(path: str) -> list[tuple]:
    table = pq.read_table(
        path, columns=["repo_full_name", "name", "description", "file_sha", "dedup_primary"]
    )
    table = table.filter(pc.equal(table["dedup_primary"], 1))
    rows = []
    for repo, name, description, sha in zip(
        table["repo_full_name"].to_pylist(),
        table["name"].to_pylist(),
        table["description"].to_pylist(),
        table["file_sha"].to_pylist(),
    ):
        name = name or ""
        description = description or ""
        repo_description = REPOS.get(repo, {}).get("description") or ""
        index, basis = classify(name, description, repo_description)
        rows.append((sha, repo, index, basis, name[:120], " ".join(description[:200].split())))
    return rows


def pct(values: list, q: float):
    if not values:
        return None
    return values[min(len(values) - 1, round(q * (len(values) - 1)))]


def share(count: int, total: int) -> float:
    return round(count / total, 4) if total else 0.0


def star_profile(sorted_stars: list[int]) -> dict:
    n = len(sorted_stars)
    return {
        "n": n,
        "median": statistics.median(sorted_stars) if n else None,
        "p75": pct(sorted_stars, 0.75),
        "p90": pct(sorted_stars, 0.90),
        "p99": pct(sorted_stars, 0.99),
        "max": sorted_stars[-1] if n else None,
        "zero_share": share(sum(1 for s in sorted_stars if s == 0), n),
        "share_ge_10": share(sum(1 for s in sorted_stars if s >= 10), n),
        "share_ge_100": share(sum(1 for s in sorted_stars if s >= 100), n),
        "share_ge_1000": share(sum(1 for s in sorted_stars if s >= 1000), n),
        "share_ge_10000": share(sum(1 for s in sorted_stars if s >= 10000), n),
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--sample", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20261028)
    args = parser.parse_args()
    OUTPUT.mkdir(exist_ok=True)

    repo_table = pa.concat_tables(
        [
            pq.read_table(path, columns=["full_name", "owner", "stars", "forks", "is_fork", "description"])
            for path in sorted((DATA / "repos").glob("*.parquet"))
        ]
    )
    REPOS.update({row["full_name"]: row for row in repo_table.to_pylist()})

    artifact_files = sorted((DATA / "artifacts").glob("*.parquet"))
    occurrences = pa.concat_tables(
        [pq.read_table(path, columns=["file_sha", "repo_full_name"]) for path in artifact_files]
    )
    total_occurrences = occurrences.num_rows
    sha_occurrences = Counter(occurrences["file_sha"].to_pylist())
    repo_occurrences = Counter(occurrences["repo_full_name"].to_pylist())
    del occurrences

    with mp.get_context("fork").Pool(args.workers) as pool:
        reps = [row for part in pool.map(classify_shard, [str(p) for p in artifact_files]) for row in part]

    labels = [name for name, _ in TAXONOMY] + [OTHER]
    by_domain = {label: {"stars": [], "skills": 0, "unknown_stars": 0, "occ": 0, "repos": set(), "top": (-1, "")}
                 for label in labels}
    basis_counts: Counter = Counter()
    repo_skill_counts: Counter = Counter()
    repo_domains: dict[str, Counter] = defaultdict(Counter)
    all_skill_stars: list[int] = []
    unknown_skill_stars = 0
    for sha, repo, index, basis, _, _ in reps:
        label = TAXONOMY[index][0] if index >= 0 else OTHER
        stars = REPOS.get(repo, {}).get("stars")
        entry = by_domain[label]
        entry["skills"] += 1
        entry["occ"] += sha_occurrences.get(sha, 0)
        entry["repos"].add(repo)
        basis_counts[basis] += 1
        repo_skill_counts[repo] += 1
        repo_domains[repo][label] += 1
        if stars is None:
            entry["unknown_stars"] += 1
            unknown_skill_stars += 1
            continue
        entry["stars"].append(stars)
        all_skill_stars.append(stars)
        if stars > entry["top"][0]:
            entry["top"] = (stars, repo)

    n_skills = len(reps)
    domain_rows = []
    for label in labels:
        entry = by_domain[label]
        if entry["skills"] == 0:
            continue
        stars = sorted(entry["stars"])
        n = len(stars)
        top_stars, top_repo = entry["top"]
        profile = star_profile(stars)
        domain_rows.append({
            "domain": label,
            "distinct_skills": entry["skills"],
            "share_skills": share(entry["skills"], n_skills),
            "occurrences": entry["occ"],
            "share_occurrences": share(entry["occ"], total_occurrences),
            "distinct_repos": len(entry["repos"]),
            "skills_with_known_stars": n,
            "unknown_star_skills": entry["unknown_stars"],
            "median_stars": profile["median"],
            "mean_stars": round(sum(stars) / n, 1) if n else None,
            "p90_stars": profile["p90"],
            "p99_stars": profile["p99"],
            "max_stars": profile["max"],
            "zero_star_share": profile["zero_share"],
            "share_ge_100": profile["share_ge_100"],
            "share_ge_1000": profile["share_ge_1000"],
            "top_repo": top_repo,
            "top_repo_stars": top_stars if top_stars >= 0 else None,
        })
    domain_rows.sort(key=lambda row: -row["distinct_skills"])

    def repo_row(name: str) -> dict:
        meta = REPOS.get(name, {})
        dominant = repo_domains[name].most_common(1)
        return {
            "repo": name,
            "stars": meta.get("stars"),
            "forks": meta.get("forks") or 0,
            "is_fork": meta.get("is_fork") or 0,
            "owner": meta.get("owner") or "",
            "occurrences": repo_occurrences.get(name, 0),
            "distinct_skills": repo_skill_counts.get(name, 0),
            "top_domain": dominant[0][0] if dominant else "",
        }

    top_by_stars = [repo_row(r) for r in sorted(
        repo_occurrences, key=lambda r: -((REPOS.get(r, {}).get("stars") or 0))
    )[:50]]
    top_by_skills = [repo_row(r) for r, _ in repo_skill_counts.most_common(30)]
    repo_star_values = sorted(
        REPOS[r]["stars"] for r in repo_occurrences if REPOS.get(r, {}).get("stars") is not None
    )
    unknown_star_repos = sum(1 for r in repo_occurrences if REPOS.get(r, {}).get("stars") is None)
    skills_in_top10 = sum(count for _, count in repo_skill_counts.most_common(10))
    repos_with_10_plus = sum(1 for count in repo_skill_counts.values() if count >= 10)

    summary = {
        "source": "GitSkills artifacts + repos, revision ebab17454a7c236f8f26b183567f1a126f42e3f8",
        "occurrences": total_occurrences,
        "distinct_skills": n_skills,
        "repositories_with_artifacts": len(repo_occurrences),
        "basis_counts": dict(basis_counts),
        "labelled_share": share(n_skills - basis_counts.get("none", 0), n_skills),
        "unknown_star_skills": unknown_skill_stars,
        "unknown_star_repos": unknown_star_repos,
        "skill_star_profile": star_profile(sorted(all_skill_stars)),
        "repo_star_profile": star_profile(repo_star_values),
        "concentration": {
            "top10_repos_skill_share": share(skills_in_top10, n_skills),
            "repos_with_10_plus_skills": repos_with_10_plus,
        },
        "domain_count": len(domain_rows),
    }
    (OUTPUT / "skill_domains_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    write_csv(OUTPUT / "skill_domains_by_domain.csv", domain_rows)
    write_csv(OUTPUT / "skill_domains_top_repos_by_stars.csv", top_by_stars)
    write_csv(OUTPUT / "skill_domains_top_repos_by_skills.csv", top_by_skills)

    rng = random.Random(args.seed)
    sample = rng.sample(reps, min(args.sample, n_skills))
    with (OUTPUT / "skill_domains_validation_sample.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["file_sha", "repo", "stars", "domain", "basis", "name", "description_excerpt"])
        for sha, repo, index, basis, name, description in sample:
            label = TAXONOMY[index][0] if index >= 0 else OTHER
            stars = REPOS.get(repo, {}).get("stars")
            writer.writerow([sha, repo, "" if stars is None else stars, label, basis, name, description])

    print(json.dumps({k: summary[k] for k in (
        "occurrences", "distinct_skills", "repositories_with_artifacts", "basis_counts",
        "labelled_share", "skill_star_profile", "repo_star_profile", "concentration")},
        ensure_ascii=False, indent=1))
    for row in domain_rows:
        print(f"{row['domain']:<18} skills={row['distinct_skills']:>8} ({row['share_skills']:.1%}) "
              f"occ={row['occurrences']:>8} median={row['median_stars']} mean={row['mean_stars']} "
              f"p90={row['p90_stars']} >=100={row['share_ge_100']:.1%} top={row['top_repo']}({row['top_repo_stars']})")


if __name__ == "__main__":
    main()
