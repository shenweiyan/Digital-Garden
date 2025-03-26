---
title: Galaxy 平台 release_24.x 升级之路
number: 90
slug: discussions-90/
url: https://github.com/shenweiyan/Digital-Garden/discussions/90
date: 2024-10-18
authors: [shenweiyan]
categories: 
  - 3.1-Galaxy
labels: ['3.1.x-GalaxyOther']
---

记录一下 Galaxy 分析平台从 **release_20.09** 升级到 **release_24.0**，横跨九个发布版本的升级之路。

<!-- more -->

## 为什么要升级

很主要的一个原因是随着新技术的更新，旧版本的使用可能会存在一些安全隐患，尤其对于提供互联网公开访问的平台。新版本的升级有助于捕获并应用所有先前的安全更新，以确保平台的安全性。

## 版本选择

最开始选择的是 [release_24.1](https://docs.galaxyproject.org/en/master/releases/24.1_announce_user.html) 版本，但好不容易安装完成后才发现，这个新版本中增加了一个常规途径下无法隐藏的 **Activity Bar Interface**，一时间无法忍受。
![23.1-activity-bar](https://kg.weiyan.cc/2024/10/23.1-activity-bar.png)     
![galaxy-24.1](https://kg.weiyan.cc/2024/10/galaxy-24.1.png)

第二个原因是，后台 PostgreSQL 数据库的升级遇到了 [function gen_random_uuid() does not exist](https://help.galaxyproject.org/t/database-upgrade-error/13687) 异常，一下子没法解决也不想去升级 PostgreSQL 版本。

所以，最终选择了从 **release_20.09** 升级到次新的 **release_24.0** 版本方案。

## 安装系统环境

这里以 release_24.1 作为示例，该环境要求同样适用于 release_24.0。

Galaxy release_24.1 默认安装 node-v18.12.1，参考：`run.sh` → `./scripts/common_startup_functions.sh` → `./scripts/common_startup.sh` → `nodeenv -n "$NODE_VERSION" -p` 的安装代码。

node-v18.12.1 下载地址：<https://nodejs.org/download/release/v18.12.1/>

node-v18.12.1 要求 g++ 8.3.0 or clang++ 8.0.0：    
![node-v18.12.1-gcc](https://kg.weiyan.cc/2024/10/node-v18.12.1-gcc.webp)

可以通过安装 Devtoolset 的方式解决：    

1. 手动调整  CentOS 7 的 SCL YUM 源（也可以 yum 安装），注意变更 `baseurl` 为阿里云或者其他的源链接。
   ```bash
   # 会默认在 /etc/yum.repos.d 下生成 2 个 repo 源文件
   # CentOS-SCLo-scl.repo
   # CentOS-SCLo-scl-rh.repo
   yum install centos-release-scl centos-release-scl-rh
   ```
2. 更新 yum 源的缓存。
   ```bash
   cd /etc/yum.repos.d
   yum clean all
   yum makecache
   ```
3. 安装 scl-utils，scl-utils 是管理 SCL (Software Collection) 环境设置和运行软件的一套软件工具。
   ```bash
   yum install scl-utils
   ```
4. 安装 devtoolset-9。
   ```bash
   yum install devtoolset-9
   ```
5. 激活 devtoolset-9。
   ```bash
   source /opt/rh/devtoolset-9/enable
   ```

## Python 环境

Galaxy 要求 Python >= 3.8，node-v18.12.1 要求 3.6<=Python<=3.10，这里选择 Python-3.9.18，安装如下。

```bash
wget https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tgz
tar zvxf Python-3.9.18.tgz
cd Python-3.9.18
$enabledevtoolset9
export TCLTK_LIBS="-L/home/shenweiyan/software/tcltK-8.5.19/lib -ltcl8.5 -ltk8.5"
export TCLTK_CFLAGS="-I/home/shenweiyan/software/tcltK-8.5.19/include"
./configure --enable-optimizations --prefix=/home/shenweiyan/software/python-3.9.18 --with-openssl=/home/shenweiyan/software/openssl-1.1.1/ --with-tcltk-includes="-I/home/shenweiyan/software/tcltK-8.5.19/include" --with-tcltk-libs="-L/home/shenweiyan/software/tcltK-8.5.19/lib -ltcl8.5 -ltk8.5" 
make -j 4
make install
```

Python-3.9.18 安装完成后，避免 `ssl` 模块无法正常 `import` 使用，需要在环境中增加以下设置。
```bash
export LD_LIBRARY_PATH=/home/shenweiyan/software/openssl-1.1.1/lib:$LD_LIBRARY_PATH
```

## Node 环境

Galaxy 的 `sh run.sh` 默认通过 `ssl` 的方式安装已经提前编译好的 node-v18.12.1-linux-x64.tar.gz（直接解压即可使用），对于系统版本比较低的服务器（如 CentOS 7）会存在 GLIBC 异常，因此需要调整为 `ignore_ssl_certs` 的下载方式 + source 源码安装的方式安装 node-v18.12.1。     
![nodeenv--help](https://kg.weiyan.tech/2024/10/nodeenv-help.webp)

所以，最终的方法为调整 `./scripts/common_startup.sh` 中 `nodeenv -n "$NODE_VERSION" -p` 的安装代码如下：
```bash
nodeenv -n "$NODE_VERSION" -p --source --ignore_ssl_certs --jobs=1
```

node-v18.12.1 下载地址：<https://nodejs.org/download/release/v18.12.1/>。

由于编译非常耗时（4核8G 的服务器编译了 1 个小时左右），且对 Python 版本有要求，建议手动安装，具体安装步骤如下。
```bash
shenweiyan@centos-vm-7 10:30:34 /home/shenweiyan/src/node-v18.12.1
$ ./configure --prefix=/home/shenweiyan/software/node-v18.12.1
Node.js configure: Found Python 3.11.6...
Please use python3.10 or python3.9 or python3.8 or python3.7 or python3.6.
```

```bash
$ wget https://nodejs.org/download/release/v18.12.1/node-v18.12.1.tar.gz
$ tar zvxf node-v18.12.1.tar.gz
$ cd node-v18.12.1
$ source /opt/rh/devtoolset-9/enable
$ ./configure --prefix=/home/shenweiyan/software/node-v18.12.1
Node.js configure: Found Python 3.9.18...
INFO: configure completed successfully
$ make -j 4
$ make install
```

## Yarn 环境

注意要先设置 `npm` 的路径，如果有多个版本的 `npm`，会因为版本混乱导致语法异常。

```bash
export PATH=/home/shenweiyan/software/node-v18.12.1/bin:$PATH
/home/shenweiyan/software/node-v18.12.1/bin/npm install --global yarn
```

## pip 源

Galaxy 在安装 `requirements.txt` 的时候默认使用下面两个源：

- <https://wheels.galaxyproject.org/simple>
- <https://pypi.python.org/simple>

对于国内服务器，可以考虑更换为阿里云或者清华大学的 pip 源。可以：

- 在 `scripts/common_startup.sh` 中修改：
  ```bash
  : ${PYPI_INDEX_URL:="https://mirrors.aliyun.com/pypi/simple/"}
  ```

- 在 `requirements.txt` 头部增加：
  ```bash
  -i https://mirrors.aliyun.com/pypi/simple/
  --extra-index-url https://wheels.galaxyproject.org/simple
  ```

## 数据库升级

这是本次 Galaxy 核心版本升级时候遇到的最大问题。

由于 Galaxy 在 release_21.05 新增加了一个 [`history_audit`](https://github.com/galaxyproject/galaxy/pull/11914) 数据表，release_20.09 的数据库直接执行 `sh manage_db.sh upgrade` 升级的时候 `history_audit` 数据表并不会一并创建和更新，因此最终导致在 Galaxy 服务启动的时候发生错误。

这应该是数据库升级时候的一个bug，经过摸索发现，目前可以参考下面的文章，通过分步升级的方式解决。

- <https://mp.weixin.qq.com/s/arRZ-3mMrpUIsXYuqg4sGQ>

以上解决方法，参考：[galaxyproject/galaxy #19016](https://github.com/galaxyproject/galaxy/issues/19016)   
  
![galaxy-issues-19016](https://kg.weiyan.cc/2024/10/galaxy-issues-19016.png)

## 总结

更新后的 release_24.0 界面看起来比旧版本要更加清爽舒服一些，各个页面的汉化功能也有所改善，新增的 Notifications 功能也挺不错，总之升级之后各个方面还是挺满意的，其他细节和功能还在体验中。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="90"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
