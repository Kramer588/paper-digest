# paper-digest 1.3.0

**把论文读成自己的能力、把英语写作练成可迁移技能的学习型 skill。**

面向**刚开始读英文论文、刚开始写英文论文**的研究生/本科生：先诊断水平，再按技能阶梯（阅读 R0–R4 / 写作 W0–W4）用「范例 → 引导 → 独立产出 → 评审反馈 → 间隔复习」把论文读懂、把写作练会。

- 版本：**1.3.0**（更新自 1.2.0；变更见 [CHANGELOG.md](./CHANGELOG.md)）
- 适用：论文精读、文献地图、学术英语写作入门、审稿式改写
- 许可证：**MIT**（© 2026 Kr）
- 依赖：联网（学术 API/检索）；无需安装额外包；HTML 课程用浏览器打开

---

## 为什么做这个 skill

通用论文总结工具停在“这篇论文讲了什么”；写作课又常脱离论文空练。学习者真正的问题是：

1. **读不懂**：不知道先看什么、哪些图是关键、哪条证据支撑哪条结论；
2. **用不上**：读完不知道和自己项目什么关系、下一步做什么；
3. **不会写**：看得懂却写不出，句子冗余、主语悬垂、claim 与证据不匹配。

paper-digest 把这三件事接成一条学习链：**读懂 → 关联 → 迁移 → 写作逆向工程 → 间隔复习**。它不是“替你读/替你写”，而是让你**下一次能独立读、独立写**。

## 核心能力

- **论文—项目关联**：基于 `RESEARCH-AGENDA.md`，写清相似点/差异点、六类逻辑联系（precursor/parallel/follow-up/alternative/baseline/tool）、可执行迁移动作与风险。
- **三遍读法**：第一遍声称（5–10 min）→ 第二遍结构与方法骨架 + claim–evidence 表（30–45 min）→ 第三遍重建、反事实、迁移（60–90 min）。
- **1.3.0 HTML digest**：三层总结、三遍记录、claim–evidence 表、论证地图、前置概念、teach-back 问答（选择题 + 自测）、**英文写作 Q&A（data-write）**、新手友好度。
- **技能阶梯与掌握度**：阅读 R0–R4、写作 W0–W4；`MASTERY.md` 只按证据升级；每级有判据。
- **间隔复习**：`review/QUEUE.md`（D1/D3/D7/D21）+ `[quiz]` 交错抽题 + `ERROR-LOG.md` 错误码驱动下一课。
- **写作训练**：W0 句子（E1 冗余/E2 垂悬/E3 过度声称等）→ W1 段落 → W2 IMRaD 动作 → W3 评审 → W4 独立；四维 rubric + 分层反馈，不替用户写整段。
- **延伸检索 + 阅读路线图**：学术 API 优先（OpenAlex/Semantic Scholar/Crossref/arXiv/Europe PMC），每条标核实状态与“建议读多深”，按 ZPD 排优先级。
- **七种显式模式**：`[read] [write] [learn] [quiz] [review] [plan] [map]`；自然语言同样生效。

## 快速开始

### 1) 安装

把本目录放进 skill 目录，保持 `SKILL.md` 在根部、`agents/`、`references/`、`assets/`、`scripts/` 为子目录：

```text
<project>/.agents/skills/paper-digest/
~/.agents/skills/paper-digest/
```

### 2) 初始化工作区（首次一次）

在你要当作“研究工作区”的目录：

```bash
mkdir -p digests lessons reference assets review sessions writing/drafts writing/reviews state
cp <skill>/assets/lesson.css <skill>/assets/quiz.js assets/     # 课程样式与交互
```

再让 agent 执行 `[plan]` 生成 `LEARNER-PROFILE.md`、`PLAN.md` 等状态文件；或手动从 `references/*-FORMAT.md` 复制模板。最后校验：

```bash
python <skill>/scripts/check_workspace.py <workspace>
# RESULT: PASS 后再开始
```

### 3) 第一次使用

```text
[plan] 我是<方向>，<英语/读论文/写作现状>，每周<时间>，目标<目标>
[read] 这篇：<DOI / arXiv / PDF>——按三遍读法精读，先 R1
[write] 用刚读的论文练 Results：先给范例，再让我写 3 句
[quiz] 考我上次的 claim 和写作句式
[review] 帮我按评审员标准看这段 Abstract
[map] 接下来该读哪 5 篇？按先读什么排
```

无触发词时：给论文→`[read]`；给草稿→`[review]`；都没有→`[plan]`。

## 触发词

