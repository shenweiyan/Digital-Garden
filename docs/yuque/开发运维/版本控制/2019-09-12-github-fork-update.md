---
title: 如何同步更新 Github 上 Fork 的项目？
urlname: 2019-09-12-github-fork-update
author: 章鱼猫先生
date: 2019-09-12
updated: "2021-11-03 15:46:14"
---

### Github Fork 过程概述

在 Github 上有很多优秀的开源项目，相信每一位热衷于技术的朋友都会在 Github 上 Fork 一些感兴趣的项目，然后在本地修改并提交。本文以 Galaxy Project 下的 galaxy 仓库为例，在 Github 上 Fork 该项目，更新提交的一个完整过程如下图所示：

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoTEC0UrbDMw2OuK_tZh5lzOjAU8.png)

1.  fork 一个项目，比如 galaxy，该操作会复制该项目的所有历史提交内容到个人仓库中，并生成一个相同的项目；
2.  clone 之前 fork 的项目到本地计算机中；
3.  在本地仓库中更新某些文件；
4.  提交更新的文件到本地仓库；
5.  将本地仓库的更改内容推送 push 到个人 github 远程仓库；
6.  创建 pull 请求，既可以把 fork 原始项目中别人的更新同步到自己的 github 仓库中，也可以提交个人更新的内容到 fork 的原始项目。

我 fork 的  [galaxyproject/galaxy](https://github.com/galaxyproject/galaxy)  项目如下：
![1-shen-galaxy-master.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuLbQzEQw_2qBwLaPfz2BBkBaipy.png)

[galaxyproject/galaxy](https://github.com/galaxyproject/galaxy)  项目 master 版本最新进展如下，可以看到已经有了很大新的代码提交：
![2-galaxyproject-master.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkQ-d450LKDnCnhGIjtNtnoVXN7R.png)

下面我们简单介绍一下，如何同被 fork 的项目保持同步更新，将以 galaxyproject/galaxy  项目为例。

### fork 同步更新步骤

1.  打开自己的 github 中 fork 的项目，打开 Code 选项卡，点击下面的 **"New pull request"** 创建一个新的 pull 请求；

![3-new-pull-request.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Frjfr8h3daSvJkimzvCswOV_Kdmd.png)

2.  在 **Comparing chanages** 页面，如下图所示，这时 base fork 默认是你 fork 的项目，而 head fork 则默认是你自己的仓库。

![5-compare-change.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqJK_irtxyxIKLRMj0gR8_360rA2.png)

3.  在上图中进行选择（前面的 base-fork 选择自己的 github 仓库）后会出现如下图所示页面，这时需要点击 **"compare across forks"**，再一次进行选择。

![5.1-compare-fork.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqZx4b3roNh9ZeI14VqRyLPEiZVh.png)

4.  具体选择如下：base:master 是自己仓库和分支，后面选择 head fork, compare:master 是你 fork 项目来源的仓库和分支，可以对比两个项目前后的变化情况。然后点击 **"Create pull request"**，创建新的 pull 请求。

![compare-change.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnI99s09kYyCTUuXCsoa-wh-d7hj.png)

5.  填写标题（Title）和评论（Comment），并点击 Create pull request。Preview 可以预览评论效果，右侧有 5 个选项可以设置检阅用户（Reviewers）、分配给哪个用户（Assignees）、Labels 标签（bug、duplocate、enhancement、help wanted、invalid、question、wontfix，也支持自定义）、项目（Projects），以及里程碑事件（Milestone）。

![pull-request-commit.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsMlmWA_jPu4mt4ic5nx3vIBS5K7.png)

6.  点击 **"Create pull request"** 之后，就可以在 Pull request 中看到刚才提交的 comment，如下所示。

![update-master.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu8ECaQSoxmoY26-j4XZB5xq8lwa.png)

7.  可以看到期间有很多的提交更新，往下翻可以找到如下图所示，点击\*\* "Merge pull request"\*\*。

![6-merge-master-pull-request.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiQUFpRTizMW1JamrEEeDUfruPsn.png)

8.  填写 Merge 的评论并且提交，如果有冲突一定要先解决冲突，然后就全部 OK 了。

![7-confirm-merge.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqSP4BB1N4wv5rIfi5XY9dQGlwEA.png)

9.  最后，再次打开自己仓库的 galaxy 项目，可以看到项目已更新到最新版本，和最开始 galaxy 原始项目内容一致了。

![8-galaxy-master-fork.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fl89acRkvA2WUX_ZTLRB3dp4XDqk.png)

![2-galaxyproject-master.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkQ-d450LKDnCnhGIjtNtnoVXN7R.png)

### 总结

本文讲解了同步更新 Github 上 Fork 项目的其中一种方法，还有其他的方法比如可以删除个人 github 中 fork 的该项目然后重新 fork，这种方式不能合并自己已更新的代码；还有另外一种方式是在本地建立两个仓库，把两个远程库都 clone 到本地，然后拉取原 fork 项目更新到本地，合并更新，最后 push 到你个人的 github 即可。
