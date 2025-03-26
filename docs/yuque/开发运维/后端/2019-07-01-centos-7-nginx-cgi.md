---
title: CentOS Linux 7 配置 nginx 支持 CGI
urlname: 2019-07-01-centos-7-nginx-cgi
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 10:52:36"
---

Nginx 本身不能执行外部程序，Nginx 处理 PHP 是通过 PHP 的 fastcgi 管理器（php-fpm）进行处理，然后 nginx 再将结果返回给用户；所以如果我们需要通过 cgi 程序（shell、perl、c/c++ 等）来编写网站后台的话，就需要使用 fcgiwrap 这个通用的 fastcgi 进程管理器来帮助 nginx 处理 cgi。

- 对于 PHP：只建议使用 PHP-FPM，因为这是官方的解决方案，性能和稳定性肯定是最好的。
- 对于其它 CGI 程序：如 Shell、Perl、C/C++、Python，推荐使用 fcgiwrap，这是一个通用的 FCGI 管理器。

写这篇博客的主要目的也是为了让 Nginx 执行 Shell、Perl、C/C++、Python 程序，因为作为一个生信出身的伪 IT 工作者，Shell、Perl、Python 永远都是我们最熟悉的，用这些语言来编写网站后台可以更加节省我们的时间，效率更高。

# 一、概念

## 1. CGI 与 FastCGI

