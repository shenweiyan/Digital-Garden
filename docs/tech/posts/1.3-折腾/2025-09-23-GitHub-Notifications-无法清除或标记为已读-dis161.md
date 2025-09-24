---
title: GitHub Notifications 无法清除或标记为已读
number: 161
slug: discussions-161/
url: https://github.com/shenweiyan/Digital-Garden/discussions/161
date: 2025-09-23
authors: [shenweiyan]
categories: 
  - 折腾
tags: ['github']
---

GitHub 使用多了，最近总是遇到一些奇奇怪怪的问题。这不，今天又遇到了一个 Notifications 无法清除或标记为已读的神奇问题。

![github-notifications](https://kg.weiyan.cc/2025/09/github-notifications.png)

<!-- more -->

这个问题，在 <https://github.com/orgs/community/discussions/174310> 也有人遇到过，在 V2EX 也有相关的讨论 ——[《疑似 GitHub × Gitcoin 的骗局》](https://www.v2ex.com/t/1161205)，是这样子解释的。

> 这是 GitHub 上一个已知的边缘情况。当触发通知的仓库或用户被删除时，有时相关通知会“卡住”，无法清除或标记为已读。这是一个偶尔会发生的错误，尤其是在垃圾邮件或已删除的帐户中。

GitHub 在这个讨论中给了四个方法：尝试将所有通知标记为已读、使用 GitHub 移动应用程序、等待 GitHub 维护、联系 GitHub 支持。都未能很好解决问题，反而是讨论中的其他用户提供了解决的方案，个人试了一下，的确可行。

参考：《[Mark GitHub notifications as read](https://gist.github.com/jeremystretch/2c09f76837fc5af787fe9ff7747ecf3f)》
```python
import requests

TOKEN = '<TOKEN>'

headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {TOKEN}',
    'X-Github-Api-Version': '2022-11-28',
}

notifications = requests.get('https://api.github.com/notifications', headers=headers)

for notification in notifications.json():
    print(f"{notification['id']}: {notification['subject']['title']}")
    requests.delete(f'https://api.github.com/notifications/threads/{notification["id"]}', headers=headers)
```

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="161"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
