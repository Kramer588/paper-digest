# DIGEST-FORMAT.md（1.3.0 · HTML 主产物）

`./digests/NNNN-slug.html` 是**论文解读档案，也是可复习的教材**。必须自包含 HTML，复用 `./assets/lesson.css` 与 `./assets/quiz.js`；**禁止写成 .md**。

## 为什么是 HTML

- 承载**问答机制**：teach-back 选择题（`data-quiz`）+ 自测题（`<details>`）+ 英文写作练习（`data-write`），即点即反馈。
- 美观与可读：目录、徽章、表格、折叠、打印样式统一。
- 可链接：lesson/plan/queue 直接锚点到 `#claims`、`#teachback`、`#writing-qa`。

## 结构模板

```html
<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{标题} · digest</title>
<link rel="stylesheet" href="../assets/lesson.css"></head>
<body class="digest"><main>

<header class="digest-head">
  <h1>{标题}</h1>
  <p class="meta">{作者}｜{年份}｜{venue}｜DOI {doi}｜阅读深度 {全文级/摘要级}｜R {级}｜新手友好度 {易/中/难}</p>
  <p class="badges"><span class="badge">claim {n} 条</span><span class="badge">证据 {充分/部分/不足}</span><span class="badge">{项目关联类型}</span></p>
  <nav class="toc">目录：<a href="#s1">元信息</a> · … · <a href="#claims">claim–evidence</a> · <a href="#teachback">teach-back</a> · <a href="#writing-qa">英文写作 Q&A</a></nav>
</header>

<section id="s1"><h2>1. 元信息</h2>…</section>
<section id="s2"><h2>2. 三层总结</h2>…</section>
<section id="s3"><h2>3. 三遍读法记录</h2>…</section>
…（问题/假设/方法骨架/证据质量/局限/项目关联/前置概念/未解问题/延伸阅读/术语）…
<section id="claims"><h2>8. 贡献—证据表</h2>
  <table class="claim-table"><tr><th>#</th><th>Claim</th><th>Evidence</th><th>强度</th><th>判断</th></tr>
  <tr><td>C1</td><td>…</td><td>§Results/Fig.2</td><td><span class="badge ok">充分</span></td><td>…</td></tr></table>
</section>
<section id="teachback"><h2>14. Teach-back 问答</h2>
  <div class="quiz" data-quiz><p class="q">Q1 …</p>
    <label data-correct="true">…</label><label data-correct="false">…</label>
    <div class="explain">…</div></div>
  <details class="qa"><summary>Q2 …（自测）</summary><p>答案要点：…</p></details>
  …（共 5 个 details）
</section>
<section id="writing-qa"><h2>15. 英文写作 Q&A</h2>
  <div class="write" data-write>
    <p class="prompt">用英文写一句 C2 的 claim（含数字与 hedging）：</p>
    <textarea></textarea>
    <button data-show-model class="ghost">查看参考句与自检</button>
    <div class="model" hidden><p>参考：We found that 5S variability was markedly higher in S-type than in L-type species (1.87 vs 0.08 per 100 bp; P&lt;0.0001).</p>
      <ul class="checklist"><li>有数字与比较方向</li><li>hedging 与证据匹配</li><li>无 E2 垂悬</li></ul></div>
  </div>
  …（≥3 个 data-write：claim / Results / hedging）
</section>
<section id="s16"><h2>16. 延伸阅读</h2>…DOI 链接 + 优先级徽章…</section>
<section id="s17"><h2>17. 关键术语</h2>…链 glossary…</section>

</main><script src="../assets/quiz.js"></script></body></html>
```

## 必需块（缺一即未完成）

- 目录 TOC（≥6 个锚点）；`header.digest-head` 元信息与徽章；
- claim–evidence 表：每条 claim 有证据位置与强度徽章；
- **teach-back**：≥2 道 `data-quiz` 选择题 + 5 个 `<details>` 自测（有答案要点）；
- **英文写作 Q&A**：≥3 个 `data-write`（claim / Results / hedging），每个有参考句 + 自检清单（引用 E1–E8）；
- 延伸阅读：DOI 可点击 + 优先级徽章；
- 术语链接；打印友好（`lesson.css` 已含）。

## 规则

- 每句论文内容标来源；无来源写“推测”。
- 区分声称与证据；强度徽章必须与判断一致。
- 关联写不出具体对应就如实说弱。
- 摘要级阅读标“摘要级”，贡献标“待全文核实”。
- 旧 .md digest：标 legacy，重读时按本模板迁移。

## 校验

`python scripts/check_workspace.py <workspace>`：检查 digest 是否为 `.html`、是否含 TOC/claim-table/teachback/writing-qa/资产引用；`.md` 记 legacy 警告。
