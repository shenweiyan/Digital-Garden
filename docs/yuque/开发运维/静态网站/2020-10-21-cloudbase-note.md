---
title: 腾讯云 cloudbase 云开发使用笔记
urlname: 2020-10-21-cloudbase-note
author: 章鱼猫先生
date: 2020-10-21
updated: "2021-06-30 09:36:01"
---

> **产品概述**

> 云开发（Tencent CloudBase，TCB）是腾讯云提供的云原生一体化开发环境和工具平台，为开发者提供高可用、自动弹性扩缩的后端云服务，包含计算、存储、托管等 serverless 化能力，可用于云端一体化开发多种端应用（小程序、公众号、Web 应用、Flutter 客户端等），帮助开发者统一构建和管理后端服务和云资源，避免了应用开发过程中繁琐的服务器搭建及运维，开发者可以专注于业务逻辑的实现，开发门槛更低，效率更高。

>

## 使用场景

> 您可以使用云开发，轻松开发多种端应用，包括小程序、公众号、Web 应用、Flutter 客户端等：
>
> - 构建属于您的博客：将您的静态网站文件部署到云开发静态托管中，您的用户可以随时随地通过域名访问您的博客。
> - 分析海量图片：将您的照片存储在云开发云存储中，使用图像标签扩展能力，轻松完成图片标签识别，帮您实现相册分类。
> - 构建运营管理后台：使用 CMS 扩展功能，帮您完成文章编辑和发布、素材管理等数据和内容的管理，省去您手动线上修改数据库数据或者开发管理后台的麻烦。

![腾讯云静态网站托管.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FntONRJ0rSf3jLzL0FUwISnD_-tP.png)
腾讯云最近在官网上线了一个静态网站托管的产品，结合腾讯云提供的 CloudBase CLI 工具，可以实现的第三方的任意一个服务器快速持续部署自己的 [Hexo](https://cloud.tencent.com/document/product/1210/43365)、[VuePress](https://cloud.tencent.com/document/product/1210/43388)、[Hugo](https://cloud.tencent.com/document/product/1210/43389)。

```bash
# 安装 cloudbase cli
npm install -g @cloudbase/cli

# 执行登录命令，登录腾讯云开发 CLI
tcb login --apiKeyId xxxxx --apiKey xxxxx

# 在 hugo-site 中将 public 目录中的文件给部署上去, EnvID 替换为在腾讯云中已经创建好的环境 ID
cloudbase hosting:deploy ./public  -e EnvID

# 打开腾讯云 云开发控制台，单击左侧菜单栏中的【静态网站托管】>【设置】，进入设置页面，
# 可以找到默认的域名，单击域名，就可以看到您刚部署的 Hugo。
```

![静态网站托管.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpbDxt-TXvDHCrVR3ioH45KEOsG1.png)
![cloudbase-deploy.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fqq-2_UYPAbz_tUPDyJpgyenrAYJ.png)

腾讯云静态网站下 cloudbase CLI 详细操作：
[403 Forbidden](https://cloud.tencent.com/document/product/876/41543)

阿里云有阿里云的 oss 静态网站产品，如果你的域名是在阿里云注册备案的，可以考虑使用阿里云自家的产品。如果你的域名是在腾讯云注册备案的，你又想在微信、QQ 这些平台快速预览你的博客或者其他 web 应用，cloudbase CLI +静态网站也算是一个挺不错的选择。

### 腾讯云域名注册优惠

\*\*
最后，安利一个腾讯云 .COM .Net 域名只要 20 元，每周四域名注册优惠价的活动：
[403 Forbidden](https://curl.qcloud.com/wgaUKLZY)

- 本活动自本日起到 2020 年 12 月 31 日期间 每个周四当天 0:00-24:00，原价 55 元的 COM 优惠价 20 元可注册。不可再使用其他优惠券等再次优惠。
- 有的周四只有 20 元的 COM，有的周四 COM NET 域名都有优惠。

![txcom20200917.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fsgt19kDrhYHffbz9JmuZPUIbJPi.png)

### 腾讯云域名续费优惠券

腾讯云域名续费优惠券满 20 减 10 ：
[腾讯云活动推荐](https://url.cn/52L4ZSe)

通过云开发  [CloudBase Framework](https://github.com/TencentCloudBase/cloudbase-framework)  框架将静态网站一键部署云开发环境，提供生产环境可用的 CDN 加速、自动弹性伸缩的高性能网站服务。可以搭配其他插件如 Node 插件、函数插件实现云端一体开发。
