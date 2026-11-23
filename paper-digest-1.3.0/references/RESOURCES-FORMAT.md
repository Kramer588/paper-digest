# RESOURCES-FORMAT.md

`RESOURCES.md` 是文献与社区库；digest 的延伸阅读、lesson 的首要来源、关联参照系都从这里取。

## 结构

```md
# {方向} Resources

## Knowledge
- {标题}（{作者}，{年份}，{venue}）。DOI：{…}。链接：{…}。检索来源：{OpenAlex/S2/Crossref/arXiv/Europe PMC/网页}。核实状态：{…}
  3–5 句梗概。与项目关系：{…}。用于：{…}。建议优先级/深度：{P1/R2 …}

## Wisdom (Communities)
- {社区/作者主页/邮件列表}：为什么可信；用于问什么。

## Gaps
- {方向}：未找到可靠来源。建议检索式：{关键词 + venue + 年份}
```

## Rules

- 核实状态与检索来源必填；没有核实状态视为编造。
- 学术 API 优先；网页只作降级；不绕过反爬。
- 禁止编造 DOI/作者/年份；检索不到写"未检索到可靠来源"+检索式。
- 每条写"用于什么"与"建议读多深"（R0–R4），否则三个月后就是垃圾。
- 按 Knowledge / Wisdom 分组；定期修剪。
