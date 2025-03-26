---
title: Pandas 处理 Excel 常用方法技巧
number: 40
slug: discussions-40/
url: https://github.com/shenweiyan/Digital-Garden/discussions/40
date: 2023-12-26
authors: [shenweiyan]
categories: 
  - 1.2-编程
labels: ['1.2.3-Python']
---

在使用 Pandas 前需要学习了解一下 Series 和 DataFrame 的基本数据结构和索引的相关概念，之后就可以练习基本的 Excel操作。Pandas 读取一个 Excel 文件后会将其转化为 DataFrame 对象，每一列或行就是一个 Series 对象。这里我们看下如何对一个 excel 进行读写，以及 Sheet、行列、表头处理的一些常用技巧。

## 读取 Excel

如果您想读取 Excel 表格中的数据，可以使用 `read_excel()` 方法，其语法格式如下：

```
pd.read_excel(io, sheet_name=0, header=0, names=None, index_col=None,
              usecols=None, squeeze=False,dtype=None, engine=None,
              converters=None, true_values=None, false_values=None,
              skiprows=None, nrows=None, na_values=None, parse_dates=False,
              date_parser=None, thousands=None, comment=None, skipfooter=0,
              convert_float=True, **kwds)
```

下表对常用参数做了说明：

|参数名称|说明|
|:----|:----|
|io|表示 Excel 文件的存储路径。|
|sheet_name|要读取的工作表名称，默认0，即读取第一个工作表作为 DataFrame(一定要加`sheet_name=None`，才能读取出所有的 sheet，否则默认读取第一个 sheet)。|
|header|指定作为列名的行，默认0，即取第一行的值为列名；若数据不包含列名，则设定 header = None。若将其设置为 header=2，则表示将前两行作为多重索引。|
|names|一般适用于Excel缺少列名，或者需要重新定义列名的情况；names的长度必须等于Excel表格列的长度，否则会报错。|
|index_col|用做行索引的列，可以是工作表的列名称，如 index_col = '列名'，也可以是整数或者列表。|
|usecols|int或list类型，默认为None，表示需要读取所有列。|
|squeeze|boolean，默认为False，如果解析的数据只包含一列，则返回一个Series。|
|converters|规定每一列的数据类型。|
|skiprows|接受一个列表，表示跳过指定行数的数据，从头部第一行开始。|
|nrows|需要读取的行数。|
|skipfooter|接受一个列表，省略指定行数的数据，从尾部最后一行开始。|

示例如下所示：
```python
import pandas as pd

# 读取所有Sheet
df = pd.read_excel('example.xlsx', sheet_name=None)

# 读取第一个、第二个和名为"Sheet5"的工作表作为 DataFrame 的字典
df = pd.read_excel('example.xlsx', sheet_name=[0, 1, "Sheet5"])
```

## 获取行数和列数
```python
import pandas as pd
 
df = pd.read_excel('example.xlsx')
# 行索引
print(df.index)  
# RangeIndex(start=0, stop=3747, step=1)

# 输出元祖,分别为行数和列数,默认第一行是表头不算行数
print(df.shape) 
# (3747, 4)
```

## 获取表头
`read_excel` 默认是把 excel 的第一行当成表头。注意：如果 `read_excel` 的 `sheet_name=None`，读取的是所有 excel 的 sheet_name(key) 和 sheet_values(values) 组成的字典，`df.keys()` 的结果是所有 sheet_name，即名字(字典的键)。

### 获取第一个 sheet
这时候 `df.keys()` 和 `df.columns` 的结果是一样的，都是第一个 sheet 的表头。

```python
import pandas as pd
 
df = pd.read_excel('input.xlsx')
print(df.keys())
print('---------------')
print(df.columns)
```

### 获取所有 sheet
```python
import pandas as pd
 
# 参数为 None 代表读取所有 sheet
df = pd.read_excel('input.xlsx',sheet_name=None)

# 获取所有sheet名字, 如果read_excel参数不是None, 则df.keys()为表头
sheet_names = list(df.keys())
print(sheet_names)
```

## 参考资料
1. 老董，《[pandas获取excel的行数,列数,表头,sheet,前后行等数据](https://www.python66.com/pandasshujufenxi/268.html)》，[Python编程网](https://www.python66.com/)
2. 《[Pandas Excel读写操作详解](https://c.biancheng.net/pandas/excel.html)》，[C语言中文网](https://c.biancheng.net/)
3. 《[pandas.read_excel — pandas 2.1.4 documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)》，[pandas documentation — pandas 2.1.4 documentation](https://pandas.pydata.org/docs/index.html)

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="40"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
