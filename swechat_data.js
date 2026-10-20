/* SWE-chat dataset (COLM 2026). Shared by the Chinese and English chart pages. */
window.SWECHAT_SOURCE = {
  tabVenue: "COLM 2026 · BAUMANN ET AL.",
  tabName: {zh: "真实编码轨迹", en: "Coding agents in the wild"},
  tabN: "18K",
  eyebrowLeft: {zh: "COLM 2026  ·  BAUMANN ET AL.", en: "COLM 2026  ·  BAUMANN ET AL."},
  backLabel: {zh: "← 全部会话", en: "← All sessions"},
  citeLabel: {zh: "引用 / CITATION", en: "CITATION"},
  citation: {
    zh: 'Baumann, J., Padmakumar, V., Li, X., Yang, J., Yang, D., &amp; Koyejo, S. (2026). <span class="work">SWE-chat: Coding Agent Interactions From Real Users in the Wild.</span> COLM 2026. arXiv:2604.20779. <a href="https://arxiv.org/abs/2604.20779" target="_blank" rel="noopener">arxiv.org/abs/2604.20779</a>',
    en: 'Baumann, J., Padmakumar, V., Li, X., Yang, J., Yang, D., &amp; Koyejo, S. (2026). <span class="work">SWE-chat: Coding Agent Interactions From Real Users in the Wild.</span> COLM 2026. arXiv:2604.20779. <a href="https://arxiv.org/abs/2604.20779" target="_blank" rel="noopener">arxiv.org/abs/2604.20779</a>'
  },
  downloads: null,
  hideViewbar: true,
  defaultView: "task-clusters",
  viewTabs: [
    {key: "task-clusters", label: {zh: "任务簇", en: "Task clusters"}},
    {key: "overview", label: {zh: "编码模式", en: "Coding modes"}},
    {key: "personas", label: {zh: "用户画像", en: "Personas"}},
    {key: "intents", label: {zh: "Prompt 意图", en: "Prompt intents"}},
    {key: "code-fate", label: {zh: "代码去向", en: "Code fate"}},
    {key: "turns", label: {zh: "轮次治理", en: "Turn oversight"}},
    {key: "tools", label: {zh: "工具调用", en: "Tool calls"}},
    {key: "repo-domain", label: {zh: "仓库领域", en: "Repo domains"}},
    {key: "repo-audience", label: {zh: "目标用户", en: "Audiences"}}
  ],
  views: {
    overview: {
      metric: "pct",
      eyebrowRight: {zh: "编码模式  ·  3 类", en: "CODING MODES  ·  3 CATEGORIES"},
      docTitle: {zh: "真实用户怎样使用编码 Agent？ · SWE-chat · N≈18K", en: "How Do People Use Coding Agents? · SWE-chat · N≈18K"},
      title: {
        zh: '真实用户 <span class="keep">怎样使用编码 Agent<span class="q">？</span></span>',
        en: 'How Do People <span class="keep">Use Coding Agents<span class="q">?</span></span>'
      },
      dek: {
        zh: '<b>N ≈ 18,000</b> 个真实会话&nbsp;&nbsp;·&nbsp;&nbsp;229K+ prompts&nbsp;&nbsp;·&nbsp;&nbsp;2M 工具调用&nbsp;&nbsp;·&nbsp;&nbsp;707 个仓库',
        en: '<b>N ≈ 18,000</b> real sessions&nbsp;&nbsp;·&nbsp;&nbsp;229K+ prompts&nbsp;&nbsp;·&nbsp;&nbsp;2M tool calls&nbsp;&nbsp;·&nbsp;&nbsp;707 repositories'
      },
      chartAria: {zh: "真实会话编码模式环形图，约 18000 个会话", en: "Donut chart of coding modes across roughly 18,000 real sessions"},
      centerEyebrow: "SWE-CHAT · REAL SESSIONS",
      centerN: "18K",
      centerLabel: {zh: "CODING MODES", en: "CODING MODES"},
      centerSub: {zh: "25.0% 人类独写 · 33.9% 协作 · 41.1% Vibe coding", en: "25.0% human-only · 33.9% collaborative · 41.1% vibe coding"},
      listAria: {zh: "真实会话编码模式", en: "Coding modes in real sessions"},
      listReason: {zh: "编码模式 / CODING MODE", en: "CODING MODE"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部会话", en: "of all sessions"},
      hint: {
        zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览",
        en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"
      },
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "Vibe coding 已成为最常见的模式：41.1% 的会话中，Agent 撰写了超过 99% 的代码。",
        en: "Vibe coding is now the most common mode: in 41.1% of sessions, the agent wrote more than 99% of committed code."
      },
      insightBody: {
        zh: "但高自主性不等于高效率：Vibe coding 每行已提交代码的成本约为协作模式的 3 倍，且单位代码引入的安全漏洞更多。",
        en: "But autonomy is not efficiency: vibe coding costs roughly 3× more per committed line than collaborative coding and introduces more security vulnerabilities per line."
      },
      stats: [
        {value: "41.1%", label: {zh: "Vibe coding", en: "Vibe coding"}, sub: {zh: "Agent 写 >99% 代码", en: "Agent authors >99% of code"}},
        {value: "33.9%", label: {zh: "协作模式", en: "Collaborative"}, sub: {zh: "人机共同作者", en: "Human and agent co-author"}},
        {value: "25.0%", label: {zh: "人类独写", en: "Human-only"}, sub: {zh: "Agent 不提交代码", en: "No agent-authored code committed"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · 约 18,000 个真实编码会话",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · roughly 18,000 real coding sessions"
      },
      rounding: {
        zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。",
        en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."
      },
      crumb: {zh: "总览", en: "Overview"},
      data: [
        {zh: "Vibe coding", en: "Vibe coding", n: 41.1, color: "#B8524A", note: {zh: "Agent 撰写 ≥99% 的已提交代码", en: "Agent authors ≥99% of committed code"}},
        {zh: "协作模式", en: "Collaborative", n: 33.9, color: "#D19A3F", note: {zh: "Agent 贡献 0–99% 的代码", en: "Agent contributes 0–99% of code"}},
        {zh: "人类独写", en: "Human-only", n: 25.0, color: "#2F4858", note: {zh: "全部提交代码由人类撰写", en: "All committed code is human-written"}}
      ]
    },
    personas: {
      metric: "pct",
      eyebrowRight: {zh: "用户画像  ·  4 类", en: "USER PERSONAS  ·  4 CATEGORIES"},
      docTitle: {zh: "谁在使用编码 Agent？ · SWE-chat", en: "Who Uses Coding Agents? · SWE-chat"},
      title: {
        zh: '谁在使用 <span class="keep">编码 Agent<span class="q">？</span></span>',
        en: 'Who Is <span class="keep">Using Coding Agents<span class="q">?</span></span>'
      },
      dek: {
        zh: '按完整会话行为分类&nbsp;&nbsp;·&nbsp;&nbsp;<b>N ≈ 18,000</b> 个会话',
        en: 'Classified from full session behaviour&nbsp;&nbsp;·&nbsp;&nbsp;<b>N ≈ 18,000</b> sessions'
      },
      chartAria: {zh: "编码 Agent 用户画像环形图", en: "Donut chart of coding-agent user personas"},
      centerEyebrow: "SESSION PERSONAS",
      centerN: "18K",
      centerLabel: {zh: "USER PERSONAS", en: "USER PERSONAS"},
      centerSub: {zh: "专家挑刺者 39.2% · 模糊需求者 21.4%", en: "Expert nitpicker 39.2% · vague requester 21.4%"},
      listAria: {zh: "用户画像分布", en: "User persona distribution"},
      listReason: {zh: "画像 / PERSONA", en: "PERSONA"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部会话", en: "of all sessions"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "Expert nitpicker 占 39.2%：最常见的用户不是甩手掌柜，而是持续修正 Agent 的人。",
        en: "Expert nitpickers account for 39.2%: the most common user is not hands-off, but someone who keeps correcting the agent."
      },
      insightBody: {
        zh: "模糊需求者占 21.4%，会在会话中改变目标的 Mind changer 占 6.7%。真实使用远比“一次给出完整规格”的 benchmark 更凌乱。",
        en: "Vague requesters make up 21.4%, while mind changers who redirect the goal mid-session make up 6.7%. Real use is far messier than benchmarks with complete up-front specs."
      },
      stats: [
        {value: "39.2%", label: {zh: "专家挑刺者", en: "Expert nitpicker"}, sub: {zh: "持续修正，目标稳定", en: "Keeps correcting, goal stays stable"}},
        {value: "21.4%", label: {zh: "模糊需求者", en: "Vague requester"}, sub: {zh: "需求欠明确", en: "Underspecified requests"}},
        {value: "6.7%", label: {zh: "目标改变者", en: "Mind changer"}, sub: {zh: "会话中重定向目标", en: "Redirects the goal mid-session"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · 会话级用户画像",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · session-level personas"
      },
      rounding: {zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。", en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."},
      listNote: {zh: "“Other” 为论文未归入三类画像的会话。", en: "“Other” covers sessions that the paper did not assign to the three named personas."},
      crumb: {zh: "用户画像", en: "Personas"},
      data: [
        {zh: "专家挑刺者", en: "Expert nitpicker", n: 39.2, color: "#B8524A", note: {zh: "持续修正输出，但保持目标稳定", en: "Corrects output repeatedly while keeping the goal stable"}},
        {zh: "其他", en: "Other", n: 32.7, color: "#A79A78", note: {zh: "未归入三个命名画像", en: "Not assigned to a named persona"}},
        {zh: "模糊需求者", en: "Vague requester", n: 21.4, color: "#2F4858", note: {zh: "需求欠明确，把决策交给 Agent", en: "Underspecifies the task and delegates decisions"}},
        {zh: "目标改变者", en: "Mind changer", n: 6.7, color: "#D19A3F", note: {zh: "在会话中改变目标", en: "Redirects the goal mid-session"}}
      ]
    },
    intents: {
      metric: "pct",
      eyebrowRight: {zh: "PROMPT 意图  ·  8 类", en: "PROMPT INTENTS  ·  8 CATEGORIES"},
      docTitle: {zh: "用户让 Agent 做什么？ · SWE-chat", en: "What Do Users Ask Agents to Do? · SWE-chat"},
      title: {
        zh: '用户让 Agent <span class="keep">做什么<span class="q">？</span></span>',
        en: 'What Do Users <span class="keep">Ask Agents to Do<span class="q">?</span></span>'
      },
      dek: {
        zh: '英文 prompt 主题聚类&nbsp;&nbsp;·&nbsp;&nbsp;<b>8</b> 类意图&nbsp;&nbsp;·&nbsp;&nbsp;229K+ prompts',
        en: 'Topic clustering of English prompts&nbsp;&nbsp;·&nbsp;&nbsp;<b>8</b> intents&nbsp;&nbsp;·&nbsp;&nbsp;229K+ prompts'
      },
      chartAria: {zh: "用户 prompt 意图环形图", en: "Donut chart of user prompt intents"},
      centerEyebrow: "PROMPT INTENTS",
      centerN: "229K",
      centerLabel: {zh: "USER INTENTS", en: "USER INTENTS"},
      centerSub: {zh: "理解 18.2% · Git 12.6% · 创建 12.1% · 调试 12.1%", en: "Understand 18.2% · Git 12.6% · Create 12.1% · Debug 12.1%"},
      listAria: {zh: "Prompt 意图分布", en: "Prompt intent distribution"},
      listReason: {zh: "意图 / INTENT", en: "INTENT"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部已分类 prompt", en: "of all classified prompts"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "Agent 不只是写新功能：理解代码（18.2%）和 Git 操作（12.6%）几乎与创建、调试同等常见。",
        en: "Agents do much more than write new features: understanding code (18.2%) and Git operations (12.6%) rival creation and debugging."
      },
      insightBody: {
        zh: "创建与调试各占 12.1%，重构占 8.6%，测试只占 4.0%。真实工作流中，阅读、定位与版本控制本身就是主任务。",
        en: "Creation and debugging each account for 12.1%, refactoring 8.6%, and testing only 4.0%. In real workflows, reading, locating code, and version control are first-class tasks."
      },
      stats: [
        {value: "18.2%", label: {zh: "理解代码", en: "Understand"}, sub: {zh: "解释代码与系统行为", en: "Explain code and system behaviour"}},
        {value: "12.6%", label: {zh: "Git 操作", en: "Git"}, sub: {zh: "提交、分支、PR", en: "Commits, branches, PRs"}},
        {value: "12.1%", label: {zh: "创建 / 调试", en: "Create / debug"}, sub: {zh: "各占 12.1%", en: "12.1% each"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · 英文 prompt 主题聚类",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · topic clustering of English prompts"
      },
      rounding: {zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。", en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."},
      listNote: {zh: "主题基于英文 prompt 聚类；Other 为未归入主要意图的 prompt。", en: "Topics are clustered from English prompts; Other covers prompts outside the named intents."},
      crumb: {zh: "Prompt 意图", en: "Prompt intents"},
      data: [
        {zh: "其他", en: "Other", n: 31.5, color: "#A79A78", note: {zh: "未归入主要意图", en: "Outside the named intents"}},
        {zh: "理解代码", en: "Understand", n: 18.2, color: "#2F4858", note: {zh: "解释代码与系统行为", en: "Explain code and system behaviour"}},
        {zh: "Git 操作", en: "Git", n: 12.6, color: "#5B7C88", note: {zh: "提交、分支、PR 等", en: "Commits, branches, pull requests"}},
        {zh: "创建", en: "Create", n: 12.1, color: "#B8524A", note: {zh: "新增功能或文件", en: "Add features or files"}},
        {zh: "调试", en: "Debug", n: 12.1, color: "#D19A3F", note: {zh: "定位并修复错误", en: "Locate and fix errors"}},
        {zh: "重构", en: "Refactor", n: 8.6, color: "#74855F", note: {zh: "重组代码而不改变行为", en: "Restructure without changing behaviour"}},
        {zh: "测试", en: "Test", n: 4.0, color: "#8D6B84", note: {zh: "编写或运行测试", en: "Write or run tests"}},
        {zh: "连接", en: "Connect", n: 1.1, color: "#C48558", note: {zh: "集成外部服务或 API", en: "Integrate external services or APIs"}}
      ]
    },
    "code-fate": {
      metric: "pct",
      eyebrowRight: {zh: "代码去向  ·  4 类", en: "CODE ATTRIBUTION  ·  4 CATEGORIES"},
      docTitle: {zh: "Agent 写的代码最后留下了多少？ · SWE-chat", en: "How Much Agent-Written Code Survives? · SWE-chat"},
      title: {
        zh: 'Agent 写的代码，<span class="keep">最后留下了多少<span class="q">？</span></span>',
        en: 'How Much <span class="keep">Agent-Written Code Survives<span class="q">?</span></span>'
      },
      dek: {
        zh: '按行归因&nbsp;&nbsp;·&nbsp;&nbsp;排除 human-only 会话&nbsp;&nbsp;·&nbsp;&nbsp;<b>59.4%</b> 最终留下',
        en: 'Line-level attribution&nbsp;&nbsp;·&nbsp;&nbsp;excluding human-only sessions&nbsp;&nbsp;·&nbsp;&nbsp;<b>59.4%</b> survived'
      },
      chartAria: {zh: "Agent 生成代码去向环形图", en: "Donut chart of the fate of agent-produced code"},
      centerEyebrow: "CODE ATTRIBUTION",
      centerN: "100%",
      centerLabel: {zh: "AGENT CODE FATE", en: "AGENT CODE FATE"},
      centerSub: {zh: "59.4% 留下 · 29.8% 被人类删除", en: "59.4% survived · 29.8% deleted by humans"},
      listAria: {zh: "Agent 生成代码去向", en: "Fate of agent-produced code"},
      listReason: {zh: "代码去向 / FATE", en: "CODE FATE"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部 Agent 生成代码", en: "of all agent-produced code"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "只有 59.4% 的 Agent 生成代码最终留在提交里；29.8% 被人类直接删除。",
        en: "Only 59.4% of agent-produced code survives into commits; 29.8% is deleted by humans."
      },
      insightBody: {
        zh: "Vibe coding 的存活率更高（65.0%），但这也可能意味着更少的人工审查。协作模式为 55.9%，人类删除比例最高（31.7%）。",
        en: "Vibe coding has a higher survival rate (65.0%), which may also reflect less human scrutiny. Collaborative sessions survive at 55.9%, with the highest human-deletion share (31.7%)."
      },
      stats: [
        {value: "59.4%", label: {zh: "代码存活", en: "Survived"}, sub: {zh: "全部模式", en: "All modes"}},
        {value: "29.8%", label: {zh: "人类删除", en: "Human deletion"}, sub: {zh: "未被提交", en: "Not committed"}},
        {value: "65.0%", label: {zh: "Vibe 存活率", en: "Vibe survival"}, sub: {zh: "高于协作 55.9%", en: "vs. 55.9% collaborative"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · Table 3（排除 human-only）",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · Table 3 (excluding human-only)"
      },
      rounding: {zh: "百分比由论文报告；Human overwrite 为推导值，合计可能因四舍五入略有偏差。", en: "Percentages are reported by the paper; Human overwrite is derived, and totals may differ slightly due to rounding."},
      listNote: {
        zh: "Human overwrite 由四项归因的剩余比例推导（100% − 59.4% − 8.1% − 29.8% = 2.7%）。按模式：协作 55.9 / 9.3 / 3.1 / 31.7；Vibe 65.0 / 6.2 / 2.1 / 26.7（存活 / 自改写 / 人改写 / 人删除）。",
        en: "Human overwrite is derived as the remainder (100% − 59.4% − 8.1% − 29.8% = 2.7%). By mode: collaborative 55.9 / 9.3 / 3.1 / 31.7; vibe 65.0 / 6.2 / 2.1 / 26.7 (survived / self-overwrite / human overwrite / human deletion)."
      },
      crumb: {zh: "代码去向", en: "Code fate"},
      data: [
        {zh: "最终留下", en: "Survived", n: 59.4, color: "#2F4858", note: {zh: "协作 55.9% · Vibe 65.0%", en: "Collaborative 55.9% · Vibe 65.0%"}},
        {zh: "被人类删除", en: "Human deletion", n: 29.8, color: "#B8524A", note: {zh: "协作 31.7% · Vibe 26.7%", en: "Collaborative 31.7% · Vibe 26.7%"}},
        {zh: "Agent 自我改写", en: "Agent self-overwrite", n: 8.1, color: "#D19A3F", note: {zh: "协作 9.3% · Vibe 6.2%", en: "Collaborative 9.3% · Vibe 6.2%"}},
        {zh: "人类改写", en: "Human overwrite", n: 2.7, color: "#74855F", note: {zh: "推导值 · 协作 3.1% · Vibe 2.1%", en: "Derived · collaborative 3.1% · vibe 2.1%"}}
      ]
    },
    turns: {
      metric: "pct",
      eyebrowRight: {zh: "轮次治理  ·  4 类", en: "TURN OVERSIGHT  ·  4 CATEGORIES"},
      docTitle: {zh: "一半的轮次，人类仍在干预 · SWE-chat", en: "Humans Intervene on Half of All Turns · SWE-chat"},
      title: {
        zh: '一半的轮次，<span class="keep">人类仍在干预<span class="q">。</span></span>',
        en: 'Humans Still <span class="keep">Step In on Half of All Turns<span class="q">.</span></span>'
      },
      dek: {
        zh: 'Claude Code 会话&nbsp;&nbsp;·&nbsp;&nbsp;按轮次统计&nbsp;&nbsp;·&nbsp;&nbsp;<b>50.2%</b> 的 prompt 被打断或反驳',
        en: 'Claude Code sessions&nbsp;&nbsp;·&nbsp;&nbsp;turn-level&nbsp;&nbsp;·&nbsp;&nbsp;<b>50.2%</b> of prompts interrupted or pushed back on'
      },
      chartAria: {zh: "Agent 轮次结果环形图", en: "Donut chart of agent turn outcomes"},
      centerEyebrow: "TURN OUTCOMES",
      centerN: "100%",
      centerLabel: {zh: "USER OVERSIGHT", en: "USER OVERSIGHT"},
      centerSub: {zh: "45.7% 反驳 · 4.5% 打断 · 3.0% 请求澄清", en: "45.7% pushback · 4.5% interruption · 3.0% clarification"},
      listAria: {zh: "Agent 轮次结果分布", en: "Turn outcome distribution"},
      listReason: {zh: "轮次结果 / OUTCOME", en: "TURN OUTCOME"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部轮次", en: "of all turns"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "用户打断或反驳了 50.2% 的 prompt，而 Agent 只有约 3% 的轮次会主动请求澄清。",
        en: "Users interrupted or pushed back on 50.2% of prompts, while the agent proactively asked for clarification in only about 3% of turns."
      },
      insightBody: {
        zh: "自主性与监督严重不对称。Pushback 中最常见的是纠正（correction），Vibe coding 会话里的失败报告比例则明显更高（7.0%）。",
        en: "Autonomy and oversight are deeply asymmetric. Correction is the most common pushback type, while vibe-coding sessions show a much higher failure-report share (7.0%)."
      },
      stats: [
        {value: "50.2%", label: {zh: "打断或反驳", en: "Interrupt or pushback"}, sub: {zh: "全部轮次", en: "All turns"}},
        {value: "45.7%", label: {zh: "软性反驳", en: "Pushback"}, sub: {zh: "Agent 回复之后", en: "After the agent responds"}},
        {value: "3.0%", label: {zh: "主动澄清", en: "Clarification"}, sub: {zh: "Agent 主动停下", en: "Agent-initiated stop"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · Figure 8（Claude Code）",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · Figure 8 (Claude Code)"
      },
      rounding: {zh: "百分比由论文报告；Uninterrupted 为剩余比例推导值，合计可能略有偏差。", en: "Percentages are reported by the paper; Uninterrupted is derived as the remainder, so totals may differ slightly."},
      listNote: {
        zh: "Pushback 细分（与总数重叠，不可相加）：Human-only 纠正 36.6 / 拒绝 7.2 / 失败报告 1.6；Collaborative 35.0 / 7.1 / 1.3；Vibe 38.2 / 1.4 / 7.0。",
        en: "Pushback subtypes (overlapping the total, not additive): human-only correction 36.6 / rejection 7.2 / failure report 1.6; collaborative 35.0 / 7.1 / 1.3; vibe 38.2 / 1.4 / 7.0."
      },
      crumb: {zh: "轮次治理", en: "Turn oversight"},
      data: [
        {zh: "未被打断", en: "Uninterrupted", n: 46.8, color: "#2F4858", note: {zh: "推导值 · 100% 减其余三项", en: "Derived · 100% minus the other three"}},
        {zh: "用户反驳", en: "Pushback", n: 45.7, color: "#B8524A", note: {zh: "纠正 / 拒绝 / 失败报告", en: "Correction / rejection / failure report"}},
        {zh: "用户打断", en: "Interruption", n: 4.5, color: "#D19A3F", note: {zh: "硬性中断 Agent", en: "Hard interruption"}},
        {zh: "Agent 请求澄清", en: "Agent clarification", n: 3.0, color: "#74855F", note: {zh: "主动停下询问用户", en: "Agent stops to ask the user"}}
      ]
    },
    tools: {
      metric: "count",
      unit: {zh: "次调用", en: "calls"},
      eyebrowRight: {zh: "工具调用  ·  20 类", en: "TOOL CALLS  ·  20 CATEGORIES"},
      docTitle: {zh: "Agent 把时间花在哪些工具上？ · SWE-chat", en: "Where Do Agents Spend Their Tool Calls? · SWE-chat"},
      title: {
        zh: 'Agent 把时间花在<span class="keep">哪些工具上<span class="q">？</span></span>',
        en: 'Where Do Agents <span class="keep">Spend Their Tool Calls<span class="q">?</span></span>'
      },
      dek: {
        zh: '<b>N = 1,996,558</b> 次工具调用&nbsp;&nbsp;·&nbsp;&nbsp;20 类&nbsp;&nbsp;·&nbsp;&nbsp;来自论文 Table 5',
        en: '<b>N = 1,996,558</b> tool calls&nbsp;&nbsp;·&nbsp;&nbsp;20 categories&nbsp;&nbsp;·&nbsp;&nbsp;from Table 5'
      },
      chartAria: {zh: "Agent 工具调用类型环形图，共 1,996,558 次调用", en: "Donut chart of agent tool-call types across 1,996,558 calls"},
      centerEyebrow: "TOOL CALLS",
      centerN: "1.99M",
      centerLabel: {zh: "AGENT ACTIONS", en: "AGENT ACTIONS"},
      centerSub: {zh: "bash 15.7% · read 14.7% · edit 14.0%", en: "bash 15.7% · read 14.7% · edit 14.0%"},
      listAria: {zh: "Agent 工具调用类型", en: "Agent tool-call types"},
      listReason: {zh: "工具 / TOOL", en: "TOOL"},
      listN: {zh: "调用", en: "Calls"},
      listPct: {zh: "占比", en: "Share"},
      sliceLabel: "pct",
      sliceGap: 0.18,
      labelCount: 2,
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "读取、编辑与 shell 操作占据绝大多数：bash、read、edit 与 bash:file 合计 56.7%。",
        en: "Reading, editing, and shell work dominate: bash, read, edit, and bash:file together account for 56.7%."
      },
      insightBody: {
        zh: "Agent 像开发者一样行动：先读文件、搜索代码，再编辑并运行构建。AskUserQuestion 只占 0.4%，再次印证 Agent 很少主动求助。",
        en: "Agents act like developers: read files, search the codebase, edit, and run builds. AskUserQuestion accounts for only 0.4%, reinforcing how rarely agents ask for help."
      },
      stats: [
        {value: "1.99M", label: {zh: "工具调用", en: "Tool calls"}, sub: {zh: "1,996,558 次", en: "1,996,558 calls"}},
        {value: "56.7%", label: {zh: "读写与 shell", en: "Read, edit, shell"}, sub: {zh: "前四类合计", en: "Top four categories"}},
        {value: "0.4%", label: {zh: "询问用户", en: "Ask the user"}, sub: {zh: "AskUserQuestion", en: "AskUserQuestion"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · Table 5（1,996,558 次工具调用）",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · Table 5 (1,996,558 tool calls)"
      },
      rounding: {zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。", en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."},
      listNote: {zh: "工具类别来自论文 Table 5；other 为 LSP、进程控制等杂项调用。", en: "Tool categories follow Table 5; other covers miscellaneous calls such as LSP and process control."},
      crumb: {zh: "工具调用", en: "Tool calls"},
      data: [
        {zh: "bash 命令行", en: "bash", n: 313837, color: "#B8524A", note: {zh: "sed / docker / gofmt 等", en: "sed, docker, gofmt, ..."}},
        {zh: "read 读取", en: "read", n: 294394, color: "#2F4858", note: {zh: "Read / read_file", en: "Read / read_file"}},
        {zh: "edit 编辑", en: "edit", n: 279413, color: "#D19A3F", note: {zh: "Edit / MultiEdit / apply_patch", en: "Edit / MultiEdit / apply_patch"}},
        {zh: "bash:file 文件命令", en: "bash:file", n: 245291, color: "#74855F", note: {zh: "cd / ls / cat / find 等", en: "cd, ls, cat, find, ..."}},
        {zh: "git / gh", en: "git / gh", n: 208746, color: "#8D6B84", note: {zh: "版本控制与 GitHub", en: "Version control and GitHub"}},
        {zh: "grep 搜索", en: "grep", n: 154160, color: "#5B7C88", note: {zh: "Grep / bash grep / rg", en: "Grep / bash grep / rg"}},
        {zh: "bash:build 构建", en: "bash:build", n: 117014, color: "#C48558", note: {zh: "go / cargo / npm / make", en: "go, cargo, npm, make"}},
        {zh: "agent 子代理", en: "agent", n: 113675, color: "#6F6A8A", note: {zh: "Task / Agent / SendMessage", en: "Task / Agent / SendMessage"}},
        {zh: "write 写入", en: "write", n: 46106, color: "#A79A78", note: {zh: "Write / write_file", en: "Write / write_file"}},
        {zh: "bash:net 网络", en: "bash:net", n: 31556, color: "#9C7A62", note: {zh: "ssh / curl / wget", en: "ssh, curl, wget"}},
        {zh: "mcp 工具", en: "mcp", n: 27327, color: "#4E6B78", note: {zh: "用户安装的 MCP 服务", en: "User-installed MCP servers"}},
        {zh: "glob 匹配", en: "glob", n: 13535, color: "#B3924E", note: {zh: "Glob", en: "Glob"}},
        {zh: "ToolSearch", en: "ToolSearch", n: 11144, color: "#9A5C5C", note: {zh: "工具检索", en: "Search for tools"}},
        {zh: "AskUserQuestion", en: "AskUserQuestion", n: 8601, color: "#8B8F96", note: {zh: "主动询问用户", en: "Ask the user"}},
        {zh: "TodoWrite", en: "TodoWrite", n: 7898, color: "#7F7668", note: {zh: "任务清单", en: "Task list"}},
        {zh: "Skill", en: "Skill", n: 7241, color: "#C27C6B", note: {zh: "调用技能", en: "Invoke a skill"}},
        {zh: "web 网页", en: "web", n: 6979, color: "#6E8B7A", note: {zh: "WebFetch / WebSearch", en: "WebFetch / WebSearch"}},
        {zh: "ExitPlanMode", en: "ExitPlanMode", n: 2966, color: "#A06E92", note: {zh: "退出计划模式", en: "Leave plan mode"}},
        {zh: "EnterPlanMode", en: "EnterPlanMode", n: 608, color: "#7A8794", note: {zh: "进入计划模式", en: "Enter plan mode"}},
        {zh: "其他", en: "other", n: 106067, color: "#C9BEA9", note: {zh: "LSP / 进程控制等", en: "LSP, process control, ..."}}
      ]
    },
    "repo-domain": {
      metric: "pct",
      eyebrowRight: {zh: "仓库领域  ·  3 类", en: "REPOSITORY DOMAINS  ·  3 CATEGORIES"},
      docTitle: {zh: "这些仓库都是什么类型？ · SWE-chat", en: "What Kinds of Repositories Are These? · SWE-chat"},
      title: {
        zh: '这些仓库<span class="keep">都是什么类型<span class="q">？</span></span>',
        en: 'What Kinds of <span class="keep">Repositories Are These<span class="q">?</span></span>'
      },
      dek: {
        zh: '<b>707</b> 个仓库&nbsp;&nbsp;·&nbsp;&nbsp;按名称、描述与 README 分类',
        en: '<b>707</b> repositories&nbsp;&nbsp;·&nbsp;&nbsp;classified from names, descriptions, and READMEs'
      },
      chartAria: {zh: "仓库领域分布环形图", en: "Donut chart of repository domains"},
      centerEyebrow: "REPOSITORY DOMAINS",
      centerN: "707",
      centerLabel: {zh: "REPO DOMAINS", en: "REPO DOMAINS"},
      centerSub: {zh: "应用 51.8% · 开发者工具 42.1% · 其他 6.1%", en: "Application 51.8% · devtools 42.1% · other 6.1%"},
      listAria: {zh: "仓库领域分布", en: "Repository domain distribution"},
      listReason: {zh: "领域 / DOMAIN", en: "DOMAIN"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部仓库", en: "of all repositories"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "51.8% 是应用，42.1% 是开发者工具——SWE-chat 更贴近真实软件工程，而不是学术玩具项目。",
        en: "51.8% are applications and 42.1% are developer tools—SWE-chat reflects real software engineering, not academic toy projects."
      },
      insightBody: {
        zh: "只有 6.1% 的仓库属于其他领域。绝大多数会话发生在有真实用户、真实发布与真实维护负担的项目中。",
        en: "Only 6.1% of repositories fall outside these two domains. Most sessions occur in projects with real users, releases, and maintenance burdens."
      },
      stats: [
        {value: "707", label: {zh: "仓库", en: "Repositories"}, sub: {zh: "去重后的公开仓库", en: "Deduplicated public repositories"}},
        {value: "51.8%", label: {zh: "应用", en: "Application"}, sub: {zh: "面向用户的软件", en: "User-facing software"}},
        {value: "42.1%", label: {zh: "开发者工具", en: "Devtools"}, sub: {zh: "开发基础设施", en: "Developer infrastructure"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · 仓库领域分类（707 个仓库）",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · repository domains (707 repositories)"
      },
      rounding: {zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。", en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."},
      crumb: {zh: "仓库领域", en: "Repo domains"},
      data: [
        {zh: "应用", en: "Application", n: 51.8, color: "#2F4858", note: {zh: "面向最终用户的软件", en: "Software for end users"}},
        {zh: "开发者工具", en: "Devtools", n: 42.1, color: "#D19A3F", note: {zh: "面向开发者的基础设施", en: "Infrastructure for developers"}},
        {zh: "其他", en: "Other", n: 6.1, color: "#A79A78", note: {zh: "未归入前两类", en: "Outside the two main domains"}}
      ]
    },
    "repo-audience": {
      metric: "pct",
      eyebrowRight: {zh: "目标受众  ·  4 类", en: "TARGET AUDIENCES  ·  4 CATEGORIES"},
      docTitle: {zh: "Agent 在为谁写代码？ · SWE-chat", en: "Who Are Agents Writing Code For? · SWE-chat"},
      title: {
        zh: 'Agent 在为<span class="keep">谁写代码<span class="q">？</span></span>',
        en: 'Who Are Agents <span class="keep">Writing Code For<span class="q">?</span></span>'
      },
      dek: {
        zh: '<b>707</b> 个仓库&nbsp;&nbsp;·&nbsp;&nbsp;按目标受众分类',
        en: '<b>707</b> repositories&nbsp;&nbsp;·&nbsp;&nbsp;classified by target audience'
      },
      chartAria: {zh: "仓库目标受众分布环形图", en: "Donut chart of repository target audiences"},
      centerEyebrow: "TARGET AUDIENCES",
      centerN: "707",
      centerLabel: {zh: "AUDIENCES", en: "AUDIENCES"},
      centerSub: {zh: "开发者 64.4% · 终端用户 25.9%", en: "Developer 64.4% · end user 25.9%"},
      listAria: {zh: "仓库目标受众分布", en: "Repository audience distribution"},
      listReason: {zh: "受众 / AUDIENCE", en: "AUDIENCE"},
      listN: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      readoutBase: {zh: "占全部仓库", en: "of all repositories"},
      hint: {zh: "悬停预览 · 点击上方标签切换分析维度 · Esc 返回总览", en: "Hover to preview · use the tabs above to switch analyses · Esc to return to the overview"},
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "64.4% 的仓库面向开发者，25.9% 面向终端用户；研究与教育项目合计不到 10%。",
        en: "64.4% of repositories target developers and 25.9% target end users; research and education together account for less than 10%."
      },
      insightBody: {
        zh: "编码 Agent 主要被嵌入生产型开发工作流，而不是被当作研究演示或教学工具。",
        en: "Coding agents are mainly embedded in production-oriented development workflows, not used as research demos or teaching tools."
      },
      stats: [
        {value: "64.4%", label: {zh: "面向开发者", en: "Developers"}, sub: {zh: "主要受众", en: "Primary audience"}},
        {value: "25.9%", label: {zh: "面向终端用户", en: "End users"}, sub: {zh: "应用型项目", en: "Application projects"}},
        {value: "9.6%", label: {zh: "研究 + 教育", en: "Research + education"}, sub: {zh: "5.1% + 4.5%", en: "5.1% + 4.5%"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · 仓库目标受众分类（707 个仓库）",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · repository audiences (707 repositories)"
      },
      rounding: {zh: "百分比由论文报告；因四舍五入，合计可能不等于 100%。", en: "Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."},
      crumb: {zh: "目标用户", en: "Audiences"},
      data: [
        {zh: "开发者", en: "Developer", n: 64.4, color: "#2F4858", note: {zh: "面向开发者使用", en: "Built for developers"}},
        {zh: "终端用户", en: "End user", n: 25.9, color: "#B8524A", note: {zh: "面向普通用户", en: "Built for end users"}},
        {zh: "研究者", en: "Researchers", n: 5.1, color: "#5B7C88", note: {zh: "研究型项目", en: "Research-oriented projects"}},
        {zh: "教育", en: "Education", n: 4.5, color: "#74855F", note: {zh: "教学与学习", en: "Teaching and learning"}}
      ]
    },
    "task-clusters": {
      kind: "task-clusters",
      metric: "pct",
      eyebrowRight: {zh: "任务簇  ·  20 类", en: "TASK CLUSTERS  ·  20 GROUPS"},
      docTitle: {zh: "真实 prompts 聚成了哪些任务簇？ · SWE-chat · Figure 23", en: "What Task Clusters Do Real Prompts Form? · SWE-chat · Figure 23"},
      title: {
        zh: '真实 prompts <span class="keep">聚成了哪些任务簇<span class="q">？</span></span>',
        en: 'What Task Clusters Do <span class="keep">Real Prompts Form<span class="q">?</span></span>'
      },
      dek: {
        zh: '<b>20</b> 个主题簇&nbsp;&nbsp;·&nbsp;&nbsp;覆盖 <b>47.6%</b> 的 prompts&nbsp;&nbsp;·&nbsp;&nbsp;规模、pushback、单轮时长与成功率',
        en: '<b>20</b> topic clusters&nbsp;&nbsp;·&nbsp;&nbsp;<b>47.6%</b> of prompts&nbsp;&nbsp;·&nbsp;&nbsp;size, pushback, turn duration, and success'
      },
      chartAria: {zh: "任务簇的四项指标对比", en: "Four-metric comparison of task clusters"},
      listAria: {zh: "任务簇指标表", en: "Task cluster metrics"},
      listReason: {zh: "任务簇 / TASK CLUSTER", en: "TASK CLUSTER"},
      listPrs: {zh: "占比", en: "Share"},
      listPct: {zh: "占比", en: "Share"},
      hint: {
        zh: "悬停预览 · 点击固定任务簇 · Esc 取消固定",
        en: "Hover to preview · click to pin a cluster · Esc to unpin"
      },
      insightKicker: {zh: "关键洞察 / INSIGHT", en: "KEY INSIGHT"},
      insightTitle: {
        zh: "界面视觉打磨和版本控制元数据调试的 pushback 率最高，均为 74%。",
        en: "User-interface refinement and version-control metadata debugging have the highest pushback rates, both at 74%."
      },
      insightBody: {
        zh: "发布就绪（36%）和 PR 评审反馈处理（37%）最低。但这 20 个簇只覆盖 47.6% 的 prompts；其余 32,835 个（52.4%）未形成紧密主题簇。",
        en: "Release readiness (36%) and PR review-feedback handling (37%) are lowest. Yet these 20 clusters cover only 47.6% of prompts; the other 32,835 (52.4%) do not form tight semantic groups."
      },
      stats: [
        {value: "20", label: {zh: "主题簇", en: "Topic clusters"}, sub: {zh: "聚类覆盖的 prompts", en: "Prompts covered by clustering"}},
        {value: "47.6%", label: {zh: "Prompt 覆盖率", en: "Prompt coverage"}, sub: {zh: "32,835 个未聚类", en: "32,835 left unclustered"}},
        {value: "74%", label: {zh: "最高 pushback", en: "Highest pushback"}, sub: {zh: "界面打磨 / 版本元数据", en: "UI refinement / version metadata"}}
      ],
      footerData: {
        zh: "数据：COLM 2026 · Baumann et al. · SWE-chat · Figure 23 · prompt 主题簇",
        en: "Data: COLM 2026 · Baumann et al. · SWE-chat · Figure 23 · prompt topic clusters"
      },
      rounding: {
        zh: "簇规模为 20 个聚类 prompts 内部的占比，而非全部 prompts。百分比由论文报告；因四舍五入，合计可能不等于 100%。",
        en: "Cluster sizes are shares of the 20 clustered prompts, not all prompts. Percentages are reported by the paper; totals may not sum exactly to 100% due to rounding."
      },
      crumb: {zh: "任务簇", en: "Task clusters"},
      detailDefault: {
        kicker: {zh: "20 个主题簇 · 47.6% PROMPTS", en: "20 CLUSTERS · 47.6% OF PROMPTS"},
        title: {zh: "悬停或点击任一任务簇，查看四项指标。", en: "Hover or select a cluster to inspect all four metrics."},
        body: {
          zh: "簇规模为 20 个聚类 prompts 内部的占比。Cluster 10 中 61% 的 prompts 来自 Entire.io 自身仓库；Cluster 14 和 17 也分别由单一仓库主导。",
          en: "Cluster sizes are shares of the 20 clustered prompts. Cluster 10 consists mostly of prompts from Entire.io's own repository; clusters 14 and 17 are also dominated by single repositories."
        }
      },
      clusterNote: {
        zh: "箱体 = 四分位距（IQR），竖线 = 中位数；成功率点 = 会话成功率中位数。悬停可预览，点击固定，Esc 取消固定。",
        en: "Box = interquartile range (IQR), line = median; success dot = median session success. Hover to preview, click to pin, Esc to unpin."
      },
      clusters: [
        {
          label: {zh: "用户界面视觉优化与响应式缺陷修复", en: "User interface visual refinement and responsive bug fixing"},
          size: 14.03, pushback: 74, iqr: [1.6, 8.7], median: 3.7, success: 72, color: "#2F6B8F"
        },
        {
          label: {zh: "基于里程碑的规划与实现", en: "Planning and executing milestone-based implementation work"},
          size: 11.40, pushback: 53, iqr: [1.4, 9.3], median: 3.4, success: 82, color: "#7D9BC4"
        },
        {
          label: {zh: "发布就绪与预发环境验证协调", en: "Coordinating release readiness and staging validation"},
          size: 9.43, pushback: 36, iqr: [1.6, 10.4], median: 4.1, success: 72, color: "#E08A3C"
        },
        {
          label: {zh: "CI 门禁下的 PR 评审与集成", en: "CI-gated pull request review and integration"},
          size: 8.03, pushback: 51, iqr: [1.5, 11.8], median: 4.3, success: 82, color: "#F0B067"
        },
        {
          label: {zh: "自动化测试覆盖的评审与加强", en: "Reviewing and strengthening automated test coverage"},
          size: 6.94, pushback: 38, iqr: [1.4, 10.0], median: 4.3, success: 82, color: "#4E9E5E"
        },
        {
          label: {zh: "容器化部署基础设施的调试与加固", en: "Debugging and hardening containerized deployment infrastructure"},
          size: 6.34, pushback: 66, iqr: [1.3, 7.6], median: 3.0, success: 72, color: "#8CC98F"
        },
        {
          label: {zh: "自动化测试维护与回归覆盖改进", en: "Automated test maintenance and regression coverage improvement"},
          size: 6.08, pushback: 58, iqr: [1.3, 11.0], median: 4.1, success: 82, color: "#C9473F"
        },
        {
          label: {zh: "源码仓库维护、迁移与同步", en: "Source repository maintenance, migration, and synchronization"},
          size: 5.35, pushback: 60, iqr: [1.2, 8.9], median: 3.2, success: 82, color: "#E88D88"
        },
        {
          label: {zh: "身份认证与凭据流程的实现与调试", en: "Implementing and debugging authentication and credential flows"},
          size: 4.30, pushback: 64, iqr: [1.4, 7.5], median: 3.1, success: 79, color: "#8A6BB5"
        },
        {
          label: {zh: "版本控制元数据工作流的调试与优化", en: "Debugging and refining version-control metadata workflows"},
          size: 3.86, pushback: 74, iqr: [2.3, 10.8], median: 5.1, success: 73, color: "#C5AFD6",
          note: {
            zh: "该簇 61% 的 prompts 来自 Entire.io 自身仓库。",
            en: "61% of prompts in this cluster come from Entire.io's own repository."
          }
        },
        {
          label: {zh: "多 Agent 软件开发工作流协调", en: "Coordinating multi-agent software development workflows"},
          size: 3.50, pushback: 65, iqr: [1.2, 7.9], median: 3.2, success: 82, color: "#8C5A45"
        },
        {
          label: {zh: "跨栈回归调试与生产验证", en: "Cross-stack regression debugging and production validation"},
          size: 3.04, pushback: 67, iqr: [1.2, 8.5], median: 3.2, success: 81, color: "#C79A83"
        },
        {
          label: {zh: "AI 编码 Agent 工作流的配置与调试", en: "Configuring and debugging AI coding agent workflows"},
          size: 2.84, pushback: 54, iqr: [1.3, 8.5], median: 3.4, success: 82, color: "#D867B5"
        },
        {
          label: {zh: "声明式工作流与文档一致性审计", en: "Auditing declarative workflows and documentation consistency"},
          size: 2.66, pushback: 50, iqr: [1.6, 7.8], median: 3.3, success: 82, color: "#E9A9CF",
          note: {
            zh: "该簇由单一仓库的 prompts 主导。",
            en: "This cluster is dominated by prompts from a single repository."
          }
        },
        {
          label: {zh: "既有代码库审计与缺陷修复", en: "Existing codebase auditing and defect remediation"},
          size: 2.46, pushback: 58, iqr: [1.3, 7.8], median: 3.0, success: 82, color: "#7E7E7E"
        },
        {
          label: {zh: "会话生命周期工作流的实现与调试", en: "Implementing and debugging session lifecycle workflows"},
          size: 2.04, pushback: 62, iqr: [1.5, 9.2], median: 3.5, success: 73, color: "#BFBFBF"
        },
        {
          label: {zh: "研究论文修订与审稿回复准备", en: "Research manuscript revision and rebuttal preparation"},
          size: 2.02, pushback: 66, iqr: [1.3, 6.2], median: 2.7, success: 82, color: "#B8C42E",
          note: {
            zh: "该簇由单一仓库的 prompts 主导。",
            en: "This cluster is dominated by prompts from a single repository."
          }
        },
        {
          label: {zh: "PR 评审反馈的分类处理与解决", en: "Triaging and resolving pull request review feedback"},
          size: 1.99, pushback: 37, iqr: [2.2, 15.4], median: 6.4, success: 82, color: "#4F7D74"
        },
        {
          label: {zh: "可复用 Agent Skills 的开发与维护", en: "Developing and maintaining reusable agent skills"},
          size: 1.89, pushback: 58, iqr: [1.2, 7.4], median: 2.8, success: 82, color: "#A65E52"
        },
        {
          label: {zh: "全栈集成、测试与发布稳定化", en: "Full-stack integration, testing, and release stabilization"},
          size: 1.79, pushback: 69, iqr: [1.9, 7.7], median: 3.7, success: 82, color: "#6E8FA0"
        }
      ]
    }
  }
};

