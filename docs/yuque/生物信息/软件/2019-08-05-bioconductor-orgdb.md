---
title: Bioconductor org.Xx.eg.db 系列包
urlname: 2019-08-05-bioconductor-orgdb
author: 章鱼猫先生
date: 2019-08-05
updated: "2021-11-17 09:19:40"
---

在 bioconductor 的官网里面可以查找到 "**OrgDb**" 的包大约有 20 个，基本上跨越了我们生物信息分析中最常用的物种啦！

![Bioconductor-BiocViews.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FqHhM0AsWb5-p7OdLHYa0CH6i7c2.png)

完整链接：[`http://bioconductor.org/packages/release/BiocViews.html#___OrgDb`](http://bioconductor.org/packages/release/BiocViews.html#___OrgDb)

R 安装示例：

```r
BiocManager::install(c("org.Hs.eg.db", "org.Mm.eg.db", "org.Mmu.eg.db",
	  "org.Pf.plasmo.db", "org.Pt.eg.db", "org.Rn.eg.db",
    "org.Sc.sgd.db", "org.Ss.eg.db", "org.Xl.eg.db",
    "org.Gg.eg.db", "org.EcSakai.eg.db", "org.EcK12.eg.db",
    "org.Dr.eg.db", "org.Dm.eg.db", "org.Cf.eg.db",
    "org.Ce.eg.db", "org.Bt.eg.db", "org.At.tair.db",
    "org.Ag.eg.db"))
```

1.  人类：[org.Hs.eg.db](http://www.bioconductor.org/packages/release/data/annotation/html/org.Hs.eg.db.html)，Homo_sapiens
2.  小鼠：[Bioconductor - org.Mm.eg.db](http://www.bioconductor.org/packages/release/data/annotation/html/org.Mm.eg.db.html)，Mus_musculus
3.  大鼠：[org.Rn.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Rn.eg.db.html)，Rat
4.  酵母：[org.Sc.sgd.db](http://bioconductor.org/packages/release/data/annotation/html/org.Sc.sgd.db.html)，Yeast
5.  飞行类：[org.Dm.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Dm.eg.db.html)，Fly
6.  拟南芥：[org.At.tair.db](http://www.bioconductor.org/packages/release/data/annotation/html/org.At.tair.db.html) , Arabidopsis（Arabidopsis_thaliana）
7.  斑马鱼：[org.Dr.eg.db](http://www.bioconductor.org/packages/release/data/annotation/html/org.Dr.eg.db.html)，Zebrafish（Danio_rerio）
8.  蠕虫：[org.Ce.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Ce.eg.db.html)，Worm
9.  牛：[org.Bt.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Bt.eg.db.html)，Bovine
10. 鸡：[org.Gg.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Gg.eg.db.html)，Chicken
11. 犬类：[org.Cf.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Cf.eg.db.html)，Canine
12. 猪：[org.Ss.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Ss.eg.db.html)，Pig
13. 恒河猴：[org.Mmu.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Mmu.eg.db.html)，Rhesus
14. 大肠杆菌 K12 株：[org.EcK12.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.EcK12.eg.db.html)，E coli strain K12
15. 非洲爪蟾：[org.Xl.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Xl.eg.db.html)，Xenopus
16. 按蚊：[org.Ag.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Ag.eg.db.html)，Anopheles
17. 黑猩猩：[org.Pt.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.Pt.eg.db.html)，Chimp
18. 疟原虫：[org.Pf.plasmo.db](http://bioconductor.org/packages/release/data/annotation/html/org.Pf.plasmo.db.html)，Malaria
19. 酒井大肠杆菌：[org.EcSakai.eg.db](http://bioconductor.org/packages/release/data/annotation/html/org.EcSakai.eg.db.html)，E coli strain Sakai
20. 粘球菌 xanthus DK 1622：[org.Mxanthus.db](http://bioconductor.org/packages/release/data/annotation/html/org.Mxanthus.db.html)，Myxococcus xanthus DK 1622
