#!/usr/bin/env python3
"""Editorial donut charts for a study of AI-generated pull requests.

Generates Chinese and English editions at 300 DPI for:
  - TOSEM 2026, Watanabe et al. (N=567 outcomes; N=92 rejection reasons;
    N=214 revised PRs, multi-label revision types)
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"

BG = "#F6F1E7"
INK = "#1F2421"
INK_SOFT = "#4A4F49"
MUTED = "#8C8578"
HAIR = "#DED4C3"
CLAY = "#B8524A"
CREAM = "#FFF8EC"

serif_bold = FontProperties(fname=str(FONTS / "NotoSerifSC-Bold.otf"))
serif_semi = FontProperties(fname=str(FONTS / "NotoSerifSC-SemiBold.otf"))
serif = FontProperties(fname=str(FONTS / "NotoSerifSC-Regular.otf"))
sans_light = FontProperties(fname=str(FONTS / "NotoSansSC-Light.otf"))
sans = FontProperties(fname=str(FONTS / "NotoSansSC-Regular.otf"))
sans_medium = FontProperties(fname=str(FONTS / "NotoSansSC-Medium.otf"))
sans_bold = FontProperties(fname=str(FONTS / "NotoSansSC-Bold.otf"))

SOURCES = {
    "tosem": {
        "slug": "tosem_rejection_pie",
        "eyebrow": "TOSEM 2026  /  WATANABE ET AL.",
        "taxonomy": "REJECTION TAXONOMY  ·  14 CATEGORIES",
        "center_eyebrow": "AI-GENERATED",
        "center_label": "REJECTED PULL REQUESTS",
        "expected_total": 92,
        "citation": {
            "authors": "Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2026).",
            "title": "On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub.",
            "venue": "ACM Transactions on Software Engineering and Methodology (TOSEM)  ·  doi:10.1145/3798166",
            "zh_title": "中文译名：论智能体编程的使用——GitHub 上 Pull Request 的实证研究",
        },
        # (Chinese label, English label, count, colour)
        "data": [
            ("未知 / 无反馈", "Unknown / no feedback", 59, "#B8524A"),
            ("被其他方案替代", "Alternative solutions", 11, "#2F4858"),
            ("仅用于验证", "Verification only", 5, "#D19A3F"),
            ("PR 太大", "Too large", 3, "#74855F"),
            ("过时", "Obsolete", 3, "#8D6B84"),
            ("不活跃", "Inactive", 2, "#5B7C88"),
            ("非最优设计", "Non-optimal design", 2, "#C48558"),
            ("无价值", "Do not add value", 1, "#A79A78"),
            ("增加复杂度", "Increase complexity", 1, "#9C7A62"),
            ("不信任 AI 代码", "No confidence in AI code", 1, "#6F6A8A"),
            ("引入 Bug / 破坏兼容性", "Bugs / breaking changes", 1, "#9A5C5C"),
            ("不符合社区利益", "Not in community interest", 1, "#4E6B78"),
            ("合并冲突", "Merge conflicts", 1, "#B3924E"),
            ("不确定", "Not sure", 1, "#8B8F96"),
        ],
        "copy": {
            "zh": {
                "title": "AI PR 为什么被拒绝？",
                "dek": "N = 92 个未合并的 AI 生成 Pull Request · 按拒绝原因拆解",
                "center_sub": "14 类原因 · 59 个没有解释",
                "list_reason": "拒绝原因  /  REASON",
                "list_prs": "PRs",
                "list_pct": "占比",
                "insight_kicker": "关键洞察  /  INSIGHT",
                "insight_title": "59 / 92 的拒绝，没有留下任何解释。",
                "insight_body": "AI PR 的反馈闭环仍然接近一个黑箱 —— 大多数时候，模型连“错在哪里”都收不到。",
                "stats": [
                    ("64.1%", "无反馈关闭", "Unknown"),
                    ("35.9%", "有明确原因", "33 of 92"),
                    ("14", "原因类别", "categories"),
                ],
                "footer_data": "数据：TOSEM 2026 · Watanabe et al. · 92 个未合并的 AI 生成 PR（拒绝原因样本）",
                "rounding": "因四舍五入，百分比合计可能不等于 100%",
                "cite_label": "引用 / CITATION",
                "title_size": 39,
            },
            "en": {
                "title": "Why Are AI PRs Rejected?",
                "dek": "N = 92 unmerged AI-generated pull requests · broken down by rejection reason",
                "center_sub": "14 categories · 59 without explanation",
                "list_reason": "REJECTION REASON",
                "list_prs": "PRs",
                "list_pct": "Share",
                "insight_kicker": "KEY INSIGHT",
                "insight_title": "59 of 92 rejections left no explanation at all.",
                "insight_body": "The feedback loop for AI PRs remains close to a black box — most of the time, the model never learns what went wrong.",
                "stats": [
                    ("64.1%", "Closed without feedback", "Unknown"),
                    ("35.9%", "Explicit reason", "33 of 92"),
                    ("14", "Reason categories", "categories"),
                ],
                "footer_data": "Data: TOSEM 2026 · Watanabe et al. · 92 unmerged AI-generated PRs (rejection-reason sample)",
                "rounding": "Percentages may not sum to 100% due to rounding.",
                "cite_label": "CITATION",
                "title_size": 37,
            },
        },
    },
}

TOSEM_CITATION = {
    "authors": "Watanabe, M., Li, H., Kashiwa, Y., Reid, B., Iida, H., & Hassan, A. E. (2026).",
    "title": "On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub.",
    "venue": "ACM Transactions on Software Engineering and Methodology (TOSEM)  ·  doi:10.1145/3798166",
    "zh_title": "中文译名：论智能体编程的使用——GitHub 上 Pull Request 的实证研究",
}

TOSEM_OVERVIEW = {
    "slug": "tosem_outcomes_pie",
    "eyebrow": "TOSEM 2026  /  WATANABE ET AL.",
    "taxonomy": "FINAL OUTCOMES  ·  3 CATEGORIES",
    "center_eyebrow": "AGENTIC PULL REQUESTS",
    "center_label": "FINAL OUTCOMES",
    "expected_total": 567,
    "citation": TOSEM_CITATION,
    "data": [
        ("直接合并（未修订）", "Merged directly", 261, "#2F4858"),
        ("修订后合并", "Merged after revision", 214, "#D19A3F"),
        ("未合并 / 拒绝", "Unmerged / rejected", 92, "#B8524A"),
    ],
    "copy": {
        "zh": {
            "title": "AI PR 最终都去哪了？",
            "dek": "N = 567 个 Agentic Pull Request · 475 个合并（83.8%）· 92 个拒绝",
            "center_sub": "475 个合并 · 92 个拒绝",
            "list_reason": "最终结局  /  OUTCOME",
            "list_prs": "PRs",
            "list_pct": "占比",
            "insight_kicker": "关键洞察  /  INSIGHT",
            "insight_title": "每 5 个 AI PR，约 4 个最终被合并。",
            "insight_body": "但接受并不等于一次通过：475 个合并 PR 中，有 214 个（45.1%）在合并前经过修订。",
            "stats": [
                ("83.8%", "最终合并", "475 / 567"),
                ("45.1%", "合并前经修订", "214 / 475"),
                ("16.2%", "未合并 / 拒绝", "92 / 567"),
            ],
            "footer_data": "数据：TOSEM 2026 · Watanabe et al. · 567 个 Agentic PR（475 个合并，92 个拒绝）",
            "rounding": "因四舍五入，百分比合计可能不等于 100%",
            "cite_label": "引用 / CITATION",
            "title_size": 39,
        },
        "en": {
            "title": "Where Do AI PRs End Up?",
            "dek": "N = 567 agentic pull requests · 475 merged (83.8%) · 92 rejected",
            "center_sub": "475 merged · 92 rejected",
            "list_reason": "FINAL OUTCOME",
            "list_prs": "PRs",
            "list_pct": "Share",
            "insight_kicker": "KEY INSIGHT",
            "insight_title": "Roughly four in five AI PRs are eventually merged.",
            "insight_body": "But acceptance is not a clean pass: 214 of 475 merged PRs (45.1%) were revised before merge.",
            "stats": [
                ("83.8%", "Eventually merged", "475 of 567"),
                ("45.1%", "Merged after revision", "214 of 475"),
                ("16.2%", "Unmerged / rejected", "92 of 567"),
            ],
            "footer_data": "Data: TOSEM 2026 · Watanabe et al. · 567 agentic PRs (475 merged, 92 rejected)",
            "rounding": "Percentages may not sum to 100% due to rounding.",
            "cite_label": "CITATION",
            "title_size": 36,
        },
    },
}

TOSEM_REVISION = {
    "slug": "tosem_revision_pie",
    "eyebrow": "TOSEM 2026  /  WATANABE ET AL.",
    "taxonomy": "REVISION TAXONOMY  ·  10 TYPES  ·  MULTI-LABEL",
    "center_eyebrow": "MERGED AFTER REVISION",
    "center_label": "REVISED PULL REQUESTS",
    "expected_total": 433,
    "denominator": 214,
    "center_total": 214,
    "citation": TOSEM_CITATION,
    "data": [
        ("修复 Bug", "Bug fixes", 102, "#B8524A"),
        ("文档", "Documentation", 62, "#2F4858"),
        ("重构", "Refactoring", 58, "#74855F"),
        ("风格 / 格式", "Style / formatting", 50, "#D19A3F"),
        ("杂项维护", "Chores", 45, "#8D6B84"),
        ("测试", "Tests", 35, "#5B7C88"),
        ("新功能", "Features", 33, "#C48558"),
        ("构建配置", "Build", 30, "#A79A78"),
        ("CI / CD", "CI / CD", 15, "#6F6A8A"),
        ("性能", "Performance", 3, "#8B8F96"),
    ],
    "copy": {
        "zh": {
            "title": "AI PR 合并前改了什么？",
            "dek": "N = 214 个修订后合并的 Agentic PR · 占已合并 PR 的 45.1%",
            "center_sub": "10 类修订 · 多标签",
            "list_reason": "修订类型  /  TYPE",
            "list_prs": "PRs",
            "list_pct": "占 214",
            "insight_kicker": "关键洞察  /  INSIGHT",
            "insight_title": "合并前的修订，近一半是在修 Bug。",
            "insight_body": "47.7% 的修订涉及 fix；style 占 23.4%，docs 占 29.0%，refactor 占 27.1%。",
            "stats": [
                ("47.7%", "修复 Bug", "102 / 214"),
                ("23.4%", "风格调整", "50 / 214"),
                ("29.0%", "文档修改", "62 / 214"),
            ],
            "footer_data": "数据：TOSEM 2026 · Watanabe et al. · 214 个修订后合并的 Agentic PR（Table 4）",
            "rounding": "修订类型为多标签分类，百分比合计超过 100%",
            "cite_label": "引用 / CITATION",
            "title_size": 39,
        },
        "en": {
            "title": "What Gets Revised Before Merge?",
            "dek": "N = 214 agentic PRs merged after revision · 45.1% of merged PRs",
            "center_sub": "10 revision types · multi-label",
            "list_reason": "REVISION TYPE",
            "list_prs": "PRs",
            "list_pct": "of 214",
            "insight_kicker": "KEY INSIGHT",
            "insight_title": "Nearly half of pre-merge revisions fix bugs.",
            "insight_body": "47.7% of revisions involve fixes; style accounts for 23.4%, docs for 29.0%, and refactor for 27.1%.",
            "stats": [
                ("47.7%", "Bug fixes", "102 of 214"),
                ("23.4%", "Style changes", "50 of 214"),
                ("29.0%", "Documentation", "62 of 214"),
            ],
            "footer_data": "Data: TOSEM 2026 · Watanabe et al. · 214 agentic PRs merged after revision (Table 4)",
            "rounding": "Revision types are multi-label; percentages sum to more than 100%.",
            "cite_label": "CITATION",
            "title_size": 31,
        },
    },
}

W, H = 16.0, 10.0
DPI = 300
LX1 = 15.25


def draw_chart(source: dict, lang: str, out_stem: Path) -> None:
    data = source["data"]
    citation = source["citation"]
    c = source["copy"][lang]
    data_total = sum(row[2] for row in data)
    assert data_total == source["expected_total"], (source["slug"], data_total)
    denominator = source.get("denominator", data_total)
    center_total = source.get("center_total", denominator)
    counts = [row[2] for row in data]
    colors = [row[3] for row in data]
    pcts = [count / denominator * 100 for count in counts]
    multi_label = denominator != data_total

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    fig.patch.set_facecolor(BG)

    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_axis_off()
    ax.set_facecolor(BG)

    # ---------------- header ----------------
    ax.text(0.75, 9.42, source["eyebrow"], color=CLAY,
            fontsize=9.2, fontproperties=sans_medium, va="center")
    ax.text(0.75, 8.86, c["title"], color=INK,
            fontsize=c["title_size"], fontproperties=serif_bold, va="baseline")
    ax.text(0.75, 8.38, c["dek"], color=INK_SOFT, fontsize=12.2,
            fontproperties=sans_light, va="center")
    ax.text(15.25, 9.42, source["taxonomy"], color=MUTED,
            fontsize=7.8, fontproperties=sans, va="center", ha="right")

    # ---------------- donut ----------------
    dax = fig.add_axes([0.85 / W, 2.72 / H, 5.0 / W, 5.0 / H])
    dax.set_facecolor("none")
    dax.pie(
        counts, colors=colors, startangle=90, counterclock=False, radius=1.0,
        wedgeprops=dict(width=0.36, edgecolor=BG, linewidth=1.7, antialiased=True),
    )
    dax.set_aspect("equal")
    dax.set_xlim(-1.12, 1.12)
    dax.set_ylim(-1.12, 1.12)
    dax.set_axis_off()

    cum = 0
    for count in counts:
        theta = np.deg2rad(90 - cum / data_total * 360)
        dax.plot([1.035 * np.cos(theta), 1.068 * np.cos(theta)],
                 [1.035 * np.sin(theta), 1.068 * np.sin(theta)],
                 color="#C9BEA9", lw=0.7, solid_capstyle="butt", zorder=5)
        cum += count

    dax.add_patch(Circle((0, 0), 1.058, fill=False, ec="#D6CBB8", lw=0.7, zorder=4))

    label_cum = 0
    for i, count in enumerate(counts[:3]):
        sweep = count / data_total * 360
        mid = 90 - label_cum - sweep / 2
        label_cum += sweep
        if i == 0 and sweep > 180:
            mid = 20
        theta = np.deg2rad(mid)
        x, y = 0.82 * np.cos(theta), 0.82 * np.sin(theta)
        if i == 0:
            dax.text(x, y, str(count) if multi_label else f"{pcts[i]:.1f}%", color=CREAM, fontsize=17,
                     fontproperties=serif_bold, ha="center", va="center", zorder=6)
            dax.text(x, y - 0.095, "PRs" if multi_label else f"{count} PRs", color=CREAM, fontsize=8.4,
                     fontproperties=sans, ha="center", va="center", alpha=0.9, zorder=6)
        else:
            dax.text(x, y, f"{count}" if multi_label else f"{count} · {pcts[i]:.1f}%", color=CREAM,
                     fontsize=9.6 if i == 1 else 8.8, fontproperties=sans_medium,
                     ha="center", va="center", zorder=6)

    dax.text(0, 0.315, source["center_eyebrow"], color=CLAY, fontsize=7.6,
             fontproperties=sans_medium, ha="center", va="center")
    dax.text(0, 0.015, str(center_total), color=INK, fontsize=55, fontproperties=serif_bold,
             ha="center", va="center")
    dax.text(0, -0.215, source["center_label"], color=MUTED, fontsize=7.4,
             fontproperties=sans, ha="center", va="center")
    dax.text(0, -0.355, c["center_sub"], color=MUTED, fontsize=6.6,
             fontproperties=sans_light, ha="center", va="center")

    # ---------------- ranked list ----------------
    NAME_X, DOT_X, RANK_X = 7.52, 7.34, 6.98
    COUNT_X, PCT_X = 13.82, 15.25
    TOP_Y = 7.50
    LIST_BOTTOM = 2.482
    STEP = (TOP_Y - LIST_BOTTOM) / (len(data) - 1) if len(data) > 1 else 0.0
    if len(data) <= 4:
        STEP = min(STEP, 1.75)
        span = STEP * (len(data) - 1)
        TOP_Y = (TOP_Y + LIST_BOTTOM) / 2 + span / 2

    ax.text(NAME_X, 7.80, c["list_reason"], color=MUTED, fontsize=7.4,
            fontproperties=sans_medium, va="center")
    ax.text(COUNT_X, 7.80, c["list_prs"], color=MUTED, fontsize=7.4,
            fontproperties=sans_medium, va="center", ha="right")
    ax.text(PCT_X, 7.80, c["list_pct"], color=MUTED, fontsize=7.4,
            fontproperties=sans_medium, va="center", ha="right")
    ax.plot([7.18, LX1], [7.68, 7.68], color="#CFC4B1", lw=0.8)

    ax.add_patch(FancyBboxPatch((7.14, TOP_Y - 0.178), LX1 - 7.14, 0.362,
                                boxstyle="round,pad=0,rounding_size=0.045",
                                fc=CLAY, ec="none", alpha=0.055, zorder=0))

    for i, (zh, en, count, color) in enumerate(data):
        primary, secondary = (zh, en) if lang == "zh" else (en, zh)
        y = TOP_Y - i * STEP
        ax.text(RANK_X, y + 0.008, f"{i + 1:02d}", color="#B3A995", fontsize=6.8,
                fontproperties=sans, va="center", ha="left")
        ax.add_patch(Circle((DOT_X, y + 0.050), 0.043, color=color, zorder=5))
        ax.text(NAME_X, y + 0.084, primary, color=INK, fontsize=10.7,
                fontproperties=sans_medium, va="center")
        ax.text(NAME_X, y - 0.052, secondary, color="#9B9182", fontsize=6.7,
                fontproperties=sans_light, va="center")
        ax.text(COUNT_X, y + 0.016, str(count), color=INK, fontsize=13.4,
                fontproperties=serif_semi, va="center", ha="right")
        ax.text(PCT_X, y + 0.016, f"{pcts[i]:.1f}%",
                color=CLAY if i == 0 else INK_SOFT, fontsize=9.0,
                fontproperties=sans_medium if i == 0 else sans,
                va="center", ha="right")
        if i < len(data) - 1:
            ax.plot([7.18, LX1], [y - 0.178, y - 0.178], color="#E7DFD1", lw=0.55)

    # ---------------- insight band ----------------
    BAND_Y = 2.30
    ax.plot([0.75, LX1], [BAND_Y, BAND_Y], color="#CFC4B1", lw=0.9)
    ax.add_patch(Rectangle((0.75, 2.015), 0.055, 0.055, color=CLAY, lw=0))
    ax.text(0.90, 2.042, c["insight_kicker"], color=CLAY, fontsize=7.8,
            fontproperties=sans_medium, va="center")
    ax.text(0.75, 1.655, c["insight_title"], color=INK,
            fontsize=17.6, fontproperties=serif_bold, va="center")
    ax.text(0.75, 1.315, c["insight_body"], color=INK_SOFT, fontsize=9.2,
            fontproperties=sans_light, va="center")

    stat_x = [9.95, 12.20, 14.40]
    for x, (value, label, sub) in zip(stat_x, c["stats"]):
        ax.text(x, 1.985, value, color=INK, fontsize=21, fontproperties=serif_semi,
                va="center")
        ax.text(x, 1.635, label, color=INK_SOFT, fontsize=8.6,
                fontproperties=sans_medium, va="center")
        ax.text(x, 1.435, sub, color=MUTED, fontsize=6.6,
                fontproperties=sans_light, va="center")
    for x in (11.68, 13.92):
        ax.plot([x, x], [1.38, 2.12], color="#E0D6C5", lw=0.6)

    # ---------------- footer + citation ----------------
    ax.plot([0.75, LX1], [1.18, 1.18], color="#E0D6C5", lw=0.6)
    ax.text(0.75, 0.96, c["footer_data"], color=MUTED, fontsize=7.8,
            fontproperties=sans_light, va="center")
    ax.text(LX1, 0.96, c["rounding"], color=MUTED,
            fontsize=7.8, fontproperties=sans_light, va="center", ha="right")

    cite_x = 1.80
    ax.text(0.75, 0.735, c["cite_label"], color=CLAY, fontsize=9.2,
            fontproperties=sans_medium, va="center")
    ax.text(cite_x, 0.735, citation["authors"], color=INK, fontsize=10.0,
            fontproperties=sans, va="center")
    ax.text(cite_x, 0.535, citation["title"], color=INK, fontsize=9.9,
            fontproperties=serif, va="center")
    if lang == "zh":
        ax.text(cite_x, 0.350, citation["zh_title"], color=INK, fontsize=9.2,
                fontproperties=sans, va="center")
        ax.text(cite_x, 0.165, citation["venue"], color=INK, fontsize=9.1,
                fontproperties=sans, va="center")
    else:
        ax.text(cite_x, 0.335, citation["venue"], color=INK, fontsize=9.4,
                fontproperties=sans, va="center")

    out_png = out_stem.with_suffix(".png")
    out_svg = out_stem.with_suffix(".svg")
    plt.rcParams["svg.fonttype"] = "path"
    fig.savefig(out_png, dpi=DPI, facecolor=BG, bbox_inches=None,
                pil_kwargs={"optimize": True})
    fig.savefig(out_svg, facecolor=BG, bbox_inches=None)
    plt.close(fig)
    print(f"wrote {out_png}")
    print(f"wrote {out_svg}")


for source in (TOSEM_OVERVIEW, SOURCES["tosem"], TOSEM_REVISION):
    for lang in ("zh", "en"):
        draw_chart(source, lang, HERE / f"{source['slug']}_{lang}")