| 触发词 | 模式 | 职责 | 主产物 |
|---|---|---|---|
| `[read]` / `[digest]` | 论文精读 | 三遍读法 + **HTML digest** + 关联 + 延伸检索 | `digests/NNNN-*.html` |
| `[write]` | 写作训练 | W0–W4 局部任务与评审反馈 | `lessons/NNNN-*.html` + `writing/PROGRESS.md` |
| `[learn]` | 概念补课 | 补前置概念/推导/实验设计 | `lessons/NNNN-*.html` |
| `[quiz]` | 复习检测 | 从队列抽题、间隔复习 | `lessons/NNNN-quiz-*.html` |
| `[review]` | 审稿/改写 | 评审员分层反馈 + 修订清单 | `writing/reviews/NNNN-*.md` |
| `[plan]` | 诊断/规划 | 学习者画像 + 课程地图 + 下次计划 | `PLAN.md`、`LEARNER-PROFILE.md` |
| `[map]` | 文献地图 | 按 ZPD 排阅读路线 | `reference/reading-map.html` |

## 工作区结构

```text
<workspace>/
├── RESEARCH-AGENDA.md          # 项目画像（研究问题/方法/瓶颈/评估/目标）
├── LEARNER-PROFILE.md          # 学习者画像（英语/读论文/写作/时间/偏好/诊断）
├── PLAN.md                     # 课程地图与本周任务
├── MASTERY.md                  # R/W 技能掌握矩阵（只按证据升级）
├── ERROR-LOG.md                # 写作/阅读错误日志（E1–E8）
├── digests/                    # HTML 论文解读档案（NNNN-slug.html，含问答与英文写作练习）
├── RESOURCES.md                # 文献库（核实状态/检索来源/建议优先级）
├── learning-records/           # 决策级学习记录
├── lessons/                    # 教学/答题主产物（自包含 HTML）
├── reference/                  # 术语表、方法对比、问题谱系、写作句式
├── review/QUEUE.md             # 间隔复习队列（D1/D3/D7/D21）
├── review/SESSIONS.md          # 复习会话记录
├── sessions/                   # 会话日志（模式/产出/表现/下一步）
├── writing/PROGRESS.md         # 写作进度（W 级、已完成、待复习）
├── writing/drafts|reviews/     # 草稿与模拟评审
├── assets/                     # lesson.css / quiz.js
├── state/SESSION.md            # 当前模式与下一步
└── NOTES.md                    # 用户偏好与工作笔记
```

## 学习系统怎么运转

```text
[plan] 诊断 → 定 R/W 起点与本周目标（ZPD）
   │
   ├─ [read] 三遍读法 → digest（claim-evidence/论证地图/teach-back）
   │        └─ [map]/检索 → 阅读路线图
   ├─ [write] 范例 → 引导 → 独立改写/段落 → rubric 反馈
   ├─ [learn] 卡点概念 → 15 分钟 HTML 课 + 闭卷检索
   └─ [quiz] 队列到期项（交错）→ 掌握度/错题/排期
        │
        └─ 每课固定：复习 → 目标 → 范例 → 引导 → 独立 → 反馈 → 记录 → 排期
```

- **掌握等级**：0 未接触 / 1 能认 / 2 能复述或照做 / 3 能独立应用 / 4 能迁移与教别人。
- **升级门槛**：本级判据达成 + 队列连续 3 次正确（D1/D3/D7）。
- **交错**：复习混合“阅读概念 + 写作句式 + 论文证据”，不只刷一篇。
- **教别人**：每升一级做一次 3 分钟 teach-back。

### 阅读阶梯（摘要）

| 级 | 目标 | 产出 |
|---|---|---|
| R0 摘要级 | 知道论文声称什么 | 3 句复述 |
| R1 结构级 | 看懂章节功能与论证顺序 | 结构图 + 10 问 |
| R2 方法级 | 重建方法与证据 | 骨架图 + claim–evidence 表 |
| R3 批判级 | 判断结论边界 | 批判清单 ≥5 条 |
| R4 迁移级 | 用到自己项目 | 1–3 条可执行动作 |

### 写作阶梯（摘要）

| 级 | 目标 | 典型任务 |
|---|---|---|
| W0 句子 | 写清楚一句英文 | E1/E2/E3 识别 + 改写 |
| W1 段落 | 段落有功能 | 主题句 + 3–5 句支撑 |
| W2 章节动作 | IMRaD 动作 | CARS/Results/Discussion/Abstract |
| W3 评审 | 以评审员标准自审 | 3 条拒稿理由 + 修订 |
| W4 独立写作 | 完成 section 草稿 | 200–300 词定稿 |

## 质量与学术底线

- **论文内容以原文为准**；没有来源的句子写“推测：…”。
- **区分声称与证据**：每条贡献标证据位置与强度（充分/部分/不足）。
- **禁止编造 DOI/作者/年份/数据**；检索不到写“未检索到可靠来源”+建议检索式。
- **关联必须具体**；写不出具体对应就如实说“关联弱”。
- **教学必须有产出与反馈**；反馈必须引用规则或错误码（E1–E8）。
- **不替用户写整段**；给修改方向与对照版本。
- **每课更新队列/掌握度/日志**；没有记录视为没发生。

## 版本历史

