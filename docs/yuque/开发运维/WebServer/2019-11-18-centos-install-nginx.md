---
title: CentOS 7 下编译安装 Nginx
urlname: 2019-11-18-centos-install-nginx
author: 章鱼猫先生
date: 2019-11-18
updated: "2021-06-25 10:38:54"
---

## 一、准备工作

为了编译  `Nginx`  源代码，需要标准的  `GCC`  编译器。`GCC`  的全称为  `GNU Compiler Collection`，其由  `GNU`  开发，并以  `GPL`  及  `LGPL`  许可证发行，是自由的类  `UNIX`  即苹果电脑  `Mac OSX`  操作系统的标准编译器。因为  `GCC`  原本只能处理  `C`  语言，所以原名为  `GNU C`  语言编译器，后来得到快速扩展，可处理  `C++`、`Fortran`、`Pascal`、 `Objective-C`、`Java`  以及  `Ada`  等其他语言。

除此之外，还需要  `Automake`  工具，以完成自动创建  `Makefile`  文件的工作。由于  `Nginx`  的一些模块需要依赖其他第三方库，通常有  `pcre`  库(支持  `rewrite`  模块)、`zlib`  库(支持  `gzip`  模块)和  `openssl`  库(支持  `ssl`  模块)等。

#### 1.1 安装第三方库

如果已经安装过以上软件，则可以略过；如果没有，可以使用一下命令进行在线安装：

```bash
$ yum -y install gcc gcc-c++ automake pcre pcre-devel zlib zlib-devel openssl openssl-devel
```

## 二、执行安装

### 2.1 创建 Nginx 用户

```bash
groupadd nginx
useradd nginx -g nginx -s /sbin/nologin -M
```

### 2.2 下载解压

Nginx 的下载地址在：<http://nginx.org/en/download.html>，我们推荐下载  Stable 的稳定版本。
![nginx-download.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk-UCu4rvnkkZA3nRizwZ-CJiSfX.png)

```bash
$ wget http://nginx.org/download/nginx-1.18.0.tar.gz
$ tar zvxf nginx-1.18.0.tar.gz
$ cd nginx-1.18.0
$ ll
total 752
drwxr-xr-x. 6 root root   4096 Nov 18 10:54 auto
-rw-r--r--. 1 root root 296463 Aug 13 20:51 CHANGES
-rw-r--r--. 1 root root 452171 Aug 13 20:51 CHANGES.ru
drwxr-xr-x. 2 root root    168 Nov 18 10:54 conf
-rwxr-xr-x. 1 root root   2502 Aug 13 20:51 configure
drwxr-xr-x. 4 root root     72 Nov 18 10:54 contrib
drwxr-xr-x. 2 root root     40 Nov 18 10:54 html
-rw-r--r--. 1 root root   1397 Aug 13 20:51 LICENSE
drwxr-xr-x. 2 root root     21 Nov 18 10:54 man
-rw-r--r--. 1 root root     49 Aug 13 20:51 README
drwxr-xr-x. 9 root root     91 Nov 18 10:54 src
```

这里对解压完成后的部分目录和文件做个简单的介绍：

- src 该目录存放了`Nginx`的所有源码；
- man 该目录存放了`Nginx`的帮助文档；
- html 该目录存放了两个`html`文件。这两个文件与`Nginx`服务器的运行相关，这两个文件的作用会在下文给出，这里不做赘述；
- conf 该目录存放的是`Nginx`服务器的配置文件，包含`Nginx`服务器的基本配置文件；
- auto 该目录存放了大量脚本文件，和`configure`脚本程序有关；
- configure 该文件是`Nginx`软件的自动脚本程序。运行`configure`脚本一般会完成两项工作：一是检查环境，根据环境检查结果生成`C`代码；二是生成编译代码需要的`Makefile`文件。

### 2.3 编译安装

在介绍生成 Makefile 文件操作之前，先介绍一下 `configure`  脚本支持的常用选项：

