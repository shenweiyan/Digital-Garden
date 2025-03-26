---
title: 阿里云 ECS 更换操作系统
urlname: 2019-09-23-alyun-change-os
author: 章鱼猫先生
date: 2019-09-23
updated: "2021-07-07 15:08:20"
---

参考：[更换系统盘（公共镜像）](https://help.aliyun.com/document_detail/50134.html?spm=a2c4g.11186623.2.8.6a6447a0NgnzZM#concept-n4k-x3j-ydb)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqY9-nAGGTmZy7Mems-OBw2BpYAc.png)

## 操作步骤

1.  登录[ECS 管理控制台](https://ecs.console.aliyun.com/)。
2.  在左侧导航栏，选择**实例与镜像  >  实例**。
3.  在顶部状态栏处，选择地域。
4.  找到需要更换系统盘的实例，在**操作**列中，单击**更多  >  实例状态  >  停止**，并按页面提示停止实例。
    **说明**  对于按量付费的 VPC 类型实例而言，停机不收费模式下，更换系统盘后可能无法成功启动实例。建议您停止实例时关闭**停机不收费**。具体操作，请参见[按量付费实例停机不收费](https://help.aliyun.com/document_detail/63353.html#concept-js1-1fd-5db)。
5.  实例停止后，在**操作**列中，单击**更多  >  磁盘和镜像  >  更换系统盘**。
6.  在弹出的对话框里，仔细阅读更换系统盘注意事项后，单击**确定，更换系统盘**。
7.  在**更换系统盘**页面上，配置以下参数。
    _ **镜像类型**：选择**公共镜像**，并选择需要的镜像版本。
    **说明**  如果您需要使用其他镜像，请参见[更换系统盘（非公共镜像）](https://help.aliyun.com/document_detail/25448.html#concept-vbb-ckj-ydb)。
    _ **系统盘**：不能更换系统盘的云盘类型，但是您能根据业务需求和新镜像的需求扩容系统盘，最大容量为 500 GiB。扩容时能设置的最小容量与系统盘当前容量有关，如下表所示。
    _ **安全设置。**
    _ 确认**配置费用**：目前中国站所有公共镜像都不收费，这里的配置费用指系统盘的费用。系统盘价格，请参见[云产品价格页](https://www.aliyun.com/price/product#/ecs/detail)。 \* 确认无误后，单击**确定更换**。

## 执行结果

登录 ECS 控制台监控系统状态，完成操作系统更换大概需要 10 分钟。完成后，实例会自动启动。

## 后续步骤

更换系统盘后，您可能需要做以下操作：

- （可选）自动快照策略与磁盘 ID 绑定。更换了新的系统盘后，旧磁盘上应用的自动快照策略自动失效。您需要对新系统盘设置自动快照策略。具体操作，请参见[为新的系统盘设置自动快照策略](https://help.aliyun.com/document_detail/25457.html#concept-nyv-k3l-xdb)。
- 如果更换前后都是 Linux 系统，而且，实例上原来挂载了数据盘并设置了开机自动挂载分区。更换系统盘后，原来系统盘中的数据盘分区挂载信息丢失。您必须在新系统盘的/etc/fstab 文件写入新分区信息，并挂载分区，不需要对数据盘格式化并分区。操作步骤如下，具体的操作命令，请参见[Linux 格式化数据盘](https://help.aliyun.com/document_detail/25426.html#concept-jl1-qzd-wdb)。
  1.  （建议）备份 etc/fstab。
  2.  向 etc/fstab 写入新分区信息。
  3.  查看 etc/fstab 中的新分区信息。
  4.  运行`mount`命令挂载分区。
  5.  查看文件系统空间和使用情况：运行命令`df -h`。
- 挂载操作完成后，不需要重启实例即可开始使用新的数据盘。
