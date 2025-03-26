---
title: 自定义 coding.net 静态网站域名
urlname: 2020-12-23-coding-net-custom-domain
author: 章鱼猫先生
date: 2020-12-23
updated: "2021-06-30 09:35:41"
---

![biying-1.jpg](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fnq5mx8M7EzOsYrrsrj0zReGYk8s.jpeg)

上一篇文章，我们介绍了怎么在 coding.net 部署个人的静态网站/博客站点，今天我们聊一下怎么来自定义已经部署好站点的域名地址。

基于腾讯云的自定义域名示例站点预览：
[Creative - Start Bootstrap Theme](https://startbootstrap-creative.bioitee.com/)

基于非腾讯云的自定义域名示例站点预览：
[Creative - Start Bootstrap Theme](https://startbootstrap-creative.ncbix.com/)

第一步，进入部署好站点的"静态网站"基本信息页面。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FjDmMQMIJIHOSdrSc97XG85pPo8k.png)
第二步，从"静态网站"基本信息页面进入"自定义域名"页面。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fu4_kUvMwvmj56j5oMwhRIi2fwJQ.png)
第三步，选择"新建域名"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiuqxZPeLxzEO43BYk_yf9kEPJVz.png)

新建域名，有两种情况，我们先介绍第一种情况：你的域名是在腾讯云注册的。

1.  新建自定义域名，点击“确定”后，会自动生成一个 CNAME 记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FojrEQWIg_NxjqOus-2bduWibTm-.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fi0m96DkTWoQSb9aSl9LESCKjMxo.png)

点击"审核中"，可以看到对应证书在腾讯云中的详细信息。等待约 10 分钟，"审核中"的状态会自动变更为"待验证"。再过约 10 分钟，对应证书状态将会由"待验证" 变更为"已签发"，即表示证书已经申请成功。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FobrZFIETt4YJF-z73ZQ8TuaWumy.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiPmpvCAN3eOXDOg269h3gv-RzEe.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgdXU-HM9vVYJNYAAkCl-_hBj-JP.png)

2.  添加 CNAME 记录。登陆腾讯云域名解析中心，添加一个 CNAME 记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fhjfa31LRogNzEOn7FkJhimovAv8.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqubIh0th2FviKeG_PX9LRRXLgFQ.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuHlUPMlzzCg2xuzLK2Z7Ibc1Tfq.png)

3.  配置证书。选择腾讯云产品里面的"CDN 与加速"→["内容分发网络"](https://console.cloud.tencent.com/cdn)，选择["证书管理"](https://console.cloud.tencent.com/cdn/certificate)→“配置证书”。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fs_bBXgQBI3nnl-C0N8N_oRbuxzN.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FmcKQ-XxScjl8axJZV27xOK6lruy.png)

4.  自定义域名完成，开启 https 访问。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiRJxCJruJsHb0fV7x9dos3ekgUd.png)

接下来，我们来看另外一种情况：新建非腾讯云注册的域名应该怎么处理。

1.  新建自定义域名，点击“确定”后，自动生成一个 CNAME 记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrCMLzW_Babu9BkGQoSdVA0aLHl9.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FoObuaMrHgp8OfgJLjmznz3C9-vB.png)

点击"审核中"，可以看到对应证书在腾讯云中的详细信息。添加非腾讯云注册的自定义域名，证书的状态不会自动由"审核中"更为"待验证" 和 "已签发"，需要一些额外的配置步骤。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FuC2tiwpPjMvn66hZ4pc81Zb8W3u.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrJ_ENsBn-KnRHdfKaEL0jaFRR0y.png)

2.  添加 CNAME 记录。登陆域名供应商的解析中心，添加一个 CNAME 记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fk-f75y5NKW7ZUIlgOHiyYiwloQJ.png)

3.  获取 DNS 验证记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtxD9d5UqnEQUomPga0M5-6gEz54.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FgxhVu6YfyXMCyfD4lABe2k3tgXN.png)

3.  在对应域名的供应商添加 TXT 解析记录。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fpk3aQMpDdOPSslMl1KkVxI7N7jm.png)
回到腾讯云"我的证书"，等待几分钟，证书状态将会由"待验证" 自动变更为"已签发"，即表示证书已经申请成功。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fm77PndnWqDkYZNZT4c1QSySnB8u.png)
coding.net 自定义域名的证书状态，在几分钟后，也会变更为"已颁发"。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FvS-g_0nM-t_KBA7Y9c1qAkTYnWa.png)

4.  配置证书。选择腾讯云产品里面的"CDN 与加速"→["内容分发网络"](https://console.cloud.tencent.com/cdn)，选择["证书管理"](https://console.cloud.tencent.com/cdn/certificate)→“配置证书”。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fs_bBXgQBI3nnl-C0N8N_oRbuxzN.png)
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FsMnKfHhGCLJokNHareNzaxIkq3Z.png)

5.  自定义域名完成，开启 https 访问。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fsu-odTNhLX_sABh1-Lbo6Kzq4F7.png)
