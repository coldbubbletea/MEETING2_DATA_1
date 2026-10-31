# GitSkills：Skill 领域与星星数画像（交接说明）

- 日期：2026-10-28
- 交接标签：`P0-handoff-gitskills-domain-stars-20261028`（本地标签，未推送到 origin）
- 数据：Hugging Face `mvaccargiu/gitskills`，版本 `ebab17454a7c236f8f26b183567f1a126f42e3f8`。本地副本位于 `/home/satoru/agent/gitskills-parquet/`，`artifacts`、`artifact_siblings`、`repos`、`mining_runs` 四个配置均已按 SHA-256 校验。
- 统计对象：全部 3,797,117 份 `SKILL.md` 副本，去重后为 1,877,981 个不同内容（每个内容取一份代表副本），分布在 282,200 个仓库中。

## 1. 主要结论

1. **领域以软件工程为主。** 前十个有标签的领域（不含“其他/未归类”）合计占 57.6%，依次为 Agent 与 Skill 工具链、版本控制与协作、测试与 QA、软件架构与规划、前端与 UI、代码审查与质量、设计与多媒体、DevOps 与云、后端与 API、文档与办公。
2. **星星数总体很低。** 按不同 Skill 计，中位数为 1 星；41.7% 的 Skill 所在仓库为 0 星；达到 100 星及以上的占 6.9%（严格超过 100 星为 6.84%），达到 10,000 星及以上的占 0.18%。
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
| [scripts/skill_file_sizes_gt100.py](scripts/skill_file_sizes_gt100.py) | 超过 100 星 Skill 的文件大小计算脚本（第 9 节） |
| [data/skill_file_sizes_gt100_summary.json](data/skill_file_sizes_gt100_summary.json) | 文件大小汇总：两种口径、覆盖情况、校验结果 |
| [data/skill_file_sizes_gt100_top20.csv](data/skill_file_sizes_gt100_top20.csv) | 文件最多的 20 个 Skill（主口径） |

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
- 早先的“超过 100 星”“超过 10,000 星”实为“达到”（≥）口径，已在第 1 节更正；严格超过 100 星为 6.84%。

## 9. 超过 100 星的 Skill：数量与文件大小

更新日期：2026-10-29。每个不同 Skill 取代表副本，所在仓库星星数严格大于 100（主口径，与前文一致）。占比的分母为全部 1,877,981 个不同 Skill。

### 9.1 数量

| 口径 | 数量 | 占比 |
|---|---:|---:|
| 不同 Skill，代表副本所在仓库 > 100 星（**主口径**） | 128,382 | 6.84% |
| 不同 Skill，达到 100 星及以上（对照） | 128,898 | 6.86% |
| 不同 Skill，任一副本所在仓库 > 100 星（**替代口径**） | 187,727 | 10.00% |
| 全部副本（3,797,117 份），各自仓库 > 100 星 | 241,017 | 6.35% |

- 主口径按星星分段：101–999 星 75,327 个；1,000–9,999 星 49,666 个；10,000 星以上 3,389 个。
- 超过 100 星的仓库中，有 9,618 个包含代表 Skill。
- “达到 100 星及以上”和“全部副本”两行是一次性计数，未保存脚本；其余数字可由第 9.2 节的脚本复现。

### 9.2 文件大小（主口径，128,382 个 Skill）

每个 Skill 的文件 = SKILL.md + 其所在文件夹内全部文件（递归，不含目录）。

| 项目 | 数值 |
|---|---:|
| SKILL.md 合计 | 958,665,240 B（0.96 GB）；128,382 个全部通过 git blob 哈希校验 |
| 目录内全部文件，按数据集记录的目录大小合计（含 SKILL.md） | **19,661,615,761 B（19.66 GB）** |
| 逐文件去重后的下界（同一仓库同一路径只计一次） | 12,029,642,943 B（12.03 GB），500,876 个文件 |
| 嵌套目录重复（仅计逐文件可见部分） | 208,160,043 B（约 1.7%） |

- **目录列表状态**：完整 98,698 个；标记为截断（`composition_truncated = 1`）29,681 个；未取得目录列表 3 个（只计 SKILL.md）。
- **截断的 142 个目录**：明细表只保存了前 500 个条目（文件加目录），目录大小按收集器记录的完整列表补齐。其余 29,539 个截断目录的明细与记录一致。
- **分布**（按可见明细）：中位数 6,003 B；90% 分位 40,670 B；99% 分位 731,963 B；最大 296,731,692 B。
- **集中度**：文件最多的前 20 个 Skill 合计 2,770,519,019 B，占 14.1%。前三名是：
  - `mikubaka88/CCFA-Skills` 的 `ccf-paper-writer`（296.7 MB，主要是 PDF 论文）；
  - `anbeime/skill`（248.9 MB，主要是视频；SKILL.md 位于仓库根目录）；
  - `SharpAI/DeepCamera`（212.1 MB，主要是模型文件和 GIF；SKILL.md 位于仓库根目录）。

### 9.3 替代口径（任一副本 > 100 星，187,727 个）

- 目录大小合计 23,303,933,352 B（23.30 GB），其中 SKILL.md 1,432,090,282 B。
- 逐文件去重下界 15,386,744,082 B（15.39 GB），722,604 个文件。

### 9.4 口径与限制

1. Skill 文件夹按数据集定义：SKILL.md 所在文件夹及其子文件夹。SKILL.md 位于仓库根目录时，整个仓库都会计入，因此视频、PDF、模型等大文件占了很大比例。
2. 按目录记录的合计可能重复计算嵌套 Skill 的文件。按逐文件可见部分估计，约为 1.7%，但无法对 142 个截断目录做去重。
3. 标记为截断的 29,681 个目录（占 23%）完整性无法确认，其大小可能偏低。
4. 3 个 Skill 未取得目录列表，只计 SKILL.md。
5. 大小来源：SKILL.md 由内容字节数还原（git blob 哈希全部通过）；附属文件取列表中的 `entry_size`。抽样 5,000 个附属文件，4,993 个与存储文本的字节数一致（99.9%），其余差异以列表大小为准。

