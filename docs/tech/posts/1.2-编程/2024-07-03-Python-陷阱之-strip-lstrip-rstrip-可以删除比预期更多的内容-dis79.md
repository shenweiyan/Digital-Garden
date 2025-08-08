---
title: Python 陷阱之 strip、lstrip、rstrip 可以删除比预期更多的内容
number: 79
slug: discussions-79/
url: https://github.com/shenweiyan/Digital-Garden/discussions/79
date: 2024-07-03
authors: [shenweiyan]
categories: 
  - 编程
tags: ['python']
---

> 本文章内容来源于 《[Python Gotcha: strip, lstrip, rstrip can remove more than expected](https://andrewwegner.com/python-gotcha-strip-functions-unexpected-behavior.html)》，由作者翻译，仅供个人学习使用，如有内容侵犯了你的权益，请联系管理员删除相关内容。

## 介绍

作为一名软件工程师，你处理过不少脏字符串。删除用户输入中的前导或尾随空格可能是最常见的工作之一。

在 Python 中，这是通过 `.strip()` 、 `.lstrip()` 或 `.rstrip()` 函数完成的，通常如下所示：
```python
>>> "     Andrew Wegner     ".lower().strip()
'andrew wegner'
>>> "     Andrew Wegner     ".lower().lstrip()
'andrew wegner     '
>>> "     Andrew Wegner     ".lower().rstrip()
'     andrew wegner'
```

<!-- more -->

这非常简单，并且没有什么意外的事情发生。

## 陷阱

陷阱在于，这些函数中的每一个都可以接受一个要删除的字符列表。

```python
>>> "Andrew Wegner".lower().rstrip(" wegner")
'and'
```

发生了什么？为什么结果不只是：
```bash
'andrew'
```

## 解释

再次仔细阅读文档中的这行说明：

> A list of **characters**

不是字符串列表 (Not a list of strings.)。

> [str.rstrip([chars])](https://docs.python.org/3/library/stdtypes.html#str.rstrip)
> 
> Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or `None`, the chars argument defaults to removing whitespace. The chars argument is **not a suffix**; rather, **all combinations of its values are stripped**.
> 
> From [Built-in Types — Python 3.12.4 documentation](https://docs.python.org/3/library/stdtypes.html)

文档中已经明确并举例说明了这一行为及其含义。然而，对于新开发者来说，这是出乎意料的行为。毕竟，这些函数看起来都很直观。

我的示例执行以下操作：
- 接收要删除的字符列表。在本例中，删除的字符是我姓氏中的所有字母，加上空格： `wegner`。
- 将输入字符串中的所有字母都转成小写，结果为 `andrew wegner`。
- 从字符串的右侧开始，删除输入列表中的字符。遇到列表中不存在的字符时停止。在本例中，这意味着从右到左删除了 `rengew wer`，然后遇到 `andrew` 中的 `d` ， `rstrip` 函数停止。
- 返回剩余的字符串 `and`。

## 解决方法

Python 有两个可以正确删除**字符串**的函数 - [`.removesuffix()`](https://docs.python.org/3.10/library/stdtypes.html#str.removesuffix) 和 [`.removeprefix()`](https://docs.python.org/3.10/library/stdtypes.html#str.removeprefix) 分别用于删除右侧和左侧的字符串。

```python
>>> "Andrew Wegner".lower().removesuffix(" wegner")
'andrew'
```

这两个函数是作为 [**PEP-616**](https://peps.python.org/pep-0616/) 的一部分在 Python 3.9 中引入的。该 PEP 明确指出了用户对 `*strip()` 函数及其行为方式的困惑。引入这两个函数是为了实现所需的行为。

需要注意的是，这两个 `remove*` 函数最多只会删除字符串的一个实例。
```python
>>> "Andrew Wegner Wegner".lower().removesuffix(" wegner")
'andrew wegner'
```

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="79"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
