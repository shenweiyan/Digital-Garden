---
title: 为 Material for MkDocs 增加博客插件
number: 36
slug: discussions-36/
url: https://github.com/shenweiyan/Digital-Garden/discussions/36
date: 2023-12-06
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

Material for MkDocs 从 9.2.0 开始内置博客插件，内置博客插件添加了对从帖子文件夹构建博客的支持，这些帖子带有日期和其他结构化数据注释。

<!-- more -->

Material for MkDocs makes it very easy to build a blog, either as a sidecar to your documentation or standalone. Focus on your content while the engine does all the heavy lifting, automatically generating archive and category indexes, post slugs, configurable pagination and more.

Material for MkDocs 使构建博客变得非常容易，无论是作为文档的附属工具还是独立的博客。专注于您的内容，而引擎会完成所有繁重的工作，自动生成存档和类别索引、帖子段、可配置的分页等等。

存在的一些问题和使用体验：

1. 在 Markdown 中使用 `<!-- more -->` 的写法分割 description 和全文，总感觉有点别扭；
2. Pagination 分页与 `git-revision-date` 冲突，会引发构建错误 - 参考 [mkdocs-material/discussions#6156](https://github.com/squidfunk/mkdocs-material/discussions/6156)

## 写博客

有感于 Material for MkDocs 的博客结构，现在基本上可以实现使用 Discussions 进行 MkDocs blog 编辑与写作 —— 在 Discussions 上写完文章，借助第三方工具或者 GitHub Actions 导出为 Markdown 文件，保存到 `docs/blog/posts` 就可以啦！

## 加评论

借助 [giscus](https://giscus.app/zh-CN)，可以非常方便在文章页中插入指定的 discussions —— 在导出 discussions 的时候，在文章尾部增加类似以下 JavaScript 即可：
```javascript
<script src="https://giscus.app/client.js"
        data-repo="shenweiyan/Knowledge-Garden"
        data-repo-id="R_kgDOKgxWlg"
        data-mapping="number"
        data-term="4"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="bottom"
        data-theme="light"
        data-lang="zh-CN"
        crossorigin="anonymous"
        async>
</script>
```

## 自定义归档页面

[mkdocs-material](https://github.com/squidfunk/mkdocs-material) 的归档页面跟博客 index 主页面基本是一个样，如果想要列表式的自定义，可以参考 [squidfunk/mkdocs-material#6324](https://github.com/squidfunk/mkdocs-material/discussions/6324) 和 [squidfunk/mkdocs-material#6383](https://github.com/squidfunk/mkdocs-material/issues/6383)。

官方在 [8ecee7b](https://github.com/squidfunk/mkdocs-material-insiders/commit/8ecee7b9dbdc5b2a0befd043a048ad25d56c784f) (Insiders) 中增加了几个个性化的新设置参数：  
  
- [`archive_pagination`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#config.archive_pagination)
- [`archive_pagination_per_page`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#config.archive_pagination_per_page)
- [`categories_pagination`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#config.categories_pagination)
- [`categories_pagination_per_page`](https://squidfunk.github.io/mkdocs-material/plugins/blog/#config.categories_pagination_per_page)

所以，等开放给公用版本使用后，可以再好好折腾一下。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="36"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
