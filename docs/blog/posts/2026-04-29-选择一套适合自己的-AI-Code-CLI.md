---
title: 选择一套适合自己的 AI Code CLI
number: 189
slug: discussions-189/
url: https://github.com/shenweiyan/Digital-Garden/discussions/189
date: 2026-04-29
authors: 
  - shenweiyan
categories: 
  - 好玩
tags: 
  - Vibe Coding

---

通义千问 OAuth 免费套餐已于 2026 年 4 月 15 日停止。这一变动使得一直在个人服务器运行的 Qwen Code 突然无法使用，对于长期依赖命令行界面（CLI）进行项目程序优化的个人而言，简直不要太糟心。              
![qwen-code-cli-oauth](https://gi.weiyan.tech/2026/04/qwen-code-cli-oauth.png)

<!-- more -->

看一下阿里云的 Token Plan 团队版，对于个人用户且使用频率特别高的我来说，性价比太低了 —— AI 写代码太烧钱！          
![aliyun-token-plan](https://gi.weiyan.tech/2026/04/aliyun-token-plan.png)

于是，开始去看一下其他的备用选择。

第一，是 Qwen Code CLI + DeepSeek V4 (flash/pro)，但是看到 GitHub 的 [#3619](https://github.com/QwenLM/qwen-code/issues/3619)、[3579](https://github.com/QwenLM/qwen-code/issues/3579)，还是会存在一些问题，有待验证。

第二，Gemini Code CLI，吸引点主要在于 `gemini-cli` 是 [开源](https://github.com/google-gemini/gemini-cli)) 的，而且功能更强大，可以搭配其他模型进行使用。

至于为什么没有使用 Claude Code CLI，除了价格因素，它的封控严格，限制国内使用，除了心里膈应外还大大提升了折腾成本。
![claude-failed-connect](https://gi.weiyan.tech/2026/04/claude-failed-connect.png)

第三，Qoder CLI。之所以看到这个，主要是因为它的[价格便宜](https://qoder.com/pricing)，Qoder CLI 和 Qwen Code CLI 的区别在于，它们都是基于 Qwen 模型的两个独立项目，目前由不同的团队开发维护，Qwen Code CLI 是阿里巴巴官方出品，是支持其最新 Qwen 模型的 "嫡系部队"。Qoder CLI 早期也来自阿里团队，但目前由独立的公司 Qoder Inc. 负责维护和商业化运营。          
![qodercli-hello-world](https://gi.weiyan.tech/2026/04/qodercli-hello-world.png)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="189"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
