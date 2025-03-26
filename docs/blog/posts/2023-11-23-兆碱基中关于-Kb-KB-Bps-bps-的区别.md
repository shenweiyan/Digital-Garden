---
title: 兆碱基中关于 Kb、KB、Bps、bps 的区别
number: 20
slug: discussions-20/
url: https://github.com/shenweiyan/Digital-Garden/discussions/20
date: 2023-11-23
authors: [shenweiyan]
categories: 
  - 知识
labels: []
---

生物信息很多文章都提到 DNA 序列的 100 万个碱基数据（兆碱基）大致相当于计算机 1 兆的存储空间。借着这个问题，我们今天来聊一聊计算机存储和数据传输中 Kb、KB、Bps、bps 的一些区别，分析一下所谓的兆碱基到底是使用哪一种标准（单位）怎么计算出来的。

<!-- more -->

## 计算机存储容量单位

Bit (binary digit)：亦称二进制位，指二进制中的一位，是信息的最小单位。位的值只会是 0 或 1。虽然计算机也提供对位的判断和操作，但是计算机指令一般以字节(Byte)为单位。在大多数的计算机系统中，八位是一个字节。一位的值通常以存储电容是否带电来衡量。

B (Byte)：字节。8 个二进制位构成 1 个"字节(Byte)"，它是电脑存储空间的基本计量单位。1 字节 (Byte)=8(bit) 位，就是有 8 个二进制数组成。1 个英文字符是 1 个字节,也就是 1B；1 个汉字为 2 个字符，也就是 2B。

GB (Gigabyte)：吉字节，是一种**十进制**的信息计量单位。Gibibyte（giga binary byte 的缩写）则是**二进制**信息计量的一个单位，简称 GiB。吉字节（Gigabyte）常容易和二进制的信息计量单位 Gibibyte 混淆。

> Gibibyte 与 Gigabyte 常常被混淆，前者的计算方式是二进制，后者的计算方式是十进制。现今的计算上，常把 Gigabyte 以二进制的方式计算，即 $2^{30} = 1,073,741,824$ 。(因为 Windows 对 GB 这个信息计量单位的误用，因此在 Windows 中显示的 "1GB"，其实应是指 "1GiB"，但 Windows 却显示为 "1GB"，而常造成误解。误用会普遍化的一大因素，是因为 Windows 的操作系统占有率高)，由于两种换算方法的不同，使容量在计算上相差了 7.3%，所以常有 Windows 系统报告的容量比硬盘标示的容量还要小的情况发生。但在苹果公司的 OS X 操作系统中，对于存储设备的容量计算方式与硬盘厂商一致，均为 1GB = 1,000,000,000 ( $10^{9}$ ) 字节的十进制，避免了计算和使用上的麻烦。
>
> —— 维基百科 - Gibibyte，<https://zh.wikipedia.org/wiki/Gibibyte>

K、M、G 都是 KB、MB、GB 的简称。由于混淆已经普遍化，Gigabyte 往往是指 Gibibyte，所以平时我们说的 1 兆存储就是 1M（MB），1G 存储就是 1GB）。我们的照片一般是 104KB、209KB、1.45MB、2.45MB、3.32MB 等等。

在说明其他储存单位的换算前，我们来看看两个标准：SI、IEC。

### 国际单位制（SI）