- **1.3.0（2026-11-23）**：主产物（digest / lesson / quiz / reference）统一为可交互 HTML；digest 内置 teach-back 问答与英文写作 Q&A，落实写作板块的问答机制；交互组件与打印样式增强。
- **1.2.0（2026-11-23）**：触发词系统、学习者画像/诊断、R/W 阶梯与掌握度、间隔复习队列、digest 1.2.0、写作 rubric/错误码/句式库、7 个 agents、HTML 资产与工作区校验。
- **1.1.0（基线）**：研究议程 + 12 节 digest + 论文—项目关联 + 延伸检索 + HTML lessons + 写作模式 A–D。

## 从 1.2.0 / 1.1.0 迁移

1. 旧工作区可直接使用：新增文件按需创建，旧 lesson 保留。
2. **旧 digest（.md）** 标“legacy 待迁移”；重读该论文时按 1.3.0 的 HTML 模板迁移（含 TOC、claim–evidence 表、teach-back 问答、`data-write` 英文练习）。**新 digest 必须写 .html。**
3. 复制 `assets/lesson.css`、`assets/quiz.js` 到工作区 `assets/`（否则 HTML 课样式/交互失效）。
4. 跑 `python scripts/check_workspace.py <workspace>`；先处理 FAIL，legacy 警告可暂留。
5. 旧 `writing/` 进度可沿用；新增 `ERROR-LOG.md`、`review/QUEUE.md`、`sessions/`、`state/SESSION.md`。

## 常见问题

**Q：需要联网吗？**
A：`[read]` 的延伸检索与 `[map]` 需要联网（学术 API 优先）；离线时可完成 digest 与教学，检索写成“建议检索式”。

**Q：会不会编造论文内容/DOI？**
A：硬规则禁止；所有论文论断要标来源，所有文献条目要标核实状态；读不到全文就标“摘要级/待全文核实”。

**Q：零基础能用吗？**
A：可以。`[plan]` 会先诊断，默认从 R0 + W0 起步；每课 ≤15 分钟、一个目标、≤5 个新术语。

**Q：和通用论文总结工具有什么区别？**
A：通用工具给“摘要”；本 skill 给“可复习的教材 + 可执行的迁移动作 + 可训练的写作反馈”，并以掌握度与间隔复习保证长期留存。

**Q：为什么主产物（含 digest）必须是 HTML？**
A：HTML 能承载问答/即时反馈/英文写作练习（`data-quiz`/`data-write`），排版更适合复习与打印；Markdown 只保留给状态与草稿。

**Q：需要 PDF 吗？**
A：PDF/DOI/arXiv/链接都可以；只有摘要时会标“摘要级”，不会用参数化知识补全。

**Q：我能改课程吗？**
A：可以。课程/规则都在 `references/`（CURRICULUM、WRITING-RUBRIC、QUIZ-FORMAT 等），agents 在 `agents/`；改完跑 `scripts/check_workspace.py` 做结构校验。

## 目录结构（skill 包）

```text
paper-digest/
├── SKILL.md                     # 主手册（触发词/学习循环/阶梯/门禁）
├── README.md                    # 本文件
├── CHANGELOG.md
├── VERSION
├── LICENSE                     # MIT（© 2026 Kr）
├── agents/                      # 7 个角色
│   ├── learning-designer.md     # 诊断/课程/ZPD/复习排期
│   ├── paper-reader.md          # 三遍读法/claim-evidence/前置概念
│   ├── context-linker.md        # 论文—项目关联
│   ├── literature-scout.md      # 延伸检索 + 阅读路线图
│   ├── digest-writer.md         # digest 合成
│   ├── writing-coach.md         # W0–W4 写作教练/评审
│   └── quiz-master.md           # 检索练习/复习单元
├── references/                  # 12 个格式与规范
│   ├── CURRICULUM.md
│   ├── LEARNER-PROFILE-FORMAT.md
│   ├── READING-PROTOCOL.md
│   ├── DIGEST-FORMAT.md
│   ├── WRITING-RUBRIC.md
│   ├── PHRASEBANK-FORMAT.md
│   ├── QUIZ-FORMAT.md
│   ├── REVIEW-QUEUE-FORMAT.md
│   ├── RESEARCH-AGENDA-FORMAT.md
│   ├── RESOURCES-FORMAT.md
│   ├── LEARNING-RECORD-FORMAT.md
│   └── SESSION-LOG-FORMAT.md
├── assets/                      # lesson.css / quiz.js
├── scripts/check_workspace.py   # 工作区结构校验
└── docs/DESIGN-AND-TRIAL.md     # 设计说明与试跑记录
```

## 许可证

本项目采用 **MIT License**，版权归 **Kr**（© 2026）。完整条款见 [LICENSE](./LICENSE)。

可以自由使用、修改、再分发（保留版权与许可声明即可）；本包未内置第三方代码，`assets/` 为本 skill 原创。
