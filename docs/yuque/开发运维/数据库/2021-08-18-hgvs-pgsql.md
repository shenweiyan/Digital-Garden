---
title: Python 包安装和 postgresql 的一些问题
urlname: 2021-08-18-hgvs-pgsql
author: 章鱼猫先生
date: 2021-08-18
updated: "2022-09-29 08:24:46"
---

今天安装 [hgvs](https://github.com/biocommons/hgvs) 这个 python 包的时候，遇到几个比较有代表性的问题，记录分享一下。

> hgvs is a Python package to parse, format, validate, normalize, and map biological sequence variants according to recommendations of the Human Genome Variation Society.

## 怎么查看 python 未安装包的依赖

我们知道的 **pip show hgvs** 和 **pipdeptree -p hgvs** 都只能看到**已安装** Python 包的依赖，但是**未安装**的 Python 包依赖目前通过 pip 应该是暂时没法看的。[stackoverflow](https://stackoverflow.com/questions/41816693/how-to-list-dependencies-for-a-python-library-without-installing) 上看到一个折中的方法，比较繁琐。

```python
In [1]: import requests

In [2]: url = 'https://pypi.org/pypi/{}/json'

In [3]: json = requests.get(url.format('hgvs')).json()

In [4]: json['info']['requires_dist']
Out[4]:
['attrs (>=17.4.0)',
 'biocommons.seqrepo (<1.0)',
 'bioutils (<1.0,>=0.4.0)',
 'configparser (>=3.3.0)',
 'ipython',
 'parsley',
 'psycopg2-binary',
 'six']

In [5]: json['info']['requires_python']
Out[5]: ''
```

除此之外，可以通过 conda 的方式查看（**conda search hgvs --info**）。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Flw6SnwGbNRSvoRHx_41pZSFo1Pe.png)

## Psycopg requires libpq >= 9.1

hgvs 的安装依赖于 psycopg2-binary，而 psycopg2-binary 又依赖于 psycopg2。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnNQMS7enSQOEFDZswwvcNDGCFZ0.png)

```python
$ pip install psycopg2
Collecting psycopg2
  Downloading psycopg2-2.9.1.tar.gz (379 kB)
     |████████████████████████████████| 379 kB 133 kB/s
Using legacy 'setup.py install' for psycopg2, since package 'wheel' is not installed.
Installing collected packages: psycopg2
    Running setup.py install for psycopg2 ... error
    ERROR: Command errored out with exit status 1:
    ......
    In file included from psycopg/psycopgmodule.c:28:0:
    ./psycopg/psycopg.h:31:2: error: #error "Psycopg requires PostgreSQL client library (libpq) >= 9.1"
     #error "Psycopg requires PostgreSQL client library (libpq) >= 9.1"
     ......
```

CentOS 6 默认的 PostgreSQL 最高版本为 8.4.18，需要安装 9.1 以上版本的 postgresql 才可以解决以上出现的 "**Psycopg requires PostgreSQL client library (libpq) >= 9.1**" 问题。

## CentOS/Red Hat 安装 PostgreSQL

使用 **yum list postgresql**\* 命令可以看到：

- CentOS 6 默认的 PostgreSQL 最高版本为 8.4.18；
- CentOS 7 默认的 PostgreSQL 最高版本为 9.2.24。

如果需要在 CentOS/Red Hat Enterprise Linux 中安装 PostgreSQL 9/10 以上版本，需要：

### 1. 配置 yum 源

该步骤安装完成后，会在 /etc/yum.repos.d 目录下生成一个 pgdg-redhat-all.repo，里面为 PostgreSQL 各个版本的源信息。

```shell
# Red Hat Enterprise Linux 7 - x86_64
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# CentOS 7 - x86_64
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Red Hat Enterprise Linux 6 - x86_64
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-6-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# CentOS 6 - x86_64
yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-6-x86_64/pgdg-redhat-repo-latest.noarch.rpm
```

最新的 yum 源 rpm 包可以在这里找到：<https://yum.postgresql.org/repopackages/>

### 2. 安装

yum 源安装完成后，再次执行 yum list postgresql\* 命令可以看到 postgresql\*、postgresql10\*、postgresql11\*、.... 各个版本的 PostgreSQL 列表，选择需要的版本安装。

