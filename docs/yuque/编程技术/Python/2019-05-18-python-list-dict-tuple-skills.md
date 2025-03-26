---
title: Python 的列表/字典/元组技巧
urlname: 2019-05-18-python-list-dict-tuple-skills
author: 章鱼猫先生
date: 2019-05-18
updated: "2023-01-06 11:01:54"
---

## 1. 字典排序

我们知道 Python 的内置 dictionary 数据类型是无序的，通过 key 来获取对应的 value。可是有时我们需要对 dictionary 中的 item 进行排序输出，可能根据 key，也可能根据 value 来排。到底有多少种方法可以实现对 dictionary 的内容进行排序输出呢？下面摘取了使用 `sorted`  函数实现对 dictionary 的内容进行排序输出一些精彩的解决办法。

### 1.1 按 key 值对字典排序

先基本介绍一下 `sorted`  函数，`sorted(iterable,key,reverse)`， `sorted`  一共有 `iterable`，`key`，`reverse` 这三个参数。

- 其中 `iterable`  表示可以迭代的对象，例如可以是 `dict.items()` ， `dict.keys()`  等。
- `key`  是一个函数，用来选取参与比较的元素。
- `reverse`  则是用来指定排序是倒序还是顺序， `reverse=true`  则是倒序， `reverse=false`  时则是顺序，默认时 `reverse=false` 。

要按 key 值对字典排序，则可以使用如下语句：

```bash
In [1]: d = {"lilee":25, "wangyuan":21, "liquan":32, "zhangsan":18, "lisi":28}

In [2]: sorted(d.keys())
Out[2]: ['lilee', 'liquan', 'lisi', 'wangyuan', 'zhangsan']

In [3]: sorted(d)
Out[3]: ['lilee', 'liquan', 'lisi', 'wangyuan', 'zhangsan']
```

直接使用 `sorted(d.keys())` 就能按 key 值对字典排序，这里是按照顺序对 key 值排序的，如果想按照倒序排序的话，则只要将 `reverse`  置为 `true`  即可。

### 1.2 按 value 值对字典排序

在 python2.4 前， `sorted()`  和 `list.sort()`  函数没有提供 `key`  参数，但是提供了 `cmp`  参数来让用户指定比较函数。此方法在其他语言中也普遍存在。

在 python2.x 中 `cmp`  参数指定的函数用来进行元素间的比较。此函数需要 2 个参数，然后返回负数表示小于，0 表示等于，正数表示大于。

在 python3.0 中， `cmp`  参数被彻底的移除了，从而简化和统一语言，减少了高级比较和 `__cmp__` 方法的冲突。

- cmp 参数（python3 中已经被移除，不推荐）

