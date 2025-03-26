---
title: Python 日期和时间函数使用指南
urlname: 2019-09-21-how-to-use-datetime-in-python
author: 章鱼猫先生
date: 2019-09-21
updated: "2021-06-30 09:41:18"
---

作者： Deepanshu Bhalla     
编译： Steven Shen      
标题： [A Complete Guide to Date and Time Functions](https://www.listendata.com/2019/07/how-to-use-datetime-in-python.html)

---

在本教程中，我们将介绍 python 的 `datetime`  模块以及如何使用它来处理日期、时间，以及日期时间的格式化处理。 它包含各种实用示例，可帮助您通过 python 函数更加快捷高效进行日期和时间处理。 一般来说，日期类型列不容易操作，因为它带来很多挑战，例如处理闰年，一个月中的不同天数，不同的日期和时间格式，或者日期值是否以字符串（字符）格式存储等等。

### 1. datatime  模块

它是一个 python 模块，它提供了几个处理日期和时间的函数。它有以下四个类，在本文的后半部分将解释这些类是如何工作的。

1.  datetime
2.  date
3.  time
4.  timedelta

没有使用真实数据集经验的人可能没有遇到 date columns。在他们的印象中可能会觉得使用日期的机会很少而且不那么重要。为了启发他们，我列出了现实世界的例子，其中使用 `datetime`  模块的好处可能是非常明显的。

1.  选择 2018 年 6 月 30 日活跃的所有储蓄账户持有人，并检查他们的状态是否仍然有效；
2.  确定在过去 3 个月内提交超过 20 件索赔的被保险人；
3.  识别在过去 6 个月内进行多笔交易的客户；
4.  从时间戳值中提取日期。

#### 导入 `datetime`  模块

您可以使用以下命令导入或加载 `datetime`  模块：

```python
import datetime
```

您不需要安装此模块，因为它与 python 软件的安装捆绑在一起。

### 2. Dates

这里我们使用 `datetime.date`  类来表示日历日期值。 `today()`  方法用于获取当前日期。

```python
>>> import datetime
>>> datetime.date.today()
datetime.date(2019, 9, 10)
```

为了将其显示为正确的日历日期，我们可以将其包装在 `print()`  命令中。

```python
>>> print(datetime.date.today())
2019-09-10
```

#### 2.1 创建 Date 对象

日期类遵循如下所示的语法：`**date(year, month, day)**`

```python
>>> dt = datetime.date(2019, 10, 20)
>>> print(dt)
2019-10-20
```

#### 2.2 从 date 值中提取 day, month 和 year 

```python
>>> dt = datetime.date(2019, 10, 20)
>>> dt.day
20
>>> dt.month
10
>>> dt.year
2019
```

#### 2.3 自定义日期格式

您可以使用 `strftime`  方法定义日期格式来自定义日期格式。它将日期对象转换为字符串。

```python
>>> dt = datetime.date(2019, 10, 20)
>>> print(dt)
2019-10-20
>>> dt.strftime("%d-%m-%Y")
'20-10-2019'
```

`%d`  指的是一个月中的某一天。在 `20-10-2019`  中， `%d`  返回 20。
`%m`  指的是一年中的某个月。在 `20-10-2019`  中， `%m`  返回 10。
`%Y`  指的是年。字母 **'Y'** 是大写的。在 `20-10-2019`  中，`%Y` 返回 2019 年。
`%y`  指的是两位数格式的年份。在 `20-10-2019`  中，`%y` 返回 19。

**其他流行的格式代码：**
`%a` 返回工作日的前三个字母，如  `Sun` ；
`%A` 返回工作日的完整名称，如  `Sunday`；
`%b` 返回月份的前三个字母，如  `Oct` ；
`%B` 返回月份的完整名称，如  `October` ；

```python
>>> dt = datetime.date(2019, 10, 20)
>>> dt.strftime("%d/%m/%Y")
'20/10/2019'

>>> dt.strftime("%b %d, %Y")
'Oct 20, 2019'

>>> dt.strftime("%B %d, %Y")
'October 20, 2019'

>>> dt.strftime("%a %B %d, %Y")
'Sun October 20, 2019'

>>> dt.strftime("%A %B %d, %Y")
'Sunday October 20, 2019'

>>> dt.strftime("%A, %B %d, %Y")
'Sunday, October 20, 2019'
```

### 3. Time

时间值使用 `datetime.time`  类定义。它遵循如下所示的语法：
`_datetime.time(hour, minute, second, microseconds)_`

```python
>>> t = datetime.time(21, 2, 3)
>>> print(t)
21:02:03
```

#### 3.1 从时间值获取小时，分钟和秒

```python
>>> t = datetime.time(21, 2, 3)
>>> t.hour
21
>>> t.minute
2
>>> t.second
3
>>> t.microsecond
0
```

#### 3.2 将时间转换为 AM PM 格式

- `%I` 将 24 小时时间格式转换为 12 小时格式。
- `%p`  根据时间值返回 AM PM。
- `%H` 返回时间值的小时数。
- `%M` 返回时间值的分钟数。
- `%S` 返回时间值的秒数。

```python
>>> t = datetime.time(21, 2, 3)
>>> print(t)
21:02:03
>>> t.strftime("%I:%M %p")
'09:02 PM'
```

### 4. 同时处理 Dates 和 Time

`datetime`  库有另一个名为 `datetime.datetime`  的类，用于表示日期加时间。你可以称之为时间戳。 `now()`  或 `today()`  方法的 `datetime`  类用于提取当前日期和时间。

```python
>>> dt = datetime.datetime.now()
>>> print(dt)
2019-09-10 10:45:46.941261
```

`%c`  表示当地的日期和时间。`%X`  表示当地的时间。

```python
>>> dt = datetime.datetime.now()
>>> print(dt)
2019-09-10 10:45:46.941261

>>> dt.strftime("%c")
'Tue Sep 10 10:45:46 2019'

>>> dt.strftime("%A %B %d %X")
'Tuesday September 10 10:45:46'

>>> dt.strftime("%A %B %d %H:%M")
'Tuesday September 10 10:45'
```

#### 4.1 创建  datetime 对象

`datetime`  类的语法如下：
`_datetime(year, month, day, hour, minute, second, microsecond)_`

```python
>>> dt = datetime.datetime(2019, 7, 20, 10, 51, 0)
>>> print(dt)
2019-07-20 10:51:00

>>> dt.strftime('%d-%m-%Y %H-%M')
'20-07-2019 10-51'
```

#### 4.2 在 python 中将字符串转换为 datetime

```python
>>> from dateutil.parser import parse
>>> print(parse('March 01, 2019'))
2019-03-01 00:00:00
```

### 5. 如何获取当前的时间？

我们可以使用我们在上一节中使用的相同函数，并使用 `time()`  方法从返回值中提取时间。

```python
print(dt.time())
```

### 6. 如何获得当前周的天？

```python
>>> dt = datetime.datetime.now()
>>> print(dt)
2019-09-10 10:58:10.044233
>>> dt.strftime("%A %B %d %H:%M")
'Tuesday September 10 10:58'

>>> dt.isoweekday()
2
```

### 7. 计算未来或过去的日期

通过使用 `timedelta` ，您可以添加或减去天，周，小时，分钟，秒，微秒和毫秒。当您想要计算未来或过去的日期时，它非常有用。假设您要求识别过去 30 天内注册产品的所有客户。要解决此问题，您需要计算今天日期之前 30 天的日期。

```python
>>> dt = datetime.datetime.now()
>>> print(dt)
2019-09-10 11:01:54.959386

#30 days ahead
>>> delta = datetime.timedelta(days=30)
>>> print(dt + delta)
2019-10-10 11:01:54.959386

#30 days back
>>> print(dt - delta)
2019-08-11 11:01:54.959386

>>> delta = datetime.timedelta(days= 10, hours=3, minutes=30, seconds=30)
>>> print(dt + delta)
2019-09-20 14:32:24.959386

>>> delta = datetime.timedelta(weeks= 4, hours=3, minutes=30, seconds=30)
>>> print(dt + delta)
2019-10-08 14:32:24.959386
```

在 `timedelta`  中，缺少月份和年份选项，这意味着您无法按月（s）或年（s）计算未来日期增量。要完成此任务，我们可以使用 `dateutil`  包。让我们通过提交以下代码来导入此包：

```python
from dateutil.relativedelta import *
```

如果 `dateutil`  包未安装在您的系统上，请通过运行此命令 `pip install python-dateutil`  来安装它。

```python
>>> from dateutil.relativedelta import *
>>> dt = datetime.datetime(2019, 7, 20, 10, 51, 0)
>>> print(dt)
2019-07-20 10:51:00

#1 Month ahead
>>> print(dt + relativedelta(months=+1))
2019-08-20 10:51:00

#1 Month Back
>>> print(dt + relativedelta(months=-1))
2019-06-20 10:51:00
```

如果您想知道这个 `relativedelta(months = + 1)`  与 `datetime.timedelta(days = 30)`  有何不同，请观察两个命令的返回值（结果）。

由于 7 月有 31 天，提前 30 天使用此 `datetime.timedelta(days=30)` 返回 2019-08-19 10:51:00。 `relativedelta(months=+1)` 返回 2019-08-20 10:51:00 这是一个完整的 1 个月。

```python
#Next month, plus one week
>>> print(dt + relativedelta(months=+1, weeks=+1))
2019-08-27 10:51:00

#Next Year
>>> print(dt + relativedelta(years=+1))
2020-07-20 10:51:00
```

#### 7.1 考虑闰年

来自 `dateutil`  包的 `relativedelta`  方法在计算未来或过去日期时会同时考虑闰年的情况。2000 年是闰年，所以 2 月份有 29 天；但明年 2 月只有 28 天。

```python
>>> print(datetime.date(2000, 2, 29)+ relativedelta(years=+1))
2001-02-28
```

### 8. 两个日期之间的差异

假设您需要计算两个日期之间的天数。当您需要计算特定信息客户的使用期限时，即当他们开立账户（开始日期）和账户关闭时（结束日期）时，这是一个非常常见的数据问题陈述。

```python
>>> date1 = datetime.date(2020, 10, 25)
>>> date2 = datetime.date(2019, 12, 25)
>>> diff = date1- date2
>>> diff.days
305
```

#### 8.1 如何计算两个日期之间的月数

一种方法是计算天数，然后除以 30 得到月数。但它并不总是正确的，因为有些月份有 31 天。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrEdr7l2wr5CfFc3K9LEOAJzKn1y.png)

