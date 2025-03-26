---
title: Python3 编译安装 --with-openssl 无效的问题
number: 27
slug: discussions-27/
url: https://github.com/shenweiyan/Digital-Garden/discussions/27
date: 2023-12-01
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.5-Python']
---

很多人在使用 Python3 经常会遇到一些 openssl 版本太低从而导致包无法正常使用的问题，尤其是 `urllib3` 这个包。
```python
Python 3.9.18 (main, Sep  7 2023, 14:32:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/software/python-3.9.18/lib/python3.9/site-packages/requests/__init__.py", line 43, in <module>
    import urllib3
  File "/usr/local/software/python-3.9.18/lib/python3.9/site-packages/urllib3/__init__.py", line 41, in <module>
    raise ImportError(
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168
>>> import ssl
>>> import urllib3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/software/python-3.9.18/lib/python3.9/site-packages/urllib3/__init__.py", line 41, in <module>
    raise ImportError(
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168
```

网络上有很多关于这方面的教程，主要解决方案：

1. 降级 `urllib3` 的版本，例如：`pip install --upgrade urllib3==1.26.15`；
2. 重新安装一个更高版本的 OpenSSL，然后备份并替换系统原来的 openssl，最后重新编译安装 Python。

个人觉得这两个方法都不够好，尤其是第二个方法 —— 

- 新装了一个更高版本的 OpenSSL，但是又不想替换系统原来的 openssl 以免出现新的问题（或者没有管理员权限）；
- 在编译的时候使用 `--with-openssl` 指定了新装的 OpenSSL 路径，编译安装完成后 Python **仍然使用旧版本的 OpenSSL**；

很不幸的是，个人在 CentOS 7.3 + Python-3.9.18 就遇到了这个问题。

1. 新装了 OpenSSL 3.0.10 
```
wget https://www.openssl.org/source/openssl-3.0.10.tar.gz --no-check-certificate
tar zvxf openssl-3.0.10.tar.gz
cd openssl-3.0.10
./config --prefix=/usr/local/software/openssl-3.0.10 shared zlib
make && make install
```

2. 添加 `~/.bashrc` 环境变量
```
export PATH=/usr/local/software/openssl-3.0.10/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/software/openssl-3.0.10/lib64:$LD_LIBRARY_PATH
```

3. 重新编译安装 Python-3.9.18
```
./configure --prefix=/usr/local/software/python-3.9.18 --with-openssl=/usr/local/software/openssl-3.0.10/
make && make install
```

等编译完成后，你会神奇的发现重新编译安装后 Python 3.9.18 **仍然使用旧版本的 OpenSSL (OpenSSL 1.0.2k-fips  26 Jan 2017)**！

其实，这还是因为 Python 在重新编译的时候没有识别到新编译的 OpenSSL，因此，我们需要把重新编译的命令调整一下：
```
/configure --prefix=/usr/local/software/python-3.9.18 \
--with-openssl=/usr/local/software/openssl-3.0.10/ \
LDFLAGS="-L/usr/local/software/openssl-3.0.10/lib64" \
CPPFLAGS="-I/usr/local/software/openssl-3.0.10/include" \
PKG_CONFIG_PATH="/usr/local/software/openssl-3.0.10/lib64/pkgconfig"
```

这样子一来，问题就迎刃而解了，编译安装完后，你会发现 Python 3.9.18 已经成功用用上了 OpenSSL 3.0.10 1 Aug 2023：
```
$ python3 -c "import ssl; print(ssl.OPENSSL_VERSION)"
OpenSSL 3.0.10 1 Aug 2023
```
![OpenSSL 3.0.10 on Python3.9.18](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/Gitbook/2023/python-3.9.18-openssl-3.0.10.png)

## 参考资料

1. [Drop support for OpenSSL<1.1.1 - urllib3/urllib3#2168](https://github.com/urllib3/urllib3/issues/2168)



<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="27"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
