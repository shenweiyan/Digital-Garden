---
title: RHEL6 ssh 到 RHEL9 的 no hostkey alg 错误
urlname: 2022-08-18-rhel-9-no-hostkey-alg
author: 章鱼猫先生
date: 2022-08-18
updated: 2024-11-01
---

前一段时间把阿里云的一个轻量云服务器的系统升级到了 AlmaLinux release 9.0 (Emerald Puma)，开启 RHEL 9 系列的新体验。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fp2J6etLXPMJzUxy_TqI3q4deG0A.png)

发现的第一个比较直观的问题：

**从 RHEL 6.x 的服务器 ssh 到 AlmaLinux 9 的轻量云服务器时候出现 no hostkey alg 错误！**

```bash
$ ssh root@xxx.123.456.xx
no hostkey alg
```

一开始拿着这个错误去谷歌，看了一些回答（例如，KexAlgorithms 算法支持问题；权限问题，`/etc/ssh/ssh_host_*key` 问题；等等）都没办法解决，后来去 AlmaLinux 社区提问，并参考了一些官方的文档说明，才最终把这个问题解决了。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Flgu92Si4SO1GDPjqVHq-UPUBRCX.png)

从 RHEL9 的官网文档《[1.0.2. Crypto-policies, RHEL core cryptographic components, and protocols](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/considerations_in_adopting_rhel_9/index#ref_considerations-security-crypto_changes-to-security)（加密策略、RHEL 核心加密组件和协议）》可以看到 **SHA-1** 已经在 RHEL9 中弃用了！

> In RHEL 9, SHA-1 usage for signatures is restricted in the DEFAULT system-wide cryptographic policy. Except for HMAC, SHA-1 is no longer allowed in TLS, DTLS, SSH, IKEv2, DNSSEC, and Kerberos protocols. Individual applications not controlled by the RHEL system-wide crypto policies are also moving away from using SHA-1 hashes in RHEL 9.

在 RHEL 9 中，用于签名的 SHA-1 用法在 DEFAULT 系统范围的加密策略中受到限制。除 HMAC 外，TLS、DTLS、**SSH**、IKEv2、DNSSEC 和 Kerberos 协议中不再允许使用 **SHA-1**。不受 RHEL 系统范围的加密策略控制的单个应用程序在 RHEL 9 中也不再使用 SHA-1 hashes。

> If your scenario requires the use of SHA-1 for verifying existing or third-party cryptographic signatures, you can enable it by entering the following command:

如果您的方案需要使用 **SHA-1** 来验证现有或第三方加密签名，您可以通过输入以下命令来启用它：

```bash
# update-crypto-policies --set DEFAULT:SHA1
```

或者，您可以将系统范围的加密策略切换到 `LEGACY` 策略。请注意，`LEGACY`还启用了许多其他不安全的算法。有关详细信息，请参阅 [RHEL 9 Security hardening](https://docs.redhat.com/zh_hans/documentation/red_hat_enterprise_linux/9/html/security_hardening/index)（RHEL 9 安全强化）文档中的 [Re-enabling SHA-1](https://docs.redhat.com/zh_hans/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening#proc_re-enabling-sha-1_using-the-system-wide-cryptographic-policies)（重新启用 SHA-1）部分。

## 参考资料

1. [1.0.2. Crypto-policies, RHEL core cryptographic components, and protocols](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/considerations_in_adopting_rhel_9/index#ref_considerations-security-crypto_changes-to-security)，RHEL9 官网文档（英文）
2. [20.2. crypto-policies、RHEL 内核加密组件和协议](https://docs.redhat.com/zh_hans/documentation/red_hat_enterprise_linux/9/html/considerations_in_adopting_rhel_9/ref_considerations-security-crypto_changes-to-security)，Red Hat Product Documentation（中文）
3. [No hostkey alg error from RHEL6 ssh to AlmaLinux9](https://almalinux.discourse.group/t/no-hostkey-alg-error-from-rhel6-ssh-to-almalinux9/1509)，AlmaLinux 社区
