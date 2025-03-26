---
title: 服务器关于 OpenSSL/SSL 的异常处理备忘
urlname: 2021-02-20-ssl-issues
author: 章鱼猫先生
date: 2021-02-20
updated: "2021-06-25 10:54:01"
---

## 1. OpenSSL: error:100AE081

这个问题其实是我在 CentOS 6.5 中安装 “packagefinder” R 包的时候遇到的一个问题（其实 wget 下载 https 资源的时候也出现了这个问题）。

```bash
> install.packages("packagefinder")
--- Please select a CRAN mirror for use in this session ---
Warning: failed to download mirrors file (cannot open URL 'https://cran.r-project.org/CRAN_mirrors.csv'); using local file '/RiboBio/home/shenweiyan/software/R/R-4.0.3/lib64/R/doc/CRAN_mirrors.csv'
trying URL 'https://mirrors.ustc.edu.cn/CRAN/src/contrib/packagefinder_0.3.2.tar.gz'
Content type 'application/octet-stream' length 433718 bytes (423 KB)
==================================================
downloaded 423 KB

* installing *source* package ‘packagefinder’ ...
** package ‘packagefinder’ successfully unpacked and MD5 sums checked
** using staged installation
** R
** inst
** byte-compile and prepare package for lazy loading
** help
*** installing help indices
*** copying figures
** building package indices
** testing if installed package can be loaded from temporary location
Warning in url(sprintf("%s/%s", cran, path), open = "rb") :
  URL 'https://CRAN.R-project.org/web/packages/packages.rds': status was 'SSL connect error'
Error: package or namespace load failed for ‘packagefinder’:
 .onAttach failed in attachNamespace() for 'packagefinder', details:
  call: url(sprintf("%s/%s", cran, path), open = "rb")
  error: cannot open the connection to 'https://CRAN.R-project.org/web/packages/packages.rds'
Error: loading failed
Execution halted
ERROR: loading failed
* removing ‘/Bioinfo/SoftWare/R/R-4.0.3/lib64/R/library/packagefinder’

The downloaded source packages are in
        ‘/tmp/RtmpTjsgn2/downloaded_packages’
Updating HTML index of packages in '.Library'
Making 'packages.html' ... done
Warning messages:
1: In download.file(url, destfile = f, quiet = TRUE) :
  URL 'https://cran.r-project.org/CRAN_mirrors.csv': status was 'SSL connect error'
2: In install.packages("packagefinder") :
  installation of package ‘packagefinder’ had non-zero exit status
>
```

```bash
[root@log01 ~]# wget https://cran.r-project.org/src/contrib/packagefinder_0.3.2.tar.gz --no-check-certificate
--2021-02-20 11:50:14--  https://cran.r-project.org/src/contrib/packagefinder_0.3.2.tar.gz
Resolving cran.r-project.org... 137.208.57.37
Connecting to cran.r-project.org|137.208.57.37|:443... connected.
OpenSSL: error:100AE081:elliptic curve routines:EC_GROUP_new_by_curve_name:unknown group
OpenSSL: error:1408D010:SSL routines:SSL3_GET_KEY_EXCHANGE:EC lib
Unable to establish SSL connection.
```

拿着这个问题，谷歌了一下，发现有些人说需要升级 wget（configure 的时候增加一个 --with-ssl=openssl 选项），个人尝试了一下，其实解决不了问题。

个人比较信服的一个解析：

> 参考 <https://www.centos.org/forums/viewtopic.php?f=14&t=43803> 这个连接的解释，说这是 CentOS 6.5 的一个 bug，不过已经修复了。如果是使用在线的 yum 源的话，应该是不会出现这个问题的。不过我使用的是本地源，所以就出现了这个问题，这个应该是版本兼容性不行导致的。
>
> 由于 CentOS 6.5 自带的 OpenSSL 最高版本是 openssl-1.0.1e-15.el6.x86_64，因此我们可以通过升级 openssl 到 openssl-1.0.1e-16 及以上，比如：openssl-1.0.1e-16.el6_5.x86_64.rpm，或者 openssl-1.0.1e-57.el6.x86_64.rpm。
>
> 由于 CentOS 已经含有 openssl-1.0.1e-15.el6_5.x86_64 这个软件，所以需要使用命令：

```bash
rpm -ivh --replacefiles openssl-*.rpm
```

:::tips
**温馨提示：**

谷歌搜索 openssl-1.0.1e-16 及以上的 rpm 时，在 <https://centos.pkgs.org/6/centos-x86_64/> 中找到的 rpm 下载包下载链接基本都会指向 404 错误，无法下载！！！

最后在 <http://ftp.iij.ad.jp/pub/linux/centos-vault/6.8/cr/x86_64/Packages/> 才找到 [openssl-1.0.1e-57.el6.x86_64.rpm](http://ftp.iij.ad.jp/pub/linux/centos-vault/6.8/cr/x86_64/Packages/openssl-1.0.1e-57.el6.x86_64.rpm) 的一个可用下载链接。
:::

最终解决方法：

```bash
[root@log01 pkgs]# wget http://ftp.iij.ad.jp/pub/linux/centos-vault/6.8/cr/x86_64/Packages/openssl-1.0.1e-57.el6.x86_64.rpm
[root@log01 pkgs]# rpm -ivh --replacefiles openssl-1.0.1e-57.el6.x86_64.rpm
warning: openssl-1.0.1e-57.el6.x86_64.rpm: Header V3 RSA/SHA1 Signature, key ID c105b9de: NOKEY
Preparing...                ########################################### [100%]
   1:openssl                ########################################### [100%]
[root@log01 pkgs]# rpm -qa|grep openssl
openssl-1.0.1e-15.el6.x86_64
openssl-1.0.1e-57.el6.x86_64
openssl-devel-1.0.1e-15.el6.x86_64
```

安装完成后，通过 wget 再次下载 https 资源，重新安装 “packagefinder” R 包都显示一切正常！