**它是怎么起作用的呢？**

- date1.month - date2.month returns -2
- 12\*(date1.year - date2.year) returns 12
- \-2 + 12 = 10

**注意：** 
假设您要计算 31/10/2018 和 01/11/2018 之间的月数，上面建议的方法将返回 1，因为两个日期位于月差异中。您可能会发现它不正确，因为两个日期之间的天数是 1。您是否知道 SAS 软件中的 INTCK 功能（默认设置）也会返回 1？ 返回 1 的用法是什么？ 当您需要将时间序列数据排序到箱中时，它非常有用。例如，每日数据可以累积到月度数据，以作为月度系列进行处理。如果您希望 0 作为月数，则可以使用上面“_Not full-proof Solution_”下面显示的代码。

### 9. 如何使用  pandas 数据框上的日期？

在现实世界中，我们通常从外部文件导入数据并将其存储在 pandas DataFrame 中。因此，了解我们如何在 DataFrame 上执行日期和时间操作非常重要。让我们创建一个示例数据框用于说明目的。

```python
>>> import pandas as pd
>>> df = pd.DataFrame({"A":["2019-01-01", "2019-05-03", "2019-07-03"],
                       "B":["2019-03-02", "2019-08-01", "2019-10-01"] })

# Let's check the column types.
>>> df.dtypes
A    object
B    object
dtype: object
```