| 选项                          | 说明                                                                                                                                                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --prefix=path                 | 定义一个目录，存放服务器上的文件 ，也就是 nginx 的安装目录。默认使用 /usr/local/nginx。                                                                                                                 |
| --sbin-path=path              | 设置 nginx 的可执行文件的路径，默认为 prefix/sbin/nginx.                                                                                                                                                |
| --conf-path=path              | 设置在 nginx.conf 配置文件的路径。nginx 允许使用不同的配置文件启动，通过命令行中的-c 选项。默认为 prefix/conf/nginx.conf.                                                                               |
| --pid-path=path               | 设置 nginx.pid 文件，将存储的主进程的进程号。安装完成后，可以随时改变的文件名 ， 在 nginx.conf 配置文件中使用 PID 指令。默认情况下，文件名 为 prefix/logs/nginx.pid.                                    |
| --error-log-path=path         | 设置主错误，警告，和诊断文件的名称。安装完成后，可以随时改变的文件名 ，在 nginx.conf 配置文件中 使用 的 error_log 指令。默认情况下，文件名 为 prefix/logs/error.log.                                    |
| --http-log-path=path          | 设置主请求的 HTTP 服务器的日志文件的名称。安装完成后，可以随时改变的文件名 ，在 nginx.conf 配置文件中 使用 的 access_log 指令。默认情况下，文件名 为 prefix/logs/access.log.                            |
| --user=name                   | 设置 nginx 工作进程的用户。安装完成后，可以随时更改的名称在 nginx.conf 配置文件中 使用的 user 指令。默认的用户名是 nobody。                                                                             |
| --group=name                  | 设置 nginx 工作进程的用户组。安装完成后，可以随时更改的名称在 nginx.conf 配置文件中 使用的 user 指令。默认的为非特权用户。                                                                              |
| --with-select_module          | 启用或禁用构建一个模块来允许服务器使用 select()方法。该模块将自动建立，如果平台不支持的 kqueue，epoll，rtsig 或/dev/poll。                                                                              |
| --without-select_module       |                                                                                                                                                                                                         |
| --with-poll_module            | 启用或禁用构建一个模块来允许服务器使用 poll()方法。该模块将自动建立，如果平台不支持的 kqueue，epoll，rtsig 或/dev/poll。                                                                                |
| --without-poll_module         |                                                                                                                                                                                                         |
| --without-http_gzip_module    | 不编译压缩的 HTTP 服务器的响应模块。编译并运行此模块需要 zlib 库。                                                                                                                                      |
| --without-http_rewrite_module | 不编译重写模块。编译并运行此模块需要 PCRE 库支持。                                                                                                                                                      |
| --without-http_proxy_module   | 不编译 http_proxy 模块。                                                                                                                                                                                |
| --with-http_ssl_module        | 使用 https 协议模块。默认情况下，该模块没有被构建。建立并运行此模块的 OpenSSL 库是必需的。                                                                                                              |
| --with-pcre=path              | 设置 PCRE 库的源码路径。PCRE 库的源码（版本 4.4 - 8.30）需要从 PCRE 网站下载并解压。其余的工作是 Nginx 的./ configure 和 make 来完成。正则表达式使用在 location 指令和 ngx_http_rewrite_module 模块中。 |
| --with-pcre-jit               | 编译 PCRE 包含“just-in-time compilation”（1.1.12 中， pcre_jit 指令）。                                                                                                                                 |
| --with-zlib=path              | 设置的 zlib 库的源码路径。要下载从 zlib（版本 1.1.3 - 1.2.5）的并解压。其余的工作是 Nginx 的./ configure 和 make 完成。ngx_http_gzip_module 模块需要使用 zlib 。                                        |
| --with-cc-opt=parameters      | 置额外的参数将被添加到 CFLAGS 变量。例如,当你在 FreeBSD 上使用 PCRE 库时需要使用:--with-cc-opt="-I /usr/local/include。.如需要需要增加 select()支持的文件数量:--with-cc-opt="-D FD_SETSIZE=2048".       |
| --with-ld-opt=parameters      | 设置附加的参数，将用于在链接期间。例如，当在 FreeBSD 下使用该系统的 PCRE 库,应指定:--with-ld-opt="-L /usr/local/lib".                                                                                   |

