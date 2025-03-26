---
title: 使用 RSS 打造你的科研资讯头条
urlname: 2019-07-01-rss-for-top-news
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 10:45:24"
---

# 一、什么是 RSS

> RSS 是站点用来和其他站点之间共享内容的一种简易方式（也叫聚合内容 Really Simple Syndication）。通常在时效性比较强的内容上使用 RSS 订阅能更快速获取信息，网站提供 RSS 输出，有利于让用户获取网站内容的最新更新。网络用户可以在客户端借助于支持 RSS 的聚合工具软件（例如 Inoreader, NewzCrawler, FeedDemon），在不打开网站内容页面的情况下阅读支持 RSS 输出的网站内容。

简单的来说，RSS 就是一个收集箱（海报栏），一个 inbox ，通过不同的 feed 地址，将各种订阅源汇总到一起，在某个客户端中统一体现，每天刷一次，一切就像清空收件箱一样方便。

# 二、为什么需要 RSS

举个例子，假如我们同时关注了知乎的某个专栏（如，R 语言中文社区）、简书某个专题（如，生物信息学与算法），以及其他一些生信大神的博客，除此之外我们还是 BBC、The Wall Street Journal 的读者。如果我们想要获取这些专栏、博客、网站的最新文章内容，按照以往的阅览模式，我们需要分别登录这些不同的网站把这些网站的内容浏览一遍才可以。这就意味着我们要每天至少分别打开上面所有网站的链接各一次，而且每次都要加载网站的动画、排版和文字内容，消耗大量的时间和流量。

有了 RSS 系统，你只需要订阅各个网站的 RSS 链接，并在 RSS 阅读器内统一阅读自己订阅的文章就行了。RSS 阅读器可以自动检索和更新各网站最新的内容，你读过的文章也可以自动标记，非常方便。

# 三、如何开始我的 RSS

## 首先，我们需要一个 RSS 源，即 Feed。

> Feed 是为满足以某种形式持续得到自己更新的需求而提供的格式标准的信息出口。就是信源。信息发布网站将网站全部或者部分信息整合到一个 RSS 文件中，这个文件就被称之为 Feed 。信源中包含的数据都是标准的 XML 格式，不但能直接被其他站点调用，也能在其他的终端和服务中使用。RSS 订阅的过程中会用到的 "Feed"，便是表示这是用来接收该信息来源更新的接口。

一般我们需要订阅的新闻或者博客网站中大部分主流网站会有专门的 RSS 链接方便用户订阅，如果没有也没关系，RSS 订阅服务通常会自动识别网站地址。或者我们可以使用专门的 RSS 生成器为没有 Feed 的网页生成 RSS 格式订阅源，如，Feed43、RSSHub 等等。

关于常用的 RSS 源，这里推荐知乎的一个回答：[你必读的 RSS 订阅源有哪些？](https://www.zhihu.com/question/19580096/answer/20490041)

## 其次，我们需要一个 RSS 阅读器。

就像电子书需要电子书阅读器才能阅读一样，Feed 只是 RSS 的一个数据源，它本身是写给程序看的，必须经过阅读器转换，才能成为可以浏览的格式。

RSS 阅读器多种多样，大致分为两种，一种是桌面型的，需要安装；另一种是在线型，直接使用浏览器进行阅读。

目前，市面上能叫得出名字的 RSS 阅读器有数十款以上，我们无意对这些阅读器进行一一测评比较，今天只聊一聊个人感觉比较满意的一款 RSS 阅读器：Inoreader。

## 最后，介绍一款 RSS 阅读器。

> Inoreader 是保加利亚一款基于网络内容和云服务的 RSS 聚合器，且支持移动设备 Android 和 iOS 端。它以统一的布局为用户编排整理定制来自在线资源的新闻源，并可与他人分享。Inoreader 由 Innologica 于 2013 年首次发布。截止 2018 年 7 月 30，Inoreader 最新版本为 5.3.26。

Google reader 是 RSS 订阅服务的鼻祖，但该业务在 2013 年被 Google 关闭了。Inoreader 是 Google reader 的继任者中做的比较好的，它的用户界面与 Google Reader 非常相似，支持中文界面，加载速度非常快，还不需要翻墙，支持快速导入，可以保留加星文章，有许多的快捷键，可订阅无限，支持分享到社交网络等等。

### 1. Inoreader 注册

登陆 Inoreader 中文版官网，注册，现在可选注册有 facebook，tweeiter，或者其他邮箱。读者可自行选择在上面注册，注册成功后即可登陆网址。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp7oA1iRTarIuLCHfpUD9r4ZkMzg.png)