可以看到，这里的 A 列和 B 列都是字符串（character values）。由于这些变量存储在字符串中，因此需要将列转换为 `datetime`  对象。

```python
>>> df['A'] = pd.to_datetime(df['A'])
>>> df['B'] = pd.to_datetime(df['B'])
>>> df.dtypes
A    datetime64[ns]
B    datetime64[ns]
dtype: object
```

为了计算在 pandas dataframe  上使用 A 列和 B 列的天数，您只需要对这两列进行计算。

```python
>>> df['C'] = df['B'] - df['A']
>>> df
           A          B       C
0 2019-01-01 2019-03-02 60 days
1 2019-05-03 2019-08-01 90 days
2 2019-07-03 2019-10-01 90 days
```

我们计算的 C 列采用日期时间格式。为了获得整数格式的差值，您可以提交以下命令。 `dt`  可以让 pandas 使用 `datetime`  方法。

```python
>>> df['C'] = (df['B'] - df['A']).dt.days
>>> df
           A          B   C
0 2019-01-01 2019-03-02  60
1 2019-05-03 2019-08-01  90
2 2019-07-03 2019-10-01  90
```

#### 9.1 获取过去 3 个月的日期

纯粹的 pythonic 方法是在 lambda 中定义函数，它在所有行上运行。

