---
title: 生信服务器基本配置：防火墙
urlname: 2019-07-01-centos-firewall
author: 章鱼猫先生
date: 2019-07-01
updated: "2021-07-26 10:48:19"
---

主要介绍一下 CentOS 7 的防火墙基本配置知识，CentOS 6 的后续如果有需要再进行补充。

Centos7 默认安装了 firewalld，如果没有安装的话，则需要 YUM 命令安装；firewalld 真的用不习惯，与之前的 iptable 防火墙区别太大，但毕竟是未来主流讲究慢慢磨合它的设置规则。

## 安装 Firewall 命令

```shell
yum install firewalld firewalld-config
```

## Firewall 开启常见端口命令

```shell
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --zone=public --add-port=22/tcp --permanent
firewall-cmd --zone=public --add-port=21/tcp --permanent
firewall-cmd --zone=public --add-port=53/udp --permanent
```

## Firewall 关闭常见端口命令

```shell
firewall-cmd --zone=public --remove-port=80/tcp --permanent
firewall-cmd --zone=public --remove-port=443/tcp --permanent
firewall-cmd --zone=public --remove-port=22/tcp --permanent
firewall-cmd --zone=public --remove-port=21/tcp --permanent
firewall-cmd --zone=public --remove-port=53/udp --permanent
```

## 批量添加区间端口

```shell
firewall-cmd --zone=public --add-port=4400-4600/udp --permanent
firewall-cmd --zone=public --add-port=4400-4600/tcp --permanent
```

## 开启防火墙命令

```shell
systemctl start firewalld.service
```

## 重启防火墙命令

```shell
firewall-cmd --reload  或者   service firewalld restart
```

## 查看端口列表

```shell
firewall-cmd --permanent --list-port
```

## 禁用防火墙

```shell
systemctl stop firewalld
```

## 设置开机启动

```shell
systemctl enable firewalld
```

## 停止并禁用开机启动

```shell
systemctl disable firewalld
```

## 查看防火墙状态

```shell
systemctl status firewalld    或者 firewall-cmd --state
```
