---
title: Fedora Redhat Centos 有什么区别和关系？
urlname: 2019-07-25-fedora-redhat-centos
author: 章鱼猫先生
date: 2019-07-25
updated: "2021-06-25 11:04:14"
---

这里对 Redhat/CentOS/Fedora 之间以及与其他 Linux 发行版关系做一个基本的介绍。给新手选择一个 Linux 发行版提供指导和帮助。

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu2Zm1XYDoC03zWbT9yI_r1MEDm2.png)
**Fedora**
Fedora 是基于 Linux 的集最新自由开源软件于一体的操作系统。Fedora **始终允许任何人自由使用，修改和发布。**它由来自世界各地的人们在 Fedora 项目社区下共同合作而成。Fedora 项目对外开放，欢迎任何人加入。Fedora 项目就在您眼前，它**引领着自由、开源软件以及内容的前进。**  特点是常常引入创新性的技术，被视为"新技术的试验场"。版本升级很快（约 6 个月），每个版本的支持较短，约为 13 个月。Red Hat 公司为 Fedora Project 提供赞助。
最新正式版本为 2013-12-17 发布的 Fedora 20，代号是 Heisenbug。
目前支持版本：19 & 20
官方网站：<http://fedoraproject.org/>
中文论坛：<http://bbs.fedora-zh.org/>
中文邮件列表：[fedora-chinese](https://admin.fedoraproject.org/mailman/listinfo/chinese)

**RHEL/Red Hat Enterprise Linux**
Red Hat Enterprise Linux 是 Red Hat 公司定位于企业级应用的**商业性质**的 Linux 发行版。提供付费的技术支持和更新支持。RHEL4 细分为 AS、ES 和 W S 和 Desktop 版本。RHEL5 开始产品分成了 6 类（见[维基](http://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux)）。红帽公司对企业版 LINUX 的每个版本提供 7 年的支持。
最新正式版本为 2013-11-22 发布的 RHEL 6.5。
RHEL 5 系列也在支持。目前最新正式版本为 RHEL 5.10。
RHEL 4 系列也仍支持，目前最新版本为 4.9。
官方网站：<http://www.redhat.com/>

**CentOS/Community ENTerprise Operating System**
CENTOS 是一个服务器级别的 Linux 发行版。由社区重新编译 Red Hat 公开的 SRPM，去除了 Red Hat 的商标，更换 LOGO 得到。
最新正式版本为 2013-12-01 发布的 CentOS 6.5，
版本 5 系列最新为 CentOS 5.10。
官方网站：<http://www.centos.org/>

以上三者均采用了 RPM 包管理机制，使用 yum 解决软件包依赖，这方面和 Debian/Ubuntu 的 deb/apt 不同。三者默认的桌面环境均为 GNOME。与 Mandriva 默认 KDE 不同。

三者差别不大，相比而言，Fedora 最适合新手做桌面使用，CentOS 适合个人做服务器应用，RHEL 适合企业应用。

三者之间有一定的依赖关系。RHEL 可以视为 Fedora 的派生版，CentOS 本身基于 RHEL。另外还有一些 Linux 发行版是基于以上的发行版制作的，例如 Oracle Linux、Scientific Linux 是基于 RHEL 的。
