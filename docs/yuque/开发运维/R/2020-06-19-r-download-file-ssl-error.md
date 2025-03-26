---
title: R 语言 download.file 的 SSL connect error
urlname: 2020-06-19-r-download-file-ssl-error
author: 章鱼猫先生
date: 2020-06-19
updated: "2021-06-25 10:41:01"
---

**异常信息：**

```r
> install.packages("rms")
--- Please select a CRAN mirror for use in this session ---
Warning: failed to download mirrors file (cannot open URL 'https://cran.r-project.org/CRAN_mirrors.csv'); using local file '/home/shenweiyan/software/R/R-3.6.1/lib64/R/doc/CRAN_mirrors.csv'
trying URL 'http://mirrors.tuna.tsinghua.edu.cn/CRAN/src/contrib/rms_6.0-0.tar.gz'
Content type 'application/x-gzip' length 623859 bytes (609 KB)
==================================================
downloaded 609 KB
......
* DONE (rms)

The downloaded source packages are in
        ‘/tmp/RtmpJF5nYY/downloaded_packages’
Updating HTML index of packages in '.Library'
Making 'packages.html' ... done
Warning message:
In download.file(url, destfile = f, quiet = TRUE) :
  URL 'https://cran.r-project.org/CRAN_mirrors.csv': status was 'SSL connect error'
>
```

**参考方法：**

- 先设置镜像，再执行包安装。

```r
# CRAN 镜像源配置文件之一是 .Rprofile (linux 下位于 ~/.Rprofile )，可以在文末添加如下语句:
options("repos" = c(CRAN="https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
```

- 也有可能是由于 CentOS 6.x 自带的 OpenSSL（最高版本是 openssl-1.0.1e-15.el6.x86_64）引发的一个 bug，如果是这种情况，请参考这篇文章解决。

[服务器关于 OpenSSL/SSL 的异常处理备忘](https://www.yuque.com/shenweiyan/cookbook/ssl-issues?view=doc_embed)

## 参考资料

1.  Tuna，[CRAN 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/CRAN/)，[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)
2.  rstudio，[Secure Package Downloads for R](https://support.rstudio.com/hc/en-us/articles/206827897-Secure-Package-Downloads-for-R)，[RStudio Suppor](https://support.rstudio.com/hc/en-us)
