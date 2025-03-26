---
title: 使用 Python 的 argparse 构建命令行界面
number: 75
slug: discussions-75/
url: https://github.com/shenweiyan/Digital-Garden/discussions/75
date: 2024-06-06
authors: [shenweiyan]
categories: 
  - 1.2-编程
labels: ['1.2.3-Python']
---

> 原文：[Build Command-Line Interfaces With Python's argparse](https://realpython.com/command-line-interfaces-python-argparse/)     


命令行应用在普通用户空间中可能并不常见，但它们存在于开发、数据科学、系统管理和许多其他操作中。每个命令行应用都需要一个用户友好的命令行界面 （CLI），以便你可以与应用本身进行交互。在 Python 中，您可以使用标准库中的 `argparse` 模块创建功能齐全的 CLI。

<!-- more -->

在本文中，你将了解如何：    

- 命令行界面入门；
- 在 Python 中组织和布局命令行应用项目；
- 使用 Python `argparse` 创建命令行界面（command-line interfaces）；
- 使用 `argparse` 一些强大的功能深度自定义您的 CLI；

若要充分利用本教程，应熟悉 Python 编程，包括面向对象编程、脚本开发和执行以及 Python 包和模块等概念。如果您熟悉与使用命令行或终端相关的一般概念和主题，这也将很有帮助。

## 了解命令行界面

自从计算机发明以来，人类一直需要并找到与这些机器交互和共享信息的方法。信息交换在人、计算机软件和硬件组件之间流动。其中任意两个元素之间的共享边界通常称为接口([interface](https://en.wikipedia.org/wiki/Interface_(computing)))。

在软件开发中，接口是给定软件的特殊部分，它允许计算机系统组件之间的交互。当涉及到人机交互和软件交互时，这个重要的组件被称为用户界面（[user interface](https://en.wikipedia.org/wiki/User_interface)）。

您会在编程中找到不同类型的用户界面。图形用户界面 （GUI） 可能是当今最常见的。但是，您还可以找到为其用户提供命令行界面 （CLI） 的应用和程序。在本教程中，你将了解 CLI 以及如何在 Python 中创建它们。

## 命令行界面 （CLI）

命令行界面允许您通过操作系统命令行、终端或控制台与应用程序或程序进行交互。

要了解命令行界面及其工作原理，请考虑此实际示例。假设您有一个名为 sample 包含三个示例文件的目录。如果您使用的是类 Unix 操作系统，例如 Linux 或 macOS，请继续在父目录中打开命令行窗口或终端，然后执行以下命令：    
```bash
$ ls sample/
hello.txt     lorem.md      realpython.md
```

Unix 的 `ls` 命令列出目标目录中包含的文件和子目录，该目录默认为当前工作目录。上面的命令调用没有显示有关 的内容 sample 的太多信息。它只在屏幕上显示文件名。

假设你想要获取有关目录及其内容的更丰富信息，那么你不需要寻找其他程序，因为 ls 命令有一个功能齐全的命令行界面，并且提供了一组有用的选项，可以用来定制命令的行为。

例如，继续执行带有 `-l` 选项的 `ls` 命令：    
```bash
$ ls -l sample/
total 24
-rw-r--r--@ 1 user  staff    83 Aug 17 22:15 hello.txt
-rw-r--r--@ 1 user  staff  2609 Aug 17 22:15 lorem.md
-rw-r--r--@ 1 user  staff   428 Aug 17 22:15 realpython.md
```

现在，`ls` 命令的输出完全不同了。该命令显示了有关 sample 目录中文件的更多信息，包括权限、所有者、组、日期和大小。它还显示了这些文件在你计算机磁盘上使用的总空间。

这种更丰富的输出结果是由于使用了 `-l` 选项，这是 Unix `ls` 命令行界面的一部分，它启用了详细的输出格式。

## 命令、参数、选项、参数和子命令

在本教程中，您将深入了解**命令**(commands)及其**子命令**(subcommands)，同时还会学习到**命令行参数**(command-line arguments)、**选项**(options)和**参数**(parameters)的相关知识。因此，建议您将这些术语纳入您的技术词汇库中。

- **命令(Command)**：在命令行或终端窗口中运行的程序或例程。通常，您可以通过其背后的程序(underlying program)或例程(routine)的名称来识别一个命令。     
- **参数(Argument)**：命令在执行其预期操作时所需或可选的信息片段。命令通常接受一个或多个参数，您可以在命令行中以空格分隔或逗号分隔的列表形式提供这些参数。     
- **选项(Option)**，也称为 **flag** 或 **switch**：一种可选的参数，用于修改命令的行为。选项通过特定的名称（如前一个示例中的 `-l`）传递给命令。     
- **参数(Parameter)**：一个选项用于执行其预期操作或动作时所使用的参数。     
- 子命令(Subcommand)**：一个预定义的名称，可以传递给应用程序来执行特定的操作。

参考上一节中的示例命令结构：
```bash
$ ls -l sample/
```

在这个例子中，您组合了命令行界面（CLI）的以下组件：    

- **ls**：命令的名称或应用的名称；
- **-l**：启用详细输出的选项(option)、开关(switch)或标志(flag)；    
- **sample**：为命令执行提供附加信息的参数(argument)；    

现在，让我们来看下面的命令结构，它展示了 Python 包管理器 `pip` 的命令行界面（CLI）：    
```bash
$ pip install -r requirements.txt
```

这是一个常见的 `pip` 命令结构，您可能之前已经见过。它允许您使用 `requirements.txt` 文件来给指定的 Python 项目安装依赖项。在这个例子中，您使用了以下命令行界面（CLI）组件：   
 
- **pip**：命令的名称；
- **install**：`pip` 的子命令(subcommand)名称；
- **-r**：`install` 子命令的选项(option)；
- **requirements.txt**：一个参数，特别是 `-r` 选项的参数。

现在您已经了解了命令行界面（CLI）是什么以及其主要部分或组件有哪些。接下来，是时候学习如何在 Python 中创建自己的 CLI 了。

## Python 中的 CLI 入门

Python 附带了一些工具，这些工具可帮助您为程序和应用程序编写命令行界面（CLI）。若您需要快速为小型程序构建一个简洁的 CLI，那么可以利用 [`sys`](https://docs.python.org/3/library/sys.html#module-sys) 模块中的 [`argv`](https://docs.python.org/3/library/sys.html#sys.argv) 属性。这个属性会自动存储您在命令行中传递给特定程序的参数。

### 使用 `sys.argv` 构建最小的 CLI

以使用 `argv` 创建最小命令行界面（CLI）为例，假设您需要编写一个小程序，该程序类似于 `ls` 命令，能够列出给定目录下的所有文件。在这种情况下，您可以编写如下代码：    
```python
# ls_argv.py

import sys
from pathlib import Path

if (args_count := len(sys.argv)) > 2:
    print(f"One argument expected, got {args_count - 1}")
    raise SystemExit(2)
elif args_count < 2:
    print("You must specify the target directory")
    raise SystemExit(2)

target_dir = Path(sys.argv[1])

if not target_dir.is_dir():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```

该程序通过手动处理命令行提供的参数来实现了一个简单的命令行界面（CLI），这些参数会自动存储在 `sys.argv` 中。`sys.argv` 的第一个元素始终是程序名称，第二个元素则是目标目录。由于应用程序不应接受超过一个目标目录，因此 `args_count` 不得超过 2。

在检查 `sys.argv` 的内容后，您创建一个`pathlib.Path`对象来存储目标目录的路径。如果该目录不存在，您将通知用户并退出程序。接下来的`for`循环将列出目录内容，每行一个条目。

如果从命令行运行该脚本，您将得到以下结果：    
```bash
$ python ls_argv.py sample/
hello.txt
lorem.md
realpython.md

$ python ls_argv.py
You must specify the target directory

$ python ls_argv.py sample/ other_dir/
One argument expected, got 2

$ python ls_argv.py non_existing/
The target directory doesn't exist
```

您的程序接受一个目录作为参数，并列出其内容。如果您运行命令时没有提供参数，您将收到一个错误消息。如果您运行命令时指定了超过一个目标目录，您同样会收到一个错误消息。如果尝试运行命令并指定一个不存在的目录，程序将输出另一个错误消息。

虽然您的程序运行正常，但对于更复杂的 CLI 应用程序来说，使用`sys.argv`属性手动解析命令行参数并不是一个可扩展的解决方案。如果您的应用需要接受更多的参数和选项，那么解析`sys.argv`将变得复杂且容易出错。您需要一个更好的解决方案，这就是 Python 中的`argparse`模块所提供的。

### 使用 `argparse` 创建 CLI

在 Python 中创建 CLI 应用程序的更便捷方法是使用标准库中的 [`argparse`](https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse) 模块。该模块首次在 Python 3.2 中随 [PEP-389](https://www.python.org/dev/peps/pep-0389/) 一同发布，是快速创建 Python CLI 应用程序的利器，无需安装如 Typer 或 Click 这样的第三方库。

`argparse` 模块是作为较旧的 [`getopt`](https://docs.python.org/3/library/getopt.html) 和 [`optparse`](https://docs.python.org/3/library/optparse.html) 模块的替代品而发布的，因为它们缺乏一些重要的功能。

Python 的 `argparse` 模块允许您：     

- 解析命令行**参数**(arguments)和**选项**(options)；
- 在一个单一选项中接受**可变数量的参数**(variable number of parameters)；
- 在 CLI 中提供子命令(subcommands)。

这些特性使 `argparse` 成为了一个强大的 CLI 框架，您在创建 CLI 应用程序时可以放心地依赖它。要使用 Python 的 `argparse`，您需要遵循以下四个简单的步骤：

1. 导入 `argparse`；
2. 通过实例化 [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) 创建**参数解析器**(argument parser)；
3. 使用 [`.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) 方法向解析器添加**参数**(arguments)和**选项**(options)；
4. 在解析器上调用 [`.parse_args()`](https://docs.python.org/3/library/argparse.html?highlight=argparse#argparse.ArgumentParser.parse_args) 以获取参数 [`Namespace`](https://docs.python.org/3/library/argparse.html#namespace)。

例如，您可以使用 `argparse` 来改进您的 `ls_argv.py` 脚本。现在，您可以创建一个名为 `ls.py` 的脚本，并编写以下代码：
```python
# ls.py v1

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
```

随着 `argparse` 的引入，您的代码发生了显著的变化。与之前的版本相比，最明显的不同是，用于检查用户提供的参数的条件语句已经消失了。这是因为 `argparse` 会自动为您检查参数的存在性。

在这个新的实现中，您首先导入 `argparse` 并创建一个参数解析器。要创建解析器，您可以使用 `ArgumentParser` 类。接下来，您定义一个名为 `path` 的参数，用于获取用户的目标目录。

接下来，您需要调用 `.parse_args()` 方法来解析输入参数，并获取一个包含所有用户参数的 `Namespace` 对象。请注意，现在 `args` 变量保存了一个 `Namespace` 对象，该对象具有从命令行收集的每个参数所对应的属性。

在这个例子中，您只有一个参数，名为 `path`。`Namespace` 对象允许您使用点表示法通过 `args` 来访问 `path`。其余的代码与第一个实现相同。

现在继续从命令行运行这个新脚本：
```bash
$ python ls.py sample/
lorem.md
realpython.md
hello.txt

$ python ls.py
usage: ls.py [-h] path
ls.py: error: the following arguments are required: path

$ python ls.py sample/ other_dir/
usage: ls.py [-h] path
ls.py: error: unrecognized arguments: other_dir/

$ python ls.py non_existing/
The target directory doesn't exist
```

第一个命令的输出与您的原始脚本 `ls_argv.py` 相同。而第二个命令的输出则与 `ls_argv.py` 中的输出大不相同。程序现在会显示一个使用说明消息，并发出错误提示，告诉您必须提供 `path` 参数。

在第三个命令中，您传递了两个目标目录，但应用程序并未为此做好准备。因此，它再次显示使用说明消息，并抛出一个错误，告知您潜在的问题。

最后，如果您运行脚本时传递了一个不存在的目录作为参数，那么您会收到一个错误，告知您目标目录不存在，因此程序无法执行其工作。

现在，您可以使用一个新的隐式特性。现在，您的程序接受一个可选的 `-h` 标志。不妨尝试一下：
```bash
$ python ls.py -h
usage: ls.py [-h] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
```

太棒了，现在您的程序会自动响应 `-h` 或 `--help` 标志，并为您显示带有使用说明的帮助消息。这真是一个很棒的特性，而且您只需在代码中引入 `argparse` 就能轻松获得！

经过这个快速介绍如何在 Python 中创建 CLI 应用后，您现在就可以深入研究 `argparse` 模块及其所有炫酷特性了。

## 使用 Python 的 argparse 创建 CLI

您可以使用 `argparse` 模块为您的应用程序和项目编写用户友好的命令行界面。该模块允许您定义应用程序所需的参数和选项。然后，`argparse` 将负责为您解析 `sys.argv` 的参数和选项。

`argparse` 的另一个酷炫特性是它可以自动为您的 CLI 应用程序生成使用说明和帮助消息。该模块还会在参数无效时发出错误提示，并具备更多功能。

在深入研究 `argparse` 之前，您需要知道该模块的文档可识别两种不同类型的命令行参数：     

- **位置参数**(Positional arguments)，您称为参数(arguments)；
- **可选参数**(Optional arguments)，即选项(options)、标志(flags)或开关(switches)。

在 `ls.py` 的示例中，`path` 是一个**位置参数**(positional argument)。这样的参数之所以被称为位置参数，是因为它在命令构造中的相对位置定义了其作用。

与位置参数不同，**可选参数**(Optional arguments)并不是必需的。它们允许你修改命令的行为。以 Unix 命令 `ls` 为例，`-l` 标志就是一个可选参数，它使得命令以详细模式显示输出。

在明确了这些概念之后，你就可以着手使用 Python 和 `argparse` 库来构建自己的命令行界面（CLI）应用程序了。

### 创建命令行参数解析器

命令行参数解析器是任何使用 `argparse` 的命令行界面（CLI）中最为关键的部分。你在命令行上提供的所有参数和选项都会经过这个解析器的处理，它会为你完成繁重的解析工作。

要使用 `argparse` 创建命令行参数解析器，您需要实例化 [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argumentparser-objects) 类：    
```python
>>> from argparse import ArgumentParser

>>> parser = ArgumentParser()
>>> parser
ArgumentParser(
    prog='',
    usage=None,
    description=None,
    formatter_class=<class 'argparse.HelpFormatter'>,
    conflict_handler='error',
    add_help=True
)
```

`ArgumentParser` 的构造函数接受多种不同的参数，你可以利用这些参数来微调你的 CLI 的多个特性。由于所有这些参数都是可选的，因此你可以通过不传入任何参数直接实例化 `ArgumentParser` 来创建一个最基本的解析器。

在本教程中，你将会更深入地了解 `ArgumentParser` 构造函数的参数，特别是在定制你的参数解析器的部分。目前，你可以开始使用 `argparse` 创建 CLI 的下一步了。这一步就是通过解析器对象来添加参数和选项。

### 添加参数和选项

要为 `argparse` 的 CLI 添加参数和选项，你将使用 `ArgumentParser` 实例的 [`.add_argument()`](https://docs.python.org/3/library/argparse.html#the-add-argument-method) 方法。请注意，这个方法对参数和选项都是通用的。在 `argparse` 的术语中，参数被称为**位置参数**(positional arguments)，而选项被称为**可选参数**(optional arguments)。

`.add_argument()` 方法的第一个参数决定了参数和选项之间的区别。这个参数被标识为[名称（name）或标志（flag）](https://docs.python.org/3/library/argparse.html?highlight=argparse#name-or-flags)。因此，如果你提供一个 name，那么你将定义一个参数(argument)。相反，如果你使用一个 flag，那么你将添加一个选项(option)。

你已经在使用 `argparse` 时处理过命令行参数了。现在，考虑以下你自定义的 `ls` 命令的增强版本，它向 CLI 添加了一个 `-l` 选项：     
```python
# ls.py v2

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
```

在这个例子中，第 11 行代码创建了一个带有 `-l` 和 `--long` 标志的选项。参数(arguments)和选项(options)在语法上的区别在于，选项名称以短横线 `-` 开头表示简写标志，以双短横线 `--` 开头表示完整标志。

请注意，在这个特定例子中，与 `-l` 或 `--long` 选项一同设置了一个 `action` 参数为 `"store_true"`，这意味着这个选项将存储一个布尔值。如果你在命令行上提供了这个选项，那么它的值将为 `True`。如果你省略了这个选项，那么它的值将为 `False`。在 "设置 Option 背后的 Action" 部分内容中，你将了解更多关于 `.add_argument()` 中的 `action` 参数的信息。

在第 21 行的 `build_output()` 函数中，当 `long` 为 `True` 时，它会返回一个详细的输出，否则返回一个简短的输出。详细的输出将包含目标目录中所有条目的大小、修改日期和名称。它使用了诸如 `Path.stat()` 这样的工具，以及带有自定义字符串格式的 `datetime.datetime` 对象。

继续在 `sample` 上执行您的程序，以检查 `-l` 选项如何工作：    
```bash
$ python ls.py -l sample/
  2609 Oct 28 14:07:04 lorem.md
   428 Oct 28 14:07:04 realpython.md
    83 Oct 28 14:07:04 hello.txt
```

新增的 `-l` 选项允许你生成并显示关于目标目录内容的更详细输出。

既然你已经知道了如何向 CLI 添加命令行参数和选项，接下来就是深入解析这些参数和选项的时候了。这将是你在接下来部分要探索的内容。

### 解析命令行参数和选项

解析命令行参数是基于 `argparse` 的任何 CLI 应用中的另一个重要步骤。一旦你解析了参数，你就可以根据它们的值来执行相应的操作。在你自定义的 `ls` 命令示例中，参数解析发生在包含 `args = parser.parse_args()` 语句的行上。

这个语句调用了 [`.parse_args()`](https://docs.python.org/3/library/argparse.html#the-parse-args-method) 方法，并将其返回值赋给 `args` 变量。`.parse_args()` 的返回值是一个 [`Namespace`](https://docs.python.org/3/library/argparse.html#the-namespace-object) 对象，其中包含了在命令行上提供的所有参数和选项以及它们对应的值。

考虑以下简单的示例：      
```python
>>> from argparse import ArgumentParser

>>> parser = ArgumentParser()

>>> parser.add_argument("site")
_StoreAction(...)

>>> parser.add_argument("-c", "--connect", action="store_true")
_StoreTrueAction(...)

>>> args = parser.parse_args(["Real Python", "-c"])
>>> args
Namespace(site='Real Python', connect=True)

>>> args.site
'Real Python'
>>> args.connect
True
```

通过在命令行参数解析器上调用 `.parse_args()` 方法得到的 `Namespace` 对象，你可以使用**点表示法**(dot notation)访问所有输入参数、选项以及它们对应的值。这样，你就可以检查输入参数和选项的列表，并根据用户在命令行上的选择来执行相应的操作。

你将在应用程序的主代码中使用这个 `Namespace` 对象。这与你在自定义 `ls` 命令示例中的 `for` 循环下所做的类似。

到目前为止，你已经了解了创建基于 `argparse` 的 CLI 的主要步骤。现在，你可以花些时间学习如何在 Python 中组织和构建 CLI 应用程序的基础知识了。

### 设置 CLI 应用程序的布局和构建系统

在继续你的 `argparse` 学习之旅之前，你应该暂停一下，思考如何组织你的代码和规划一个 CLI 项目。首先，你应该考虑以下几点：    

- 你可以创建模块和包来组织代码。
- 你可以将 Python 应用的核心包命名为应用本身的名字。
- 你会根据每个 Python 模块的具体内容或功能来命名它们。
- 如果你希望某个包可以直接执行，你可以在该 Python 包中添加一个 `__main__.py` 模块。

将这些想法铭记于心，并考虑到模型-视图-控制器（MVC）模式是一种有效组织应用程序结构的方法，你在规划 CLI 项目时可以采用以下目录结构：    
```
hello_cli/
│
├── hello_cli/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   └── model.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_model.py
│
├── pyproject.toml
├── README.md
└── requirements.txt
```

`hello_cli/` 目录是项目的根目录。在那里，您将放置以下文件：    

- pyproject.toml 是一个 TOML 文件，用于指定项目的构建系统(build system)和其他配置(configurations)。
- README.md 文件提供了项目的描述以及安装和运行应用程序的说明。为你的项目添加一个描述性且详细的 README.md 文件是编程中的最佳实践，特别是如果你打算将项目作为开源解决方案发布的话。
- requirements.txt 是一个常规文件，列出了项目的外部依赖项(external dependencies)。你将使用这个文件，结合 `pip` 的 `-r` 选项，来自动安装这些依赖项。

接下来是 `hello_cli/` 目录，它包含了应用的核心包，该包包含以下模块：    

- `__init__.py` 文件使得 `hello_cli/` 可以作为一个 Python 包被识别。
- `__main__.py` 文件提供了应用程序的**入口点脚本**(entry-point script)或可执行文件，这是启动程序的主要入口。
- `cli.py` 文件为应用提供了命令行界面。在此文件中的代码将扮演基于 MVC 架构中的视图-控制器角色。
- `model.py` 文件包含了支持应用主要功能的代码。这部分代码将在你的 MVC 布局中扮演模型角色。

你还需要一个 `tests/` 包，其中包含针对应用程序组件的单元测试文件。在这个具体的项目布局示例中，你有 `test_cli.py` 用于检查 CLI 功能的单元测试，以及 `test_model.py` 用于检查你的模型代码的单元测试。

`pyproject.toml` 文件允许你定义应用程序的构建系统以及许多其他常规配置。以下是一个如何为你的示例 hello_cli 项目填写此文件的简单示例：    
```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=64.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "hello_cli"
version = "0.0.1"
description = "My awesome Hello CLI application"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]

[project.scripts]
hello_cli = "hello_cli.__main__:main"
```

`[build-system]` 表头将 `setuptools` 设置为应用程序的构建系统，并指定 Python 需要安装哪些依赖项来构建应用程序。`[project]` 表头为你的应用提供了通用元数据。这些元数据在你想要将应用发布到 Python 包索引（PyPI）时非常有用。最后， `[project.scripts]` 表头定义了你的应用程序的入口点。

经过这次对 CLI 项目布局和构建的快速探索，你已经准备好继续学习 `argparse` 了，特别是如何自定义你的命令行参数解析器。

## 自定义你的命令行参数解析器

在前面的部分中，你已经学习了如何使用 Python 的 `argparse` 模块为你的程序或应用实现命令行接口的基础知识。同时，你也了解了如何按照 MVC 模式组织和规划 CLI 应用项目。

在接下来的部分中，你将更深入地探索 `argparse` 的许多其他强大功能。特别是，你将学习如何在 `ArgumentParser` 构造函数中使用一些最有用的参数，这将使你能够自定义 CLI 应用的一般行为。

### 调整程序的 Help 和 Usage 内容

向 CLI 应用程序的用户提供使用说明和帮助是一种最佳实践，可以通过出色的用户体验 (UX) 让用户更加愉快。在本节中，你将了解如何利用 `ArgumentParser` 的一些参数来微调 CLI 应用程序向用户显示帮助和使用消息的方式。你将学习如何：    
- 设置程序名称
- 定义程序的描述和结束消息
- 对参数和选项进行分组显示帮助

首先，你将开始设置你的程序名称，并指定该名称在帮助或使用说明消息中的显示方式。

#### 设置程序名称

默认情况下，`argparse` 会使用 `sys.argv` 中的第一个值来设置程序的名称。这个第一项包含你刚刚执行的 Python 文件的名称。这个文件名在使用说明消息中看起来会有些奇怪。

例如，继续使用 `-h` 选项运行自定义 `ls` 命令：
```bash
$ python ls.py -h
usage: ls.py [-h] [-l] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
  -l, --long
```

命令输出中的高亮行显示 `argparse` 正在使用文件名 `ls.py` 作为程序的名称。这看起来有些奇怪，因为在使用说明消息中，应用名称很少包含文件扩展名。

幸运的是，你可以使用 `prog` 参数来指定你的程序名称，就像下面的代码片段所示：     
```python
# ls.py v3

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(prog="ls")

# ...

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
```

使用 `prog` 参数，你可以指定将在使用说明消息中使用的程序名称。在这个例子中，你使用了字符串 "ls"。现在，继续运行你的应用：     
```bash
$ python ls.py -h
usage: ls [-h] [-l] path

positional arguments:
  path

options:
  -h, --help  show this help message and exit
  -l, --long
```

很好！这个输出的第一行中的使用说明消息显示程序名称为 `ls`，而不是 `ls.py`。

除了设置程序名称外，`argparse` 还允许你定义应用的描述和结尾信息。在接下来的部分中，你将学习如何进行这两方面的操作。

#### 定义程序的描述和结语消息

你还可以为你的应用定义一个通用的描述和一个结尾或结束语。为此，你将分别使用 `description` 和 `epilog` 参数。接下来，请更新 `ls.py` 文件，在 `ArgumentParser` 构造函数中添加以下内容：     
```python
# ls.py v4

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
)

# ...

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
```

在这次更新中，`description` 参数允许你为应用提供一个通用的描述。这个描述将显示在帮助消息的开头。`epilog` 参数则允许你定义一些文本作为应用的结尾或结束语。请注意，你可以使用旧式的字符串格式化操作符(`%`)将 `prog` 参数插入到 `epilog` 字符串中。    

如果再次运行该应用程序，你将得到如下输出：     
```bash
$ python ls.py -h
usage: ls [-h] [-l] path

List the content of a directory

positional arguments:
  path

options:
  -h, --help  show this help message and exit
  -l, --long

Thanks for using ls! :)
```

现在，输出会在使用消息之后显示描述消息，并在帮助文本末尾显示结语消息。

#### 显示参数和选项的分组帮助

**帮助分组**(Help groups)是 `argparse` 的另一个有趣特性。它们允许你将相关的命令和参数进行分组，从而帮助你组织应用的帮助消息。要创建这些帮助分组，你将使用 `ArgumentParser` 的 `.add_argument_group()` 方法。

作为一个例子，请考虑你自定义的 `ls` 命令的以下更新版本：     
```python
# ls.py v5
# ...

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
)

general = parser.add_argument_group("general output")
general.add_argument("path")

detailed = parser.add_argument_group("detailed output")
detailed.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

# ...

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))
```

在这次更新中，你为显示一般输出的参数和选项创建了一个帮助分组，并为显示详细输出的参数和选项创建了另一个分组。

如果你在命令行中使用 `-h` 选项运行应用程序，那么你将获得以下输出：   
```bash
python ls.py -h
usage: ls [-h] [-l] path

List the content of a directory

options:
  -h, --help  show this help message and exit

general output:
  path

detailed output:
  -l, --long

Thanks for using ls! :)
```

现在，你的应用的参数和选项在帮助消息中以描述性的标题进行了方便的分组。这个整洁的特性将帮助你为用户提供更多的上下文，并帮助他们更好地理解应用的工作原理。

### 为参数和选项提供全局设置

除了自定义使用说明和帮助消息外，`ArgumentParser` 还允许你对命令行界面（CLI）应用进行其他一些有趣的调整。这些调整包括：

- 为参数和选项定义全局默认值
- 从外部文件中加载参数和选项
- 允许或禁止选项缩写

有时，你可能需要为你的应用的参数和选项指定一个全局默认值。你可以通过在调用 `ArgumentParser` 构造函数时，将默认值传递给 `argument_default` 参数来实现这一点（注意：实际上 `ArgumentParser` 没有 `argument_default` 这个参数，但这里是为了说明可以全局设置默认值的概念。在实际应用中，你可能需要为每个参数单独设置默认值）。

这个特性可能并不常用，因为参数和选项通常具有不同的数据类型或意义，很难找到一个满足所有需求的值。

然而，`argument_default`(尽管 `ArgumentParser` 并没有直接提供这个参数，但这里是为了说明概念）的一个常见用例是当你想要避免将参数和选项添加到 `Namespace` 对象中。在这种情况下，你可以使用 `SUPPRESS` 常量作为默认值。这个默认值将确保只有命令行中提供的参数和选项才会被存储在 `arguments` 的 `Namespace` 中。

作为一个例子，请继续修改你的自定义 `ls` 命令，如下面的代码片段所示：     
```python
# ls.py v6

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
    argument_default=argparse.SUPPRESS,
)

