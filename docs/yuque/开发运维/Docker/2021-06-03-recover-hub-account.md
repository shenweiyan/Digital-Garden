---
title: 终于把 7 年前的 Docker Hub 账号恢复了
urlname: 2021-06-03-recover-hub-account
author: 章鱼猫先生
date: 2021-06-03
updated: "2021-06-25 10:49:05"
---

折腾 docker，向 Docker Hub 提交镜像的时候发现原来自己在 2014 年就已经注册过 Docker Hub 的账号了，而且在 <https://hub.docker.com/u/shenweiyan> 也看到了自己在 Docker Hub 的一些镜像信息。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj5eN7DggLqaamb8WHWAqZq7Emf3.png)
悲催的是，自己把密码给忘记了，找回密码甚至发现连注册邮箱都忘记了！！！

于是回去翻历史邮件（个人一直以来都喜欢把所有的邮箱 163、outlook、gmail ...... 都是设置自动转发到 QQ 邮箱，或者通过 QQ 邮箱代收代发！）感谢这个好习惯！！终于让我找到了线索！！！
![docker-passwd-reset.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjxsY8xHqiVgb7st9NFSYZtvDqcM.png)
由于注册的 gmail 账号很早前就已经被自己注销删除了，于是想着去恢复（或者重新注册）！
![gmail.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvIjl3qYhSYRvuG99JosxIPC5M2p.png)
自己操作恢复不了，于是参考了 YouTube 的 《[Couldn't find your google account But username is taken | How to resolve?](https://www.youtube.com/watch?v=QDy9voxTHW4)》的视频教程给 Google Team 求助。
![restore_gmail.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgHdrASQAFuW6tYcLSea0vcQm7it.png)
Gmail 恢复无望！

接着，通过 Email 和 [Recover your Docker Hub account | Docker Documentation](https://docs.docker.com/docker-hub/2fa/recover-hub-account/) 中的 [Contact Support form](https://hub.docker.com/support/contact/?category=2fa-lockout) 给 Docker Hub 发送求助！
![help-dockerhub.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkWUqznpeyNAjQQW-miDUQXXmH34.png)

等待了 1 到 2 天，终于收到 Docker Hub 的答复，根据链接，重置密码成功！
![dockerhub-reset-passwd.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fs9OwyN_x4afH-QEH5XPNGf9upbj.png)
最后，简单总结一下。

1.  找回来 Docker Hub 的账号，本来没抱多大希望，但试试也无妨，努力一下或许就会有好结果。

2.  有些人可能有多个邮箱账号在使用，如 QQ/163/gmail/outlook 等等，可以把这些邮箱的邮件通过转发（或设置代收/代发）的方式，在一个常用的主邮箱里面进行统一管理，一来省心省力，二来方便检索。

3.  个人比较喜欢 QQ 邮箱（可以设置成 foxmail 作为你的 QQ 主显邮箱），配合日历、记事本、在线文档使用，简直不要太爽！![qq-mail.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmw7fPzKTXdtV6bgQtIBfZ1XUdoU.png)
