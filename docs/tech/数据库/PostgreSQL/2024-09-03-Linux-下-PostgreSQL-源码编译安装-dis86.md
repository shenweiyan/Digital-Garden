---
title: Linux 下 PostgreSQL 源码编译安装
number: 86
slug: discussions-86/
url: https://github.com/shenweiyan/Digital-Garden/discussions/86
date: 2024-09-03
authors: [shenweiyan]
categories: 
  - 1.4-数据库
labels: ['1.4.1-PostgreSQL']
---

PostgreSQL 是一个功能强大的开源对象关系数据库管理系统(ORDBMS)，它从伯克利写的 POSTGRES 软件包发展而来（1995 年几个 UCB 的学生为 Post-Ingres 开发了 SQL 的接口，正式发布了 PostgreSQL95，随后一步步在开源社区中成长起来），经过十几年的发展， PostgreSQL 已经成为世界上发展最快最受欢迎的数据库系统之一。

本文章主要介绍在 CentOS 下源码编码安装 PostgreSQL-10.0 的一些简单步骤，以供参考。

<!-- more -->

## 1. 新增用户组及用户

PostgreSQL 默认是通过 `postgres:postgres` 来启动和使用的，因此在安装 PostgreSQL 前需要先创建 `postgres` 用户组及 `postgres` 用户。

```bash
# 在root权限下进行
groupadd postgres                    # 添加postgres用户组
useradd postgres -g postgres         # 添加postgres用户
passwd postgres                      # 设置postgres用户密码
```

## 2. 安装

```
$ wget https://ftp.postgresql.org/pub/source/v10.0/postgresql-10.0.tar.gz
$ tar zvxf postgresql-10.0.tar.gz
$ cd postgresql-10.0
$ ./configure --prefix=/data/softwares/pgsql
$ make
$ make install
```

解决依赖：

```
FAQ1：configure: error: readline library not found
$ yum install readline-devel

FAQ2：configure: error: zlib library not found
$ yum install zlib-devel
```

## 3. 启动

```
＃ 新建数据库数据文件目录
$ mkdir /data/softwares/pgsql/data
 
# 新建数据库 log 文件目录
$ mkdir /data/softwares/pgsql/log
 
# 修改目录拥有者
$ chown postgres:postgres /data/softwares/pgsql/data -R
$ chown postgres:postgres /data/softwares/pgsql/log -R
 
# 执行数据库初始化脚本
$ su postgres
$ /data/softwares/pgsql/bin/initdb --encoding=utf8 -D /data/softwares/pgsql/data
 
# 启动 PostgreSQL 服务
$ /data/softwares/pgsql/bin/pg_ctl -D /data/softwares/pgsql/data -l /data/softwares/pgsql/log/postgresql.log start    #postgres 用户下执行
 
# 登录 PostgreSQL 数据库
$ psql
```

![psql-db-list](https://kg.weiyan.cc/2024/09/psql-db-list.webp)

## 4. 重启

```
$ su postgres
$ /data/softwares/pgsql/bin/pg_ctl -D /data/softwares/pgsql/data -l /data/softwares/pgsql/log/postgresql.log restart
```

## 5. 设置开机启动

解压后的 postgresql-x.x.x 下提供了基于 freebsd、linux、osx 3 个系统的 `postgresql` 启动命令。

**1）对于通过源码自定义安装的 pgsql，需要修改相关启动脚本：**

```bash
$ cd postgresql-10.0/postgresql-10.0/contrib/start-scripts
$ vi linux
......
......
# Installation prefix
prefix=/data/softwares/pgsql
  
# Data directory
PGDATA="/data/softwares/pgsql/data"
  
# Who to run the postmaster as, usually "postgres".  (NOT "root")
PGUSER=postgres
  
# Where to keep a log file
PGLOG="$PGDATA/serverlog"
......
......
```

**2）设置数据库开机启动：**

```bash
$ cp /data/softwares/source/postgresql-10.0/postgresql-10.0/contrib/start-scripts/linux /etc/init.d/postgresql

# 添加执行权限
$ chmod a+x /etc/init.d/postgresql

# 添加至开机启动
$ chkconfig --add postgresql
$ chkconfig postgresql on
```

**3）查看 postgresql 状态**

```bash
$ service postgresql status
pg_ctl: server is running (PID: 32586)
/data/softwares/pgsql/bin/postgres "-D" "/data/softwares/pgsql/data"
```

## 6. 禁止管理员空密码登录

在 PostgreSQL 中，如果你想禁止管理员（通常是 `postgres` 用户）使用空密码登录（正常情况下 `postgres` 用户可以直接使用 `psql` 命令直接登录 PostgreSQL），你可以通过修改 `pg_hba.conf` 文件来实现。

1. 找到你的 `pg_hba.conf` 文件。这个文件通常位于 PostgreSQL 的数据目录中，例如 `/var/lib/pgsql/data` 或 `/etc/postgresql/<version>/main`。

2. 修改 `pg_hba.conf` 文件，将管理员的登录方式从 `trust` 更改为 `md5` 或 `password`。这意味着所有连接，包括 `postgres` 用户的，都需要提供密码。

例如，将以下行：
```
local   all             postgres                                trust
```

修改为：
```
local   all             postgres                                md5
```

3. 重新加载或重启 PostgreSQL 服务以应用更改。

重新加载配置的命令通常是：
```bash
pg_ctl reload
```

或者重启服务：
```bash
systemctl restart postgresql
```

或者在不同的系统中可能是：
```bash
service postgresql restart
```

完成这些步骤后，`postgres` 用户将不能再使用空密码登录数据库。其他用户如果想登录数据库，也需要提供密码。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="86"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
