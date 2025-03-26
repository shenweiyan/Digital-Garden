---
title: 使用阿里云 ECS 搭建自己的 Leanote 云笔记服务
urlname: 2019-07-04-leanote-for-ecs-tutorial
author: 章鱼猫先生
date: 2019-07-04
updated: "2021-06-30 09:35:06"
---

Leanote（中文名 "蚂蚁笔记"），横跨 Windows、MacOS、Android、iOS、Linux 多平台，支持富文本和 Markdown 文本格式，自由度非常之高，你可以让笔记内容玩出新花样来。除了主打的笔记同步、编辑功能外，还支持开设博客，展示你公开的笔记内容。总体来说 Leanote 使用起来挺顺手，最重要一点，**这个笔记是开源的**。

下面将基于阿里云 ECS 服务端搭建 Leanote 云笔记服务器的步骤分享出来，给需要使用私人云笔记的筒子们。详细安装请参考官方文档：《[Leanote 源码版详细安装教程 Mac and Linux](https://github.com/leanote/leanote/wiki/Leanote-%E6%BA%90%E7%A0%81%E7%89%88%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B----Mac-and-Linux)》。

## 1. Golang 安装

```bash
$ cd /usr/local/src
$ wget https://studygolang.com/dl/golang/go1.10.1.linux-amd64.tar.gz
$ tar zvxf go1.10.1.linux-amd64.tar.gz -C /usr/local/software/
$ mv /usr/local/software/go /usr/local/software/go-1.10.1
$ su steven
$ mkdir -p /data/LeaNote/bin
$ ln -s /usr/local/software/go-1.10.1/bin/* /data/LeaNote/bin
```

## 2. 获取 Revel 和 Leanote 的源码

## 2.1 方法 1 （推荐方法）:

请下载 [leante-all-master.zip](https://github.com/leanote/leanote-all/archive/master.zip)。解压后，将 src 文件夹复制到 /data/LeaNote/gopackage/。

使用如下命令生成 revel 二进制命令, 稍后运行 Leanote 需要用到：

```bash
$ go install github.com/revel/cmd/revel
```

### 2.2 方法 2

该方法使用 Golang 的 go get 来下载包, 这个命令会调用 git, 所以必须先安装 git。

```bash
# ubuntu 下安装 git
$ sudo apt-get install git-core openssh-server openssh-client

# centos 下安装git
$ sudo yum install git
```

获取 Revel 和 Leanote:

打开终端, 以下命令会下载 Revel 和 Leanote 及依赖包, 时间可能会有点久, 请耐心等待。

```bash
$> go get github.com/revel/cmd/revel
$> go get github.com/leanote/leanote/app
```

下载完成后，Leanote 的源码在 /data/LeaNote/gopackage/src/github.com/leanote/leanote 下。

## 3. 安装 Mongodb

## 3.1 安装 Mongodb

到 [Mongodb 官网](http://www.mongodb.org/downloads) 下载相应系统的最新版安装包，或者从以下链接下载旧版本：

- 64 位 linux Mongodb 3.0.1 下载链接(推荐): <https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.0.1.tgz>
- 64 位 linux Mongodb 3.6.4 下载链接：<https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.4.tgz>

```bash
$ cd /usr/local/src
$ wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.6.4.tgz
$ tar -xzvf mongodb-linux-x86_64-3.6.4.tgz
$ cd mongodb-linux-x86_64-3.6.4
$ su root
$ cp /usr/local/src/mongodb-linux-x86_64-3.6.4 /usr/local/software
$ mv /usr/local/software/mongodb-linux-x86_64-3.6.4 /usr/local/software/mongodb-linux-3.6.4
$ su steven
$ vi ~/.bashrc
export PATH="/usr/local/software/mongodb-3.6.4/bin:$PATH"
```

### 3.2 测试 Mongodb 安装

```bash
# 先在 /data/LeaNote 下新建一个目录 mongodata 存放 Mongodb 数据:
$ mkdir -p /data/LeaNote/mongodb/data

# 用以下命令启动 mongod:
$ mongod --dbpath /data/LeaNote/mongodb/data

# 这时 mongod 已经启动，重新打开一个终端, 键入 mongo 进入交互程序：
$> mongo
> show dbs
admin  0.000GB
local  0.000GB
```

Mongodb 安装到此为止, 下面为 Mongodb 导入 Leanote 初始数据。

## 4. 导入初始数据

leanote 初始数据在 /data/LeaNote/gopackage/src/github.com/leanote/leanote/mongodb_backup/leanote_install_data 中。

打开终端， 输入以下命令导入数据：

```bash
$ mongorestore -h localhost -d leanote --dir /data/LeaNote/gopackage/src/github.com/leanote/leanote/mongodb_backup/leanote_install_data
```

现在在 mongodb 中已经新建了 leanote 数据库, 可用命令查看下 Leanote 有多少张"表"：

```bash
$ mongo
> show dbs     #　查看数据库
admin    0.000GB
config   0.000GB
leanote  0.001GB
local    0.000GB
> use leanote     # 切换到 leanote
switched to db leanote
> show collections     # 查看表
albums
attachs
blog_comments
....
files
has_share_notes
note_content_histories
note_contents
....
```

初始数据的 users 表中已有 2 个用户:

    user1 username: admin, password: abc123 (管理员, 只有该用户才有权管理后台, 请及时修改密码)
    user2 username: demo@leanote.com, password: demo@leanote.com (仅供体验使用)

## 5. 配置 Leanote

Leanote 的配置存储在文件 /data/LeaNote/gopackage/src/github.com/leanote/leanote/conf/app.conf 中。

请务必修改 app.secret 一项, 在若干个随机位置处，将字符修改成一个其他的值, 否则会有安全隐患!

其它的配置可暂时保持不变, 若需要配置数据库信息, 请参照 [Leanote 问题汇总](https://github.com/leanote/leanote/wiki/QA)。

## 6. 运行 Leanote

注意: 在此之前请确保 Mongodb 已在运行！

新开一个窗口, 运行：

```bash
$ revel run github.com/leanote/leanote

# leanote 切入后台运行
$ nohup revel run github.com/leanote/leanote 2>&1 &
```

恭喜你, 打开浏览器输入: <http://localhost:9000> 体验 Leanote 吧！

## 7. Leanote 其他配置

按照本教程启动 Mongodb 是没有权限控制的, 如果你的 Leanote 服务器暴露在外网, 任何人都可以访问你的 Mongodb 并修改, 所以这是极其危险的!!!!!!!!!!! 请务必为 Mongodb 添加用户名和密码并以 auth 启动，方法如下。

### 7.1 为 mongodb 数据库添加用户

像 mysql 一样有 root 用户, mongodb 初始是没有用户的，这样很不安全，所以要为 leanote 数据库新建一个用户来连接 leanote 数据库(注意，并不是为 leanote 的表 users 里新建用户, 而是新建一个连接 leanote 数据库的用户，类似 mysql 的 root 用户).

mognodb v2 与 v3 创建用户命令有所不同。

- mongodb v2 创建用户如下：

```bash
# 首先切换到leanote数据库下
> use leanote;
# 添加一个用户root, 密码是abc123
> db.addUser("root", "abc123");
{
	"_id" : ObjectId("53688d1950cc1813efb9564c"),
	"user" : "root",
	"readOnly" : false,
	"pwd" : "e014bfea4a9c3c27ab34e50bd1ef0955"
}
# 测试下是否正确
> db.auth("root", "abc123");
1 # 返回1表示正确
```

- mongodb v3 创建用户如下：

```bash
# 首先切换到leanote数据库下
> use leanote;
# 添加一个用户root, 密码是abc123
> db.createUser({
    user: 'root',
    pwd: 'abc123',
    roles: [{role: 'dbOwner', db: 'leanote'}]
});
# 测试下是否正确
> db.auth("root", "abc123");
1 # 返回1表示正确
```

用户添加好后重新运行下 mongodb，并开启权限验证. 在 mongod 的终端按 ctrl+c 即可退出 mongodb。

启动 mongodb：

```bash
$ mongod --dbpath /data/LeaNote/mongodb/data --auth
```

还要修改配置文件 : （修改 leanote/conf/app.conf）

    db.host=localhost
    db.port=27017
    db.dbname=leanote # required
    db.username=root # if not exists, please leave blank
    db.password=abc123 # if not exists, please leave blank

### 7.2 Mongodb 设置后台运行

Mongodb 安装完成后，我们通常通过 `mongod --dbpath /usr/local/mongo/data` 让 mongodb 启动，但是我们关闭 shell，mongodb 就停止运行了。**如果想在后台运行，启动时只需添加 --fork 函数即可。可以在日志路径后面添加 --logappend，防止日志被删除。**

```bash
$ mongod --fork --dbpath=/data/LeaNote/mongodb/data --logpath=/data/LeaNote/mongodb/logs/mongodb.log --logappend
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoimxB-mRKTlFQHliLg3z3reWVyL.png)

### 7.3 Mongodb 设置开机启动

当我们把服务器关闭，重启之后，发现 mongodb 又停止了，有没有开机就启动的方法呢？我们把上面代码放到 /etc/rc.local，中，就可以了。

具体操作步骤：

```bash
# 在 /etc/rc.local 添加以下代码
/usr/local/software/mongodb-3.6.4/bin/mongod --fork --dbpath=/data/LeaNote/mongodb/data --logpath=/data/LeaNote/mongodb/logs/mongodb.log --logappend
```

下次重启就可以直接运行 mongodb 了！

### 7.4 为 Leanote 配置 https

**1. 生成 SSL 证书**

可以在网上买一个, 或者自己做一个。这里有一个 shell 脚本可以自动生成证书: (cert.sh)

```bash
#!/bin/sh

# create self-signed server certificate:

read -p "Enter your domain [www.example.com]: " DOMAIN

echo "Create server key..."

openssl genrsa -des3 -out $DOMAIN.key 1024

echo "Create server certificate signing request..."

SUBJECT="/C=US/ST=Mars/L=iTranswarp/O=iTranswarp/OU=iTranswarp/CN=$DOMAIN"

openssl req -new -subj $SUBJECT -key $DOMAIN.key -out $DOMAIN.csr

echo "Remove password..."

mv $DOMAIN.key $DOMAIN.origin.key
openssl rsa -in $DOMAIN.origin.key -out $DOMAIN.key

echo "Sign SSL certificate..."

openssl x509 -req -days 3650 -in $DOMAIN.csr -signkey $DOMAIN.key -out $DOMAIN.crt
```

假设得到了两个文件: **a.com.crt**, **a.com.key**。

**2. 配置 Nginx**

假设 Leanote 运行的端口是 9000, 域名为 a.com, 那么 nginx.conf 可以配置如下：

```nginx
upstream leanote_app {
    server localhost:9000;
}

server {
    listen  80;
    listen  443;
    server_name  note.shenweiyan.cn;
    ssl on;
    client_max_body_size 30M;
    index index.html index.htm index.php default.html default.htm default.php;
    ssl_certificate   ../cert/leanote/note.shenweiyan.cn.crt;
    ssl_certificate_key  ../cert/leanote/note.shenweiyan.cn.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    #rewrite ^/(.*) https://note.shenweiyan.cn/$1 permanent;

    location / {
        proxy_pass         http://leanote_app;
        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
    }

    access_log  logs/leanote_access.log;
    error_log   logs/leanote_error.log;
}
```

最后，执行 `nginx -s reload` 重启 nginx 服务，打开 [https://note.shenweiyan.cn](http://blog.leanote.com/shenweiyan) 即可看到 leanote 的 index 主页。

### 7.5 Leanote 配置开机启动

虽然通过命令让 Leanote 进程进入后台运行了，但是一旦重启还是要手动开启，略麻烦，这时可以自己新建 \_.sh 脚本文件，将命令写入脚本文件里，然后在 rc.local 配置文件中运行 \_.sh 脚本文件就能实现开机启动 Leanote 服务端。

可以参考我的 \*.sh 写法：

```bash
#!/bin/bash
mongod --fork --dbpath=/data/LeaNote/mongodb/data --logpath=/data/LeaNote/mongodb/logs/mongodb.log --logappend
nohup revel run github.com/leanote/leanote 2>&1 &
sstr=$(echo -e $str)
echo "$sstr"
```

若脚本文件命名为 run.sh，且存放在 /root/gopackage 目录里，可以编辑 rc.local 配置文件 /etc/rc.local，加入下面的命令然后保存即可：

```bash
source /etc/profile
/root/gopackage/run.sh
```

## 参考资料：

- <https://blog.csdn.net/adrianandroid/article/details/56277347>
- [https://github.com/leanote/leanote/wiki/Leanote-源码版详细安装教程----Mac-and-Linux](https://github.com/leanote/leanote/wiki/Leanote-%E6%BA%90%E7%A0%81%E7%89%88%E8%AF%A6%E7%BB%86%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B----Mac-and-Linux)
- [https://github.com/leanote/leanote/wiki/QA#如何绑定域名](https://github.com/leanote/leanote/wiki/QA#%E5%A6%82%E4%BD%95%E7%BB%91%E5%AE%9A%E5%9F%9F%E5%90%8D)
