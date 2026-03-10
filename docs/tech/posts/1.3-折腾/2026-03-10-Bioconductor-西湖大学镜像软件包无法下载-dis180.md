---
title: Bioconductor 西湖大学镜像软件包无法下载
number: 180
slug: discussions-180/
url: https://github.com/shenweiyan/Digital-Garden/discussions/180
date: 2026-03-10
authors: 
  - shenweiyan
categories: 
  - 折腾
tags: ['1.3.6-R', 'Bioconductor']
---

[**Bioconductor**](https://www.bioconductor.org/) 为高通量基因组数据的分析和可视化提供开源工具。Bioconductor 多数软件包采用 R 统计编程语言开发。Bioconductor 每年释出两个版本，并有活跃的用户社区。

## 版本说明

由于 Bioconductor 的 rsync 上游会自行删除非最新的版本，大部分镜像站仅提供 Bioconductor 的当前最新版本和开发版本，只有少量镜像站点会保留过时的版本。目前已知[西湖大学镜像站](https://mirrors.westlake.edu.cn/)提供了历史版本的镜像。

详细讨论参见 [tuna/issues#1969](https://github.com/tuna/issues/issues/1969)。

## 问题

先看一下问题，在 R 里面直接配置配置西湖大学的 bioconductor 镜像站，执行 `BiocManager::install` 包安装提示 "cannot open URL"。
```r
> options(BioC_mirror="https://mirrors.westlake.edu.cn/bioconductor")
> BiocManager::install("ChAMP")
Warning: unable to access index for repository https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/bioc/src/contrib:
  cannot open URL 'https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/bioc/src/contrib/PACKAGES'
Warning: unable to access index for repository https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/data/annotation/src/contrib:
  cannot open URL 'https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/data/annotation/src/contrib/PACKAGES'
Warning: unable to access index for repository https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/data/experiment/src/contrib:
  cannot open URL 'https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/data/experiment/src/contrib/PACKAGES'
Warning: unable to access index for repository https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/workflows/src/contrib:
  cannot open URL 'https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/workflows/src/contrib/PACKAGES'
Warning: unable to access index for repository https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/books/src/contrib:
  cannot open URL 'https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/books/src/contrib/PACKAGES'
Bioconductor version 3.18 (BiocManager 1.30.22), R 4.3.0 (2023-04-21)
Installing package(s) 'ChAMP'
```

<!-- more -->

在 R 中验证 `libcurl` 支持，也发现不支持 http2，而且 `download.file` 时候提示 'SSL connect error'。
```r
# 1. 检查 R 是否编译支持 libcurl
capabilities("libcurl")
# TRUE = 支持，FALSE = 不支持

# 2. 查看 R 的完整编译配置
R.version$capabilities

# 3. 查看 libcurl 版本信息（如果支持）
if (capabilities("libcurl")) {
  print(curl::curl_version())  # 需要 curl 包
}

# 4. 测试实际下载（使用 libcurl 方法）
options(download.file.method = "libcurl")
options(download.file.quiet = FALSE)  # 显示下载过程

test_url <- "https://mirrors.westlake.edu.cn/bioconductor/3.18/bioc/PACKAGES"
download.file(test_url, destfile = "test_PACKAGES", method = "libcurl")
```

但是，用 `wget` 测试却是正常的！
```bash
$ wget -S "https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/bioc/src/contrib/PACKAGES"
--2026-03-10 13:17:10--  https://mirrors.westlake.edu.cn/bioconductor/packages/3.18/bioc/src/contrib/PACKAGES
Resolving mirrors.westlake.edu.cn (mirrors.westlake.edu.cn)... 124.160.108.195, 42.247.30.189, 2001:250:6413:1002:250:56ff:10:195
Connecting to mirrors.westlake.edu.cn (mirrors.westlake.edu.cn)|124.160.108.195|:443... connected.
HTTP request sent, awaiting response...
  HTTP/1.1 200 OK
  Date: Tue, 10 Mar 2026 05:17:28 GMT
  Content-Length: 836345
  Connection: keep-alive
  Accept-Ranges: bytes
  Alt-Svc: h3=":443"; ma=2592000
  Etag: "d0nehqitrzwjhxbt"
  Last-Modified: Thu, 18 Apr 2024 16:48:34 GMT
  Vary: Accept-Encoding
Length: 836345 (817K)
Saving to: ‘PACKAGES’

PACKAGES                                100%[===============================================================================>] 816.74K  1.00MB/s    in 0.8s

2026-03-10 13:17:13 (1.00 MB/s) - ‘PACKAGES’ saved [836345/836345]
```

使用 `wget` 下载具体的包也是正常的。
```bash
wget  -c -t 0 --no-check-certificate https://mirrors.westlake.edu.cn/bioconductor/3.18/data/experiment/src/contrib/ChAMPdata_2.34.0.tar.gz
```

事情到这里，基本可以肯定是默认的 `libcurl` 有问题，至于具体是什么问题，折腾了好久都没排查个所以然来，虽然在 《[R 语言 download.file 的几点知识](https://shenwy.com/yuque/%E5%BC%80%E5%8F%91%E8%BF%90%E7%BB%B4/r/2021-02-20-r-download-file/)》也讨论过 R 通过 `download.file` 下载数据和软件包默认方法的问题，但对 `libcurl` 一直都了解的太少。

## 使用 wget 方法

**既然 `wget` 可以正常下载西湖大学镜像的具体包，说明网络和镜像本身没问题。我们可以通过配置 R 的下载方法，让 BiocManager 调用 `wget` 而非默认的 `libcurl`/`internal` 方法。**
```r
# 设置全局下载方法为 wget
options(download.file.method = "wget")

# （可选）BiocManager 专属选项（某些版本支持）
options(BiocManager.download.file.method = "wget")

# （可选）添加 wget 额外参数，如超时、重试、断点续传
options(download.file.extra = paste(
  "--timeout=60",      # 超时时间（秒）
  "--tries=3",         # 重试次数
  "--progress=bar:force",  # 强制显示进度条
  "--no-check-certificate" # 跳过证书验证（仅限内网/自签名证书）
))
```

这样子配置完后，就可以让  R 使用 `wget` 作为下载工具去下载西湖大学镜像的具体包了。

## 使用 curl 方法

这个方法其实在《[R 语言 download.file 的几点知识](https://shenwy.com/yuque/%E5%BC%80%E5%8F%91%E8%BF%90%E7%BB%B4/r/2021-02-20-r-download-file/)》也提到过，具体就是 —— 使用 `curl` 方法时，通常需要加上 `-L` 参数。这时候 R 会自动调用系统的 `curl` 命令在后台执行对应包的下载。
```r
# For method "curl" use argument extra = "-L".
options(download.file.method = "curl", extra = "-L")

# （可选）BiocManager 专属选项（某些版本支持）
options(BiocManager.download.file.method = "curl", extra = "-L")
```

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="180"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
