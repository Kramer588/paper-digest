# REVIEW-QUEUE-FORMAT.md：间隔复习队列

`./review/QUEUE.md` 是学习系统的调度中心。没有队列，学过的会忘。

## 条目字段

```md
## Q-0001
- type: concept | claim | phrase | error | paper
- prompt: {问题/提示}
- answer: {答案要点，≤3 句}
- source: {digest/lesson/paper 位置}
- first_learned: {YYYY-MM-DD}
- interval: D1 | D3 | D7 | D21
- due: {YYYY-MM-DD}
- mastery: 0–3
- history: [{date:result}, …]
- status: active | retired
```

## 调度算法

1. 新学内容：D1 到期；D1 答对（mastery≥2）→ D3；D3 对 → D7；D7 对 → D21；D21 对 → retired。
2. 答错：mastery −1，interval 回 D1，写 `ERROR-LOG.md`。
3. 每天到期项 ≤12 条；超出按"paper > concept > phrase > error"优先级取前 12。
4. 每周至少 1 次交错复习：三类以上混合。

## 会话记录

`./review/SESSIONS.md` 每次追加：
- 日期、抽题数、正确率、错题 id、下次调整、新增队列项。
