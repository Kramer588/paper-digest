# paper-digest 1.3.0 · 设计说明与第一轮试跑结果（发布版）

> 日期：2026-11-23 ｜ 对象：`paper-digest` skill（原版在 `D:\Users\KK\Desktop\paper-digest`，另有 `teach` 教学 skill 作参照）
> 交付：`paper-digest/`（skill 包）、`trial workspace/`（试跑工作区）、`paper-digest-1.2.0.zip`

---

## 一、复查结论：原版强在哪、对"新生"缺什么

**原版已经很好的地方**（保留）：
- 研究议程（`RESEARCH-AGENDA.md`）作为一切解读的地基；论文—项目关联六类（precursor/parallel/…）；延伸检索"学术 API 优先、核实状态、禁止编造 DOI"；digest 来源标注；lesson 用 HTML + 检索练习；写作模式 `[write]` 四模块 A–D；学习记录（ADR 式）。
- 这些是**研究者工具**的正确骨架，1.2.0 不推翻。

**对"刚开始读论文/写论文"的新生，原版有 5 个缺口**：
1. **没有学习者画像与诊断**：只有项目议程，没有"用户英语如何、读过几篇、写作到哪一步"，无法决定讲多深。
2. **没有技能阶梯与掌握标准**：digest/lesson 做得很深，但不知道"读到 R1 算会了、W1 要满足什么"。
3. **没有间隔复习系统**：lesson 里有检索练习，但学完就丢；没有 D1/D3/D7/D21 队列、错题日志、掌握度矩阵。
4. **写作训练起点偏高**：A–D 直接进 IMRaD 与评审，缺少 W0 句子层（冗余/垂悬/hedging）、W1 段落层（主题句/衔接）这些新生真正卡住的地方；词汇训练没有"搭配/慎用/场景"的硬约束。
5. **触发词只有 `[write]`**：阅读、补课、复习、审稿、规划、文献地图没有显式入口，主 agent 靠猜。

## 二、设计思路：把"学习科学"落成可执行机制

| 原则 | 1.3.0 机制 |
|---|---|
| **先诊断，再教学**（ZPD） | `[plan]` 6 问 → `LEARNER-PROFILE.md` → 三档默认路径（零基础/入门/进阶） |
| **技能阶梯 + 掌握学习** | 阅读 R0–R4、写作 W0–W4；每级有目标/产出/判据；`MASTERY.md` 只按证据升级 |
| **检索练习 + 间隔** | 每课先复习；`review/QUEUE.md`（D1/D3/D7/D21）；`[quiz]` 交错抽题；错题 `ERROR-LOG.md` |
| **范例 → 半成品 → 独立**（fading） | lesson 固定结构：标注范例 → 引导练习 → 独立产出 → rubric 反馈 |
| **认知负荷管理** | 新生每课 ≤15 分钟、1 个目标、≤5 个新术语；一次只一级 |
| **教别人（teach-back）** | digest 5 个 teach-back 问题 + 升级前 3 分钟复述 |
| **写作是逆向工程** | 从已读论文拆 IMRaD 动作、坏句→好句、功能句式库；四维 rubric + E1–E8 错误码 + 修订循环 |
| **状态可见** | 每次会话更新 `state/SESSION.md`、`sessions/`、`PLAN.md`、队列、掌握度；下次从状态接续 |

## 三、1.3.0 的结构（与 1.2.0 / 1.1.0 的差异）

### 1) 触发词系统（新增）

`[read]/[digest]` 精读 · `[write]` 写作 · `[learn]` 概念补课 · `[quiz]` 复习检测 · `[review]` 审稿/改写 · `[plan]` 诊断/规划 · `[map]` 文献地图。自然语言同义词生效；显式触发优先；一次只进一个模式；`state/SESSION.md` 记录模式。

### 2) 学习者与课程（新增）

- `LEARNER-PROFILE.md`（6 问诊断 + 画像）
- `PLAN.md`（当前 R/W 级、本周任务、排队）
- `MASTERY.md`（R/W 矩阵 + 证据）
- `references/CURRICULUM.md`（R0–R4 / W0–W4 的目标、任务、判据、课时、推进规则）

