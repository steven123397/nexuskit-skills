# 网络调研摘要

调用方需要外部调研摘要时使用。它定义摘要内容与体量；是否写文件、路径及回传方式由调用方指定。只保留本次任务相关的栏目，不为补齐栏目扩大调研。

Open the digest with a one-line research value assessment so the caller can weight the findings:

```
**Research value: high** -- [one-sentence justification]
```

Research value levels:
- **high** -- Substantial prior art, named patterns, or directly applicable cross-domain analogies found.
- **moderate** -- Useful background and orientation, but no decisive prior art.
- **low** -- Topic is sparsely covered externally; the caller should not lean heavily on these findings.

Then return findings in these sections, omitting any section that produced nothing substantive:

### Prior Art
What has already been built or tried for this exact problem. Name systems, papers, or projects. Note whether they succeeded, failed, or are still in flux.

### Adjacent Solutions
Approaches to nearby problems that could be ported or adapted. Name the solution, the original problem domain, and why the structural similarity holds.

### Market and Competitor Signals
What vendors, open-source projects, or community patterns are doing today. Pricing, positioning, and capability gaps relevant to the topic. Be specific; vague competitive landscape paragraphs are not useful.

### Cross-Domain Analogies
Patterns from unrelated fields (other industries, biology, games, infrastructure, history) that map onto the topic in a non-obvious way. Skip rather than force.

### Sources
Compact list of sources actually used in the synthesis, with URL and a one-line description. Do not include sources that were searched but not consulted in the final synthesis.

**Token budget:** Keep the digest inside these bounds whether it is returned or written to the caller's file. Target ~500 tokens for sparse results, ~1000 for typical findings, and cap at ~1500 even for rich results. Compress by tightening summaries, not by dropping findings.

When external signal is genuinely thin, return:

"**Research value: low** -- External signal on [topic] is thin after a phased search; the caller should rely primarily on local or internal grounding."

