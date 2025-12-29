---
title: Dify 上的 Ollama 不支持 Rerank 模型
number: 156
slug: discussions-156/
url: https://github.com/shenweiyan/Digital-Garden/discussions/156
date: 2025-07-15
authors: [shenweiyan]
categories: 
  - 人工智能
tags: ['1.3.26-人工智能', 'dify', 'ollama']
---

在 Dify Cloud 平台调用各大平台的大模型 API 一直都没发现这个问题，随着开始折腾本地化使用，才发现 Ollama 部署大模型虽然方便，但是 RAG 中 Dify 知识库混合检索，需要 Rerank 模型时，这一点上，Ollama 居然是不支持 Rerank 模型的。     
![rag-pipelines](https://gi.weiyan.tech/2025/07/rag-pipelines.webp)

<!-- more -->

Dify Cloud 的系统模型设置，在接入了阿里云百炼的通义千问 API Key 后，Rerank 模型会默认显示通义千问的 `gte-rerank` 和 `gte-rerank-v2`。
![dify-cloud-rerank](https://gi.weiyan.tech/2025/07/dify-cloud-rerank.webp)

本地部署 Ollama + Dify，在 Dify 选择 Ollama 模型供应商，发现 Ollama 只支持 LLM 和 Text Embedding，不支持 Rerank 模型。
![dify-local-ollama-models](https://gi.weiyan.tech/2025/07/dify-local-ollama-models.webp)

看到有提到使用 Xinference 平台来部署 Rerank 模型的，特意去看了一下 Xorbits Inference，发现的确是除了 LLM 和 Text Embedding 还支持 Rerank、Speech2text、TTS。
![dify-xorbits-inference](https://gi.weiyan.tech/2025/07/dify-xorbits-inference.webp)

## 参考资料

- [安装 Dify 并集成 Ollama 和 Xinference](https://zhuanlan.zhihu.com/p/719782211)
- [**add Ollama rerank model** - langgenius/dify#10917](https://github.com/langgenius/dify/issues/10917)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="156"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
