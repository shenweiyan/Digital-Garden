---
title: Python Excel 操作 | xlrd+xlwt 模块笔记
urlname: 2020-02-18-xlrd-xlwt-notes
author: 章鱼猫先生
date: 2020-02-18
updated: "2022-04-19 16:52:09"
---

Python 的 pandas 模块使用 **xlrd** 作为读取 excel 文件的默认引擎。但是，**xlrd** 在其最新版本（从 2.0.1 及后面版本）中删除了对 xls 文件以外的任何文件的支持。

> xlsx files are made up of a zip file wrapping an xml file.
>
> Both xml and zip have well documented security issues, which xlrd was not doing a good job of handling. In particular, it appeared that defusedxml and xlrd did not work on Python 3.9, which lead people to uninstall defusedxml as a solution, which is absolutely insane, but then so is sticking with xlrd 1.2 when you could move to openpyxl.

从官方的[邮件](https://groups.google.com/g/python-excel/c/IRa8IWq_4zk/m/Af8-hrRnAgAJ)中，说的应该是 xlsx 本身是由一个 zip 文件和 xml 的头文件构成的，但是 xml 和 zip 都有详细记录的安全问题，特别是，**defusedxml** 和 **xlrd** 似乎在 Python 3.9 上不起作用，这导致人们卸载 **defusedxml** 作为解决方案，这绝对是疯了，但是，当然了，您也可以转移到 **openpyxl**，或者仍然坚持使用 xlrd 1.2。

```bash
$ conda search xlrd
Loading channels: done
# Name                       Version           Build  Channel
xlrd                           1.0.0          py27_0  conda-forge
xlrd                           1.0.0          py27_1  conda-forge
xlrd                           1.0.0          py35_0  conda-forge
xlrd                           1.0.0          py35_1  conda-forge
xlrd                           1.0.0          py36_0  conda-forge
xlrd                           1.0.0          py36_1  conda-forge
xlrd                           1.1.0          py27_1  pkgs/main
xlrd                           1.1.0  py27ha77178f_1  pkgs/main
xlrd                           1.1.0          py35_1  pkgs/main
xlrd                           1.1.0  py35h45a0a2a_1  pkgs/main
xlrd                           1.1.0          py36_1  pkgs/main
xlrd                           1.1.0  py36h1db9f0c_1  pkgs/main
xlrd                           1.1.0          py37_1  pkgs/main
xlrd                           1.1.0            py_2  conda-forge
xlrd                           1.2.0          py27_0  pkgs/main
xlrd                           1.2.0          py36_0  pkgs/main
xlrd                           1.2.0          py37_0  pkgs/main
xlrd                           1.2.0            py_0  conda-forge
xlrd                           1.2.0            py_0  pkgs/main
xlrd                           1.2.0    pyh9f0ad1d_1  conda-forge
xlrd                           2.0.1    pyhd3eb1b0_0  pkgs/main
xlrd                           2.0.1    pyhd8ed1ab_3  conda-forge
```

上面的问题将导致您在使用 pandas 调用 xlsx excel 上的 read_excel 函数时收到一个错误，即不再支持 xlsx filetype。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fg6HK5M3KsF5KE0SMNROvn1g9PHc.png)
为了解决这个问题，你可以：

1.  安装 [openpyxl](https://openpyxl.readthedocs.io/en/stable/) 模块：这是另一个仍然支持 xlsx 格式的 excel 处理包。
2.  在 pandas 中把默认的 engine 由原来的 xlrd 替换成 openpyxl。

```bash
# Install openyxl
pip install openpyxl

# set engine parameter to "openpyxl"
pd.read_excel(path, engine = 'openpyxl')
```

下面重点介绍 Python 读写 Excel 需要导入的 xlrd(读)，xlwd（写）模块的一些常用操作。

# 1. xlrd 模块

## 1.1 Excel 文件处理

- 打开 excel 文件

```python
import xlrd
excel = xlrd.open_workbook("data.xlsx")
```

- 获取并操作  sheet 工作表

```python
sheet_names = excel.sheet_names()        # 返回book中所有工作表的名字, ['Sheet1', 'Sheet2', 'Sheet3']
excel.sheet_loaded(sheet_name or indx)   # 检查某个sheet是否导入完毕

# 以下三个函数都会返回一个 xlrd.sheet.Sheet() 对象
sheet = excel.sheet_by_index(0)        # 通过索引获取，例如打开第一个 sheet 表格
sheet = excel.sheet_by_name("sheet1")  # 通过名称获取，如读取 sheet1 表单
sheet = excel.sheets()[0]              # 通过索引顺序获取

sheet.row_values(0) #获取第一行的数据
sheet.col_values(0) #获取第一列的数据
sheet.nrows         #获取总共的行数
sheet.ncols         #获取总共的列数
```

- 遍历所有行

```python
for i in range(0, sheet.nrows):
    row_list = sheet.row_values(i) # 每一行的数据在row_list 数组里
```

## 1.2 日期处理

`**xldate_as_tuple**`和`**xldate_as_datetime**`第二个参数有两种取值，0 或者 1：

- **0** 是以 **1900-01-01** 为基准的日期；
- **1** 是以 **1904-01-01** 为基准的日期。

```python
import datetime
from xlrd import xldate_as_datetime, xldate_as_tuple

xldate_as_datetime(43346.0, 0)
# datetime.datetime(2018, 9, 3, 0, 0)

xldate_as_tuple(43346.0, 0)
# (2018, 9, 3, 0, 0, 0)

xldate_as_datetime(43346.0, 0).strftime('%Y/%m/%d %H:%M:%S')
# '2018/09/03 00:00:00'

# 时间比较
xldate_as_datetime(43346.0, 0) < datetime.datetime(2019, 9, 3, 0, 0)
# True

```

## 1.3 编码处理

一些编译异常的处理示例。

```bash
# xlrd 中 sheet0.row_values(n) 的每个元素都是 unicode;
# Python 中如果执行 str+unicode 拼接会出现 UnicodeDecodeError 错误.
geneid = str(line[2]) if isinstance(line[2], float) else line[2].encode("utf-8")
```

# 2. xlwt 模块

## 2.1  创建 Book 工作簿(即 excel 工作簿)

```python
import xlwt
workbook = xlwt.Workbook(encoding = 'utf-8')	# 创建一个workbook并设置编码形式
```

## 2.2  添加 sheet 工作表

```python
worksheet = workbook.add_sheet('My Worksheet')  # 创建一个worksheet
```

## 2.3  向工作表中添加数据并保存

```python
worksheet.write(1,0, label = 'this is test') # 参数对应行, 列, 值

workbook.save('save_excel.xls')  # 保存
```

## 2.4 设置宽度

xlwt 中列宽的值表示方法：默认字体 0 的 1/256 为衡量单位。
xlwt 创建时使用的默认宽度为 2960，既 11 个字符 0 的宽度，所以我们在设置列宽时可以用如下方法：
width = 256 \* 20，其中 256 为衡量单位，20 表示 20 个字符宽度。

参考：<https://www.cnblogs.com/landhu/p/4978705.html>
