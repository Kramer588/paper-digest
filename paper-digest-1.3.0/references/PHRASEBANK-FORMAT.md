# PHRASEBANK-FORMAT.md：功能句式与搭配库

按**修辞功能**组织，不按字母表。每轮 3–5 条；积累到 `./reference/writing-phrases.html`。

## 条目模板

```md
### 功能：{指缺口 / 报告结果 / 比较 / hedging / 局限 / 结论 …}
- **表达**：…（英文）
- **使用场景**：…（用在 Introduction 第 2 段 / Results 报告主结果 / Discussion 解释）
- **搭配**：…（动词+介词、常见宾语）
- **慎用**：…（强度过强 / 只用于一手证据 / 避免口语化）
- **例句**：…（来自已读论文或用户草稿，标明来源）
```

## 功能清单（初版）

| 功能 | 常用表达 | 场景 | 慎用 |
|---|---|---|---|
| 引入重要性 | has attracted increasing attention; remains poorly understood | Intro 第 1 段 | 不堆两句同义 |
| 指缺口 | however, little is known about; previous studies have not addressed | Intro 第 2 段 | 必须真缺口，不能造 |
| 本文贡献 | here we show; we report; we provide | Intro 末/Abstract | 不与 evidence 脱节 |
| 方法 | we reconstructed; we quantified; using … we | Methods/Results | 被动/主动一致 |
| 报告结果 | we found that; increased by X%; compared with | Results | 数字要具体 |
| 比较 | in contrast; consistent with; unlike | Results/Discussion | 比较对象对齐（E5） |
| hedging | may; suggest; likely; appears to | Discussion | 与证据强度匹配 |
| 局限 | limited by; could not exclude; small sample | Discussion 末 | 不自我否定贡献 |
| 结论 | together, these results suggest; our findings provide | Conclusion | 不再引新证据 |
| 过渡 | moreover; in addition; by contrast; therefore | 段间 | 不滥用 therefore（因果） |

## HTML 结构（writing-phrases.html）

- 顶部分类导航（锚点）。
- 每条卡片：功能标签、英文表达、场景、搭配、慎用、例句、来源链接。
- 搜索框（纯前端过滤）与"已掌握"勾选（localStorage）。
- 打印友好。

## Rules

- 不收录孤立单词；每条必须有场景与慎用点。
- 例句优先来自已读论文或用户草稿，标来源。
- 与 digest/lesson 链接；重复表达合并，不堆同义。
