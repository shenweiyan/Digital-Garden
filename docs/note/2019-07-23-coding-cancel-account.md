---
title: 不提供账号注销等于耍流氓
urlname: 2019-07-23-coding-cancel-account
author: 章鱼猫先生
date: 2019-07-23
updated: "2021-06-30 09:47:49"
---

![zhanghao.jpg](https://shub.weiyan.tech/yuque/elog-notebook-img/FgjHQn_wdWob063qAiBlTG8nlKn2.jpeg)

作为一个生信工程师，不知道大家平时是怎么管理和备份自己的一些流程和脚本？而我个人则比较喜欢用 git。

说到 git 代码托管，国外的 GitHub、GitLab 相信大家都已经很熟悉；国内比较知名的，除了码云，CODING 应该也算得上一个。在最开始的前几年，甚至到 2017、2018 年，Coding.net 代码托管平台的用户体验都还挺不错的，但 2019 年和腾讯云开发者平台合并后，就开始变得越来越鸡肋了，合并后虽然说是不限存储不限项目提供代码托管。

CODING 个人版有几点不太友好的体检经历：

- 在同一个产品中过多的嵌套 coding.net 和 dev.tencent.com 两个域名的链接跳转，用着用着就让人有一种分不清楚这个到底是原来的 CODING 还是腾讯云开发者平台！

- CODING 个人版个人主页，公开的项目却显示的是仓库名称！这样，在仓库中设置项目名称的意义是什么？

![image.png](https://shub.weiyan.tech/yuque/elog-notebook-img/FsIF_mY1Mplnv6WHf_Oc0LlOTAR3.png)

- 注销账号， CODING 只提供账号锁定功能！！！

《电信和互联网用户个人信息保护规定》（工业和信息化部令第 24 号）第九款第四款规定：“电信业务经营者、互联网信息服务提供者在用户终止使用电信服务或者互联网信息服务后，应当停止对用户个人信息的收集和使用，并为用户提供注销号码或账号的服务。”

![image.png](https://shub.weiyan.tech/yuque/elog-notebook-img/FhEmqoge2p383tBp-vjGxFoAw3gk.png)

最后只想说，如果不是出于墙内网络的考虑，很多人应该都会选择 Github、Gitlab 的代码托管服务。当然，或许也有些人出于对  Github 账户/开源项目是否会受到美国出口管理条例管制的担心，或者追求更高的速度体验，而转向国内的代码托管服务。

对于国内代码托管服务，开源中国旗下的 Gitee 应该是目前做的最好的，但对 git 空间和单个仓库都有一定限制。反观那些不限空间、不限项目的后来者，CODING 也好，腾讯云开发者平台也罢，用户体验不好，产品不过关，再多的免费空间也是白搭吧！

不管怎么说，对于一些重要的生信分析流程脚本选择 git 进行管理个人觉得还是非常有必要的。你可以选择自建服务进行托管，也可以选择付费进行托管，重要的一点，如果你是土豪，就当我什么都没说。