### 9.5 复现

将 [scripts/skill_file_sizes_gt100.py](scripts/skill_file_sizes_gt100.py) 复制到 `gitskills-parquet/analysis/`，在 `gitskills-parquet/` 下运行 `python3 analysis/skill_file_sizes_gt100.py --workers 6`。结果写入 `gitskills-parquet/output/`。

## 10. 网页下钻用的 >100 星领域统计

网页先展示全部 1,877,981 种内容的星标筛选图，再进入主口径 A 的 128,382 种内容：

- 代表仓库 >100 星：128,382；≤100 星：1,748,812；星标缺失：787。恰好 100 星的 516 种内容不纳入。
- [data/skill_domains_gt100.csv](data/skill_domains_gt100.csv) 使用原分类规则重新扫描主口径 A，每个领域占比的分母都是 128,382；不是全量领域占比的直接沿用。
- 标签依据：名称/描述 85,830 种、仓库描述兜底 35,711 种、未归类 6,841 种。该高星子集尚未独立抽检，不能将第 4 节的全量抽检一致率解释为高星子集准确率。
- 计数及方法记录见 [data/skill_domains_gt100_summary.json](data/skill_domains_gt100_summary.json)。

在本仓库根目录复现：

```bash
PYTHONDONTWRITEBYTECODE=1 python gitskills_domain_star_profile_20261028/scripts/skill_domains_gt100.py \
  --data /home/satoru/agent/gitskills-parquet/data \
  --output gitskills_domain_star_profile_20261028/data
```

输入应为同一固定版本 `ebab17454a7c236f8f26b183567f1a126f42e3f8` 的 Parquet 副本。脚本会检查全量、>100 星与缺失计数是否符合交接结果，不修改原始数据。

## 11. 超过 100 星 Skill 的自然语言（2026-11-01）

沿用主口径 A：`dedup_primary == 1`，且代表仓库 `stars > 100`，共 **128,382** 个不同内容。统计的是 `SKILL.md` 说明正文的自然语言，不是仓库的编程语言，也不分析附属文件。

| 自动语言标签 | Skill 数 | 占 128,382 个 |
|---|---:|---:|
| 英语 | 91,191 | 71.03% |
| 汉语 | 10,528 | 8.20% |
| 中英混合 | 57 | 0.04% |
| 其他语言 | 25,926 | 20.19% |
| 无法判断 | 680 | 0.53% |

五类互斥，每个 Skill 只计一次，无法判断项不从分母中剔除。百分比四舍五入后合计可能不是 100%。

### 11.1 方法与限制

- 使用 `lingua-language-detector==2.1.1`，全部支持语言、低精度模式，主语言最小相对置信差为 0.15。
- 排除文件开头的 YAML front matter、反引号或波浪号围栏代码块、四空格或制表符缩进的行、行内代码、图片、URL 和文件路径；Markdown 链接保留可读标签。清洗规则是启发式，不等同于完整 Markdown 语法解析。
- 对清洗后的全文识别主语言，并对多语言片段按 Unicode 字母数计权，汉字计入。少于 40 个正文语言字符，或没有足够置信度的主语言，归为无法判断；主语言不是英语或汉语时归为其他语言。
- 中英混合要求英语、汉语识别片段各至少 40 个语言字符、各占全文语言字符至少 20%、合计至少 80%。英文片段还须至少出现 3 个常见英语功能词；词表保存于 JSON。该限制用于减少英文工具名、API 名称和路径导致的混合误判，不代表所有含两种语言的文件都会被归入混合。
- 抽查了其他语言、汉语、混合和无法判断的部分实例，并根据工具名误判修正了混合判定。代码测试覆盖纯英文、中文夹技术词、中英混合、混合阈值、日语、西班牙语以及代码/元数据排除。**这不是独立人工抽检，不能将自动标签当成人工金标准或宣称准确率。**
- 短文本、技术词、引用示例、多语说明以及清洗规则都可能影响结果。全部内容已经过分类，计数不是从样本外推的。

### 11.2 数据与复现

- [语言汇总 CSV](data/skill_languages_gt100.csv)
- [方法与计数 JSON](data/skill_languages_gt100_summary.json)
- [128,382 条逐项标签（压缩 CSV）](data/skill_languages_gt100_items.csv.gz)：含仓库、路径、内容哈希、标签、正文字符数及各识别语言片段字符数。以 gzip 压缩后上传，避免提交约 57 MB 的未压缩文件。
- [统计脚本](scripts/skill_languages_gt100.py)与[分类测试](scripts/test_skill_languages_gt100.py)。

在已有 PyArrow 的环境中，从本仓库根目录运行（原路径仍通过软链接指向数据盘）：

```bash
python3 -m pip install -r gitskills_domain_star_profile_20261028/scripts/requirements-language.txt
PYTHONDONTWRITEBYTECODE=1 python3 gitskills_domain_star_profile_20261028/scripts/skill_languages_gt100.py \
  --data /home/satoru/agent/gitskills-parquet/data \
  --output gitskills_domain_star_profile_20261028/data --workers 6
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s gitskills_domain_star_profile_20261028/scripts -p 'test_skill_languages_gt100.py'
```

脚本检查仓库总数、128,382 条代表项及其内容哈希唯一性；缺少已选代表项正文时明确报错，不静默当作无法判断。网页新增“>100 星：编写语言”页，沿用现有饼图、中文/英文切换和高星筛选导航，原页面序号不变。
