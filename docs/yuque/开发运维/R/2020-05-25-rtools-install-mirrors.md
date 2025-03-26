---
title: 使用镜像加速 Rtools 下载与安装
urlname: 2020-05-25-rtools-install-mirrors
author: 章鱼猫先生
date: 2020-05-25
updated: "2021-06-25 10:41:19"
---

## Rtools 是什么

在 windows 使用 R，尤其是安装 R 包的时候，经常会遇到一些 Rtools 的问题。Rtools 作用很大，但我们一般不怎么会直接使用。

> Rtools provides a toolchain for Windows platform that work well with R. It mainly includes GNU make, GNU gcc, and other utilities commonly used on UNIX-ish platform. R statistical language & environment is that it is open source and cross-platform.

## Rtools 安装

在 RStudio 中安装 shiny 包的时候，就出现了要安装 Rtools 的 warning，提示信息中还给出了下载的链接地址。但问题是  <https://cran.rstudio.com/bin/windows/Rtools/>  是位于国外的服务器，下载速度慢的令人发指。
![Rtools.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlFdrUE7yY-fxOa_xV4JL1njI0nP.png)

### 方法一

使用清华大学的 CRAN 镜像下载 Rtools，镜像地址：<https://mirrors.tuna.tsinghua.edu.cn/CRAN/>，如果你记不住这一串常常地址，可以从 CRAN 官网点击进去。
![cran-mirrors.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fh9lDB_tIj_d10FyEu489TCJYQgD.png)

在清华大学的 CRAN 页面选择  [Download R for Windows](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/)，在出现的 R for Windows 页面选择 Rtools：
![r-for-win.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvVvo41dX4Ii00yCL-vrbouQDjYJ.png)
![rtootls.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FohxkjxwTpndCpbuN04GLyZIZe5Q.png)

在 Rtools 选择下载最新版本的 Rtools，或者下载 R 版本对应 Rtools：
![rtools-main.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoJQZqNUIiZ7D5K2m7VZnY5OpzNu.png)
![rtools-download.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FouJ2qmcRIHkGPhHtEdgtacDQec7.png)\*\*

:::tips
**注意！！！**
\*\*
\*\*当我们通过下面\***\*的链接直接访问清华大学 CRAN 的 Rtools 时：\*\*** **[**https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/Rtools/**](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/Rtools/)** \*\*
\*\*
**这里面有一个问题需要注意，即点击 "this page" 访问 R 其他版本对应的 Rtools 时会默认跳转到 CRAN 官网默认的\*\*\*\*页面！**
[**https://cran.r-project.org/bin/windows/Rtools/history.html**](https://cran.r-project.org/bin/windows/Rtools/history.html)

**正常情况下应该是跳转到清华大学的 Rtools history 页面\*\*\*\*才对！！！**
[**https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/Rtools/history.html**](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/Rtools/history.html)
:::

[Building R for Windows](https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/Rtools/history.html)

![bug-cran-rtools.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FstA08MbJIAHF0uIfZD7i-ZYGVrU.png)

最后，安装 Rtools，这没什么好说的，按照默认设置一路 Next 下去，最后就安装成功，这里只强调一点是把勾选添加 rtools 到环境变量中。
![add-rtools-to-path.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsJDVwIrbX-Bi9RkRtqzJ7TI3fMm.png)

### 方法二

第二种方法，我是在网络上看到，大家也可以参考一下。

```r
options("repos"=c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
install.packages('installr')
library(installr)
install.Rtools()
```

这是通过设置清华大学 CRAN 后，先安装  installr 包，再通过这个包直接下载安装 Rtools，速度上同样也是杠杠的。\*\*