### 3) 复习与评估（新增）

- `review/QUEUE.md`（字段 + D1/D3/D7/D21 调度）
- `review/SESSIONS.md`（每次抽题、正确率、调整）
- `ERROR-LOG.md`（E1–E8 错误码驱动下一轮）
- `references/QUIZ-FORMAT.md`（回忆/辨析/纠错/改写/迁移/teach-back 六型；等长选项、干扰项精确错误）

### 4) 阅读与写作的规范升级

- `references/READING-PROTOCOL.md`：三遍读法时间盒 + 5/10/5 问题 + claim–evidence 表 + 标注约定 + 新手模式。
- `references/DIGEST-FORMAT.md`（1.2.0）：三层总结、三遍记录、claim–evidence 表、论证地图、前置概念、teach-back 5 题、新手友好度。
- `references/WRITING-RUBRIC.md`：四维 rubric（内容/组织/语言/规范）+ E1–E8 + 分层反馈 + 自审清单 + 模拟评审。
- `references/PHRASEBANK-FORMAT.md`：按功能收句式（引入/缺口/方法/结果/比较/hedging/局限/结论），每条带场景、搭配、慎用、例句来源。

### 5) 角色与资产

- 7 个 agents：`learning-designer`（新）、`paper-reader`（升级三遍/claim-evidence/前置概念）、`context-linker`、`literature-scout`（升级阅读路线图）、`digest-writer`（1.2.0 模板）、`writing-coach`（W0–W4 + rubric）、`quiz-master`（新）。
- `assets/lesson.css`、`assets/quiz.js`：统一课程外观与交互。
- `scripts/check_workspace.py`：工作区结构校验（兼容 v1 旧 digest，标"待迁移"）。

## 四、第一轮试跑（真实执行，1.3.0 HTML 主产物）

**工作区**：复制现有 rDNA 研究工作区（5 篇 digest + RESOURCES + 议程）→ `trial workspace/`。
**试跑论文**：Vitales et al. 2026, *Genome architecture modulates 35S and 5S rDNA homogenization in Asteraceae*, Plant J 128: e71174, DOI 10.1111/tpj.71174（Europe PMC OA 全文，与用户项目高度相关）。
**画像（模拟该用户）**：CET-6、没写过英文论文、读过 6 篇（摘要级）、每周 6 h；诊断 R0→R1、W0→W1。

### 产出（第一轮）

| 类型 | 文件 | 内容 |
|---|---|---|
| 画像/计划 | `LEARNER-PROFILE.md`、`PLAN.md`、`MASTERY.md`、`state/SESSION.md` | 6 问诊断；R1/W0 起点；本周 5 项任务；掌握矩阵 |
| digest | `digests/0006-genome-architecture-rdna-homogenization-asteraceae.html` | 1.3.0 的 17 节（HTML + 交互）：三层总结、三遍记录、C1–C5 + claim–evidence 表、论证地图（标最脆弱环）、前置概念 5 个、teach-back 5 题、延伸阅读 6 条（含 DOI/核实状态/优先级） |
| **HTML digest（含问答/英文写作）** | `digests/0006-*.html` | TOC、claim–evidence 表、teach-back（3 选择 + 5 details）、英文写作 Q&A（3 个 data-write）、延伸阅读 |
| 阅读课 | `lessons/0001-three-pass-reading.html` | 三遍读法 + 摘要 5 句功能标注 + 3 道判断题 + 闭卷复述 + 自评标准 |
| 写作课 | `lessons/0002-writing-results-move.html` | E1/E2/E3 坏句→好句、3 道纠错题、3 句独立改写、自检清单 |
| 句式库 | `reference/writing-phrases.html` | 6 组功能、12 条表达，每条含场景/搭配/慎用/例句 |
| 队列 | `review/QUEUE.md`、`review/SESSIONS.md` | 10 条（claim 4 / concept 1 / evidence 1 / phrase 2 / error 2），D1/D3 排期 |
| 学习记录 | `learning-records/0002-context-dependent-concerted-evolution.md` | 掌握证据 + 解锁/排除/下次 |
| 会话日志 | `sessions/0001-read-vitales2026.md` | 目标、复习、范例、练习、反馈、掌握证据、落盘、下次 |

