---
title: Chrome/Edge 地址栏正常显示完整的 URL
number: 74
slug: discussions-74/
url: https://github.com/shenweiyan/Digital-Garden/discussions/74
date: 2024-05-29
authors: [shenweiyan]
categories: 
  - 好玩
labels: []
---

对于在 Chrome/Edge 使用 IP 或者其他 URL 访问网页，地址栏想复制 IP/URL 非要给我自动加上 `http://`(或者 `https://`) 前缀。

<!-- more -->

## Chrome

Google Chrome 对于这个问题的解决方法很简单：在 URL 地址栏点击 "鼠标右键" -> 选择 "总是显示完整网址"。

![chrome-show-url](https://kg.weiyan.cc/2024/06/chrome-show-url.png)

## Edge

1. 右键点击 Microsoft Edge 的桌面快捷方式，选择属性。
   ![edge-1](https://kg.weiyan.cc/2024/05/edge-1.png)

2. 在启动目标结尾追加空格以及下面这段代码并保存。
   ```
   --disable-features=msHideSteadyStateUrlPath
   ```
   ![edge-disable-features](https://kg.weiyan.cc/2024/05/edge-disable-features.png)

3. 重启浏览器后地址栏就可以显示完整 URL 了。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="74"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
