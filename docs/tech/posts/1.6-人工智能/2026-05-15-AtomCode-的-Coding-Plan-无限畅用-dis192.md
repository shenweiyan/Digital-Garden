---
title: AtomCode 的 Coding Plan 无限畅用
number: 192
slug: discussions-192/
url: https://github.com/shenweiyan/Digital-Garden/discussions/192
date: 2026-05-15
authors: 
  - shenweiyan
categories: 
  - 人工智能
tags: ['Vibe Coding']
---

之所以去试用这个智能体，最大的吸引力正如标题所说的 **"Coding Plan 无限畅用"** —— 它提供了可以不限总量调用的两个昇腾编码模型 DeepSeek-V4-Flash 和 Qwen3.6-35B-A3B，并打出了 "订阅式编码权益，昇腾国产算力支撑，一次领取告别按 Token 计费" 的口号。

![atomcode-serverless-api](https://gi.weiyan.tech/2026/05/atomcode-serverless-api.avif)

<!-- more -->

## 介绍

AtomCode 是一款 2026 年 4 月开源的、基于 Rust 构建的本地化 AI 编码终端智能体（Claude Code 的国产替代）。它支持 DeepSeek、Qwen 等国产大模型，能够通过自然语言指令，在本地自动完成代码生成、重构、诊断、运行和修复的全流程开发任务。

![atomcode-homepage](https://gi.weiyan.tech/2026/05/atomcode-homepage.avif)

## 安装

参考官方[安装说明](https://atomcode.atomgit.com/#install)，一键式安装。

![atomcode-install](https://gi.weiyan.tech/2026/05/atomcode-install.avif)

安装完成后，可以通过 `atomcode` 命令运行，然后通过扫码或者链接登录，即可领取不限量使用的 CodingPlan 免费额度。

```bash
首次运行 — 欢迎界面
$ atomcode

欢迎使用 AtomCode · 开始使用：

  ▸ Set up CodingPlan    免费额度 · 推荐
    Configure manually   API Key
    Skip for now          先看看再说
```    

![atomcode-codingplan-setup](https://gi.weiyan.tech/2026/05/atomcode-codingplan-setup.avif)

通过 `model` 内置命令可以自行选择 `DeepSeek-V4-Flash` 或者 `Qwen3.6-35B-A3B` 模型。

![atomcode-model](https://gi.weiyan.tech/2026/05/atomcode-model.avif)

## 使用体验

个人主要用的是 `Qwen3.6-35B-A3B` 模型，对于一些站点主题功能调整，或者代码优化，用了一天下来感觉还算不错，最起码速度还是挺快的，复杂的项目代码重构目前没试过。

第二个想说的是，天下没有免费的午餐，在目前满大街的 token plan 付费环境下，**"Coding Plan 无限畅用" 是站不住脚的，都是套路——先免费拉人头在想办法收费，大家需要有心理准备**。今天（2026.05.15）再去一看，果然发现不到一个月的时间这个 Coding Plan 就开始调整为 30 天有效了，模型倒是增加了一个 GLM-5.1。

![atomcode-doingplan](https://gi.weiyan.tech/2026/05/atomcode-codingplan.avif)

如果你的代码复杂性并不是特别高，又想 AI 辅助进行代码优化，可以考虑尝试一下。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="192"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
