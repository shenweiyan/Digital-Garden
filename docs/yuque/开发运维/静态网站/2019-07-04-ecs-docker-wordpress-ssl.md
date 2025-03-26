---
title: 阿里云 ECS+Docker+WordPress 搭建个人博客
urlname: 2019-07-04-ecs-docker-wordpress-ssl
author: 章鱼猫先生
date: 2019-07-04
updated: "2022-06-23 11:29:05"
---

虽然已经入手 leanote，开启了以笔记+博客的方式记录学习生活琐事，但当手上有个续费了三年的 ECS，总想折腾点事情。于是想着在阿里云 ECS 上，使用 docker+wordpress 搭建个人博客，并基于 nginx 实现 ssl 证书的 https 访问。

在阿里云上搭建使用个人博客主要分为以下几个步骤：

1.  购买阿里云 ECS 主机
2.  购买域名
3.  申请备案
4.  环境配置
5.  域名解析
6.  安装 SSL 证书开启 https 访问

---

# 1. 购买 ECS 主机

如果只用来做简单的个人博客，1 核 1G 足够，当然后面也可以根据需求自己扩容。本人用的阿里的主机，平时工作需要搭其他环境，用的 2 核 4G，价钱就不说了，如果经济紧张，或只是搭个玩的，可以入搬瓦工或者腾讯云，具体价格可以去各自的官网查看。

阿里云：<https://ecs-buy.aliyun.com/>
腾讯云：<https://buy.cloud.tencent.com/cvm>
搬瓦工：<https://bandwagonhost.com/vps-hosting.php>
国外服务器详细对比（要翻墙）：<https://shadowsocks.blogspot.jp/>

百度上有详细的购买流程，这不重复造轮子了，实在不明白可以留言。

# 2. 购买域名

这个没什么说的，直接进网站找自己喜欢域名，支付就 OK。

万网：<https://wanwang.aliyun.com/>

# 3. 申请备案

阿里云网站备案：<https://beian.aliyun.com/>

需要提醒大家的是，如果你买了阿里云的服务器，并且想要通过域名访问，那域名是必须要备案的，总结一句：必须先将域名备案，才能通过域名访问阿里云的服务器。

一提到备案，可能你会觉得备案这个事情很麻烦，各种流程啊，手续啊。其实没这么麻烦，因为阿里云已经提供了一条龙服务，通过阿里云的代备案系统，一些都会变得容易很多，不管是个人网站的备案，还是企业网站的备案，都只是时间上的问题，一般备案审核需要二十天左右。

# 4. 环境配置

WordPress 是一个非常著名的 PHP 编写的博客平台，发展到目前为止已经形成了一个庞大的网站平台系统。在 WP 上有规模庞大的插件和主题，可以帮助我们快速建立一个博客甚至网站。

在 Windows 上可以非常方便的安装 WordPress，因为 IIS 上 集成了 WordPress 的一键安装包。而在 Linux 上安装 WordPress 就比较复杂了，我们需要配置 php 环境、Apache 或者 Nginx 服务器、MySQ L 数据库以及各种权限和访问问题。所以在 Linux 上最好的办法就是使用 Docker 来安装 WordPress。

本人购买的 ECS 预装的 CentOS 7.4，通过 XShell 登入。

① 安装 Docker

    yum update
    yum install docker
    systemctl start docker

如果是国内用户的话可能还需要设置 Docker 加速，可以用阿里的 docker 镜像仓库，不然下国外的资源真的会崩溃。参考：<https://cr.console.aliyun.com/?spm=5176.1971733.2.28.394b9fbdrASJma#/accelerator>

② 安装 mysql，wordpress 镜像

    # 拉取 mysql,wordPress镜像
    docker pull mysql:latest
    docker pull wordpress:latest

    # 先实例化 Mysql 镜像
    docker run -itd  --name mysql -p 127.0.0.1:3306:3306 -e MYSQL_ROOT_PASSWORD=new.1234  mysql

    # 接下来后执行下面命令将两都结合
    docker run -itd --name wordpress -p 127.0.0.1:8090:80 --link mysql:mysql -v /home/shenweiyan/wordpress/:/var/www/html/ wordpress

- docker 参数映射前面是主机，后面是容器，比如 mysql:mysql 前面是主机的 docker name 叫 mysql，后面是容器中的 mysql， port 同理。
- `-p 127.0.0.1:8090:80` 会启用 docker 的 ipv4 网络，方便后面 Nginx 做域名和端口映射；如果直接使用 `-p 8090:80`，会默认使用 docker 的 ipv6 网络，ECS 中对于 ipv6 的监听和基于 Nginx 域名绑定比较麻烦，个人在这个坑尝试了很久，目前还没找到好的解决方法。

到这里，docker+wordpress 就安装完成了。这时候尚不能打开网页，因为是配置在 127.0.0.1 上的，只有本机可以访问。

# 5. 域名解析

## 5.1 安装并启动 nginx

    yum install nginx
    systemctl start nginx

## 5.2 配置 nginx.conf