### 第二轮（间隔复习）

- `[quiz]` D1：6 题混合（claim 2 / concept 1 / evidence 1 / phrase 1 / error 1）→ 模拟结果 **5/6**；错 Q5（E3 过度声称）。
- 队列更新：5 项升 D3；新增 Q-0009（E3）、Q-0010（in contrast to）D1；`ERROR-LOG` 新增 E3；`MASTERY` R1 1→2、W0 1→2；`sessions/0002-spaced-review.md`。
- **这演示了闭环**：错题 → 错误码 → 下一课专项 → 队列重排。

### 校验

`python scripts/check_workspace.py trial workspace` → **RESULT: PASS**（6 个结构文件 + 2 个 assets + 1 篇 1.3.0 HTML digest + 3 个 lesson 通过；旧的 5 篇 1.1.0 digest 标"legacy 待迁移"，不阻塞）。
- **HTML 视觉验证**：用 Edge headless 截图 + print-to-pdf 检查 `lessons/0001` 与 HTML digest：digest 的目录、claim 表、teach-back 选择题/折叠自测、英文写作 textarea + 参考按钮均正常（截图 `digests/_check_top2.png`、`digests/_digest_p-6.png`、`_digest_p-7.png`）。试跑中曾因工作区缺 `assets/` 导致样式失效——这是初始化步骤缺失，1.2.0 已在「二点五、首次运行」写入复制 assets 的硬步骤，并让 `check_workspace.py` 检查资产。

## 五、从"老师/评审员"角度的判断

- **对新生最关键的三个改动**：①先诊断再教（防止一上来讲 Methods）；②每课必须有产出与反馈（防止"讲解=学习"）；③间隔复习 + 错误码（防止"看过就忘"、同类错误反复犯）。
- **写作训练的关键调整**：从 W0 句子层开始，先修"评审员一眼看到"的 E1/E2/E3，再进 IMRaD 动作；这比直接教"A 框架"更符合零基础——先能写对一句，再能写对一段。
- **digest 的关键调整**：三层总结 + teach-back 5 题 + 新手友好度，让 digest 从"资料"变成"可复习的教材"。
- **没有放松学术底线**：来源标注、claim–evidence 强度、禁止编造 DOI、关联必须具体——这些原版硬规则全部保留。

## 六、局限与下一步

1. **用户是模拟画像**：没有真实新生交互；下次用真实用户跑一轮（画像诊断 → 2 周计划 → 第一次复习）。
2. **HTML 只视觉验证了 lesson 0001**：0002/0003 未逐页截图；首次使用时建议打开检查。已把「复制 assets + 跑 checker」写成首次运行硬步骤（本轮试跑曾因漏复制 assets 导致样式失效，已修正）。
3. **旧的 5 篇 1.1.0 digest 未迁移**：1.2.0 规定"重读时迁移"；`check_workspace.py` 已把它们标 legacy，不阻塞新内容。
4. **`[map]` 与 `[learn]` 只给了规范与示例，未跑完整会话**：下一轮补这两条路径的试跑。
5. **写作 W2–W4 未试跑**：本轮只到 W0/W1；下一轮用用户真实草稿跑 W1→W2。

## 七、怎么开始用

```text
[plan] 我是<方向>，<英语/读论文/写作现状>，每周<时间>，目标<目标>
[read] 这篇：<DOI/arXiv/PDF>——按三遍读法精读，先 R1
[write] 用刚读的论文练 Results：先给范例，再让我写 3 句
[quiz] 考我上次的 claim 和写作句式
[review] 帮我按评审员标准看这段 Abstract
[map] 接下来该读哪 5 篇？按先读什么排
```

## 八、文件清单

- skill 包：paper-digest/（SKILL.md、README.md、CHANGELOG.md、VERSION、agents×7、references×12、assets×2、scripts×1、docs×1）
- 试跑工作区：`trial workspace/`（含 0006 digest、3 个 lesson、队列、掌握度、两轮会话日志）
- 压缩包：`paper-digest-1.2.0.zip`