了解了如上选项后，就可以根据实际情况使用 configure 脚本生成 Makefile 文件了。若上面的选项无法满足需求，可自行 Google 其他选项，上面介绍的只是其中的一小部分。

### 2.4 生成 Makefile 文件

使用下面的命令配置并生成`Makefile`文件：

```bash
$ ./configure --prefix=/data/software/nginx-1.18.0 --with-http_ssl_module
checking for OS
 + Linux 3.10.0-957.el7.x86_64 x86_64
checking for C compiler ... found
 + using GNU C compiler
 + gcc version: 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC)
checking for gcc -pipe switch ... found
checking for -Wl,-E switch ... found
checking for gcc builtin atomic operations ... found
checking for C99 variadic macros ... found
checking for gcc variadic macros ... found
checking for gcc builtin 64 bit byteswap ... found
...
... 这里省略n行
...
checking for zlib library ... found
creating objs/Makefile

Configuration summary
  + using system PCRE library
  + using system OpenSSL library
  + using system zlib library

  nginx path prefix: "/data/software/nginx-1.18.0"
  nginx binary file: "/data/software/nginx-1.18.0/sbin/nginx"
  nginx modules path: "/data/software/nginx-1.18.0/modules"
  nginx configuration prefix: "/data/software/nginx-1.18.0/conf"
  nginx configuration file: "/data/software/nginx-1.18.0/conf/nginx.conf"
  nginx pid file: "/data/software/nginx-1.18.0/logs/nginx.pid"
  nginx error log file: "/data/software/nginx-1.18.0/logs/error.log"
  nginx http access log file: "/data/software/nginx-1.18.0/logs/access.log"
  nginx http client request body temporary files: "client_body_temp"
  nginx http proxy temporary files: "proxy_temp"
  nginx http fastcgi temporary files: "fastcgi_temp"
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"
```

- `--prefix` 配置置指定了`Nginx`的安装路径，其他的配置使用默认的配置。

- 默认情况下，Nginx 的 https/ssl 协议模块是没有被构建的。需要增加 **--with-http_ssl_module** 建立并运行该模块的 OpenSSL 库。否则在配置 SSL 时可能会导致 **nginx: \[emerg] unknown directive "ssl"** 报错。

- 在运行过程中，`configure` 脚本调用 `auto` 目录中的各种脚本对系统环境及相关配置和设置进行了检查。

### 2.4 编译安装

得到了 Makefile 文件后，就可以编译源码了。

```bash
$ make && make install
```

到此，我们已经安装后了一个最基本的 Nginx 服务器，其安装路径为 /data/software/nginx-1.18.0。

## 三、启动与测试

### 3.1 启动

使用下面的命令启动 nginx：

```bash
$ ./sbin/nginx
```

### 3.2 测试

使用下面的命令执行测试：

```bash
$ curl localhost
```

![nginx-curl-localhost.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlzwvP17jTxavBAndazgmWoFGYQE.png)

若返回类似如上的结果，证明已成功启动。其实，上面返回的是目录`/Nginx/html/`下的`index.html`文件，可以使用`cat /Nginx/html/index.html`命令进行验证。

若是有图形界面，在浏览器访问 [localhost](https://links.jianshu.com/go?to=localhost) 或者你本机的公网 ip，可以看到类似下图的页面：
![welcome-to-nginx.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fg8DlX9CsT8zQEpdzOBtLnS8lMaM.png)

## 四、常用命令

附上一些 nginx 的常用命令。

```bash
nginx  					# 启动nginx
nginx -s quit  	# 快速停止nginx
nginx -V 				# 查看版本，以及配置文件地址
nginx -v 				# 查看版本
nginx -s reload|reopen|stop|quit   # 重新加载配置|重启|快速停止|安全关闭nginx
nginx -h 				# 帮助
```

## 五、参考资料

1.  sprinkle_liz，《[Centos 7 下编译安装 Nginx](https://www.jianshu.com/p/2c30ab4f5478)》，简书