# ...

for entry in target_dir.iterdir():
    try:
        long = args.long
    except AttributeError:
        long = False
    print(build_output(entry, long=long))
```

通过将 `SUPPRESS` 传递给 `ArgumentParser` 构造函数，你可以防止未提供的参数被存储在 `argparse.Namespace` 对象中。这就是为什么在调用 `build_output()` 之前，你需要检查 `-l` 或 `--long` 选项是否实际被传递了。否则，你的代码会因为 `args` 中不存在 `long` 属性而引发 `AttributeError` 错误。

`ArgumentParser` 的另一个酷炫功能是允许你从外部文件中加载参数值。当你有一个具有冗长或复杂的命令行结构的应用，并希望自动化加载参数值的过程时，这个功能就非常有用。

在这种情况下，你可以将参数值存储在一个外部文件中，并让你的程序从该文件中加载它们。为了尝试这个功能，请继续创建一个简单的命令行界面（CLI）应用，如下所示：     
```python
# fromfile.py

import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars="@")

parser.add_argument("one")
parser.add_argument("two")
parser.add_argument("three")

args = parser.parse_args()

print(args)
```

在这里，你向 `ArgumentParser` 的 `fromfile_prefix_chars` 参数传递 `@` 符号。然后，你创建了三个必须在命令行中提供的必需参数。

现在，假设你经常使用此应用程序，并且总是使用相同的一组参数值。为了简化和优化你的工作流程，你可以创建一个文件，其中包含所有必需参数的适当值，每个参数占一行，就像下面的 `args.txt` 文件一样：   
```
first
second
third
```

有了这个文件，您现在可以调用您的程序并指示它从 `args.txt` 文件加载值，如以下命令运行所示：    
```bash
$ python fromfile.py @args.txt
Namespace(one='first', two='second', three='third')
```

在此命令的输出中，你可以看到 `argparse` 已经读取了 `args.txt` 的内容，并顺序地将值分配给了 `fromfile.py` 程序的每个参数。所有参数及其值都已成功存储在 `Namespace` 对象中。

接受缩写选项名称的能力是 `argparse` 命令行界面（CLI）的另一个酷炫特性。这个特性是默认启用的，当你的程序具有长选项名称时非常有用。例如，考虑以下程序，它会在命令行下打印出你在 `--argument-with-a-long-name` 选项后指定的值：     
```python
# abbreviate.py

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--argument-with-a-long-name")