### 2. Inoreader 登陆

注册成功后即可登陆网址，显示首页。这里界面如下。如果是英文界面想要切换成中文：点击右上角齿轮图标 → Preferences → Interface → Language：简体中文 → 右下角点击 "Save"。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuuzwZmZUZ05xVEij427Hjz0L8qv.png)

### 3. Inoreader 添加订阅

1.  常用订阅

可以通过点击 "<https://www.inoreader.com/folder/8648252>" 中的 "订阅" 把网友分享的 "我的必读订阅源" 添加到自己的 Inoreader（订阅后的源可以自定义增删）：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FojYPZewaCzWERChr2qtJ7GLDoJx.png)

比如我们输入 "PLOS ONE" 关键词就可以看到该杂志的一系列订阅源，点击即可完成订阅。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmi8KUPu6Ce55eaSkEgRIr_2Pe5M.png)

这是一种比较详细的订阅方式，我们需要去各大数据库选择自己需要的，比如 pubmed，你打开之后，输入你想要的关键词，在搜索框下方有一个 "create RSS" 直接点击：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgGVlLvVLWNm9_DvUMkmJ2EkHo-R.png)

Inoreader 支持知乎专栏的 URL 搜索，比如我们要把知乎的 "R 语言中文社区" 专栏添加到 Inoreader，只需要把该专栏的 URL 粘贴到 Inoreader 搜索区，在找到的源中点击订阅即可。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoTZAKYBkQBf1l_VuIGgNt3z8VYZ.png)

简书默认是没有提供 RSS 输出的。因此我们想要添加简书专题、文集或者作者的订阅，需要借助简书 RSS 生成器，这里推荐一个神器：JianshuRSS（链接：<http://jianshu.milkythinking.com/）。>

首先，我们把简书的 "生物信息" 专题链接 "<https://www.jianshu.com/c/2e21055ceb0e>" 粘贴到 JianshuRSS：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj513Pf-Nt9OAqFQpe42Rshft9Ed.png)

关于 Inoreader 的 RSS 源就写到这里了。对于普通大众而言，RSS 的上手门槛高确实有点高，需要自己找链接，也缺少互动，但是在知识爆炸的今天却很实用。

### 4. Inoreader 使用设置

当我们完成订阅后，许多订阅源你可以对它进行整理，在 Inoreader 中右键即可实现。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Ft4Mf4V_RXsLc3qOw3-wqyAeLeCp.png)

为了提高阅读效率，我们也可以选择切换视图。就是右上角那个很像眼睛的图标，选择杂志视图，即可如下。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlZ14yPuIw4d1JN5m74FwacGLq63.png)

当然 Inoreader 在左边下角提供其他的服务，如 Inoreader 下方还有统计数据，统计你一天看了多少，，快捷键大全，新手指导，联系客服，调整左栏项目等等。有兴趣的童鞋可以自行去体验一下。

最后，提供几张 Inoreader 在安卓手机上使用的截图：
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjzyUDFZ6rxhOEgbgCzNq791m26g.jpeg)

# 四、参考资料

- Platycodon，《2018 年主流 RSS 服务选哪家？Feedly、Inoreader 和 NewsBlur 全面横评》，少数派，<https://sspai.com/post/44420>
- 数据小冰，《inoreader 阅读器使用》，CSDN，<https://blog.csdn.net/mingyong_blog/article/details/40792687>
- 阮一峰，《如何使用 RSS》，阮一峰的网络日志，<http://www.ruanyifeng.com/blog/2006/01/rss.html>
- 哈尔滨工业大学学报编辑部，《RSS 订阅》，<http://swxxx.alljournals.cn/ch/reader/rss.aspx>
- 程引，Alpha，等，《你必读的 RSS 订阅源有哪些》，知乎，<https://www.zhihu.com/question/19580096/answer/20490041>
- 爱因斯没有坦，《科研利--inoreader 同步世界的资讯》，简书，<https://www.jianshu.com/p/66acd42a1fff>