<!---->

    In [3]: sorted(d.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    Out[3]:
    [('liquan', 32),
     ('lisi', 28),
     ('lilee', 25),
     ('wangyuan', 21),
     ('zhangsan', 18)]

- key 参数（推荐）

<!---->

    In [4]: sorted(d.items(), key=lambda item:item[1], reverse=True)
    Out[4]:
    [('liquan', 32),
     ('lisi', 28),
     ('lilee', 25),
     ('wangyuan', 21),
     ('zhangsan', 18)]

1.  这里的 `d.items()` 实际上是将 d 转换为可迭代对象，迭代对象的元素为 `('liquan', 32)`，`('lisi', 28)`，`......`，`('zhangsan', 18)`。
2.  `items()`  方法将字典的元素转化为了元组，而这里 key 参数对应的 lambda 表达式的意思则是选取元组中的第二个元素作为比较参数（如果写作 `key=lambda item:item[0]` 的话则是选取第一个元素作为比较对象，也就是 key 值作为比较对象。`lambda x:y` 中 x 表示输出参数，y 表示 lambda 函数的返回值），所以采用这种方法可以对字典的 value 进行排序。
3.  注意排序后的返回值是一个 list，而原字典中的名值对被转换为了 list 中的元组。

## 2. 列表/元组排序

### 2.1 列表(元组)简单排序

从 Python 2.4 开始， `list.sort()`  和 `sorted()`  都添加了一个 `key`  参数，以指定要在进行比较之前在每个列表元素上调用的函数。

例如，这是一个不区分大小写的字符串比较：

```bash
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

### 2.2 对嵌套列表(元组)进行排序

网上有不少关于 Python 列表的排序，这里整理一下 Python 对嵌套列表（多重列表）排序的一些方法，以作备忘。

#### Key Functions

> The value of the `key` parameter should be a function that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record.
> `key`  参数的值应该是一个采用单个参数并返回用于排序目的键的函数。这种技术之所以快捷，是因为对于每个输入记录，键函数仅被调用一次。

一种常见的模式是使用对象的某些索引作为键来对复杂的对象进行排序。例如：

```python
>>> student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

具有命名属性的对象也可以使用相同的技术。例如：

```python
>>> class Student:
        def __init__(self, name, grade, age):
                self.name = name
                self.grade = grade
                self.age = age
        def __repr__(self):
                return repr((self.name, self.grade, self.age))
        def weighted_grade(self):
                return 'CBA'.index(self.grade) / float(self.age)

>>> student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
]
>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

#### Operator Module Functions

上面显示的键功能模式（key-function patterns）非常普遍，因此 Python 提供了便利功能，使访问器功能更容易，更快捷（make accessor functions easier and faster）。[operator module](http://docs.python.org/library/operator.html#module-operator)  模块内置了 `itemgetter` ， `attrgetter `  函数，并且从 Python 2.6 开始增加了 `methodcaller`  函数。

使用这些功能，以上示例变得更加简单和快捷。

```python
>>> from operator import itemgetter, attrgetter, methodcaller

>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

`operator` 模块还有可以进行多个级别排序的功能。例如，要按年级然后按年龄排序：

```python
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

在下面的示例中，使用了 `operator` 模块的第三个函数 `methodcaller`，其中在对每个学生进行排序之前显示了每个学生的加权成绩：

```python
>>> [(student.name, student.weighted_grade()) for student in student_objects]
[('john', 0.13333333333333333), ('jane', 0.08333333333333333), ('dave', 0.1)]

>>> sorted(student_objects, key=methodcaller('weighted_grade'))
[('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]
```

## 3. 升序和降序

`list.sort()` 和 `sorted()` 方法都接受带有布尔值的 `reverse` 参数。这用于标记降序排序。

例如，要以相反的年龄顺序获取学生数据：

```python
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

## 4. 排序稳定性和复杂排序

从 Python 2.2 开始，排序已经被保证是稳定的（sorts are guaranteed to be [stable](http://en.wikipedia.org/wiki/Sorting_algorithm#Stability)）。这意味着当多个记录具有相同的键时，将保留其原始顺序。

```python
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
```

请注意，"blue" 的两个记录如何保留其原始顺序，从而确保 ('blue', 1) 优先于 ('blue', 2)。

这个奇妙的属性使您可以通过一系列排序步骤来构建复杂的排序。例如，要按年级降序然后按年龄升序对学生数据进行排序，请先对年龄进行排序，然后再使用年级再次排序：

```python
>>> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
>>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

> The [Timsort](http://en.wikipedia.org/wiki/Timsort) algorithm used in Python does multiple sorts efficiently because it can take advantage of any ordering already present in a dataset.

> Python 中使用的 [Timsort](http://en.wikipedia.org/wiki/Timsort) 算法可以高效地执行多种排序，因为它可以利用数据集中已经存在的任何排序。

## 5. 多重列表(元组)取交集、并集

这是个人实际项目中的遇到的问题，例如，我们要获取某个基因或者序列的覆盖区域（并集），或者重叠区域（交集），通过多重列表(元组)取交集、并集的方法就可以快速解决这一问题。

```python
"""
获取两个区间的交集区域。
每个区间可以用元组 (start, end), 或者列表 [start, end] 的形式表示起始和终止位置。
> set1 = (1, 1347)
> set2 = (100, 416)
> intersection(set1, set2)
[100, 416]
"""
def intersection(interval_1, interval_2):
    start = max(interval_1[0], interval_2[0])
    end = min(interval_1[1], interval_2[1])
    if start < end:
        return [start, end]
    return None

"""
获取一个列表集的覆盖区域。
每个区间可以用元组 (start, end), 或者列表 [start, end] 的形式表示起始和终止位置。
> positions = [(0, 3), (7, 13), (6, 16)]
> get_union_section(positions)
[(0, 3), (6, 16)]
"""
def get_union_section(intervals):
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = [lower[0], upper_bound]  # replace by merged interval
            else:
                merged.append(higher)
    return merged

"""
获取两列表集的 overlap 交集区域,。
每个区间可以用元组 (start, end), 或者列表 [start, end] 的形式表示起始和终止位置。
> NM_0311 = [(1, 316), (516, 746), (218, 328)]
> XM_0173 = [(416, 3915), (1, 106), (512, 3915), (18, 116)]
> get_inersection(NM_0311, XM_0173)
[[1, 116], [516, 746]]
"""
def get_inersection(intervals1, intervals2):
    start = 0
    out_list = []
    ins1 = get_union_section(intervals1)
    ins2 = get_union_section(intervals2)
    for interval1 in ins1:
        for j in range(start, len(ins2)):
            inter_section = intersection(interval1, ins2[j])
            if inter_section:
                out_list += [inter_section]
    return out_list
```

## 6. 参考资料

1.  [Python Wiki：Sorting Mini-HOW TO](https://wiki.python.org/moin/HowTo/Sorting/)
2.  [How to sort a list of lists by a specific index of the inner list?](https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list)
