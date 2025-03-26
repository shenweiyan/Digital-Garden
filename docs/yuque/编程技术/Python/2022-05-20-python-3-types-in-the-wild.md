---
title: 失控的 Python3 类型
urlname: 2022-05-20-python-3-types-in-the-wild
author: 章鱼猫先生
date: 2022-05-20
updated: "2023-09-08 09:34:55"
---

> **作者 |** [James Somers](https://www.theatlantic.com/author/james-somers/) <br>
> **编译 |** [史提芬先森](https://www.yuque.com/shenweiyan/)<br>
> **原文 |** [Python 3 Types in the Wild](https://www.theatlantic.com/science/archive/2018/04/the-scientific-paper-is-obsolete/556676/)

<!-- -->

> Python used to be the kind of language you could pick up in a couple of days, but "used to be" was many years ago. Coming back to developing products with it after 11 years away, I've been a little overwhelmed by how many features have been added, and how hard it is to make sense of a modern code base without understanding all of them.

Python 曾经是一种你可以在几天内学会的语言，但 "曾经是" 是很多年前的事了。最近，我相隔 11 年后重新用这门语言开发产品时，有点不知所措，它添加了太多的新功能，如果你不了解所有这些新功能，理解现代 Python 代码将是多么困难的一件事。

> One of the biggest changes has been the addition of type annotations, which allow developers to say that a function returns `Dict[List[Set[FrozenSet[int]]], str]` (i.e., a dictionary that maps lists of sets of frozensets of integers onto strings). \[[RakAmnouykit2020](https://neverworkintheory.org/bib/#RakAmnouykit2020)] takes an empirical look at how programmers use these annotations, and turns up some surprising results. For one, the most common kind of type annotation is a user-defined type:

最大的变化之一是添加了类型注释，它允许开发人员通过一个函数返回 `Dict[List[Set[FrozenSet[int]]], str]`（即，一个映射一组整数的不可变集合列表到字符串的字典）。\[[RakAmnouykit2020](https://neverworkintheory.org/bib/#RakAmnouykit2020)] 对程序员如何使用这些注释进行了实证研究，并得出了一些令人惊讶的结果。一方面，最常见的类型注释是用户定义的类型。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FtZT3mwYmnkeFlO-MzJvRhFPgkLC.png)

> What's more interesting is that when the authors stripped annotations out of files and asked [PyType](https://google.github.io/pytype/) to infer them, it failed to do so in 77% of cases, which means that the user-written annotations were capturing information that automatic tools couldn't. On the other hand, [MyPy](http://mypy-lang.org/) found that only 15% of the 2,678 repositories examined were type-correct; this may be a result of MyPy being very conservative and producing false positives. More troubling are the disagreements between these different tools, but studies like these are exactly what we need to make those tools more consistent and more helpful.

更有趣的是，当作者从文件中剥离注释并要求 [PyType](https://google.github.io/pytype/) 推断它们时，在 77% 的情况下它未能这样做，这意味着用户编写的注释正在捕获自动工具无法捕获的信息。另一方面，[MyPy](http://mypy-lang.org/) 发现在检查的 2,678 个存储库中，只有 15% 是类型正确的；这可能是因为 MyPy 非常保守并产生误报。更令人不安的是这些不同工具之间的分歧，但像这样的研究正是我们需要使这些工具更加一致和更有帮助的。

\[[RakAmnouykit2020](https://neverworkintheory.org/bib/#RakAmnouykit2020)] Ingkarat Rak-amnouykit, Daniel McCrevan, Ana Milanova, Martin Hirzel, and Julian Dolby: Python 3 types in the wild: a tale of two type systems. In Proc. ISDL 2020, [doi:10.1145/3426422.3426981](https://doi.org/10.1145/3426422.3426981).

> Python 3 is a highly dynamic language, but it has introduced a syntax for expressing types with PEP484. This paper ex- plores how developers use these type annotations, the type system semantics provided by type checking and inference tools, and the performance of these tools. We evaluate the types and tools on a corpus of public GitHub repositories. We review MyPy and PyType, two canonical static type checking and inference tools, and their distinct approaches to type analysis. We then address three research questions: (i) How often and in what ways do developers use Python 3 types? (ii) Which type errors do developers make? (iii) How do type errors from different tools compare? Surprisingly, when developers use static types, the code rarely type-checks with either of the tools. MyPy and PyType exhibit false positives, due to their static nature, but also flag many useful errors in our corpus. Lastly, MyPy and PyType embody two distinct type systems, flagging different errors in many cases. Understanding the usage of Python types can help guide tool-builders and researchers. Understanding the performance of popular tools can help increase the adoption of static types and tools by practitioners, ultimately leading to more correct and more robust Python code.

Python 3 是一种高度动态的语言，但它引入了一种用 PEP484 表达类型的语法。本文探讨了开发人员如何使用这些类型注释、类型检查和推理工具提供的类型系统语义以及这些工具的性能。我们评估公共 GitHub 存储库语料库中的类型和工具。我们回顾了 MyPy 和 PyType 这两个规范的静态类型检查和推理工具，以及它们不同的类型分析方法。然后我们解决三个研究问题：（i）开发人员使用 Python 3 类型的频率和方式是什么？ (ii) 开发人员会犯哪些类型的错误？ (iii) 来自不同工具的类型错误如何比较？令人惊讶的是，当开发人员使用静态类型时，代码很少使用任何一种工具进行类型检查。 MyPy 和 PyType 由于它们的静态性质而表现出误报，但也会在我们的语料库中标记出许多有用的错误。最后，MyPy 和 PyType 体现了两个不同的类型系统，在许多情况下标记不同的错误。了解 Python 类型的使用有助于指导工具构建者和研究人员。了解流行工具的性能有助于增加从业者对静态类型和工具的采用，最终导致更正确和更健壮的 Python 代码。
