---
title: 语雀图片的同步迁移解决方案
urlname: 2019-08-08-sync-from-yuque-to-oss
author: 章鱼猫先生
date: 2019-08-08
updated: "2023-03-01 15:24:35"
---

登录 Github Hugo 自建博客时候，忽然发现很多文章的图片都出现了 404！后来检查才知道，原来从 2019 年 8 月起，语雀上的一些静态图片开启了防外链设置，因此之前通过 api 同步语雀文章的内容到第三方的平台，会导致包括图片在内的静态资源都无法访问。

于是乎，开始寻找解决方案。

- 方案一，通过七牛的镜像空间同步语雀的图片，然后渲染博客页面的时候将语雀域名转换为七牛上绑定的自定义域名，从而确保博客的图片都正常可用。关于七牛云镜像存储，这里列举两点介绍：

> 1.  七牛的镜像存储服务是一种快速的数据迁移和加速服务。可以帮助用户实现无缝数据迁移，迁移过程中并不影响原有业务系统的访问。镜像存储适用于迁移原有业务系统的已有数据。七牛提供分布式存储和加速分发服务，以分布式存储为核心服务。
>
> 2.  在镜像存储的业务模型里面，原来的图片或者视频访问域名将被配置为七牛的源站，而页面里面引用图片或视频链接的地方必须使用新的访问域名。然后将新的访问域名绑定 (CNAME) 到七牛空间对应的域名。在这些操作完成之后，终端用户就可以通过七牛访问图片或者视频等非结构化资源了。在每个访问请求到七牛的时候，如果七牛空间中不存在这个资源，那么七牛将主动回客户源站抓取资源并存储在空间里面，这样七牛就不需要再次回源客户的资源站点了。
>
> 更详细的介绍，请参考七牛云官方文档：《[七牛镜像存储使用手册](https://developer.qiniu.com/kodo/kb/1376/seven-cattle-image-storage-instruction-manuals)》。

- 方案二，使用对象存储的镜像回源，不管是阿里云的 oss，还是腾讯云的 cos 都可以满足这一点。什么是回源，镜像回源又是什么意思，这里摘录几点信息：

> 1.  回源的概念。说的简单点，就是当访问的 OSS 资源不存在，则直接跳过对 OSS 的请求，直接去访问网站本身存在的文件。例如网站上使用了一张图片 `static.a.com/images/a.jpg` ，按道理，应该在 OSS 的 bucket 中也存在 `/images/a.jpg` ，这样访问 `static.a.com/images/a.jpg`  时，才能正常看到这张图片。但是，可惜的是，管理员把图片上传到了 `www.a.com/images/a.jpg` ，也就是上传到了网站服务器上面去，而 OSS 中没有这张图片。而这个时候，回源的效果就是，访问 `static.a.com/images/a.jpg`  时，发现 OSS 中没有这张图片，CDN 立即去找 `www.a.com/images/a.jpg` ，如果有，则返回这张图片。
>
> 2.  那镜像又是怎么回事呢？就是做一个备份。上面这个情况中，OSS 中没有这张图片，而网站服务器上有这张图片，通过访问 `static.a.com/images/a.jpg`  时，正常显示了图片，这个时候通过镜像功能，直接把这张图片镜像到 OS S 中的 `/images/a.jpg` ，下一次再访问 `static.a.com/images/a.jpg`  时，OSS 中就有这张图片了。

下面具体介绍一下这两种方案的一些具体操作。

# 一、使用七牛云的镜像存储

## 1.1 注册，并新建对象存储的存储空间

七牛云注册，实名认证，这里不细说，很简单。新建对象存储的存储空间也很简单：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhD1lAfu-UV6bpzBTXa7vns2waaO.png)

## 1.2 增加镜像存储的镜像源

在创建好的对象存储空间（note-db）中，选择 "镜像存储"，添加语雀镜像源地址：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqnSjqQ1h_AGmImexpTVpUuHqrGf.png)

## 1.3 绑定域名

七牛云绑定域名，并且设置 CNAME 的一个重要前提是：域名必须备案成功了才可以使用的！

简单说一下绑定了域名的作用：我们在七牛云上存储了图片文件什么的，访问地址都需要加上一个域名的。起初我们开通对象存储的时候，七牛云会给我们一个测试域名。但是测试域名会被收回，公告如下：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FijLo6r-uVq2ZLTbH_MvILEk3piD.png)

所以我们需要用我们自己的二级域名来绑定七牛云进行访问（最好不用 www 开头的二级域名来绑定，因为 www 开头的域名，我们都是作为主域名的），具体绑定步骤如下。

### 1.3.1 绑定域名

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fjq2sidHfcWc1BP9pZn9EM2jQvq2.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fg2gkw0JFg8QVidXq5rQ7NqVDM7h.png)