```python
>>> from dateutil.relativedelta import *
>>> df['D'] = df["B"].apply(lambda x: x - relativedelta(months=3))
>>> df
           A          B   C          D
0 2019-01-01 2019-03-02  60 2018-12-02
1 2019-05-03 2019-08-01  90 2019-05-01
2 2019-07-03 2019-10-01  90 2019-07-01
```

另一种方法是使用 `pandas`  包的内置函数 `DateOffset` ，它可以增加或减少天，月，年，周，小时，分钟，秒，微秒和纳秒。

```python
df['D1'] = df['B'] - pd.DateOffset(months=3)
```

#### 9.2 按日期过滤数据框

假设您只想选择列 B 的值大于 2019 年 5 月 1 日的那些行。

```python
df[df['B']>datetime.datetime(2019,5,1)]
```

#### 9.3 选择两个日期之间的数据

假设您要在两个日期之间从 pandas 数据框中选择行（比如 5 月 1 日到 9 月 30 日之间）。

```python
df[df.B.between(datetime.datetime(2019,5,1), datetime.datetime(2019,9,30))]

# OR
df[(df['B'] > datetime.datetime(2019,5,1)) & (df['B'] < datetime.datetime(2019,9,30))]
```

### 10. 如何使用不同的时区

很多时候我们在不同的时区有日期值，我们需要将它转换为我们当地的时区。手动解决这个问题并不容易。在 python 中，有一个名为 `pytz`  的库用于设置和转换时区。

您可以通过提交此命令找到所有时区。

```python
import pytz
pytz.all_timezones
```

要在特定时区设置日期时间对象（比如说亚洲/加尔各答），可以使用名为 `tzinfo`  的参数。

```python
dt = datetime.datetime(2019, 7, 20, 10, 10, 0, tzinfo=pytz.timezone('Asia/Kolkata'))
```

要将其转换为美国/亚利桑那州时区，我们可以使用名为 `astimezone`  的方法进行转换。如果你观察到转换后的日期已经改变，是因为这两个时区之间的差异超过 12 小时。

```python
>>> dt = datetime.datetime(2019, 7, 20, 10, 10, 0, tzinfo=pytz.timezone('Asia/Kolkata'))
>>> print(dt)
2019-07-20 10:10:00+05:53

>>> print(dt.astimezone(pytz.timezone('US/Arizona')))
2019-07-19 21:17:00-07:00
```
