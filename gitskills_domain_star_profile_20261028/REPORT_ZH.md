# GitSkills：Skill 领域与星星数画像（交接说明）

- 日期：2026-10-28
- 交接标签：`P0-handoff-gitskills-domain-stars-20261028`（本地标签，未推送到 origin）
- 数据：Hugging Face `mvaccargiu/gitskills`，版本 `ebab17454a7c236f8f26b183567f1a126f42e3f8`。本地副本位于 `/home/satoru/agent/gitskills-parquet/`，`artifacts`、`artifact_siblings`、`repos`、`mining_runs` 四个配置均已按 SHA-256 校验。
- 统计对象：全部 3,797,117 份 `SKILL.md` 副本，去重后为 1,877,981 个不同内容（每个内容取一份代表副本），分布在 282,200 个仓库中。

## 1. 主要结论

1. **领域以软件工程为主。** 前十个有标签的领域（不含“其他/未归类”）合计占 57.6%，依次为 Agent 与 Skill 工具链、版本控制与协作、测试与 QA、软件架构与规划、前端与 UI、代码审查与质量、设计与多媒体、DevOps 与云、后端与 API、文档与办公。
2. **星星数总体很低。** 按不同 Skill 计，中位数为 1 星；41.7% 的 Skill 所在仓库为 0 星；只有 6.9% 超过 100 星，0.18% 超过 10,000 星。
3. **星星高度集中，且与 Skill 数量不一致。** Skill 最多的仓库多是低星的聚合或镜像仓库；星星最多的仓库中，有的只含与其他仓库重复的副本（见第 5 节）。
4. **领域标签只能作粗略参考。** 有标签样本的准确率约为 62%（严格）至 80%（宽松）（见第 4 节）。

## 2. 领域分布

占比以全部 1,877,981 个不同 Skill 为分母。中位数、均值和 ≥100 星占比按各 Skill 所在仓库的星星计算。“星星最多的代表仓库”是该领域代表副本中星星最多的仓库，不代表该领域的主要来源。完整数据见 [data/skill_domains_by_domain.csv](data/skill_domains_by_domain.csv)。

| 领域 | Skill 数 | 占比 | 中位星星 | 均值星星 | ≥100 星占比 | 星星最多的代表仓库（星星数） |
|---|---:|---:|---:|---:|---:|---|
| 其他/未归类 | 287,988 | 15.3% | 1 | 46.0 | 2.4% | google-gemini/gemini-cli（106,010） |
| Agent 与 Skill 工具链 | 153,336 | 8.2% | 1 | 91.4 | 6.7% | openclaw/openclaw（383,040） |
| 版本控制与协作 | 131,719 | 7.0% | 1 | 331.3 | 19.5% | Significant-Gravitas/AutoGPT（185,565） |
| 测试与 QA | 127,514 | 6.8% | 1 | 147.0 | 6.1% | affaan-m/ECC（230,097） |
| 软件架构与规划 | 117,997 | 6.3% | 1 | 66.4 | 4.7% | paperclipai/paperclip（73,819） |
| 前端与 UI | 105,215 | 5.6% | 0 | 240.7 | 5.4% | ant-design/ant-design（98,744） |
| 代码审查与质量 | 105,157 | 5.6% | 1 | 146.5 | 5.8% | DietrichGebert/ponytail（83,990） |
| 设计与多媒体 | 93,260 | 5.0% | 1 | 113.3 | 6.3% | affaan-m/ECC（230,097） |
| DevOps 与云 | 87,198 | 4.6% | 1 | 109.9 | 6.7% | affaan-m/ECC（230,097） |
| 后端与 API | 84,384 | 4.5% | 1 | 112.7 | 5.4% | affaan-m/ECC（230,097） |
| 文档与办公 | 76,510 | 4.1% | 1 | 121.7 | 6.2% | ant-design/ant-design（98,744） |
| 安全与审计 | 61,756 | 3.3% | 1 | 150.3 | 9.9% | affaan-m/ECC（230,097） |
| 写作与营销 | 54,962 | 2.9% | 1 | 130.5 | 7.4% | openclaw/openclaw（383,040） |
| 编程语言与框架 | 52,089 | 2.8% | 1 | 155.8 | 6.8% | react/react（246,506） |
| 科研与学术 | 45,701 | 2.4% | 1 | 125.3 | 11.0% | nexu-io/open-design（78,601） |
| AI 与机器学习 | 42,928 | 2.3% | 2 | 94.7 | 5.3% | Egonex-AI/Understand-Anything（74,301） |
| 个人效率与生活 | 41,734 | 2.2% | 1 | 87.3 | 5.7% | thedaviddias/Front-End-Checklist（73,218） |
| 数据分析与可视化 | 34,519 | 1.8% | 2 | 122.1 | 6.6% | affaan-m/ECC（230,097） |
| 数据库与数据工程 | 33,970 | 1.8% | 1 | 121.3 | 5.8% | ClickHouse/ClickHouse（48,658） |
| 金融与会计 | 28,000 | 1.5% | 2 | 92.5 | 7.4% | thedaviddias/Front-End-Checklist（73,218） |
| 自动化与爬虫 | 24,202 | 1.3% | 2 | 418.1 | 14.0% | n8n-io/n8n（196,579） |
| 商业与电商 | 20,959 | 1.1% | 3 | 94.1 | 6.3% | thedaviddias/Front-End-Checklist（73,218） |
| 教育与培训 | 20,574 | 1.1% | 1 | 115.0 | 6.6% | nexu-io/open-design（78,601） |
| 医疗健康 | 18,717 | 1.0% | 2 | 170.3 | 10.5% | paperclipai/paperclip（73,819） |
| 法律与合规 | 17,561 | 0.9% | 4 | 137.2 | 10.7% | thedaviddias/Front-End-Checklist（73,218） |
| 游戏 | 10,031 | 0.5% | 1 | 65.7 | 5.0% | HKUDS/CLI-Anything（45,368） |