args = parser.parse_args()

print(args.argument_with_a_long_name)
```

这个程序会打印出你在 `--argument-with-a-long-name` 选项后传入的任何参数值。现在，请继续运行以下命令来检查 Python 的 `argparse` 模块如何处理这些缩写：    
```bash
$ python abbreviate.py --argument-with-a-long-name 42
42

$ python abbreviate.py --argument 42
42

$ python abbreviate.py --a 42
42
```

这些示例展示了如何缩写 `--argument-with-a-long-name` 选项的名称，而应用程序仍能正常工作。此功能是默认启用的。如果你希望禁用它并禁止缩写，那么可以在 `ArgumentParser` 中使用 `allow_abbrev` 参数：    
```python
# abbreviate.py

import argparse

parser = argparse.ArgumentParser(allow_abbrev=False)

parser.add_argument("--argument-with-a-long-name")

args = parser.parse_args()

print(args.argument_with_a_long_name)
```

将 `allow_abbrev` 设置为 `False` 会禁用命令行选项中的缩写。从这一点开始，你将需要为程序提供完整的选项名称才能正确工作。否则，你会收到一个错误：     
```bash
$ python abbreviate.py --argument-with-a-long-name 42
42

$ python abbreviate.py --argument 42
usage: abbreviate.py [-h] [--argument-with-a-long-name ...]
abbreviate.py: error: unrecognized arguments: --argument 42
```

第二个示例中的错误消息告诉你 `--argument` 选项没有被识别为有效的选项。要使用该选项，你需要提供它的完整名称。

## 微调你的命令行参数和选项

到目前为止，你已经学习了如何定制 `ArgumentParser` 类的多个功能，以改善你的命令行界面（CLI）的用户体验。现在，你知道了如何调整你的应用程序的使用说明和帮助信息，以及如何微调命令行参数和选项的一些全局方面。

在本节中，你将学习如何定制你的 CLI 的命令行参数和选项的其他几个功能。在这种情况下，你将使用 `.add_argument()` 方法及其一些最相关的参数，包括 `action`、`type`、`nargs`、`default`、`help` 等。     

### 设置 Option 背后的 Action

当你向命令行界面添加一个选项或标志时，通常需要定义如何将选项的值存储在调用 `.parse_args()` 后得到的 `Namespace` 对象中。为此，你会使用 `.add_argument()` 的 `action` 参数。`action` 参数的默认值为 "store"，意味着提供的选项值将原样存储在 `Namespace` 中。

`action` 参数可以接受几个可能的值。以下是这些可能值的列表及其含义：

<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="75"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
