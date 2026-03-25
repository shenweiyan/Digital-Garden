---
title: 用 AI 优化 mRNA 序列设计软件 LinearDesign 的一些尝试
number: 181
slug: discussions-181/
url: https://github.com/shenweiyan/Digital-Garden/discussions/181
date: 2026-03-13
authors: 
  - shenweiyan
categories: 
  - 人工智能
tags: []
---

在 OpenClaw 如火如荼，全民养虾的当下，聚焦一下自己更加关注的 AI 在编程中的应用场景 —— 在编程中如何让 AI 更好为自己服务。本次优化的 LinearDesign 代码也已经提交到 GitHub，感兴趣的小伙伴可以参考。

- <https://github.com/shenweiyan/LinearDesignPY3>

## LinearDesign

LinearDesign 是百度自主研发的 mRNA 序列设计优化算法，其核心功能是同时优化 mRNA 的折叠自由能（MFE）和密码子适应指数（CAI），为研究人员提供专业的序列设计解决方案。

LinearDesign 项目的源代码托管在 GitHub 上，全球的开发者和研究人员都可以共同协作和改进。安装和使用过这个软件的小伙伴，都会发现几个问题：

1. 默认仅支持 Python2 语法；
2. 编译后的程序默认只能在当前目录执行，不支持绝对路径；
3. LinearDesign 自 203 年 4 月开源发布以来，基本没有任何实际性的更新，各种 Issues 也是没有任何响应。

## Qwen Code CLI

Qwen Code CLI 是阿里巴巴通义千问团队推出的一款，基于 Gemini CLI 改造、针对 Qwen3-Coder 模型优化的开源命令行工具，专为终端用户设计，能够实现自然语言生成代码、调试 bug、解释代码、文件操作及自动化工作流，显著提升开发效率。

虽然 Gemini CLI 能力更强（如联网搜索、长上下文），但 Qwen Code 在本地文件操作、代码生成方面更成熟，而且主打国产自主、每天 2000 次免费额度，适合中文社区和阿里生态。因此，我们在这里选择使用 Qwen Code CLI 对 LinearDesign 上面提到的两个尝试进行 AI 优化修复。

<!-- more -->

## 优化修复

1. 把 LinearDesign 的开源代码 `clone` 到本地。

2. 进入 `LinearDesign` 源码根目录，打开 `qwen`，输入需求。
    ```bash
    优化 LinearDesign 项目，要求可以在任何路径下通过绝对路径调用编译好的 lineardesign 进行mRNA序列优化，要求支持 python >= 3.7 语法
    ```
    ![qwen-lineardesign-start](https://gi.weiyan.tech/2026/03/qwen-lineardesign-1.png)

3. Qwen 接下来就会分析整个项目的代码逻辑，并开始进行优化修改，每次如果需要编辑源码，或者执行命令，Qwen Code CLI 都会让你进行选择。      
    ![qwen-code-apply-change](https://gi.weiyan.tech/2026/03/qwen-code-apply-change.png)

4. 优化修改完成后，还会对代码进行编译测试，直至最后完成。
    ![qwen-lineardesign-test](https://gi.weiyan.tech/2026/03/qwen-lineardesign-test.png)
    
## 测试验证

优化完成后，验证了一下，的确能正常执行。

![lineardesign-run](https://gi.weiyan.tech/2026/03/lineardesign-run.png)

## 想法

从这一次的尝试体验来看，AI 的确是给编程带了巨大的变化，在效率的提升上极其明显，这也为一些历史项目的优化更新甚至重构提供了支持。作为程序员，不管是 Qwen Code CLI，还是 Gemini CLI，都是值得我们去折腾的。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="181"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
