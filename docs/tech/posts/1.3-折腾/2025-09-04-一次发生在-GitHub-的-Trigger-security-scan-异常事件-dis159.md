---
title: 一次发生在 GitHub 的 Trigger security scan 异常事件
number: 159
slug: discussions-159/
url: https://github.com/shenweiyan/Digital-Garden/discussions/159
date: 2025-09-04
authors: [shenweiyan]
categories: 
  - 折腾
tags: ['github']
---

2025年9月4日，早上起来看邮件时候，突然发现，邮箱一下子多了几百封 GitHub Actions 构建异常的邮件！

震惊紧张后，第一个反应就是，该不会是个人的 personal access token，或者密码泄露了，被人动态进行 commit 提交，以至于出现批量的 Actions 异常。于是，赶紧登录 GitHub 看一下到底发生了什么事。

首先，看到个人账号下基本每个 Public 仓库，甚至包括 organization 下个人创建的所有 Public 仓库，都出现了类似 **"Trigger security scan"** 的 commits 提交。
![trigger-security-scan](https://kg.weiyan.cc/2025/09/trigger-security-scan.png)

<!-- more -->

点击进去一看，好家伙，直接往 README 里面进行注释性的提交。
![commit-change-readme](https://kg.weiyan.cc/2025/09/commit-change-readme.png)

再回到 commits 记录一看，果然有连续多次的提交。
![commits-20250902](https://kg.weiyan.cc/2025/09/commits-20250902.png)

第二，回去仓库的 `.github/workflows` 下一看，还莫名其妙多了一个 `github_actions_security.yml` 自动化流程。
![github-actions-security](https://kg.weiyan.cc/2025/09/github-actions-security.png)

![github-actions-security-yaml](https://kg.weiyan.cc/2025/09/github-actions-security-yaml.png)

这就直接把 `PERSONAL_ACCESS_TOKEN` 的信息提交到了一个 `https://bold-dhawan.45-139-104-115.plesk.page` 的未知站点。
![bold-dhawan-45-139-104-115-plesk-page](https://kg.weiyan.cc/2025/09/plesk-page.png)

这一连串的骚操作下来，**可以肯定的是 token 或者其他密码泄露，或者是某个共用的 actions 出问题了**，所以：

1. 第一件事情，先把 personal access token 全部删除。
2. 清除所有仓库已存在的 `github_actions_security.yml`。
3. 最后，静观后效。

在文章最后，感谢 @guedou 在问题仓库中的建议。  
    
![compromised-token](https://kg.weiyan.cc/2025/09/compromised-token.png)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="159"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
