---
title: RSS 订阅插件 mkdocs-rss-plugin 的一些问题
number: 65
slug: discussions-65/
url: https://github.com/shenweiyan/Digital-Garden/discussions/65
date: 2024-04-11
authors: [shenweiyan]
categories: 
  - 乱弹
labels: ['mkdocs']
---

聊一下 Mkdocs Material 的默认插件 [mkdocs-rss-plugin](https://github.com/Guts/mkdocs-rss-plugin) 在使用上的一些问题。

<!-- more -->

对于 blog 插件，默认的 RSS 里边提供的地址有一部分会默认为目录链接(例如 `category` 和 `archive`)，而非文章地址。

![rss-item.webp](https://static.weiyan.tech/2024/04/rss-item.webp)

针对这一种情况，需要使用 RSS 配置的 [`match_path`](https://guts.github.io/mkdocs-rss-plugin/configuration/#match_path-filter-pages-to-include-in-feed)，即可解决：

```
plugins:
  - rss:
      match_path: "(blog/posts|flinks|galaxy|message|note|readme|tech|yuque)/.*"
      date_from_meta:
        as_creation: date
      categories:
        - categories
        - tags
```


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="65"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
