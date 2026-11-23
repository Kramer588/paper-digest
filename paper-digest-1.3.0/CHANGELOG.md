# Changelog

## 1.3.0 — 2026-11-23

更新自 1.2.0。**主产物（学习课程、digest、参考速查）统一为可交互 HTML**，让英语文献写作板块的问答机制真正落地，并提升排版/复习体验。

### 新增
- **HTML digest（主产物）**：`digests/NNNN-slug.html`，含目录锚点、claim–evidence 表（强度徽章）、**teach-back 问答**（≥2 道 `data-quiz` + 5 个 `<details>` 自测）、**英文写作 Q&A**（≥3 个 `data-write`：claim/Results/hedging 句子 + 参考句 + E 码自检）。
- **交互组件**：`quiz.js` 新增 `data-write`（显示参考句与自检清单）、`data-quiz`/`data-recall` 保留；`lesson.css` 新增 digest 专用样式（`digest-head`、`toc`、`claim-table`、`badge`、`write`、`qa`、打印样式）。
- **校验**：`check_workspace.py` 增加 digest HTML 结构检查（TOC/表格/问答/写作块/资产引用）；旧 `.md` digest 标 legacy。

### 变更
- SKILL 新增「六点五、主产物一律 HTML」硬规则：lesson/quiz/digest/reference 主产物必须 HTML；Markdown 仅用于状态与草稿。
- `DIGEST-FORMAT.md` 重写为 HTML 模板规范（结构、必需交互块、锚点、打印、无外链依赖）。
- `digest-writer` 改为产出 HTML digest；`writing-coach` 可把英文 Q&A 写入 digest 的 `data-write` 块。
- README/版本号同步 1.3.0。

### 兼容与迁移
- 1.2.0 工作区可用；旧 `.md` digest 保留但标 legacy，重读时迁移为 HTML。
- 链接从 `digests/*.md` 改为 `digests/*.html`（lesson/plan/queue 内的引用同步）。
- 复制 `assets/` 后跑 `scripts/check_workspace.py`。

## 1.2.0 — 2026-11-23

更新自 1.1.0（基线）。本版把 paper-digest 从「研究者工具」升级为「新手可学的课程系统」，并保持全部学术底线（来源标注、claim–evidence、禁止编造 DOI）。

### 发布
- 采用 **MIT License**（© 2026 Kr），新增 `LICENSE` 文件。

### 新增
- **触发词系统**：`[read]/[digest] [write] [learn] [quiz] [review] [plan] [map]` 七个模式 + 自然语言同义词 + `state/SESSION.md` 模式状态。
- **学习者模型**：`LEARNER-PROFILE.md` 诊断（6 问）+ 三档默认路径（零基础/入门/进阶）+ ZPD 判定。
- **技能阶梯**：阅读 R0–R4、写作 W0–W4，每级目标/任务/产出/掌握判据；`MASTERY.md` 只按证据升级。
- **学习循环**：每课固定「复习→目标→范例→引导→独立→反馈→记录→排期」；范例→半成品→独立（fading）。
- **间隔复习系统**：`review/QUEUE.md`（D1/D3/D7/D21）、`review/SESSIONS.md`、`ERROR-LOG.md`（E1–E8 错误码）。
- **digest 1.2.0 模板**：三层总结、三遍读法记录、claim–evidence 表、论证地图、前置概念、teach-back 5 题、新手友好度。
- **写作课程**：W0 句子（E1/E2/E3…）、W1 段落、W2 IMRaD 动作、W3 评审、W4 独立；四维 rubric + 分层反馈 + 修订清单；`PHRASEBANK-FORMAT`（功能/场景/搭配/慎用）。
- **阅读路线图**：`literature-scout` 按 ZPD 排 3–8 篇，标深度（R0–R4）与优先级。
- **7 个 agents**：新增 `learning-designer`、`quiz-master`；升级 `paper-reader`、`context-linker`、`literature-scout`、`digest-writer`、`writing-coach`。
- **资产与工具**：`assets/lesson.css`、`assets/quiz.js`（统一课程外观/交互）；`scripts/check_workspace.py`（结构校验，兼容旧 digest）。
- **文档**：`references/CURRICULUM.md`、`READING-PROTOCOL.md`、`WRITING-RUBRIC.md`、`QUIZ-FORMAT.md`、`REVIEW-QUEUE-FORMAT.md`、`SESSION-LOG-FORMAT.md`；`docs/DESIGN-AND-TRIAL.md` 设计与试跑记录。

### 变更
- `SKILL.md`：从「论文解读 + 写作模式」扩展为「模式化学习系统」；新增首次运行、学习者模型、每课循环、评估与门禁、版本兼容。
- `writing-coach`：由 A–D 模块扩展为 W0–W4 阶梯，增加 rubric/错误码/修订循环/句式库约束。
- `paper-reader`：增加三遍读法、claim–evidence 表、前置概念、teach-back 问题、新手友好度。
- `literature-scout`：检索结果增加「建议优先级/深度」并输出阅读路线图。
- `DIGEST-FORMAT`：12 节 → 17 节（三层总结/三遍记录/claim–evidence/论证地图/前置概念/teach-back/新手友好度）。

### 兼容与迁移
- 1.1.0 工作区可直接使用；旧 digest 标「legacy 待迁移」，重读时补 1.2.0 字段。
- 首次使用需复制 `assets/` 到工作区并运行 `scripts/check_workspace.py`（见 README「首次使用」）。
- 旧 `writing/PROGRESS.md` 可沿用；新增 `ERROR-LOG.md`、`review/`、`sessions/`、`state/`、`MASTERY.md`。

## 1.1.0 — 基线

- 研究工作区：`RESEARCH-AGENDA.md`、`digests/`、`RESOURCES.md`、`learning-records/`、`lessons/`（HTML）、`reference/`。
- 12 节 digest（元信息/一句话/问题/假设/贡献/方法骨架/证据/局限/项目关联/未解问题/延伸阅读/术语）。
- 论文—项目关联六类（precursor/parallel/follow-up/alternative/baseline/tool）+ 迁移动作 + 风险。
- 学术 API 优先的延伸检索，含核实状态与检索来源；禁止编造 DOI。
- 英语写作模式 `[write]`：A 框架 / B 范例与反例 / C 词汇与搭配 / D 答题检验；HTML 教学单元。
