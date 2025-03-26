---
title: 基于 Web 的 Linux 终端 WebTerminal
urlname: 2019-07-01-webterminal-for-linux
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-25 10:39:03"
---

有时候用公共电脑，或者在没有安装 putty、xshell 之类的终端的电脑上访问或展示服务器上的一些资料数据，甚至是在运维平台开发中想要嵌入 WebTerminal 功能，于是找到了这个项目 —— 基于 Web 的 Linux 终端 webSSH。

webSSH 是 Python 语言写的一个基于 tornado 和 paramiko 包的 web 应用，它可以作为一个 ssh 终端连接你的服务器。webSSH 主要特点：

- 支持 SSH 密码认证，包括空密码；
- 支持 SSH 公钥认证，包括 DSA RSA ECDSA Ed25519 keys；
- 支持 Encrypted keys；
- 支持全屏终端，且终端窗口可调整大小；
- 自动检测系统默认编码；
- 适用于 Python 2.7-3.6。

# 1. 安装

```bash
pip install webssh
```

# 2. 启动

webssh 安装完成，我们可以通过 wssh 命令进行启动

```bash
$ wssh
[I 180627 11:14:55 settings:67] WarningPolicy
[I 180627 11:14:55 main:33] Listening on 127.0.0.1:8888
```

wssh 默认启用 localhost 的 8888 端口开启服务，我们也可以通过监听 0.0.0.0 来使用本地的 iP 并指定服务端口

```bash
$ wssh --address='0.0.0.0' --port=8000
[I 180627 11:07:05 settings:67] WarningPolicy
[I 180627 11:07:05 main:33] Listening on 0.0.0.0:8000
```

这时候，在浏览器打开 <http://ip:8000，输入登陆信息，登陆> web 终端：
![webt.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsqW5kM2kU_rElrYV0WCyo0EFp9h.png)

![webt-2.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlO0DMXBgSzrdAddMrEebbNUrw-p.png)

# 3. 参数

wssh 的一些主要参数如下

```bash
#配置监听地址与服务端口
wssh --address='0.0.0.0' --port=8000

#配置缺少主机密钥策略
wssh --policy=reject

#配置日志级别
wssh --logging=debug

#配置保存日志到指定文件
wssh --log-file-prefix=main.log

#更多参数说明
wssh --help
```

# 4. Nginx

wssh 可以使用 Nginx 作为后台代理，以及启用 SSL 访问，参考配置文件

```basic
location / {
    proxy_pass http://127.0.0.1:8888;
    proxy_http_version 1.1;
    proxy_read_timeout 300;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $http_host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Real-PORT $remote_port;
}
```

- 使用 Nginx 作为后台代理，并启用 SSL 访问，可以避免你的 ssh 证书被暴露。此外，你的浏览器和 Web 服务器之间的通信将使用安全的 Websockets 进行加密。
- 尝试使用 reject policy 作为缺少主机密钥时的策略，以及经过验证的 known_hosts，可以防止中间人的攻击。其思路是，webssh 会依次检查系统主机密钥文件（"\~/.ssh/known_hosts"）和应用程序主机密钥文件（"./known_hosts"），如果 ssh 服务器的主机名（hostname）没有被发现或者密钥不匹配，连接将被中止。

# 5. 参考资料

- <https://www.oschina.net/p/webterminal>
