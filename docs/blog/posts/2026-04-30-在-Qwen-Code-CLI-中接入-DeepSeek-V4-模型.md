---
title: 在 Qwen Code CLI 中接入 DeepSeek V4 模型
number: 190
slug: discussions-190/
url: https://github.com/shenweiyan/Digital-Garden/discussions/190
date: 2026-04-30
authors: 
  - shenweiyan
categories: 
  - 好玩
tags: 
  - Vibe Coding

---

在前一篇《[选择一套适合自己的 AI Code CLI](https://shenwy.com/blog/discussions-189/)》文章中，我们提到通义千问 OAuth 免费套餐已经成为了历史，作为付费备选方案，今天介绍一下 Qwen Code CLI + DeepSeek V4（Flash/Pro）这一套组合，方便国内的用户可以直接配置使用。     

![qwen-deepseek-v4](https://gi.weiyan.tech/2026/04/qwen-deepseek-v4.png)

<!-- more -->

首先，在 DeepSeek 开放平台的 [充值](https://platform.deepseek.com/top_up) 页面先充值。

![deepseek-top-up](https://gi.weiyan.tech/2026/04/deepseek-top-up.png)

第二，在 DeepSeek 开放平台的 [API Keys](https://platform.deepseek.com/api_keys) 页面创建 API Key。

![deepseek-api-keys](https://gi.weiyan.tech/2026/04/deepseek-api-keys.png)

第三，配置 Qwen Code。有两种配置方式，一个是直接编辑 `settings.json` 文件；第二是通过 `qwen` 命令，一步步进行配置。

方法一，直接编辑 `settings.json` 文件。具体是，找到 `settings.json` 文件（通常在 `~/.qwen` 目录下，或通过终端输入配置命令打开），填写和编辑下面的内容。
```json
{
  "env": {
    "QWEN_CUSTOM_API_KEY_OPENAI_HTTPS_API_DEEPSEEK_COM": "YOUR_DEEPSEEK_API_KEY"     // 填入你的 API Key
  },
  "modelProviders": {
    "openai": [
      {
        "id": "deepseek-v4-flash",
        "name": "deepseek-v4-flash",
        "baseUrl": "https://api.deepseek.com",
        "envKey": "QWEN_CUSTOM_API_KEY_OPENAI_HTTPS_API_DEEPSEEK_COM"
      }
    ]
  },
  "security": {
    "auth": {
      "selectedType": "openai"
    }
  },
  "model": {
    "name": "deepseek-v4-flash"
  }
}
```

方法二，在命令行打开 `qwen`，根据提示进行一步一步配置。

1. 命令行打开 `qwen`，认证方式选择 **API Key**。
   ![qwen-setting-api-key](https://gi.weiyan.tech/2026/04/qwen-setting-api-key.png)        

2. **API Key Type** 选择 **"Custom API Key"**。
   ![qwen-setting-api-key-type](https://gi.weiyan.tech/2026/04/qwen-setting-api-key-type.png)          
    
3. 由于 [DeepSeek API 使用与 OpenAI/Anthropic 兼容的 API 格式](https://api-docs.deepseek.com/zh-cn/)，在 Protocol 这一步可以选择 **"OpenAI-compatible"**，或者 **"Anthropic-compatible"**，我这里选择前者。
    ![qwen-openai-compatible](https://gi.weiyan.tech/2026/04/qwen-openai-compatible.png)          

4. API endpoint 这里填写：`https://api.deepseek.com`。         
   ![qwen-seeting-api-endpoint](https://gi.weiyan.tech/2026/04/qwen-seeting-api-endpoint.png)          
    
5. API Key 填写前面创建的 API Key。         
   ![qwen-setting-enter-api-key](https://gi.weiyan.tech/2026/04/qwen-setting-enter-api-key.png)          
    
6. **Model IDs** 这里填写 `deepseek-v4-flash`。          
   ![qwen-setting-model-ids](https://gi.weiyan.tech/2026/04/qwen-setting-model-ids.png)          

7. **Advanced Config** 这里选择 `Enable thinking`。          
   ![qwen-setting-advanced-config](https://gi.weiyan.tech/2026/04/qwen-setting-advanced-config.png)          

8. 最后，一路回车，直至配置完成。完成配置后通过 `/model` 指令，就可以看到你现在使用的模型。
   ![qwen-deepseek-v4-flash](https://gi.weiyan.tech/2026/04/qwen-deepseek-v4-flash.png)

完成上面的 8 步后，在 Qwen Code CLI 中接入 DeepSeek-V4-Flash 模型就算全部配置完成了，接下来就可以在 Qwen Code CLI 中体验智能编程的乐趣了。

![qwen-deepseek-v4-coding](https://gi.weiyan.tech/2026/04/qwen-deepseek-v4-coding.png)

回到 DeepSeek 开放平台的 [用量信息](https://platform.deepseek.com/usage) 页面就可以看到自己的用量信息和余额。

![platform-deepseek-usage](https://gi.weiyan.tech/2026/04/platform-deepseek-usage.png)




<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="190"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
