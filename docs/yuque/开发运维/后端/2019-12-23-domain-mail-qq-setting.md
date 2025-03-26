---
title: QQ 邮箱设置自定义域名邮箱
urlname: 2019-12-23-domain-mail-qq-setting
author: 章鱼猫先生
date: 2019-12-23
updated: "2021-11-19 16:27:16"
---

> 关于学术机构的官方邮箱，听的最多的一个问题就是，要投稿要发论文了，用 QQ 邮箱或者网易邮箱可不可以，会不会有影响？再比如，有时很正式很重要的通讯，如申请博后或访问学者，学术交流等，国内学者大多留下的联络邮箱常为普通公共邮箱，如 hotmail.com，126.com，163.com，QQ.com，sohu.com，sina.com，yahoo.com，… 等。虽然这些非学术公共邮箱使用是没有任何问题的，但总不够正式。那么，有没有什么办法自己可以申请或创建一个看起来更专业高大上的邮箱呢？
>
> 首先理解一下，qq 邮箱设置域名邮箱，其实就是给你的 qq 邮箱起个别名而已，可以用自定义邮箱去收发邮件，但是邮件还是在 qq 邮箱里，qq 邮箱的无限邮箱容量对你的域名邮箱同样适用。

**2020.01.20：**
更新一下信息，今天登陆 QQ 邮箱，看到域名邮箱那里有个感叹号提醒，点开来看了看，发现是目前 QQ 邮箱已经不支持新增域名邮箱了，现有的域名邮箱暂时可以正常使用，但是鬼知道什么时候说不定就不能用了！！！ [V2EX](https://www.v2ex.com/t/639288) 上关于这件事情，有些评论挺有意思，可以去吃个瓜。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhU35B7YKc4qHQueZK5StGJP-lwg.png)

## 1. 创建域名邮箱

域名邮箱的主页是：<http://domain.mail.qq.com/>，这也是  QQ 域名邮箱直接登录的地址。我们直接在浏览器打开，在页面的左边栏就可以看到域名邮箱的创建入口。我们需要先通过 QQ 邮箱登陆。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp9-NJfVmtRkDz9BfmO3fZ174vs-.png)

登录后，选择创建域名邮箱。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiUSwqm-LtQbtWKrU6gagBfIitvO.png)

## 2. 填写自己的域名

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkNmKzg-YX60pXCAnujM5Jj-xR_f.png)

点击下一步，出现下面的页面，选择我们域名的提供商。小编的邮箱如果是在阿里云注册，所以选择其他提供商。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjXgEQ3GrtVIgOZ1Fog5zVlg5Gpt.png)

## 3. 添加 CNAME 和 Mx 记录

点击下一步，会出现下面的页面，根据提示添加 CNAME 和 Mx 记录。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhUfS-UpD_CL3LvZENvK1FimCcXB.png)

### 3.1  域名解析

这里以阿里云为例，登陆阿里云账号，选择对应域名的解析，点击"**添加记录**"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FteM2j-Q1qiwLOtyZ7wLOLqUuv7s.png)

### 3.2 添加记录

添加两条记录，将前面的内容直接复制过来，其余的默认就好。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpKitZ0d66F6rlk6ci1JSLPE9zqt.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fo9j5P8u3ZuImpG5msg-7N_AyHWJ.png)

## 4.  提交验证

返回 qq 邮箱刚才界面，点击提交验证。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FngioyeeV1BuUzgwMwLW7GZJeNrO.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk0doy0Bu616LDaGx7I5wEumf0Zy.png)

## 5. 添加成员

添加一个成员（注意，在添加新成员之前，需要首先设置域名邮箱的管理员），名字随便起，就跟你在别的平台注册邮箱一样。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlYFQSYQ9BbZ2GDJKcC7YhRXdjkI.png)

新建成员，点击"确定" 完成后。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fn0ioHNHdogTh8uJfWLeszdpdSEB.png)

进入新创建用户的 QQ 邮箱，在收到的域名邮箱确认邮件中，点击 "**接受这个邮箱账号**"，即可完成最后的创建。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu4UONWvHFt4ipp9kayo2BgH8Uj4.png)

最后，我们再次回到新创建用户 qq 邮箱\*\*设置  \*\*–>**账户**–>**账号管理**，此时就会出现刚刚设置的域名邮箱。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FomX7g66qMuir7-xZVhzQ-lfn1LB.png)

## 6. 主显账号

QQ 邮箱默认是以 xxx.qq.com 作为你的发信账号和主显账号，如果我们想在打开 QQ 邮箱的时候第一眼看到的就是自己的域名邮箱，我们可以这样设置。

通过 QQ 邮箱的"**设置 →  账户 →  账号管理 → 默认发信账号**"，选择你想要的邮箱。
**![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkOMW6bYzrpd6fccWhlIh5Zsrh1Y.png)**

**"保存更改"**  后，你就可以看到自己的默认 QQ 邮箱已经变成了你所设置的域名邮箱。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmzluQZQYrk77BQOEqdMiZlOPizk.png)

到这里，QQ 邮箱的自定义域名邮箱就全部设置完成了。接下来，你就可以使用 163 或者其他邮箱，对新创建的域名邮箱收发邮件进行测试验证一下。

最后想说的是，在阿里云，一个 `.cn`  域名一年才 29 块钱，而 `.top`  、 `.site`  之类域名一年更是 10 块钱不到，更不要说价格更加便宜的腾讯云域名，所以如果你想拥有一个自己专属的域名，除了备案可能过程稍微繁琐点，其他门槛都是极低的。