## 3. 星星数

| 统计口径 | 有星星数据的样本 | 中位数 | 75% | 90% | 99% | 最大 | 0 星 | ≥100 星 | ≥1,000 星 | ≥10,000 星 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 每个不同 Skill | 1,877,194 | 1 | 8 | 41 | 1,547 | 383,040 | 41.7% | 6.9% | 2.8% | 0.18% |
| 每份副本（全部副本，各计入自身仓库的星星） | 3,789,592 | 1 | 7 | 36 | 2,259 | 383,040 | 46.1% | 6.4% | 2.4% | 0.41% |
| 每个仓库 | 281,685 | 0 | 2 | 15 | 1,278 | 383,040 | 59.3% | 4.1% | 1.2% | 0.25% |

- 星星数为空的记录未计为 0：Skill 787 个、副本 7,525 份、仓库 515 个。
- 星星数是数据集记录的值（版本 `ebab174`），不是实时数值，也不代表 Skill 的使用量。
- Skill 最多的前 10 个仓库合计占 10.5% 的不同 Skill；共有 31,038 个仓库包含至少 10 个不同 Skill。
- 例：`NeuralBlitz/buggy` 含 30,308 个不同 Skill，只有 3 星；`majiayu000/claude-skill-registry-data` 含 27,643 个，只有 16 星；`Klotzkette/claude-fuer-deutsches-recht` 含 21,955 个，有 1,332 星。

## 4. 领域标签的可靠性

- **方法**：25 个关键词领域加上“其他/未归类”。先匹配名称（权重 2）和描述（权重 1）；都不命中时，用仓库描述兜底（占 10.6%）；仍无匹配则归入“其他/未归类”（占 15.3%）。
- **抽检**：从全部代表副本中按固定种子 20261028 随机抽取 100 条。逐条判定见 [data/skill_domains_validation_judgements.csv](data/skill_domains_validation_judgements.csv)，其中 `idx` 即 [data/skill_domains_validation_sample.csv](data/skill_domains_validation_sample.csv) 中的数据行序号。判定由助手逐条完成，未做独立复核。
- **结果**：
  - 有领域标签的 79 条中，正确 49 条（62%），存疑 14 条，错误 16 条；宽松口径（存疑算正确）为 80%。
  - 应归类却归入“其他”的 5 条；合理未归类的 3 条；没有名称和描述、无法判断的 13 条。
  - 仅靠仓库描述兜底得到标签的 4 条中，正确 1 条、存疑 1 条、错误 2 条。
