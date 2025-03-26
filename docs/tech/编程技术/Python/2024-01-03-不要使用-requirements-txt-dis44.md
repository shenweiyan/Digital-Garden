---
title: 不要使用 requirements.txt
number: 44
slug: discussions-44/
url: https://github.com/shenweiyan/Digital-Garden/discussions/44
date: 2024-01-03
authors: [shenweiyan]
categories: 
  - 1.2-编程
labels: ['翻译', '1.2.3-Python']
---

> 作者：[Miikka Koskinen](https://miikka.me/)       
> 编译：[沈维燕](https://weiyan.cc)       
> 时间：原文发表于 2023-10-31       
> 原文：[Do not use requirements.txt](https://quanttype.net/posts/2023-10-31-do-not-use-requirements.txt.html)

你是否在用 Python 开发后端服务？我有两条建议：

- 不要使用 `pip` 和 `requirements.txt` 来管理 Python 依赖。它们缺乏一些应该内置的关键功能。
- 改用 [Poetry](https://python-poetry.org/)。

<!-- more -->

对我来说，第一条建议毋庸置疑。第二条则更具有暂时性：Poetry 是一个很好的选择，但并非唯一值得考虑的选择。

我将在下面进行解释。

请注意：如果你使用 Python 做其他事情而不是构建后端服务，那么本文中的建议可能并不适用于你。例如，如果你是[一个正在迁移 `setup.py` 的库开发者](https://gregoryszorc.com/blog/2023/10/30/my-user-experience-porting-off-setup.py/)，Poetry 并不明显是一个完美的选择。

## PIP 缺失的功能
[pip](https://pypi.org/project/pip/) 是一个工具，你可以用它从 [The Python Package Index (PyPI)](https://pypi.org/) 中安装软件包。它随 Python 一起安装，如果你是 Python 开发者，你可能已经多次使用过它。

管理 Python 项目依赖的传统方式是将它们列在一个名为 `requirements.txt` 的文件中，并使用 `pip install -r requirements.txt` 进行安装。然而，`pip` 被设计成一个软件包安装工具，而不是一个功能齐全的项目工作流工具。**pip 缺乏两个关键功能，即依赖的锁定文件 (dependency lockfiles) 和虚拟环境的自动管理(automatic management of virtualenvs)。**

## 依赖锁定文件
如果你希望在所有环境中（比如你的笔记本电脑、持续集成(CI)、生产环境）获得相同的行为，你需要锁定你的依赖项及其传递依赖的版本。你可以在 `requirements.txt` 中锁定你直接依赖的版本，例如，使用 `requests==2.31.0` 而不是 `requests`。

然而，pip 不会锁定传递依赖的版本。这可以通过使用 [pip-tools](https://github.com/jazzband/pip-tools) 来解决，将 `requirements.txt` 扩展成一个列出完整依赖图的文件，包括准确版本和构件的校验和(checksums for the artifacts)。pip-tools 很不错，但你需要自行设置并弄清楚它如何适应你的工作流程。

在其他编程语言中，这个功能是基本要求的 - 例如，npm 多年来一直有 `package-lock.json`，Cargo 也有 `Cargo.lock`。这个功能实在应该是一个项目工作流工具中的内置功能。

## 虚拟环境的自动管理

在 Python 中创建隔离环境的方式是使用 [virtualenvs](https://docs.python.org/3/library/venv.html)。传统上，你需要手动管理它们：通过一个 shell 命令创建一个（比如 `python -m venv example` 来创建名为 `example` 的虚拟环境），当你想要使用它时，需要用另一个 shell 命令来激活它。

这容易出错：忘记激活虚拟环境或者激活错误的虚拟环境是常见的错误。有一堆的解决方法。例如，你可以使用 [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)，在进入项目目录时让你的 shell 自动激活一个虚拟环境。[direnv](https://github.com/direnv/direnv/wiki/Python) 也可以做到。

同样，这也应该成为工作流工具中的一个内置功能。你不应该需要将多个工具粘合在一起。你不会听到 npm 或 Cargo 用户在虚拟环境上遇到问题的。

## Poetry 及其他选择

幸运的是，许多人已经意识到这些问题并努力解决它们。不太幸运的是，这导致了大量的 Python 项目工作流工具涌现。那么该如何选择呢？

我的建议是：**选择 [Poetry](https://python-poetry.org/docs/)**。它有锁定文件，有虚拟环境管理，而且很受欢迎且在积极开发中。根据我的经验，它并不完美，但是它起作用。

你也可以考虑 [Hatch](https://hatch.pypa.io/latest/) 或 [PDM](https://github.com/pdm-project/pdm)。它们与 Poetry 相似。我自己没有使用过它们，但我听说其他人成功地使用了它们。Hatch 似乎在库作者 (library authors) 中特别受欢迎。

如果你正在寻找一个更强大的选项，可以处理多个子项目，[Pants 构建系统](https://www.pantsbuild.org/)在 Python 支持方面做得很好。然而，它的学习曲线相对陡峭。

最后，如果你正在寻找一个类似 rustup 那样可以为你安装 Python 的解决方案，那么有 [rye](https://github.com/mitsuhiko/rye)。它是新的实验性工具，但也许它对你来说是正确的选择？

## 哪个是权威的工作流工具？

如果 Python 自带一个权威的项目工作流工具会很好。很多人希望 pip 成为这样一个工具。Node.js 自带 npm，Rust 自带 Cargo，那么为什么 Python 就不能有一个呢？为什么会有这么多竞争的选择呢？

据我所知，最大的障碍是，由于 Python 被广泛使用且用于许多不同的用例，制定一个通用的官方解决方案是困难且缓慢的（并且资金不足的）工作。另外，也不清楚 pip 是否适合这些功能。

如果你想了解更多信息，请阅读和听取这些与我不同、深度参与 Python 社区的人的意见：    
- Stargirl (Thea Flowers) on Fediverse：《[所以你想解决 Python 打包问题：一个实用指南](https://hachyderm.io/@stargirl/109697057391904145)》
- Pradyun Gedam：《[关于 Python 打包生态系统的思考](https://pradyunsg.me/blog/2023/01/21/thoughts-on-python-packaging/)》
- Talk Python to Me (podcast)：《[重新构想 Python 的打包工作流程](https://talkpython.fm/episodes/show/406/reimagining-pythons-packaging-workflows)》

## 关于 Clojure 

阅读我的博客的 Clojure 开发者可能会问：嘿，Clojure 怎么样？为什么我们没有锁定文件呢？这是一个很好的问题！

Clojure 社区通过始终使用明确的版本而不是版本范围来解决了这个问题，即使在库中也是如此。版本描述实际上支持范围，但没有人会使用它们。这样，只要版本解析算法稳定，你总是会得到相同的版本。

理论上，传递依赖项版本不匹配可能是一个问题，但 Clojure 支持一种编码风格，很少引起问题。

相比之下，在 Python 和 Node.js 社区，通常期望库列出其依赖项的版本范围，而软件包管理工具会抱怨版本不匹配的问题。

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="44"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
