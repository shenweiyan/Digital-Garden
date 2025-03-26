---
title: 在 RHEL 使用 gdc-client 下载 TCGA 数据
urlname: 2020-08-17-gdc-client-for-redhat-centos
author: 章鱼猫先生
date: 2020-08-17
updated: "2021-06-25 10:37:33"
---

今天，只聊一下 RedHat/CentOS 下 gdc-client 安装的那些事~

gdc-client（<https://gdc.cancer.gov/access-data/gdc-data-transfer-tool>）是由 GDC 官方提供的一个可以在命令行下批量下载 TCGA 数据的客户端工具。

在 gdc-client 官网可以看到 Mac、Windows 和 Ubuntu 的二进制版本下载，却唯独没看到 CentOS/RedHat 版本的！而且还给了我们一个提示说，如果你想要安装 RedHat Enterprise Release 6  版本的 gdc-client 需要跟 GDC 进行联系！！
![gdc.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FkbXuAPJHZiZqpBVCEwgBZ0wsYgt.png)

如果你用 "gdc-client" + "centos6" 的关键字去谷歌，会发现大部分的答案都是教你用 Python2 的虚拟环境去安装 gdc-client。
![gdc-client-centos6-Google.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Frjz_5OxHOVj_DEDt6G_24tUvuMQ.png)

其实，这些大部分都存在误导的成分，虽然 gdc-client 官网虽然没有提供 CentOS 6 的二进制程序包，但它托管在 GitHub 的源码我们是可以直接安装的，而且是只支持 Python 3！！

### 坑一：Python 2 引发 parse 模块异常

```bash
conda create -n Python2 python=2.7
source activate Python2
git clone https://github.com/NCI-GDC/gdc-client
cd gdc-client
python setup.py install 2>&1 | tee -a install.log
```

这种方法虽然看起来没什么问题，却会执行 `gdc-client -h`  提示 parse 模块异常。其原因是 **build/bdist.linux-x86_64/egg/gdc_client/download/parser.py**  的第三行 `from urllib import parse as urlparse`  是 py3 的语法：在 python 2.x 中的 `urlparse`  模块在 Python 3 中已经重命名为 `urllib.parse` 。

```python
# Python 2 正确语法
from urlparse import urlparse

# Python 3 正确语法
from urllib import parse as urlparse
```

![gdc-client-parser.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlPrmE8ny-JWm3fe_bQeAEMKbjXs.png)

### 坑二：conda 安装无法响应

bioconda 虽然也提供了 gdc-client，但是本人 一直没法安装成功，可能是我的运气不太好！
![bioconda-gdc-client.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FpoqmI7dfG3xa5xgcfP9opZ_KRIS.png)

### 最后，CentOS 6 的正确解锁姿势

```bash
conda create -n gdc python=3.7
source activate gdc

git clone https://github.com/NCI-GDC/gdc-client
cd gdc-client
pip install -r requirements.txt
python setup.py install 2>&1 | tee -a install.log
```

![gdc-client-help.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjrP1HvQh-x25C1FNQeZmRl8deT9.png)

最后，打开 GDC 的官方《[Data Transfer Tool Command Line Documentation](https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/Data_Download_and_Upload/)》文档，查看在命令下怎么使用 gdc-client 下载你想要的 TCGA 数据吧！