```bash
yum install -y postgresql10 postgresql10-devel
```

**yum 的方式安装的 PostgreSQL 默认保存在 /usr/pgsql-10（/usr/pgsql-9.6）下面。**

### 3. 初始化与启动

具体自己去谷歌，或者参考：《[Linux 下 PostgreSQL 源码编译安装](https://www.yuque.com/bioitee/mp/linux-postgresql-install?view=doc_embed)》。

## undefined symbol: PQescapeIdentifier

安装完 psycopg2 和 hgvs 后，如果 import 过程中出现类似于 **\_psycopg.cpython-37m-x86_64-linux-gnu.so: undefined symbol: PQescapeIdentifier** 的异常，可以查看一下 **\_psycopg.cpython-37m-x86_64-linux-gnu.so** 的对应的动态库链接 **libpq.so** 是否正确。

```bash
$ ldd /SoftWare/Python-3.7.3/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-x86_64-linux-gnu.so
        linux-vdso.so.1 =>  (0x00007fff65bff000)
        libpq.so.5 => /usr/lib64/libpq.so.5 (0x00007fbe7bb03000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fbe7b8e6000)
        libc.so.6 => /lib64/libc.so.6 (0x00007fbe7b551000)
        libssl.so.10 => /usr/lib64/libssl.so.10 (0x00007fbe7b2e5000)
        libcrypto.so.10 => /usr/lib64/libcrypto.so.10 (0x00007fbe7af00000)
        libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007fbe7acbb000)
        libldap_r-2.4.so.2 => /lib64/libldap_r-2.4.so.2 (0x00007fbe7aa67000)
        /lib64/ld-linux-x86-64.so.2 (0x0000003636a00000)
        libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007fbe7a781000)
        libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007fbe7a57c000)
        libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007fbe7a350000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007fbe7a14c000)
        libz.so.1 => /RiboBio/Bioinfo/APPS/R-3.3.2/lib/libz.so.1 (0x00007fbe79f34000)
        libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007fbe79d29000)
        libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007fbe79b26000)
        libresolv.so.2 => /lib64/libresolv.so.2 (0x00007fbe7990b000)
        liblber-2.4.so.2 => /lib64/liblber-2.4.so.2 (0x00007fbe796fc000)
        libssl3.so => /usr/lib64/libssl3.so (0x00007fbe794bf000)
        libsmime3.so => /usr/lib64/libsmime3.so (0x00007fbe79292000)
        libnss3.so => /usr/lib64/libnss3.so (0x00007fbe78f54000)
        libnssutil3.so => /usr/lib64/libnssutil3.so (0x00007fbe78d28000)
        libplds4.so => /lib64/libplds4.so (0x00007fbe78b23000)
        libplc4.so => /lib64/libplc4.so (0x00007fbe7891e000)
        libnspr4.so => /lib64/libnspr4.so (0x00007fbe786e1000)
        libsasl2.so.2 => /usr/lib64/libsasl2.so.2 (0x00007fbe784c6000)
        libselinux.so.1 => /lib64/libselinux.so.1 (0x00007fbe782a7000)
        librt.so.1 => /lib64/librt.so.1 (0x00007fbe7809e000)
        libcrypt.so.1 => /lib64/libcrypt.so.1 (0x00007fbe77e67000)
        libfreebl3.so => /lib64/libfreebl3.so (0x00007fbe77bf0000)
```

正常情况下，/usr/lib64/libpq.so.5 应该对应于 /usr/pgsql-10/lib/libpq.so.5，如果不是，可以参考下面两种方法：

1.  通过设置 **LD_LIBRARY_PATH**，使其链接正确的动态库。

**export LD_LIBRARY_PATH=/usr/pgsql-10/lib:$LD_LIBRARY_PAT**

2.  先备份重命名 /usr/lib64/libpq.so.5，再把正确的 libpq.so.5 软连接过去。

```bash
$ mv /usr/lib64/libpq.so.5 /usr/lib64/libpq.so.5.old
$ ln -s /usr/pgsql-10/lib/libpq.so.5 /usr/lib64/libpq.so.5
```
