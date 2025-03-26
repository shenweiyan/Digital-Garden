---
title: SSH 登录与配置
urlname: 2021-10-08-ssh-config
author: 章鱼猫先生
date: 2021-10-08
updated: "2022-08-18 09:23:54"
---

# 解决 SSH Failed Permission Denied

在 SSH 服务器上修改了与权限相关的设置之后，会出现 SSH 权限拒绝错误（SSH Permission denied error）。通常的场景包括安装新的软件包或创建新用户。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuDhlk0w8wDpdRM2uh0B508OzPs9.png)
在本教程中，您将学习如何排除 SSH Permission denied 错误并重新连接到 SSH 服务器。

### 前提条件

- 以本地计算机作为 SSH Client 客户机和远程系统作为 SSH server 服务器。
- 通过一个用户账号对远程服务器进行访问(用于基于密码的登录)。
- 需要一个具有 sudo 或 root 特权的用户帐户(用于修改 SSH 相关配置)。

### SSH 权限拒绝

当尝试通过 SSH 进入服务器时，会出现 SSH 权限拒绝错误：

```bash
Permission denied (publickey,gssapi-keyex,gssapi-with-mic)
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fl0Um1zz_a2haoBC95bM-E9iyATa.png)
在 Permission denied 语句之后，括号里面包含了在连接启动时失败时尝试的身份验证方法。这个错误表明公钥才是问题所在，这其实是一种误导。

出现该错误的一个原因可能是与 **sshd_config** 的配置有关，这个文件包含了 SSH 服务器的配置。另一种可能性是授权的 **authorized_keys** 文件没有足够的权限，这个文件包含了允许从 Client 客户机 SSH 到远程服务器的公钥列表。因此，当系统无法正常读取文件就会导致“权限拒绝”错误。

### 修复 SSH Permission denied

两个解决方案都包含需要在服务器端执行的步骤。首先打开服务器上的终端，然后执行下面的解决方案之一。

#### 解决方案 1：启用密码身份验证

如果您想使用密码访问 SSH 服务器，修复 Permission denied 错误的解决方案是在 **sshd_config** 文件中启用密码登录。

要做到这一点，在文本编辑器中打开文件：

```bash
sudo nano /etc/ssh/sshd_config
```

- 在文件中，找到 **PasswordAuthentication** 行，并确保它以 **yes** 结尾。
- 在文件中，找到 **ChallengeResponseAuthentication** 选项，并通过添加 **no** 来禁用它。
- 如果行被注释掉了，删除散列符号\*\* #\*\* 以取消注释。

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvmtituWoEUKfE68c3lIOvjlQZJD.png)
保存文件并退出。

最后，通过输入以下命令重新启动 SSH 服务：

```bash
sudo systemctl restart sshd
```

#### 解决方案 2：更改文件系统权限

出于安全考虑，不推荐使用基于密码的登录作为 SSH 身份验证方法。因此，下面的解决方案可能是可取的，因为它解决了公共密钥认证的方法。

首先，使用文本编辑器打开 sshd_config 文件：

```bash
sudo nano /etc/ssh/sshd_config
```

在文件中，确保下列选项设置如下：

```bash
PermitRootLogin no
PubkeyAuthentication yes
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmBtxXXzvWUgnE0hmbGqc99dOFBz.png)
:::tips
\*\*注意: \*\*以上步骤被认为是最佳安全实践。如果需要使用 root 登录，请将相关行设置为 **yes**。
:::

注释掉与 gssapi 相关的选项，在行首添加 # 符号：

```bash
#GSSAPIAuthentication yes
#GSSAPICleanupCredentials no
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvrgRKB3xIKFGJ5YH8CCouJtb_O1.png)
另外，确保 **UsePAM** 行设置为 **yes**：

```bash
UsePAM yes
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuoChiJxnlCg3somKCSt5EKyBI1C.png)
保存文件并重新启动 sshd 服务：

```bash
systemctl restart sshd
```

接下来，导航到你的主文件夹并检查权限：

```bash
ls -ld
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FhsXKH2Qsd6vgBpZnwUkkWShZw2A.png)
如果您的所有者权限没有设置为读、写和执行(**drwx------**) ，请使用 **chmod** 命令更改它们：

```bash
chmod 0700 /home/[your-username]
```

现在进入 **.ssh** 文件夹，并重新检查该目录的权限：

```bash
ls -ld
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuSd31JgCeH2hRZ4FZ3xWed-sWtJ.png)
这个目录还应该具有文件所有者的读、写和执行权限，如果没有，请使用 **chmod** 命令更改它们：

```bash
chmod 0700 /home/your_home/.ssh
```

接着，再来检查 .**ssh** 文件夹包含授权的 **authorized_keys** 文件的权限：

```bash
ls –ld authorized_keys
```

![](https://shub.weiyan.tech/yuque/elog-cookbook-img/FnrHAhLGh4q6rv9bfwj9izV45_wd.png)
文件所有者应该具有该 **authorized_keys** 文件的读写权限。如果没有，请使用下面的方法修改：

```bash
chmod 0600 /home/[username]/.ssh/authorized_keys
```

现在再次尝试使用密钥对登录。下面的输出显示了一次成功的登录尝试。
![](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fv4k89FRw83fFI31fSukTwPzjJ0X.png)
:::tips
\*\*注意：\*\*有关 Linux 文件权限的详细信息，请阅读 Linux 文件权限教程。
:::

## 总结

本教程介绍了解决 SSH Permission denied (publikey、 gssapi-keyex、 gssapi-with-mic) 错误所需的步骤。通过完成指南中的步骤，您应该可以修复错误并成功地通过 SSH 连接到服务器。

# 解决 SSH 一段时间不操作就退出

在 CentOS/openEuler/Debian 系统上，发现了这个问题，SSH 登录后，一段时间吧不操作，SSH 就会自动退出。解决这个问题的办法，可以修改 SSH 服务器端的配置，也可以修改 SSH 客户端的配置。

## 修改 SSH 服务端的配置

**sudo vim /etc/ssh/sshd_config**

把下面这两行的注册打开，然后修改参数：
**ClientAliveInterval 30** # 表示每 30 秒服务器向客户端发起一次心跳，如果客户端响应就保持连接
**ClientAliveCountMax 5** # 如果连续 5 次服务器收不到心跳，就断开连接

以上两个参数，可以根据自己的情况来设置。

最后，配置要生效，需要重启 sshd 服务：

```bash
$ systemctl restart sshd.service

#或者
$ service sshd restart
```

正常情况，客户端不会不响应服务器的心跳，因此 SSH 客户端就不会再自动退出了。

## 修改 SSH 客户端的配置

修改客户端的配置的好处是，不需要重启服务端，如果你没有权限修改 SSH 服务器，也只能修改客户端的配置了。
**sudo vim /etc/ssh/ssh_config**

增加：
**TCPKeepAlive yes** # 据说这个配置项默认是开启的
**ServerAliveInterval 30** #客户端主动向服务端请求响应的间隔
**ServerAliveCountMax 5** # 连续 5 次客户端收不到服务器的响应，就是退出链接

好像大家都不太喜欢修改客户端的配置，而更新换直接在 ssh 命令行上输入这些配置项：
**ssh -o TCPKeepAlive=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=5 username\@serverip**

使用的是 -o 参数。

SSH 断开链接原因，常常是因为长时间没有数据传输，被中间的路由器掐断的。有了心跳，就可以解决这个问题。
