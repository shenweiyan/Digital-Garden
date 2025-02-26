---
title: Python 获取 NCBI 基因名 SSL 证书出现异常
urlname: 2021-09-26-unable-to-get-local-issuer-certifica
author: 章鱼猫先生
date: 2021-09-26
updated: "2021-11-06 19:29:44"
---

源自于前几天对一批转录本的批量化操作的一些记录。

即想要通过 Python 在线获取某个转录本对应的基因 Symbol 时，发现出现 SSL 无法获取本地证书：**unable to get local issuer certificate (\_ssl.c:1056)**！

```python
>>> from Bio import SeqIO
>>> from Bio import Entrez
>>> Entrez.email = "A.N.Other@example.com"
>>> records = SeqIO.parse(Entrez.efetch(id='NM_001009537.4', db="nucleotide", rettype="gb", retmode="text"), "gb")
Traceback (most recent call last):
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 1317, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 1229, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 1275, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 1224, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 1016, in _send_output
    self.send(msg)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 956, in send
    self.connect()
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/http/client.py", line 1392, in connect
    server_hostname=server_hostname)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/ssl.py", line 412, in wrap_socket
    session=session
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/ssl.py", line 853, in _create
    self.do_handshake()
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/ssl.py", line 1117, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 184, in efetch
    return _open(cgi, variables, post=post)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/site-packages/Bio/Entrez/__init__.py", line 543, in _open
    handle = _urlopen(cgi)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 525, in open
    response = self._open(req, data)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 543, in _open
    '_open', req)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 503, in _call_chain
    result = func(*args)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 1360, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "/home/shenweiyan/software/Python-3.7.3/lib/python3.7/urllib/request.py", line 1319, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)>
```

根据网络上的解析，当使用 **urllib.urlopen** 打开一个 https 链接时，会验证一次 SSL 证书。而当目标网站使用的是自签名的证书时就会抛出如下异常：

**ssl.SSLCertVerificationError: \[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1056)**

解决方法也很简单，下面是个人简单总结的 3 种常用解决方法。

### 方法一，全局取消证书验证

```python
>>> import ssl
>>> ssl._create_default_https_context = ssl._create_unverified_context
```

### 方法二，指定位置安装证书

1.  查看证书默认位置。

```python
>>> import ssl
>>> print(ssl.get_default_verify_paths())
DefaultVerifyPaths(cafile=None, capath='/home/shenweiyan/software/LibDependence/openssl-1.1.1/ssl/certs', openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/home/shenweiyan/software/LibDependence/openssl-1.1.1/ssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/home/shenweiyan/software/LibDependence/openssl-1.1.1/ssl/certs')
```

由于在 **openssl_cafile** 中指定的 CA 文件（**cert.pem**）不存在，所以导致上面的错误。

2.  下载 CA 文件，将下载的 CA 文件放到 **openssl_cafile** 指定位置。注意，如果放到 **openssl_capath** 目录下还会出现类似的问题，一定要放到 **openssl_cafile** 指定的位置。

```python
$ cd /home/shenweiyan/software/LibDependence/openssl-1.1.1/ssl
$ wget http://curl.haxx.se/ca/cacert.pem -O cert.pem --no-check-certificate
```

### 方法三，设置环境变量

也可以参考 [stackoverflow](https://stackoverflow.com/questions/55736855/how-to-change-the-cafile-argument-in-the-ssl-module-in-python3) 上的做法，通过修改下面环境变量的方式解决（亲测可行）。

```python
export SSL_CERT_FILE=/usr/local/etc/openssl/cert.pem
export REQUESTS_CA_BUNDLE=/usr/local/etc/openssl/cert.pem
```

最后，问题解决。

```python
>>> from Bio import SeqIO
>>> from Bio import Entrez
>>> Entrez.email = "A.N.Other@example.com"
>>> records = SeqIO.parse(Entrez.efetch(id='NM_001009537.4', db="nucleotide", rettype="gb", retmode="text"), "gb")
>>> for record in records:
...     for feature in record.features:
...         if feature.type == "gene":
...             print(feature.qualifiers['gene'])
...
['Zfp799']
```
