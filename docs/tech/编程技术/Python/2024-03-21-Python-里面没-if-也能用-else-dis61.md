---
title: Python 里面没 if 也能用 else
number: 61
slug: discussions-61/
url: https://github.com/shenweiyan/Digital-Garden/discussions/61
date: 2024-03-21
authors: [shenweiyan]
categories: 
  - 1.2-编程
labels: ['翻译', '1.2.3-Python']
---

> 这是来自于 [Yang Zhou](https://twitter.com/YangZhou1993) 发表在 [Medium](https://medium.com/techtofreedom/beyond-if-else-leveraging-pythons-versatile-else-statements-9ac260dac102) 的一篇文章 《[Beyond If-Else: Leveraging Python’s Versatile “Else” Statements](https://medium.com/techtofreedom/beyond-if-else-leveraging-pythons-versatile-else-statements-9ac260dac102)》，作者觉得挺有意思的，拿过来简单翻译了一下在这里分享给大家。

<!-- more -->

当我们说到 "else"，必须先有 "if"。

这对于许多编程语言来说都是正确的，但对于 Python 来说却不然。

Python 的 else 语句比我们想象的更通用。

从循环后的 "else" 到 try- except 块后的 "else"，本文将探讨 else 语句鲜为人知的功能。

我们不一定需要在生产中使用这些技巧，尤其是当我们的同事还不知道它们时，但仅仅意识到它们的存在就可以让我们再次感受到 Python 的灵活性和多功能性。

## 1. While-Else 结构

在 Python 中， `while` 循环可以与 `else` 块配对。当且仅当循环正常完成时，`else` 块才会执行，这意味着它不会通过 `break` 语句终止。

换句话说，如果 `while` 循环被 `break` 终止，则 `else` 块将不会被执行。
```python
leaders = ["Elon", "Tim", "Warren"]
i = 0
while i < len(leaders):
    if leaders[i] == "Yang":
        print("Yang is a leader!")
        break
    i += 1
else:
    print("Not found Yang!")

# Not found Yang!
```

如上面的示例所示， `while` 循环迭代 `leaders` 列表，搜索领导者 "Yang"。不幸的是，"Yang" 并不是该名单中真正的领导者。所以 `break` 语句没有被执行。因此，`else` 语句下的代码就被执行了。

`else` 语句的这种意外用法使我们无需添加额外的标志变量来标记循环是否被破坏。这样我们的 Python 程序就可以精简一些了。

## 2. 带有 For 循环的 Else 语句

For 循环和 `while` 循环是编程的孪生兄弟。如果我们可以在 while 循环中利用 else 语句的多功能性，那么毫无疑问它可以用于 for 循环。

这个想法是完全相同的：      

> The "else" block only executes when there is no break in the for loop.     
> "else" 块仅在 for 循环中没有中断时执行。     

让我们用 for 循环重写前面的示例：
```python
leaders = ["Elon", "Tim", "Warren"]

for i in leaders:
    if i == "Yang":
        print("Yang is a leader!")
        break
else:
    print("Not found Yang!")

# Not found Yang!
```

代码更简洁了，不是吗？你能用其他编程语言做到这一点吗？

## 3. 使用 Else 语句进行异常处理

异常处理是编写健壮且无错误的代码的一项重要技术。

在 Python 中，整个异常处理代码块的结构应该如下：
```python
try:
    # Code that might raise an exception
except SomeException:
    # Code that runs if the try block raised 'SomeException'
else:
    # Code that runs if the try block did NOT raise any exceptions
finally:
    # Code that always runs no matter what, often for cleanup
```

除了 `try` 块之外，所有其他部分都是可选的。

当 `try` 块未引发异常时， `else` 块就会执行。这是放置仅当 `try` 块成功且无异常时才运行的代码的好地方。这对于阐明代码的意图并防止 `except` 块意外捕获非常有用。

例如，以下程序实现了一个非常简单的除法函数：
```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero.")
    else:
        print(f"Result is {result}")
    finally:
        print("Executing finally clause.")
```

如果没有遇到 `ZeroDivisionError`，结果如下：

```python
divide(2077, 1)
# Result is 2077.0
# Executing finally clause.
```

当然，如果满足定义的异常，则会打印相关的 `Error` 消息：
```python
divide(2077, 0)
# Error: Division by zero.
# Executing finally clause.
```

## 要点总结

在 Python 中，else 语句不一定位于 if 语句之后。

它还有三个额外但鲜为人知的用途：     

- while-else 循环     
- for-else 循环     
- 使用 else 块进行异常处理     

但是，我不建议您在生产中频繁应用它们，因为使用鲜为人知的功能可能会降低可读性并使您的同事感到困惑。但理解并随意应用它们会给你的同事留下深刻的印象，并巩固你作为 "Python 大师" 的地位。 😎

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="61"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