### 1.3.2 配置 CNAME

**首先**，上面 3.1 步骤，点击 "确认" 完成后，即可看到新增加域名的 CNAME 信息：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjBW4--eURX63coCfMwPmOTkE_oR.png)

**第二步**，到你买域名的地方去配置。我是在阿里云上面买的，下面以阿里云为例：

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmVa6wK7g8yWzYayK-NCR1HeFHSQ.png)
\*\*做到这一步就算已经完成了。成功之后，回到七牛云对象存储，在存储空间的概览也可以看到 CNAME 状态显示为"成功"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqUy4JQdwDQ1EM_k1dRzGZCTUtVu.png)

**第三**，在博客中把博客所有  [https://cdn.nlark.com](https://cdn.nlark.com/)  的域名都替换成  [http://qiniu.bioinit.com](http://qiniu.bioinit.com/)  即可。

**第四**，如果想要换成  [https://qiniu.bioinit.com](http://qiniu.bioinit.com/)，需要在存储空间的 **"域名管理"**  中修改 https 配置。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpYa6F1OQtJVZ7_8n4raCIyNU40b.png)

HTTPS 配置中的 SSL 证书可以选择申请七牛与的免费证书；也可以申请阿里云的\*\* "免费型 DV SSL" **证书，然后选择本地上传 **"证书内容"** 和 **"证书私钥"**，我这里选择的是阿里云的** "免费型 DV SSL" \*\*证书。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fq5JW6xmF4nNAp4LU1HUH3Ymmlar.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkezkzI6uURpQNZfRzZjTtVGWWvz.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgFHSAFRhVRDMysAoCY4vHN1x9Bw.png)

**"确认"**  提交后，等待大约 10 分钟，可以在七牛云对象存储空间的 **"域名管理"** → **"HPPTS 配置"**  看到 HTTPS 已经开启。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fuv4WG_FNYVPd_ntz4H4xht6NGAa.png)

**最后**，在博客中把博客所有  [https://cdn.nlark.com](https://cdn.nlark.com/)  的域名都替换成  [https://qiniu.bioinit.com](http://qiniu.bioinit.com/)，并检查图片是否正常显示。

# 二、使用对象存储的镜像回源

关于对象存储的镜像回源，我们以阿里云的 oss 对象存储为例。

## 2.1 创建 bucket，选择镜像回源

我们可以在 oss 的 bucket 中选择 "**基础设置**" 页面的   "**镜像回源**" 设置。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fkuic0mx5CeObKnuCjAaIZC1nh-D.png)

## 2.2 添加镜像回源规则

在 "**镜像回源**" 设置中 "**添加规则**"，添加规则时，会问你是否需要镜像，如果不镜像，就不会自动备份迁移一个到 OSS 中，下次访问的时候，虽然还会回源，但不一定正常显示图片，因此这里选择"**镜像**"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoqlqaHkkKXxB0avqMsrInEc_GVM.png)

这里有两个前缀的选项，比较好玩：

- 第一个前缀实际上是一个判断条件，比如你访问 `https://bucketname.oss-endpoint.com/yuque/xxx`  就遵循这条规则，如果你访问 `https://bucketname.oss-endpoint.com/videos/xxx`  则不遵循这条规则，就不会回源了。

- 第二个实际上是一个 url 重写的条件，比如你访问通过 bucketname.oss-endpoint.com/demo.jpg 这链接去访问 cdn.nlark.com/yuque/0/2019/png/1232/demo.jpg  这张语雀的图片，这个时候你就可以你可以把 yuque/0/2019/png/1232  当做前缀。如果你想选择最省事的做法，可以跟我一样选择留空。

- 你也可以针对不同格式、不同年份的文件设置粒度更细的镜像回源规则，详细可以参考：《[管理回源设置](https://help.aliyun.com/document_detail/31865.html)》。

## 2.3 变更链接

上一步镜像回源的规则创建好，点击 "确定" 后，在博客中我们只需要把博客所有 `https://cdn.nlark.com` 的域名都替换成你 oss 对应的外网访问 Bucket 域名（如， `https://bucketname.oss-endpoint.com`  即可），并检查图片是否正常显示。

对于其他镜像回源规则的链接变更：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhwUMa1xlPdbZ91XKtVQ-hTWQpin.png)

- 把 cdn.nlark.com/yuque/0 替换成 notedb.oss-cn-shenzhen.aliyuncs.com 即可。

# 三、个人博客

最后，附上与语雀文章同步更新，基于 Hugo 的个人博客。
![shen-bioitee.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjMPtnGLbxm5-GoDa34mLICaFti5.png)
