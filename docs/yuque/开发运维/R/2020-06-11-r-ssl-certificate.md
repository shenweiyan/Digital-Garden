---
title: R 语言关于 SSL 证书异常处理笔记
urlname: 2020-06-11-r-ssl-certificate
author: 章鱼猫先生
date: 2020-06-11
updated: "2023-07-10 16:32:03"
---

![ssl.jpg](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fud21xdJYwOyX5x2rMd29G6uNZYl.jpeg)

## 一、关于 TCGAbiolinks

TCGAbiolinks 是一个用于 TCGA 数据综合分析的 R/BioConductor 软件包，能够通过 GDC Application Programming Interface (API) 访问 National Cancer Institute (NCI) Genomic Data Commons (GDC) ，来搜索、下载和准备相关数据，以便在 R 中进行分析。

## 二、问题

神奇的是，今天在 R 操作 TCGAbiolinks 却遇到了一个极其棘手的问题：

```r
library(TCGAbiolinks)
query <- GDCquery(project = "TARGET-OS",
                  data.category = "Transcriptome Profiling",
                  data.type = "Gene Expression Quantification",
                  workflow.type = "HTSeq - Counts")
```

![gdc-server-down.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp1rdqfkUkqDET2HNBAeyAsaIFIp.png)
拿着这个 error 去谷歌，看到的结果都是教你用 devtools 或者 TCGAbiolink 官网提供的方法从 github 重装一遍这个包：

```r
devtools::install_github("BioinformaticsFMRP/TCGAbiolinks")
BiocManager::install("BioinformaticsFMRP/TCGAbiolinks")
```

![google-gdc-error.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FotaPM7dMID-C-ktkZKEwJ85WoYy.png)
然而这些方法都未能解决我的问题，于是乎有了下面的一些探索。

## 三、源码分析

首先，我去 TCGAbiolink 中的源码看这个异常是在哪里导致的，在 R/internal.R 中发现：
![get-gdc-info.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtJNUd5A5Wc5zmqnd1Jf913oyu6q.png)

```r
> library(jsonlite)
> fromJSON("https://api.gdc.cancer.gov/status",simplifyDataFrame = TRUE)
Error in open.connection(con, "rb") :
  SSL certificate problem: unable to get local issuer certificate
```

后来又看了一下 `jsonlite`  的 `fromJSON`  函数，发现它其实是基于 `curl`  包来实现获取，以及下载相关的数据。

