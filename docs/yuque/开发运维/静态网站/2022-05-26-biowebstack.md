---
title: 将重点资源整理成一个生信导航网页
urlname: 2022-05-26-biowebstack
author: 章鱼猫先生
date: 2022-05-26
updated: "2022-10-28 11:02:00"
---

前不久在 [@王诗翔(shixiangwang)](https://github.com/shixiangwang) GitHub 的讨论组上看到了类似的这个讨论 ["将重点资源整理成一个生信导航网页"](https://github.com/ShixiangWang/self-study/issues/65)，加上 [@郑宝童(btzheng)](https://github.com/btzheng) 曾经也做了一个[生信极客部落网址导航](https://zhengbaotong.gitee.io/biogeekgps/)（旨在搭建一个生信专属网址导航），好像也有一段时间没更新过了。
![@王诗翔 Bioinformatics Guide Site](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuIFnzVdyzCMNdx5Zqhg9YasujHi.png "@王诗翔 Bioinformatics Guide Site")
![@郑宝童 生信极客部落网址导航](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnACpSdO1EtsMWUKT86C7GYqFpTa.png "@郑宝童 生信极客部落网址导航")
于是有了 **生信重点资源+WebStack-Hugo=生信导航** 的初步的想法。[WebStackPage](https://github.com/WebStackPage) 本身是一个由 [viggo](https://www.viggoz.com/) 开发的一个网址导航开源项目，有许多的魔改版本，而 [WebStack-Hugo](https://github.com/shenweiyan/webstack-hugo) 则是本人基于 Hugo 进行修改调整的其中一个主题。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmrOp_BZ5HFjluUmdtF4WtbcWlK8.png)
有了现成的主题，又有了前人的一些资源整理（轮子都已经有了，就缺组装），于是在 GitHub 上开始了 [BioWebStack](https://github.com/bioitee/BioWebStack) 这一个将重点资源整理成一个生信导航网页的仓库（目前已初步把站点搭建了起来，资源内容还在更新中）。

:::success

- **GitHub 开源地址：**<https://github.com/bioitee/BioWebStack>
- **BioWebStack 站点地址：**<https://bioit.top/>（备用链接：<https://hao.bioitee.com/>）

:::

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiA1dbQM1-wPqbJOxVR6pg_0EQTU.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoP6x13jwOrNri7NiKhwP-1rO1O3.png)

**关于 BioWebStack 的一些特点和说明：**

- 致力于将一些重点资源整理成一个生信导航网页。
- 该网站用于个人学习和科研。
- 长期开源，欢迎大家提交错误报告以及宝贵的资源。
- 采用了一直以来最喜欢的 Hugo 部署方式，方便高效。
- 主要的配置信息都集成到了 **config.toml**，一键完成各种自定义的配置。
- 导航的各个信息都集成在 **data/webstack.yml** 文件中，方便后续增删改动。
- 无需服务器，GitHub Pages/Webify Pages/Cloudfare Pages 均可部署。

如果你也是做生信研究，如果你也正好喜欢学习生信，如果你一直苦于收藏夹越来越多，很难找到某个不常用的网站，那希望这个网站能给你带来一些作用。
