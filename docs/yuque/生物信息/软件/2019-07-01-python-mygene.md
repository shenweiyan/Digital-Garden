---
title: 使用 Python 中的 mygene 模块进行 ID 匹配
urlname: 2019-07-01-python-mygene
author: 章鱼猫先生
date: 2019-07-01
updated: "2023-08-24 11:42:50"
---

## 一、背景

对于每个生物信息分析的人来说，ID 匹配（映射）是一项非常常见，但又很繁琐的任务。假设，我们有一个来自上游分析的 gene symbol 或报告的 ID 列表，然后我们的下一个分析却需要使用基因 ID（例如 Entrez gene id 或 Ensembl gene id）。这时候，我们就希望将基因符号或报告的 ID 的列表转换为相应的基因 ID。

在开始介绍今天的主角 mygene 前，我们先来认识一下 **[MyGene.info](https://mygene.info/)**。

### MyGene.info

MyGene.info 是一个由 NIH(美国国立卫生研究院)/NIGMS 资助，用于提供简单易用的 REST Web 服务来查询/检索基因注释数据的 API。 MyGene.info 目前包含了 NCBI Entrez、Ensembl、Uniprot、UCSC 在内的 20 多个数据库，MyGene.info 会每周从这些数据库中进行数据更新。虽然 MyGene.info 中包含的各个数据源可能有数据使用限制，但 MyGene.info 本身的服务是免费的，其源码托管在：<https://github.com/biothings/mygene.info>。

MyGene.info 提供两种简单的 Web 服务：一种用于基因查询，另一种用于基因注释检索。两者都以 JSON 格式返回结果。截至 2019 年 3 月 6 日，MyGene.info 最新的 API 为 v3，相比 v1、v2，v3 新增了以下几点内容：

- Refseq accession number now contains version
- "ensembl", "refseq" and "accession" contains associations between RNA and protein
- Better mapping between Ensembl and Entrez gene IDs
- JSON structure slightly changed
- and more bugfixes

虽然 MyGene.info 是一个在线的 web 服务，但它同时也提供了基于 R 和 Python 的第三方模块，源码均在 GitHub 上开源：

- MyGene R Client：<https://github.com/biothings/mygene.R>
- MyGene Python Client：<https://github.com/biothings/mygene.py>

在这里，我们简单展示如何在 Python 中使用 **mygene**  模块来快速轻松地进行类似的 ID 匹配（映射）。**mygene**  本质上是一个方便的 Python 模块，通过这个模块我们可以访问 [MyGene.info](https://mygene.info/) 的基因查询 Web 服务。

## 二、mygene 安装与使用

### 1. 安装 mygene

在 Python 中 mygene 的安装非常简单，直接使用 pip 就可以安装。

```shell
pip install mygene
```

mygene 安装完成后，现在我们只需要导入它并实例化 mygeneinfo 类：

```python
import mygene

mg = mygene.MyGeneInfo()
```

### 2. 把 gene symbols 转换成 Entrez gene ids

假设 xli 是我们要转换为 entrez gene id 的 gene symbol 列表：

```python
xli = ['CCDC83',
       'MAST3',
       'FLOT1',
       'RPL11',
       'ZDHHC20',
       'LUC7L3',
       'SNORD49A',
       'CTSH',
       'ACOT8']
```

然后我们调用 `querymany`  方法，并告诉它我们输入的是 "符号(symbol)"，我们想要返回的是 "entrezgene"(Entrezgene ids)：

```python
>>> out = mg.querymany(xli, scopes='symbol', fields='entrezgene', species='human')
querying 1-9...done.
Finished.
>>> for i in out:
...     print(i)
...
{u'entrezgene': u'220047', u'query': u'CCDC83', u'_id': u'220047', u'_score': 87.6894}
{u'entrezgene': u'23031', u'query': u'MAST3', u'_id': u'23031', u'_score': 88.66032}
{u'entrezgene': u'10211', u'query': u'FLOT1', u'_id': u'10211', u'_score': 89.97141}
{u'entrezgene': u'6135', u'query': u'RPL11', u'_id': u'6135', u'_score': 82.54278}
{u'entrezgene': u'253832', u'query': u'ZDHHC20', u'_id': u'253832', u'_score': 87.46338}
{u'entrezgene': u'51747', u'query': u'LUC7L3', u'_id': u'51747', u'_score': 86.709984}
{u'entrezgene': u'26800', u'query': u'SNORD49A', u'_id': u'26800', u'_score': 107.5259}
{u'entrezgene': u'1512', u'query': u'CTSH', u'_id': u'1512', u'_score': 85.86504}
{u'entrezgene': u'10005', u'query': u'ACOT8', u'_id': u'10005', u'_score': 84.415535}
```

上面程序的匹配（映射）结果作为字典列表返回。每个字典都包含我们要求返回的字段，在本例中为 "entrezgene" 字段。 每个字典还返回匹配的查询词 "query" 和内部 id("**\_id**")，大部分时间与 "entrezgene" 相同（如果基因仅来自 Ensembl，则为 ensembl 基因 id）。

### 3. 把 gene symbols 转换成 Ensembl gene ids

如果我们只需要返回  Ensembl gene ids 时，只需要把  fields 参数值改成  'ensembl.gene' 即可：

```python
>>> out = mg.querymany(xli, scopes='symbol', fields='ensembl.gene', species='human')
querying 1-9...done.
Finished.

>>> for i in out:
...     print i
...
{u'ensembl': {u'gene': u'ENSG00000150676'}, u'query': u'CCDC83', u'_id': u'220047', u'_score': 87.86632}
{u'ensembl': {u'gene': u'ENSG00000099308'}, u'query': u'MAST3', u'_id': u'23031', u'_score': 88.42681}
{u'ensembl': [{u'gene': u'ENSG00000230143'}, {u'gene': u'ENSG00000236271'}, {u'gene': u'ENSG00000137312'}, {u'gene': u'ENSG00000206379'}, {u'gene': u'ENSG00000232280'}, {u'gene': u'ENSG00000206480'}, {u'gene': u'ENSG00000224740'}, {u'gene': u'ENSG00000223654'}], u'query': u'FLOT1', u'_id': u'10211', u'_score': 90.23538}
{u'ensembl': {u'gene': u'ENSG00000142676'}, u'query': u'RPL11', u'_id': u'6135', u'_score': 82.40764}
{u'ensembl': {u'gene': u'ENSG00000180776'}, u'query': u'ZDHHC20', u'_id': u'253832', u'_score': 87.6894}
{u'ensembl': {u'gene': u'ENSG00000108848'}, u'query': u'LUC7L3', u'_id': u'51747', u'_score': 86.635506}
{u'ensembl': {u'gene': u'ENSG00000277370'}, u'query': u'SNORD49A', u'_id': u'26800', u'_score': 107.55141}
{u'ensembl': {u'gene': u'ENSG00000103811'}, u'query': u'CTSH', u'_id': u'1512', u'_score': 85.88113}
{u'ensembl': {u'gene': u'ENSG00000101473'}, u'query': u'ACOT8', u'_id': u'10005', u'_score': 83.99602}
```

### 4. ID 与基因不匹配

如果输入 id 没有匹配的基因，mygene 将在屏幕输出中打印相关的通知。此查询条目返回的字典中将包含 "notfound" 值为 True 的关键字。

```python
>>> xli = ['CCDC83', 'MAST3', 'FLOT1', 'RPL11', 'Gm10494']
>>> out = mg.querymany(xli, scopes='symbol', fields='entrezgene', species='human')
querying 1-5...done.
Finished.
1 input query terms found no hit:
        [u'Gm10494']
Pass "returnall=True" to return complete lists of duplicate or missing query terms.

>>> for i in out:
...     print(i)
...
{u'entrezgene': u'220047', u'query': u'CCDC83', u'_id': u'220047', u'_score': 87.6894}
{u'entrezgene': u'23031', u'query': u'MAST3', u'_id': u'23031', u'_score': 88.89522}
{u'entrezgene': u'10211', u'query': u'FLOT1', u'_id': u'10211', u'_score': 89.862946}
{u'entrezgene': u'6135', u'query': u'RPL11', u'_id': u'6135', u'_score': 82.584694}
{u'query': u'Gm10494', u'notfound': True}
```

### 5. 输入 ID 不仅仅是符号

```
xli = ['DDX26B', 'CCDC83', 'MAST3', 'FLOT1', 'RPL11', 'Gm10494', '1007_s_at', 'AK125780']
```

上面的 xli 列表包含了 symbols, reporters 和 accession numbers，现在我们想要找回 Entrez gene id 和 uniprot id。 幸运的是，mygene 的参数范围，字段，物种都足够灵活，可以支持多个值，列表或逗号分隔的字符串：

```python
>>> mg.querymany(xli, scopes='symbol,reporter,accession', fields='entrezgene,uniprot', species='human')
querying 1-8...done.
Finished.
1 input query terms found dup hits:
        [('1007_s_at', 2)]
2 input query terms found no hit:
        ['DDX26B', 'Gm10494']
Pass "returnall=True" to return complete lists of duplicate or missing query terms.
[{'query': 'DDX26B', 'notfound': True},
 {'query': 'CCDC83', '_id': '220047', '_score': 88.13916, 'entrezgene': '220047', 'uniprot': {'Swiss-Prot': 'Q8IWF9', 'TrEMBL': 'H0YDV3'}},
 {'query': 'MAST3', '_id': '23031', '_score': 88.42681, 'entrezgene': '23031', 'uniprot': {'Swiss-Prot': 'O60307', 'TrEMBL': 'V9GYV0'}},
 {'query': 'FLOT1', '_id': '10211', '_score': 90.16039, 'entrezgene': '10211', 'uniprot': {'Swiss-Prot': 'O75955', 'TrEMBL': ['A2AB09', 'Q5ST80', 'A2ABJ5', 'A2AB10', 'A2AB12', 'A2AB13', 'A2AB11']}},
 {'query': 'RPL11', '_id': '6135', '_score': 82.44751, 'entrezgene': '6135', 'uniprot': {'Swiss-Prot': 'P62913', 'TrEMBL': ['Q5VVC8', 'Q5VVD0', 'A0A2R8Y447']}},
 {'query': 'Gm10494', 'notfound': True},
 {'query': '1007_s_at', '_id': '100616237', '_score': 12.442588, 'entrezgene': '100616237'},
 {'query': '1007_s_at', '_id': '780', '_score': 11.8290205, 'entrezgene': '780', 'uniprot': {'Swiss-Prot': 'Q08345', 'TrEMBL': ['A0A0A0MSX3', 'A0A024RCL1', 'A0A024RCQ1', 'A0A024RCJ0', 'Q96T61', 'Q96T62', 'A2ABM8', 'A2ABL2', 'A2ABL0', 'E7ERN0', 'A0A0G2JIA2', 'D6RB35', 'A0A0G2JI85', 'D6RAJ3', 'A0A0G2JHK4', 'A0A0G2JJA0', 'H0YAH6', 'A0A140T972', 'E7EUD5', 'E7EXB0', 'E7EPN2', 'E7ETI3', 'E7EVT1', 'E7EVW6', 'A0A0G2JNZ7', 'H0Y717', 'E7ESR9', 'D6R9C4', 'E7EQ23', 'E7EUP7', 'E7EQ30', 'E7EPH4', 'H0Y9F4', 'E7EN94', 'D6RBU7', 'D6RGW5', 'D6RB82', 'E7ETX3', 'E7EX99', 'E7ERI6', 'E7ES06', 'E7ENJ2']}},
 {'query': 'AK125780', '_id': '2978', '_score': 10.087812, 'entrezgene': '2978', 'uniprot': {'Swiss-Prot': 'P43080', 'TrEMBL': ['A6PVH5', 'B2R9P6', 'A0A0A0MTF5']}}
]
```

### 6. ID 匹配多个基因

从上一个结果中，你可能已经注意到查询词 "1007_s_at" 与两个基因匹配。在这种情况下，我们将从输出中收到通知，返回的结果将包括两个匹配的基因。

通过传递"returnall = True"，我们将从返回的结果中获得重复或缺少的查询条目以及匹配的输出：

```python
>>> mg.querymany(xli, scopes='symbol,reporter,accession', fields='entrezgene,uniprot', species='human', returnall=True)
querying 1-8...done.
Finished.
1 input query terms found dup hits:
        [('1007_s_at', 2)]
2 input query terms found no hit:
        ['DDX26B', 'Gm10494']
{'out': [{'query': 'DDX26B', 'notfound': True},
         {'query': 'CCDC83', '_id': '220047', '_score': 88.13916, 'entrezgene': '220047', 'uniprot': {'Swiss-Prot': 'Q8IWF9', 'TrEMBL': 'H0YDV3'}},
         {'query': 'MAST3', '_id': '23031', '_score': 88.42681, 'entrezgene': '23031', 'uniprot': {'Swiss-Prot': 'O60307', 'TrEMBL': 'V9GYV0'}},
         {'query': 'FLOT1', '_id': '10211', '_score': 90.20853, 'entrezgene': '10211', 'uniprot': {'Swiss-Prot': 'O75955', 'TrEMBL': ['A2AB09', 'Q5ST80', 'A2ABJ5', 'A2AB10', 'A2AB12', 'A2AB13', 'A2AB11']}},
         {'query': 'RPL11', '_id': '6135', '_score': 82.584694, 'entrezgene': '6135', 'uniprot': {'Swiss-Prot': 'P62913', 'TrEMBL': ['Q5VVC8', 'Q5VVD0', 'A0A2R8Y447']}},
         {'query': 'Gm10494', 'notfound': True},
         {'query': '1007_s_at', '_id': '100616237', '_score': 12.392551, 'entrezgene': '100616237'},
         {'query': '1007_s_at', '_id': '780', '_score': 11.8290205, 'entrezgene': '780', 'uniprot': {'Swiss-Prot': 'Q08345', 'TrEMBL': ['A0A0A0MSX3', 'A0A024RCL1', 'A0A024RCQ1', 'A0A024RCJ0', 'Q96T61', 'Q96T62', 'A2ABM8', 'A2ABL2', 'A2ABL0', 'E7ERN0', 'A0A0G2JIA2', 'D6RB35', 'A0A0G2JI85', 'D6RAJ3', 'A0A0G2JHK4', 'A0A0G2JJA0', 'H0YAH6', 'A0A140T972', 'E7EUD5', 'E7EXB0', 'E7EPN2', 'E7ETI3', 'E7EVT1', 'E7EVW6', 'A0A0G2JNZ7', 'H0Y717', 'E7ESR9', 'D6R9C4', 'E7EQ23', 'E7EUP7', 'E7EQ30', 'E7EPH4', 'H0Y9F4', 'E7EN94', 'D6RBU7', 'D6RGW5', 'D6RB82', 'E7ETX3', 'E7EX99', 'E7ERI6', 'E7ES06', 'E7ENJ2']}},
         {'query': 'AK125780', '_id': '2978', '_score': 10.106351, 'entrezgene': '2978', 'uniprot': {'Swiss-Prot': 'P43080', 'TrEMBL': ['A6PVH5', 'B2R9P6', 'A0A0A0MTF5']}}
        ],
 'dup': [('1007_s_at', 2)],
 'missing': ['DDX26B', 'Gm10494']
}
```

上面代码返回的结果包含了用于匹配输出的列表 "out"，用于缺少查询项（列表）的 "missing"，以及用于具有多个匹配（包括匹配数）查询项的 "dup"。

根据 mygene 的说法，mygene 可以支持大批量的列表 ID 转换。如传递一个大于 1000 ids 的 id 列表（即上面的 xli），mygene 将一次批量映射 1000 个 ID，然后将所有结果连接起来。因此，从用户端来看，它与传递较短列表完全相同。同时我们不必担心 mygene 后端服务器的饱和。

mygene 是一款强大的基因 ID 匹配转换模块，以 MyGene.info 为后台也可以有更多的玩法，感兴趣的可以参考 MyGene.info 的官方文档：<http://docs.mygene.info/en/latest/index.html>，也欢迎留言交流。