> The curl package provides bindings to the [libcurl](https://curl.haxx.se/libcurl/) C library for R. The package supports retrieving data in-memory, downloading to disk, or streaming using the [R “connection” interface](https://stat.ethz.ch/R-manual/R-devel/library/base/html/connections.html). Some knowledge of curl is recommended to use this package. For a more user-friendly HTTP client, have a look at the [httr](https://cran.r-project.org/package=httr/vignettes/quickstart.html) package which builds on curl with HTTP specific tools and logic.

![curl-fail.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjYgbIsfonnHL2KbOs-3psDhzZtM.png)
curl 去访问 https 的站点报错

看了一下 curl 和 curl 命令都是支持 ssl 的：

```r
$ curl -V
curl 7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.47.1 OpenSSL/1.0.1e zlib/1.2.8 libidn/1.18
Protocols: dict file ftp ftps gopher http https imap imaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: IDN IPv6 Largefile NTLM SSL libz
$ curl -h|grep ssl
    --ftp-ssl       Try SSL/TLS for ftp transfer (F)
    --ftp-ssl-ccc   Send CCC after authenticating (F)
    --ftp-ssl-ccc-mode [active/passive] Set CCC mode (F)
    --ftp-ssl-control Require SSL/TLS for ftp login, clear for transfer (F)
    --ftp-ssl-reqd  Require SSL/TLS for ftp transfer (F)
 -2/--sslv2         Use SSLv2 (SSL)
 -3/--sslv3         Use SSLv3 (SSL)
```

curl 的默认证书路径可以通过下面的命令查看：

```bash
$ curl -v https://www.baidu.com|& grep CAfile
*   CAfile: /etc/pki/tls/certs/ca-bundle.crt

$ curl-config --ca
/etc/pki/tls/certs/ca-bundle.crt
```

在前面 `jsonlite` 的 `fromJSON` 报错信息中有一个 More details here 的提示，里面给了证书下载地址：

```bash
http://curl.haxx.se/docs/sslcerts.html
```

![ca.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoBx529dQMZYOUY3aEizYeedqHKI.png)
下载并绑定证书：

```bash
$ wget https://curl.haxx.se/ca/cacert.pem --no-check-certificate
$ export CURL_CA_BUNDLE="/home/shenweiyan/certs/cacert.pem"
$ $ curl -v https://api.gdc.cancer.gov/status
*   Trying 192.170.230.246...
* Connected to api.gdc.cancer.gov (192.170.230.246) port 443 (#0)
* Cipher selection: ALL:!EXPORT:!EXPORT40:!EXPORT56:!aNULL:!LOW:!RC4:@STRENGTH
* successfully set certificate verify locations:
*   CAfile: /home/shenweiyan/cacert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Client hello (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
* Server certificate:
*        subject: CN=api.gdc.cancer.gov
*        start date: Jan 29 00:00:00 2020 GMT
*        expire date: Feb 16 23:59:59 2022 GMT
*        subjectAltName: api.gdc.cancer.gov matched
*        issuer: C=FR; ST=Paris; L=Paris; O=Gandi; CN=Gandi Standard SSL CA 2
*        SSL certificate verify ok.
> GET /status HTTP/1.1
> Host: api.gdc.cancer.gov
> User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.47.1 OpenSSL/1.0.1e zlib/1.2.8 libidn/1.18
> Accept: */*
>
< HTTP/1.1 200 OK
< Date: Thu, 11 Jun 2020 09:17:33 GMT
< Server: Apache
< Content-Length: 144
< Access-Control-Allow-Origin: *
< Access-Control-Expose-Headers: Content-Disposition
< Content-Type: application/json
< X-Frame-Options: SAMEORIGIN
< Strict-Transport-Security: max-age=63072001; includeSubdomains; preload
<
{"commit":"ab22b47a0f2ba62dd69e83fc287fe0581e839cad","data_release":"Data Release 24.0 - May 07, 2020","status":"OK","tag":"2.1.2","version":1}
* Connection #0 to host api.gdc.cancer.gov left intact
```

## 四、解决问题与验证

虽然环境变量 CURL_CA_BUNDLE （也可以添加到 \~/.bashrc 中）可以解决 curl 命令行中的证书问题，但是在 R 中依然没办法解决 SL certificate problem: unable to get local issuer certificate 的问题。折腾了许久，找到两个方法。

### 1. 更新系统默认证书

这是最快捷的方法，但需要管理员的权限。

```bash
## 管理员权限下，所有操作都应该备份。
mv ca-bundle.crt >ca-bundle.crt.bak

## 下载新的证书
wget https://curl.haxx.se/ca/cacert.pem --no-check-certificate

## 更新证书
cat ca-bundle.crt.bak cacert.pem >ca-bundle.crt
```

### 2. 新装 curl，绑定证书，重新编译 R

```bash
$ wget https://curl.haxx.se/download/curl-7.64.1.tar.gz --no-check-certificate
$ tar zvxf curl-7.64.1.tar.gz
$ cd curl-7.64.1

## 不指定证书
$ ./configure --prefix=/Bioinfo/SoftWare/NewLibs/curl-7.64.1

## 指定证书(推荐)
$ wget https://curl.haxx.se/ca/cacert.pem -O /Bioinfo/SoftWare/certs/ca-bundle.crt --no-check-certificate
$ ./configure --prefix=/Bioinfo/SoftWare/NewLibs/curl-7.64.1 --with-ca-bundle=/Bioinfo/SoftWare/certs/ca-bundle.crt

$ make
$ make install
```

R 的编译请参考：
[手把手教你在 Linux 源码安装最新版本的 R](https://www.yuque.com/shenweiyan/cookbook/install-latest-r-from-source?view=doc_embed)

### 3. 问题解决

一切准备就绪后，重新打开 R，验证问题是否解决。

```r
> library(TCGAbiolinks)
> query <- GDCquery(project = "TARGET-OS",
+                   data.category = "Transcriptome Profiling",
+                   data.type = "Gene Expression Quantification",
+                   workflow.type = "HTSeq - Counts")
--------------------------------------
o GDCquery: Searching in GDC database
--------------------------------------
Genome of reference: hg38
--------------------------------------------
oo Accessing GDC. This might take a while...
--------------------------------------------
ooo Project: TARGET-OS
--------------------
oo Filtering results
--------------------
ooo By data.type
ooo By workflow.type
----------------
oo Checking data
----------------
ooo Check if there are duplicated cases
ooo Check if there results for the query
-------------------
o Preparing output
-------------------
>
```

## 五、总结

从 TCGAbiolinks 的 GDC server down 到 SSL certificate problem: unable to get local issuer certificate，从发现问题到谷歌、定位解决，前后耗费了差不多整整一天的时间！

R 语言的 curl 包和系统 curl 的关系目前看不太懂，虽然 curl 包为 R 提供了到 libcurl c 语言库的绑定，但貌似 [R “connection” interface](https://stat.ethz.ch/R-manual/R-devel/library/base/html/connections.html) 才是 curl 实现 retrieving data in-memory, downloading to disk, or streaming 的关键。

包括 curl 在内有些后续的问题，需要深入再研究一下，也希望有此问题的同行们多多指教。

## 六、参考资料

1.  奔狼的春晓，《[curl 支持 ssl 报错：SSL certificate problem: unable to get local issuer certificate](https://blog.csdn.net/lixuande19871015/article/details/88788699?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)》，CSDN
2.  curl，《[SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html)》，curl.haxx.se
3.  curl vignettes，《[The curl package: a modern R interface to libcurl](https://cran.r-project.org/web/packages/curl/vignettes/intro.html)》，cran.r-project.org
4.  《[How to update cURL CA bundle on RedHat?](https://serverfault.com/questions/394815/how-to-update-curl-ca-bundle-on-redhat)》，Server Falut
