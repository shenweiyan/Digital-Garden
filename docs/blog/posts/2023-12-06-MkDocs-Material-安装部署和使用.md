---
title: MkDocs Material 安装部署和使用
number: 37
slug: discussions-37/
url: https://github.com/shenweiyan/Digital-Garden/discussions/37
date: 2023-12-06
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

MkDocs 是一个快速、简单、华丽的静态网站生成器，适用于构建项目文档。文档源文件以 Markdown 编写，并使用一个 YAML 文件来进行配置。[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 是 [MkDocs](https://www.mkdocs.org/) 的一个主题配置，更加简洁美观，更新和维护也更加及时和频繁，且社区也更加活跃。

<!-- more -->

## 安装

主要使用的一些软件包以及模块 (requirements.txt) 如下：
```
mkdocs==1.5.3
mkdocs-material
mkdocs-rss-plugin
mkdocs-git-revision-date-plugin
mkdocs-include-dir-to-nav==1.2.0
mkdocs-glightbox
jieba
```

```
pip3 install -r requirements.txt
```

查看 `mkdocs-material`, `mkdocs` 的版本：
```python
$ mkdocs --version
mkdocs, version 1.5.3 from /usr/local/software/python-3.9.18/lib/python3.9/site-packages/mkdocs (Python 3.9)

$ pip3 show mkdocs-material
Name: mkdocs-material
Version: 9.4.4
Summary: Documentation that simply works
Home-page: 
Author: 
Author-email: Martin Donath <martin.donath@squidfunk.com>
License: 
Location: /usr/local/software/python-3.9.18/lib/python3.9/site-packages
Requires: babel, colorama, jinja2, markdown, mkdocs, mkdocs-material-extensions, paginate, pygments, pymdown-extensions, regex, requests
Required-by:
```

## 使用

本地预览：
```
$ mkdocs serve -a 0.0.0.0:8000
```

## 问题与解决

1. Pagination 分页与 `git-revision-date` 冲突，导致无法构建 - 参考 [mkdocs-material/discussions/6156](https://github.com/squidfunk/mkdocs-material/discussions/6156)
2. [Support Markdown in the copyright string #5134](https://github.com/squidfunk/mkdocs-material/issues/5134)
3. [如何在 MkDocs 的版权部分自动添加年份 - squidfunk/mkdocs-material#4969](https://github.com/squidfunk/mkdocs-material/discussions/4969)
4. [如何定制博客插件的归档页面 - squidfunk/mkdocs-material#6324](https://github.com/squidfunk/mkdocs-material/discussions/6324)

## 期待的功能

这是一个个人非常期待的功能，大部分目前已经可以在 [Insiders](https://squidfunk.github.io/mkdocs-material/insiders/) 版本中使用，社区公开的版本尚无法使用。

- 博客插件的自定义归档、目录页面每页文档数 - [squidfunk/mkdocs-material#6383](https://github.com/squidfunk/mkdocs-material/issues/6383)
- 内置隐私插件（方便内网/国内部署加速访问）- [Built-in privacy plugin - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/plugins/privacy/)    
    内置隐私插件(privacy plugin) 在 [9.5.0](https://github.com/squidfunk/mkdocs-material/releases/tag/9.5.0) 中已经k可以正常使用了，下一个值得期待的就是该插件的 [`assets_exclude`](https://squidfunk.github.io/mkdocs-material/plugins/privacy/#config.assets_exclude) 功能！

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="37"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
