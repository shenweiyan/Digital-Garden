---
title: CentOS Linux 7 安全基线设置
urlname: 2019-07-01-security-for-centos-7
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-06-30 09:34:53"
---

作为一个生信人，不管是日常的数据分析还是其他工具应用的开发，服务器的安全始终是一个无法避免的话题。尤其是当我们拿到一台新的服务器，我们需要怎样才能确保它是安全可靠，并最小限度降低它被攻击的可能性？

下面我们就来分享一份关于 CentOS Linux 7 安全的基线设置指南，希望对服务器管理的童鞋有所帮助。

① 设置用户权限配置文件的权限。

```bash
$ chown root:root /etc/passwd /etc/shadow /etc/group /etc/gshadow
$ chmod 0644 /etc/group
$ chmod 0644 /etc/passwd
$ chmod 0400 /etc/shadow
$ chmod 0400 /etc/gshadow
```

② 确保 SSH LogLevel 设置为 INFO，记录登录和注销活动。

```bash
# 编辑 /etc/ssh/sshd_config 文件以按如下方式设置参数(取消注释):
LogLevel INFO
```

③ 设置 SSH 空闲超时退出时间，可降低未授权用户访问其他用户 ssh 会话的风险。

```bash
# 编辑 /etc/ssh/sshd_config，将 ClientAliveInterval 设置为 300 到 900，即 5-15 分钟，将 ClientAliveCountMax 设置为 0。
ClientAliveInterval 900 ClientAliveCountMax 0
```

④ SSHD 强制使用 V2 安全协议。

```bash
# 编辑 /etc/ssh/sshd_config 文件以按如下方式设置参数：
Protocol 2
```

⑤ 确保 SSH MaxAuthTries 设置为 3 到 6 之间。设置较低的 Max AuthTrimes 参数将降低 SSH 服务器被暴力攻击成功的风险。

```bash
# 在 /etc/ssh/sshd_config 中取消 MaxAuthTries 注释符号 #，设置最大密码尝试失败次数 3-6，建议为 4：
MaxAuthTries 4
```

⑥ 设置密码修改最小间隔时间，限制密码更改过于频繁。

```bash
# 在 /etc/login.defs 中将 PASS_MIN_DAYS 参数设置为7-14之间,建议为7：
PASS_MIN_DAYS 7

# 需同时执行命令为 root 用户设置：
chage --mindays 7 root
```

⑦ 设置密码失效时间，强制定期修改密码，减少密码被泄漏和猜测风险，使用非密码登陆方式(如密钥对)请忽略此项。

    # 使用非密码登陆方式如密钥对，请忽略此项。

    # 在 /etc/login.defs 中将 PASS_MAX_DAYS 参数设置为 60-180之间，如:
    PASS_MAX_DAYS 90

    # 需同时执行命令设置 root 密码失效时间：
    chage --maxdays 90 root

⑧ 禁止 SSH 空密码用户登录。

```bash
# 编辑文件 /etc/ssh/sshd_config ，将 PermitEmptyPasswords 配置为 no:
PermitEmptyPasswords no
```

⑨ 密码复杂度检查，检查密码长度和密码是否使用多种字符类型。

```bash
# 编辑 /etc/security/pwquality.conf，把 minlen（密码最小长度）设置为 9-32 位。
# 把 minclass（至少包含小写字母、大写字母、数字、特殊字符等4类字符中等3类或4类）设置为 3 或 4。
minlen=10 minclass=3
```

⑩ 确保密码到期警告天数为 7 或更多。

```bash
# 在 /etc/login.defs 中将 PASS_WARN_AGE 参数设置为7-14之间，建议为7：
PASS_WARN_AGE 7

# 同时执行命令使 root 用户设置生效：
chage --warndays 7 root
```

⑪ 确保 root 是唯一的 UID 为 0 的帐户，除 root 以外其他 UID 为 0 的用户都应该删除，或者为其分配新的 UID。

```bash
# 除 root 以外其他 UID 为 0 的用户(查看命令如下)都应该删除，或者为其分配新的 UID。
cat /etc/passwd | awk -F: '($3 == 0) { print $1 }'|grep -v '^root$'
```

⑫ 开启地址空间布局随机化，它将进程的内存空间地址随机化来增大入侵者预测目的地址难度，从而降低进程被成功入侵的风险。

```bash
# 执行命令：
sysctl -w kernel.randomize_va_space=2
```

⑬ 检查系统空密码账户。

```
# 为用户设置一个非空密码

```

⑭ 访问控制配置文件的权限设置。

```bash
# 运行以下4条命令：
$ chown root:root /etc/hosts.allow
$ chown root:root /etc/hosts.deny
$ chmod 644 /etc/hosts.deny
$ chmod 644 /etc/hosts.allow
```

⑮ 确保 rsyslog 服务已启用，记录日志用于审计。

```bash
# 运行以下命令启用rsyslog服务:
systemctl enable rsyslog
```

⑯ 检查密码重用是否受限制，强制用户不重用最近使用的密码，降低密码猜测攻击风险。

```bash
# 在 /etc/pam.d/password-auth 和 /etc/pam.d/system-auth 中 password sufficient pam_unix.so 这行的末尾配置 remember 参数为5-24之间，原来的内容不用更改。
# 如下面只在末尾加了 remember=5，即可限制不能重用最近5个密码。
password sufficient pam_unix.so sha512 try_first_pass remember=5
```

以上就是关于 CentOS Linux 7 安全的一些基本设置总结。服务器的安全与管理是一个庞大的工程，如果你有更好的建议，欢迎留言交流。