国际单位制(简称 SI，来自于法语 Système International d'Unités)，是世界上最普遍采用的标准度量系统。国际单位制以七个基本单位(米（m），千克（kg），秒（s），安培（A），开尔文（K），摩尔（mol），坎德拉（cd）)为基础，由此建立起一系列相互换算关系明确的"一致单位"。另有二十个基于十进制的词头，当加在单位名称或符号前的时候，可用于表达该单位的倍数或分数。

### 国际电工委员会（IEC）

国际电工委员会（IEC, International Electrotechnical Commission）成立于 1906 年，至今已有 90 多年的历史。它是世界上成立最早的国际性电工标准化机构，负责有关电气工程和电子工程领域中的国际标准化工作。

IEC 的宗旨是，促进电气、电子工程领域中标准化及有关问题的国际合作，增进国际间的相互了解。为实现这一目的，IEC 出版包括国际标准在内的各种出版物，并希望各成员在本国条件允许的情况下，在本国的标准化工作中使用这些标准。

目前 IEC 的工作领域已由单纯研究电气设备、电机的名词术语和功率等问题扩展到电子、电力、微电子及其应用、通讯、视听、机器人、信息技术、新型医疗器械和核仪表等电工技术的各个方面。IEC 标准的权威性是世界公认的，截止到 2008 年 12 月底，IEC 已制定了 5425 个国际标准。

不同标准下储存单位的次方单位 ( $2^{10}=1024$ )：

![字节的次方单位](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/KGarden/2023/byte-wiki.png)

## 比特率单位

在电信和计算领域，比特率（Bit rate）是指单位时间内传输送或处理的比特的数量。比特率经常在电信领域用作连接速度、传输速度、信息传输速率和数字带宽容量的同义词。

在数字多媒体领域，比特率是单位时间播放连续的媒体如压缩后的音频或视频的比特数量。在这个意义上讲，它相当于术语数字带宽消耗量，或吞吐量。

比特率规定使用"比特每秒"（bit/s 或 bps）为单位，经常和国际单位制词头关联在一起：

- bps(bit/s)，即 bit pro second（位每秒）；

- Kbps(Kbit/s)，即 Kilobit pro second(千位每秒)；

- Mbps(Mbit/s)，即 Milionbit pro second(百万位每秒)。

其中，bit 即比特，通常用 b（小写）表示，指一位二进制位，Milionbit=1000Kilobit=1000 000bit，所以 1Mbps=1000 000bps；

### bps 和 Bps

bps 是通常用来**衡量带宽**的单位，常见于表示数据机及网络通讯的传输速率，指每秒钟传输的二进制位数。例如 GigabitEthernet 端口。
```
5 minute input rate 38410000 bits/sec, 6344 packets/sec
382410000 bits/sec = 382.41Mbps
```

通常电脑(软件)上显示的上传下载速度（如下面的阿里云 OSSBrowser、Google Chrome 数据下载速度），则是指每秒种传输的字节数（Byte）通常用 B（大写）表示：MB 即百万字节也称兆字节；KB 即千字节；B 即字节。

- 1B=8b

- 1MB=1024KB=1024\*1024B

- 1Mbps=1000Kbps=1000/8KBps=125KBps

我们通常说的 1M 带宽即指 1Mbps，因此 1M 的带宽下载的速度一般不会超过 125KB 每秒。2M、3M 带宽的下载速度分别不会超过 250KB、375KB 每秒。

![download-byte-rate](https://slab-1251708715.cos.ap-guangzhou.myqcloud.com/KGarden/2023/download-byte-rate.png)

**数据传输速率的衡量单位 K 是十进制含义，但数据存储的 K 是 2 进制含义。**

1kbit/s 就是 1000bit/s，而 KB 是 1024 个字节,注意 KB(KByte) 和 kbit 的区别，另外，数据传输速率的单位是 bit/s 记作：bps 。

在实际应用中：

- 1kbps=1000bps

- 1Mbps=1000,000bps

- 1bps=0.000001bps

1Mbps 与 1m/s 是有区别的，1m/s 指的是 1024KB/s，而 1Mbps 指的是(1000/8)KB/s 也就是 125KB/S。

记住 K 和 k 是没区别的  ，区别在于 bps 属于位每秒的单位，而 m/s ,KB/s 这两个属于字节每秒的单位，一字节等于 8 位，即 1k=8b。

## 兆碱基

所以，在文章开头提到的 DNA 序列的 100 万个碱基数据（兆碱基）大致相当于计算机 1 兆的存储空间。其实也就是这么计算来得：

一个碱基就是一个英文字母，而一个英文字母是 1 个字节（Byte），所以 100 万个碱基就是 1000,000 Byte。按照 SI 国际单位的十进制标准，正好相当于 1 MB，如果按照 IEC 国际电工委员会的二进制标准，应该为：1000,000 / 1024 /1024 ≈ 0.95 MB，则是大致相当于计算机 1 兆的存储空间。

## 参考资料

- [Wiki: Gibibyte](https://zh.wikipedia.org/wiki/Gibibyte)，维基百科
- [Wiki：比特率](https://zh.wikipedia.org/wiki/%E6%AF%94%E7%89%B9%E7%8E%87)，维基百科
- 沙翁，《[什么是 Mbps、Kbps、bps、kb、mb 及其换算和区别](https://www.cnblogs.com/shaweng/p/3816985.html)》，博客园
- 大任 Dren，《[bit、Byte、bps、Bps、pps、Gbps 的单位详细说明及换算](https://blog.csdn.net/a9254778/article/details/8513086)》，CSDN-专业 IT 技术社区


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="20"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