进入服务器 nginx 安装路径，进入 conf 文件夹，编辑 nginx.conf，加入一行 `include sites-available/*.conf`。

    user  nobody;
    worker_processes  1;
    ......
    http {
        include       mime.types;
        default_type  application/octet-stream;
        ......
        server {
            listen       80;
            server_name  localhost;
            ......
        }
        ......
        include sites-available/*.conf;
    }

## 5.3 配置 wordpress.conf

    server {
        listen       80;
        server_name  youdomain.com;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        location / {
            proxy_pass http://127.0.0.1:8090;
        }

        access_log  logs/wordpress_access.log;
        error_log   logs/wordpress_error.log;
    }

## 5.4 添加域名解析

登入阿里域名解析：<https://netcn.console.aliyun.com/core/domain/list，点击相应域名的> "解析" 链接，根据提示添加域名的 A 记录，解析到你的服务器 ip 下。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fm-MQeQpFEqp0LeZEAXEySUs16i_.png)

## 5.5 安装 wordpress

添加完域名解析后，打开浏览器，输入 <http://youdomain.com，然后就可以看到> WordPress 了。按照提示输入用户名等信息，然后安装 WordPress。等到它提示安装完成，那么 WordPress 的安装就算大功告成了。

# 6. 安装 SSL 证书开启 https 访问

## 6.1 单域名免费证书申请

登入阿里域名解析：<https://netcn.console.aliyun.com/core/domain/list，点击相应域名的> "SSL 证书" 链接，设置单域名免费证书。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuBDrUkhJAGUHmJMSmoAv9A30FG3.png)

## 6.2 SSL 证书下载

单域名免费证书提交申请后，一般十分钟就会审批下来。这时候，我们登陆 "[CA 证书服务（数据安全）](https://yundun.console.aliyun.com/?spm=5176.2020520163.aliyun_sidebar.24.4eb62b7auFTPPK&p=cas#/cas/home)"，在 "我的订单" 中找到已经签发的域名证书，点击 "下载" 链接，通过 "下载证书 for Nginx" 下载证书。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkqqJGGi5jsGXc4BDQ9LN0NcOoth.png)

## 6.3 SSL 证书安装

( 1 ) 在 Nginx 的安装目录下创建 cert 目录，并且将下载的全部文件拷贝到 cert 目录中。
( 2 ) 将 wordpress.conf 修改为：

    server {
        listen 80;
        listen 443;
        server_name site.shenweiyan.cn;
        ssl on;
        root /home/shenweiyan/wordpress;
        index index.html index.htm index.php default.html default.htm default.php;
        ssl_certificate   cert/1524404277557.pem;
        ssl_certificate_key  cert/1524404277557.key;
        ssl_session_timeout 5m;
        ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers on;

        location / {
            proxy_pass http://127.0.0.1:8090;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        access_log  logs/wordpress_access.log;
        error_log   logs/wordpress_error.log;
    }

( 3 )重启 nginx 服务

    systemctl restart nginx

进行到这一步，你已经弄好了 ssl 证书，在服务器导入并且绑定好了 443 端口，也已开启 https 跳转了，正常情况下你可以使用 <https://site.shenwieyan.cn> 访问你的 wordpress。

但是，你会遇到如下的情况：

1.  wordpress 样式错乱，图片打不开；
2.  wordpress/wp-admin 后台进不去，登录无反应；
3.  百度找了很多解决方法，却依然没有解决，甚至搞的连网站都打不开了；
4.  等等。。。

请按照 6.4 方法修改，本人亲测，wordpress4.9.1-4.9.2 完美解决。

## 6.4 全站开启 https

**1、系统文件修改**

    路径：网站根目录（/home/shenweiyan/wordpress）/wp-includes/functions.php
    找到代码：require( ABSPATH . WPINC . '/option.php' );
    在下方添加：
    add_filter('script_loader_src', 'agnostic_script_loader_src', 20,2); function agnostic_script_loader_src($src, $handle) { return preg_replace('/^(http|https):/', '', $src); } add_filter('style_loader_src', 'agnostic_style_loader_src', 20,2); function agnostic_style_loader_src($src, $handle) { return preg_replace('/^(http|https):/', '', $src); }

**2、后台文件修改**

    路径：网站根目录（/home/shenweiyan/wordpress）/wp-config.php
    找到代码：

    *
    * @package WordPress
    */

    在下方添加如下代码：
    _SERVER['HTTPS'] = 'on';
    define('FORCE_SSL_LOGIN', true);
    define('FORCE_SSL_ADMIN', true);

**3、安装插件**
完成以上两步操作后，可以正常访问 https 开头的网站和后台，下载这个叫 "really-simple-ssl" 的 wordpress 插件：

    https://wordpress.org/plugins/really-simple-ssl/

登录后台安装此插件。

或者登陆 wordpress 后台，在"设置"→ "常规" 中设置 "WordPress 地址（URL）" 和 "站点地址（URL）"为 https 链接地址。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlaMAwW6wsKGgbgxOVbDyv8MafLl.png)

至此，真正意义上解决 wordpress 全站开启 https 的 ssl 证书问题。

# 7. 填坑总结

## 7.1. 更换域名无法登陆后台

在后台—设置—常规—WordPress 地址或者网站域名处设置了别的域名，结果导致后台无法登录了，这是一种情况；还有一种情况就是网站搬家了，或者是换域名了，也会出现这类问题，那么就需要重新配置下当前域名才能使得网站正常运行。

方法：修改 wp-config.php 文件

第一步：在网站根目录找到 wp-config.php 文件，在其中添加以下两行内容：

    define('WP_HOME, 'http://要修改的域名');
    define('WP_SITEURL', 'http://要修改的域名');

第二步：登录后台—设置—常规—重新输入新博客地址（WordPressAddress(URL)）和安装地址（SiteAddress(URL)），修改完毕后删除上面在 wp-config.php 文件中添加的内容（如何一切正常，不删除也可以，具体情况，具体操作）。

---

使用过程中我们可以通过 wordpress 大学，或其他平台找一些喜欢的主题，不过很多好看的主题是收费的。

有其他问题可以留言，谢谢！
