---
title: 富集分析的几个区别
urlname: 2019-12-05-enrichment-analysis-differentiation
author: 章鱼猫先生
date: 2019-12-05
updated: "2023-07-25 02:40:09"
---

## 名词解释

### GO

GO 是 Gene Ontology 的缩写，是基因功能国际标准分类体系。它旨在建立一个适用于各种物种的，对基因和蛋白质功能进行限定和描述的，并能随着研究不断深入而更新的语言词汇标准。GO 数据库分别从**分子功能(Molecular Function)**、**生物过程(Biological Process) **及**细胞组成(Cellular Component) **对基因产物进行了标准化描述，即对基因产物进行了简单注释。

通过 **GO 富集分析**可以粗略了解差异基因富集在哪些生物学功能、途径或者细胞定位。

### Pathway

Pathway 指代谢通路，对差异基因进行 pathway 分析，可以**了解实验条件下显著改变的代谢通路**，在机制研究中显得尤为重要。

GO 分析好比是将基因分门别类放入一个个功能类群，而 pathway 则是将基因一个个具体放到代谢网络中的指定位置。

## 1. 什么是富集分析

基因富集分析是分析基因表达信息的一种方法，富集是指将基因按照先验知识，也就是基因组注释信息进行分类。

# 2. 富集分析原理是什么

## 3. 怎么做富集分析

基因富集分析需要我们提供某一类功能基因的集合用于背景，常用的注释数据库如：

- The Gene Ontology Consortium: 描述基因的层级关系
- Kyoto Encyclopedia of Genes and Genomes: 提供了 pathway 的数据库。

未完，待续....
