---
title: Mkdocs material 使用自定义 slug 和 url
number: 54
slug: discussions-54/
url: https://github.com/shenweiyan/Digital-Garden/discussions/54
date: 2024-01-23
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

Mkdocs material 默认使用目录+文件名作为 post 展示的 URL，如果目录名/文件名太长的话，你的 URL 就会显得非常长。尤其是当你从浏览器地址栏中复制某一篇文档的链接时候，如果你的 URL 同时包含了中文，URL 转码后会导致你复制后粘贴的链接变得更加长。

<!-- more -->

Mkdocs material 目前我是没看到有什么具体的插件解决这个问题，只不过有人在 [squidfunk/mkdocs-material#5161](https://github.com/squidfunk/mkdocs-material/discussions/5161) 基于 hook 提供了一个解决的方案。这个方案基本上能满足我们的需求，但也有一些限制。

- slug 必须是不能以 `/` 作为开头，且必须以 `/` 作为结尾。
- 可能会导致内部链接引用出现问题。
- 会重复读取任务，如果文件非常多，会降低相对于文件量的整体性能。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="54"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
