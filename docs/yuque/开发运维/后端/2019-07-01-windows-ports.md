---
title: Windows server 2008 开启端口
urlname: 2019-07-01-windows-ports
author: 章鱼猫先生
date: 2019-07-01
updated: "2023-07-19 15:15:03"
---

## 1. 问题

将项目部署到 Windows server 2008 服务器上，开启了 http/https 之后，在用服务器本身的浏览器访问：<http://domain.com>  就可以访问，可是在外用其他电脑就访问相同的 url 就不能够访问。

## 2. 原因

造成以上问题，很大部分的原因在于服务器的防火墙限制了 80、443 对外的端口，也就是说没有开放这个端口给外部客户端访问。

## 3. 开启端口

windows server 2008 大多数端口都是默认关闭的，这里我们使用 httpd 的 80 端口为例，演示如何开启一个端口。

"**开始**" -> "**控制面板**" ->"**Windows 防火墙**" -> "**高级设置**" -> "**入站规则**"：

选择 "**Windows 防火墙**"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuU4mCyOX_sp8wjLIexY2Q3lWL3U.png)

选择"**高级设置**"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrNz2UBGthK-zZ1Vr7hxBLzyYe2y.png)

选择 "入站规则" → "新建规则"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn41UCaM6TpIMcc7H6ndGhgpqUkf.png)

点击端口：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Frp1_rWXCD9zjDkpufmBnl0esfLx.png)

添加 80 端口：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fnfc6xDDg6Qq5H907V4kbo7HSpnv.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjY5C9XEtMxXi9kKRNlnb8AhWbbx.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjefYCTty1rTBy28IK6ocbBiVeoM.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsnM5HeP5caLsiAxIMMfoY9QAIsM.png)

这样我们就可以访问我们的主机 apache 服务了。
