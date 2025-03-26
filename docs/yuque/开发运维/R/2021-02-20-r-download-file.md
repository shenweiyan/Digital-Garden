---
title: R 语言 download.file 的几点知识
urlname: 2021-02-20-r-download-file
author: 章鱼猫先生
date: 2021-02-20
updated: "2021-12-07 10:22:00"
---

R 语言中，不管是安装包，还是下载数据，很多时候都会用到 download.file 这个函数。如果你在安装包或者下载数据过程中出现中断，或者异常，想要判断是远程源服务器的问题，还是自身服务器的问题，还是网络故障，甚至于你想要换一种方法去继续你的下载，了解一下 download.file 还是很有帮助的。

[download.file: Download File from the Internet](https://rdrr.io/r/utils/download.file.html)

上面的链接是关于 **download.file** 函数非常详细的一个文档，个人非常关注就是它关于 \*\*method \*\*参数设置和理解。

> If `method = "auto"` is chosen (the default), the behavior depends on the platform:
>
> - On a Unix-alike method `"libcurl"` is used except `"internal"` for file:// URLs, where `"libcurl"` uses the library of that name (<https://curl.se/libcurl/>).
> - On Windows the `"wininet"` method is used apart from for ftps\:// URLs where `"libcurl"` is tried. The `"wininet"` method uses the WinINet functions (part of the OS).
>
> Support for method `"libcurl"` is optional on Windows: use `capabilities("libcurl")` to see if it is supported on your build. It uses an external library of that name (<https://curl.se/libcurl/>) against which R can be compiled.

**关于 download.file 的几点理解和值得注意的地方：**

- **download.file** 是来源于 R 自带的 `utils`  包的一个函数，使用 `packageVersion("utils")` 可以查看该包的版本。

- 在类 Unix 系统中，默认使用 `"libcurl"` 的方法，而对 file:// 的链接会使用 `"internal"` 的下载方法。

- 在 windows 中，默认使用 `"wininet"` 的方法，对于 ftps\:// 的资源会尝试使用 `"libcurl"` 的下载方法。

- Method to be used for downloading files. Current download methods are  `"internal"`， `"wininet"` (Windows only) `"libcurl"`, `"wget"` and `"curl"`, and there is a value `"auto"` .

- 注意 `"libcurl"` 和  `"curl"` 的区别，严格意义上，两者不是同一个东西。

  - **相同点：**
    - curl 和 libcurl 都可以利用多种多样的协议来传输文件，包括 HTTP, HTTPS, FTP, FTPS, GOPHER, LDAP, DICT, TELNET and FILE 等。
  - **不同点**
    - curl 是命令行工具，可以通过 shell 或脚本来运行 curl。curl 底层所使用的库是 libcurl。
    - libcurl 是一个库，通常与别的程序绑定在一起使用，如命令行工具 curl 就是封装了 libcurl 库。所以我们也可以在你自己的程序或项目中使用 libcurl 以获得类似 CURL 的强大功能。

- The method can also be set through the option `"download.file.method"`: see `options()`.

  - 可以使用 \*\*options(download.file.method = "libcurl") \*\*的方式指定全局下载的方法。
  - 参考：<https://stackoverflow.com/a/63104633>

```r
install.packages("devtools", method = "libcurl", extra = " --insecure --user")

libcurl_opts <- list(
  download.file.method = "libcurl",
  download.file.extra = " --insecure --user"
)
old_opt <- options(libcurl_opts)

getOption("download.file.method")

options(old_opt)
getOption("download.file.method")
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpMVz5NAdqvK7DdK8zMMIkKZIbhd.png)

- 使用 curl 方法时，通常需要加上 -L 参数。这时候 R 会自动调用系统的 curl 命令在后台执行对应包的下载。

```r
# For method "curl" use argument extra = "-L".
options(download.file.method = "curl", extra = "-L")
```

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuApwtzylYe69akxEZhm0C1phg5h.png)