- **典型错误**：
  - 关键词歧义：merge（Lean 证明归为版本控制）、forensic（文本取证研究归为安全）、training（标注数据集归为教育）、deployment（销售看房归为 DevOps）、branch（ops 配置归为版本控制）、lessons（复盘归为教育）。
  - 同分时按类别顺序决定：“Claude Code skills”与“Anthropic”同分，结果归入 AI，而不是 Agent 工具链。
  - 词表缺口：排名追踪（SERP）、WAF 绕过、日文邮件、ML 实验、spin up agent advisor 等未覆盖。
- **建议用法**：只看大类趋势，不要把占比当作精确值；各领域占比可能有几个百分点的误差。

## 5. 代表副本对星星数的影响

- 去重时每个内容只保留一份代表副本（README 说明优先选择 `.claude/skills/` 下的文件）。每个 Skill 的星星取其代表副本所在仓库的星星。
- `anthropics/skills`（163,055 星）有 3 份副本，但都不是代表，因此不计入按 Skill 的统计。
- `openclaw/openclaw`（383,040 星）有 46 份副本，其中 2 份是代表。
- 因此按 Skill 统计会低估原创仓库的影响。按副本统计（每份副本计入自身仓库的星星）结果几乎相同，说明这一偏差对整体分布影响有限，但对个别原创仓库影响很大。

## 6. 文件

| 路径 | 内容 |
|---|---|
| [scripts/skill_domain_stars.py](scripts/skill_domain_stars.py) | 分析脚本（与 `gitskills-parquet/analysis/skill_domain_stars.py` 逐字节一致） |
| [data/skill_domains_summary.json](data/skill_domains_summary.json) | 总体计数、星星分布、集中度 |
| [data/skill_domains_by_domain.csv](data/skill_domains_by_domain.csv) | 26 个领域的统计 |
| [data/skill_domains_top_repos_by_stars.csv](data/skill_domains_top_repos_by_stars.csv) | 星星最多的 50 个仓库（至少含一份副本，不一定有代表 Skill） |
| [data/skill_domains_top_repos_by_skills.csv](data/skill_domains_top_repos_by_skills.csv) | 代表 Skill 最多的 30 个仓库 |
| [data/skill_domains_validation_sample.csv](data/skill_domains_validation_sample.csv) | 100 条抽样（种子 20261028） |
| [data/skill_domains_validation_judgements.csv](data/skill_domains_validation_judgements.csv) | 每条抽样的判定与说明 |

**复现**：将脚本复制到 `gitskills-parquet/analysis/`，在 `gitskills-parquet/` 下运行 `python3 analysis/skill_domain_stars.py --workers 16`，结果写入 `gitskills-parquet/output/`。脚本不保存每个 Skill 的领域标签；如需逐条标签，需修改脚本导出。

## 7. 限制

- 领域标签为关键词规则，准确率有限。
- 星星数是数据集记录的值，不代表 Skill 的使用量或实时星标。
- 数据只覆盖公开仓库，README 称其应视为总体的下界。
- 抽检判定由助手完成，未做独立复核。

## 8. 更正（相对于早先口头汇报）

- “其他/未归类”中**并非约 13% 没有名称和描述**。13% 是全部 Skill 中名称为空的比例（244,478 个，占 13.0%）。在抽样的 17 条“其他/未归类”中，有 9 条名称和描述均为空。
- 除“其他/未归类”外共有 25 个领域，前十之后还有 15 个（早先写成 16 个）；其余 15 个领域中，占比最高的安全与审计为 3.3%，所以各占 0.5% 到 3.3%（早先写成 0.5% 到 3%）。
- 抽检判定由助手逐条完成，早先描述为“人工核对”并不准确。