CGI 全称是"公共网关接口"(Common Gateway Interface)，HTTP 服务器与你的或其它机器上的程序进行 "交谈" 的一种工具，其程序须运行在网络服务器上。它和 FastCGI（快速通用网关接口）都是语言无关的协议。CGI 诞生已经非常久远了，由于它每次在处理一个请求（连接）时都要重新启动脚本（可执行文件），重新传递所有的环境变量（其中非常多是完全一样的），导致性能非常低下。虽然性能较低，但功不可没，后来出现了性能更高的  [FastCGI](https://en.wikipedia.org/wiki/FastCGI)。

FastCGI（简称 FCGI）是 CGI 的增强版本，FCGI 可以简单的理解为 CGI + 多进程模型。FCGI 的工作模式有点类似于 Nginx，一个 Master 进程和多个 Worker 进程。Master 进程主要用来监控 Worker 进程的运行情况，当某个 Worker 进程意外退出时，Master 进程会随即启动一个新的 Worker 进程；Worker 进程则是真正干活的进程，用来执行 CGI 程序（传递环境变量、标准输入），获取 CGI 程序的标准输出，再将其返回为 Web 服务器（如 Apache、Nginx）。Worker 进程处理完请求后不会结束运行，而是继续等待下一个请求的到来，直到我们手动关闭它们。

## 2. Spawn-FCGI 与  FcgiWrap

Spawn-FCGI 是一个通用的 FastCGI 管理服务器，它是 lighttpd 中的一部份，很多人都用 Lighttpd 的 Spawn-FCGI 进行 FastCGI 模式下的管理工作。之前一直以为 Nginx 执行 CGI 程序需要 spawn-fcgi 和 fcgiwrap 两个东西（网上很多文档都是抄来抄去，搞得我也一头雾水，只好照做），但是实际上只需要 fcgiwrap，spawn-fcgi 的作用仅仅是启动和配置 fcgiwrap，这个工作完全可以由 fcgiwrap 自己来完成，所以 spawn-fcgi 不安装也不会影响 fcgiwrap 的使用。

Spawn-FCGI 目前已经独成为一个项目，更加稳定一些，也给很多 Web 站点的配置带来便利。已经有不少站点将它与 nginx 搭配来解决动态网页。目前 Spawn-FCGI 的下载地址是：<http://redmine.lighttpd.net/projects/spawn-fcgi>，最新版本是：<http://download.lighttpd.net/spawn-fcgi/releases-1.6.x/spawn-fcgi-1.6.4.tar.gz>。

[FcgiWrap](https://github.com/gnosek/fcgiwrap)：Simple FastCGI wrapper for CGI scripts。首先这个东西的作用。它为那些不支持直接运行 CGI 脚本的 Web 服务器提供一种运行 CGI 脚本的方式。[NGINX](http://nginx.org/)  就是一个只支持 FastCGI，不支持 CGI 的 HTTP（Web）服务器之一。也是我用得最多最熟悉的 Web 服务器。虽然 Apache 支持直接跑 CGI，但从来没用过它的我对它并不感冒，这里也就不再讨论了。

# 二、安装与配置

## 2.1  安装 fcgiwrap

安装依赖：

```shell
yum -y install autoconf automake libtool fcgi fcgi-devel spawn-fcgi
```

安装 fcgiwrap：

```shell
$ git clone https://github.com/gnosek/fcgiwrap
$ cd fcgiwrap
$ autoreconf -i
$ ./configure     # fcgiwrap 默认安装到 /usr/local/sbin/fcgiwrap
$ make
$ make install
```

## 2.2 配置 spawn-fcgi

通过 `yum install spawn-fcgi`  方式安装的 spawn-fcgi 配置文件默认为：/etc/sysconfig/spawn-fcgi，编辑该文件：

```bash
vi /etc/sysconfig/spawn-fcgi

# You must set some working options before the "spawn-fcgi" service will work.
# If SOCKET points to a file, then this file is cleaned up by the init script.
#
# See spawn-fcgi(1) for all possible options.
#
# Example :
#SOCKET=/var/run/php-fcgi.sock
#OPTIONS="-u apache -g apache -s $SOCKET -S -M 0600 -C 32 -F 1 -P /var/run/spawn-fcgi.pid -- /usr/bin/php-cgi"
FCGI_SOCKET=/var/run/fcgiwrap.sock
FCGI_PROGRAM=/usr/local/sbin/fcgiwrap
FCGI_USER=nginx
FCGI_GROUP=nginx
FCGI_EXTRA_OPTIONS="-M 0777"
OPTIONS="-u $FCGI_USER -g $FCGI_GROUP -s $FCGI_SOCKET -S $FCGI_EXTRA_OPTIONS -F 1 -P /var/run/spawn-fcgi.pid -- $FCGI_PROGRAM"
```

## 2.3 启动 spawn-fcgi 服务

```bash
[root@ecs-steven conf]# systemctl enable spawn-fcgi	 # 添加开机启动（或者：chkconfig spawn-fcgi on）
spawn-fcgi.service is not a native service, redirecting to /sbin/chkconfig.
Executing /sbin/chkconfig spawn-fcgi on

$ systemctl start spawn-fcgi    # 启动 spawn-fcgi 服务（或者：service spawn-fcgi start）
```

spawn-fcgi 启动出现下面报错：

```shell
[root@ecs-steven ~]# service spawn-fcgi start
Starting spawn-fcgi (via systemctl):  Job for spawn-fcgi.service failed because the control process exited with error code. See "systemctl status spawn-fcgi.service" and "journalctl -xe" for details.
                                                           [FAILED]

[root@ecs-steven ~]# systemctl status spawn-fcgi.service
● spawn-fcgi.service - LSB: Start and stop FastCGI processes
   Loaded: loaded (/etc/rc.d/init.d/spawn-fcgi; bad; vendor preset: disabled)
   Active: failed (Result: exit-code) since Fri 2019-04-26 08:31:51 CST; 9min ago
     Docs: man:systemd-sysv-generator(8)
  Process: 7069 ExecStart=/etc/rc.d/init.d/spawn-fcgi start (code=exited, status=1/FAILURE)

Apr 26 08:31:51 ecs-steven systemd[1]: Starting LSB: Start and stop FastCGI processes...
Apr 26 08:31:51 ecs-steven spawn-fcgi[7069]: Starting spawn-fcgi: spawn-fcgi: can't find user name nginx
Apr 26 08:31:51 ecs-steven spawn-fcgi[7069]: [FAILED]
Apr 26 08:31:51 ecs-steven systemd[1]: spawn-fcgi.service: control process exited, code=exited status=1
Apr 26 08:31:51 ecs-steven systemd[1]: Failed to start LSB: Start and stop FastCGI processes.
Apr 26 08:31:51 ecs-steven systemd[1]: Unit spawn-fcgi.service entered failed state.
Apr 26 08:31:51 ecs-steven systemd[1]: spawn-fcgi.service failed.
```

这种情况我们需要创建 nginx 用户，然后启动  spawn-fcgi.service：

```shell
[root@ecs-steven conf]# /usr/sbin/useradd nginx -s /bin/false

[root@ecs-steven conf]# service spawn-fcgi start
Starting spawn-fcgi (via systemctl):                       [  OK  ]
```

## 2.4 配置 Nginx

```bash
[root@ecs-steven conf]# vim nginx.conf

user  nginx nginx;
worker_processes  1;

error_log  	logs/error.log;
pid 				logs/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  logs/access.log  main;

    sendfile        			on;
    #tcp_nopush     			on;
    client_max_body_size  50m;

    keepalive_timeout  65;
    gzip  on;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }

    include sites-available/*.conf;
}
```

在 Nginx 目录下添加  sites-available/fcgi.conf：

```bash
[root@ecs-steven conf]# cat sites-available/fcgi.conf
server {
    listen 80;

    access_log  logs/fcgi_access.log;
    error_log   logs/fcgi_error.log debug;

    # 开启 SSL 配置
    #listen  443;
    #ssl on;
    #server_name tools.shenweiyan.com;
    #ssl_certificate   ../cert/tools/tools.shenweiyan.com.pem;
    #ssl_certificate_key  ../cert/tools/tools.shenweiyan.com.key;
    #ssl_session_timeout 5m;
    #ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    #ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    #ssl_prefer_server_ciphers on;

    root /apps/tools;

    location / {
        index  index.html index.htm;
    }

   location ~ .*\.(pl|py|cgi)?$ {
        include        /usr/local/software/nginx/conf/fastcgi_params;
        fastcgi_pass   unix:/var/run/fcgiwrap.sock;
        fastcgi_index  index.cgi;
        fastcgi_param  SCRIPT_FILENAME /apps/tools/$fastcgi_script_name;
    }
}
```

最后，重启 Nginx：

```bash
$ service nginx reload

或者：
$ systemctl restart nginx
```

# 三、添加 CGI 程序

编写 CGI 测试程序：

```bash
$ vim /apps/tools/test.cgi

#!/usr/bin/perl -w
print "Content-type: text/html\n\n";
print "<html><head><title>Hello World!</title></head>\n";
print "<body><h1>Hello world, CGI work!</h1>
</body></html>\n";
```

设定权限：

```bash
$chmod 0755 /apps/tools/test.cgi
$ chown nginx.nginx /apps/tools/test.cgi
```

最后，利用 firefox/chrome 测试！<http://192.168.xxx.xxx/test.cgi> 访问出现 "**Hello world, CGI work!**" 即说明配置部署成功。

# 四、参考资料

- Linux 无限，《[在 CentOS7/RHEL7 上，為 Nginx 加上 Perl CGI 模組](http://linux.onlinedoc.tw/2017/01/centos7rhel7-nginx-perl-cgi.html)》，博客
- 陪她去流浪，《[fcgiwrap 的简单使用](https://blog.twofei.com/642/)》，博客
- Otokaze，《[nginx fastcgi 配置](https://www.zfl9.com/nginx-fcgi.html)》，Otokaze's blog
- 《[Perl + nginx 403 errors again](https://stackoverflow.com/questions/31746462/perl-nginx-403-errors-again)》，Stack Overflow
- 《[Nginx - Use Perl Script](https://www.server-world.info/en/note?os=CentOS_6&p=nginx&f=6)\*\*》，\*\*Server World
- shouhou2581314，《[nginx 调用 cgi 脚本](https://blog.51cto.com/thedream/1718527)》，51CTO 博客
