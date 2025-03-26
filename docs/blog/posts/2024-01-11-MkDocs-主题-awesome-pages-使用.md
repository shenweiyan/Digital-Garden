---
title: MkDocs 主题 awesome-pages 使用
number: 51
slug: discussions-51/
url: https://github.com/shenweiyan/Digital-Garden/discussions/51
date: 2024-01-11
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

很长一段时间都在使用 [mkdocs_include_dir_to_nav](https://github.com/mysiki/mkdocs_include_dir_to_nav) 这个插件来自动包含目录下的所有 md 文件，但随着新需求的出现 —— **如何给某一个指定的子目录使用 `reverse_sort_file`，即升序排列展示子目录相应的 markdown 内容**。这才开始接触到 [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) 这个插件。

<!-- more -->

## 开始

从 GitHub 可以很直观看到的是 [mkdocs_include_dir_to_nav](https://github.com/mysiki/mkdocs_include_dir_to_nav) 自从 2022-05-01 更新了 [V1.2.0](https://github.com/mysiki/mkdocs_include_dir_to_nav/releases/tag/v1.2.0) 版本后基本就已经停止了更新，Star 也才 20 多人。       
![mkdocs-include-dir-to-nav](https://shub.weiyan.tech/kgarden/2024/01/mkdocs-include-dir-to-nav.png)

反而是 [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) 一直保持着非常积极的更新频率，而且维护者和关注和使用用户也远远比 [mkdocs_include_dir_to_nav](https://github.com/mysiki/mkdocs_include_dir_to_nav) 多得多。     
![mkdocs-awesome-pages-plugin](https://shub.weiyan.tech/kgarden/2024/01/mkdocs-awesome-pages-plugin.png)

于是，开始着入手 [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)。不得不说，Awesome-Pages 这个插件的功能很强大，可以很好解决我"指定子目录自定义文档排序"的需求。但不可否认的是 Awesome-Pages 的文档写的的确有点糙，不认真看还真不知道应该如何上手，这也是花费我最多时间的地方。

## 使用

使用 [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) 有两个很重要的前提：

1. 如果你在 `mkdocs.yml` 定义了 `nav` 或 `pages` 条目，则此插件不会执行任何操作。要使用该插件列出的功能，我们必须完全删除该条目或向其中添加 `...` 条目 ([add a `...` entry to it](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin?tab=readme-ov-file#combine-custom-navigation--file-structure))。
2. 自定义导航时，在目录(或者子目录)中创建一个名为 `.pages` 的文件时，使用 `nav` 属性只能自定义**该级别的导航**！然后，按照文件和子目录在导航中出现的顺序列出文件和子目录。

```
docs/
├── README.md
├── dirNamedA
│   ├── dirA-page01.md
│   ├── dirA-page02.md
│   └── subDirNamedA1
│   │   ├── subDirA1-page01.md
│   │   └── subDirA1-page02.md
│   └── subDirNamedA2
│       ├── subDirA2-page01.md
│       └── subDirA2-page02.md
├── dirNamedB
│   ├── dirB-page01.md
│   ├── dirB-page02.md
│   └── subDirNamedB1
│       ├── subDirB1-page01.md
│       └── subDirB1-page02.md
└── emptyDir
```

这就发现了 [MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) 和 MkDocs  、[mkdocs_include_dir_to_nav](https://github.com/mysiki/mkdocs_include_dir_to_nav) 在设置 navigation 时候的区别：[MkDocs Awesome Pages Plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin) 的 `nav` 属性只能自定义**该级别的导航**！即无法只通过一个 `.pages` 实现所有目录+子目录的 navigation 排序配置。

所以，最好的做法就是在 `docs` 目录下(包含 `docs`) 给每个目录增加一个 `.pages` 文件，用于控制当前目录的所有子目录(或者 Posts) 的排序和展示。



<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="51"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
