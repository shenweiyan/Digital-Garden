---
title: 如何卸载 python setup.py install 安装的包？
urlname: 2020-05-09-uninstall-setup-py
author: 章鱼猫先生
date: 2020-05-09
updated: "2021-06-25 10:44:56"
---

当我们半自动安装某些 python 包时，总是存在很多依赖关系的问题，而这些问题还是很难避免的，所以，当我们安装一个不确定的包的时候，最好提前收集一些相关资料，或者请教他人，同时最好把安装过程都记录下来。不然到时候想要卸载半天都卸不干净，即麻烦又白白浪费时间。

### 1. pip 方法

\*\*直接使用 \*\*`**pip uninstall package**` 即可。

```python
## 卸载 numpy
pip3 uninstall numpy
```

### 2. easy_install 方法

\*\*直接使用 \*\*`**easy_install -m lib**` 卸载。

```python
## 卸载 numpy
easy_install -m numpy
```

### 3. setup.py 方法

**安装前记录安装细节，以便日后卸载。**

```python
## 记录安装日志
# 安装numpy
python3 setup.py install --record install.log
## 卸载的时候使用日志文件install.log
cat install.log | xargs rm -rf
```

**与安装时创建这些文件相反，读取日志文件 install.log，删除安装时创建的所有文件和目录。**
\*\*

### 4. 卸载与 Pip 的包依赖项

当使用 `pip` 安装包时，它还会安装包所需的所有依赖项。 不幸的是，当您卸载原始包时，`pip` 不会卸载依赖项。 这里有几个不同的过程可以用来卸载依赖项。

1.  如果一个软件包是通过 pip 需求文件安装的（即`pip install requirements.txt`），那么这个软件包的依赖项可以通过下面的命令卸载：

```bash
pip uninstall requirements.txt
```

2.  如果没有使用`requirements.txt`，您可以使用`pip show`命令输出指定软件包的所有依赖项：

```bash
pip show <packagename>
```

例如，输入`pip show cryptography`，即可看到类似  `'Requires: six, cffi'`  的依赖提示：
![pip-show.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiXQc_h02lAJdYuTKQux-GJM__xl.png)

然后，可以使用 `pip uninstall`  命令来卸载这些依赖项。 但是，在卸载之前，应确保这些软件包不与其他现有软件包相关。

### 5. 资料链接

1.  activestate，[How To Uninstall Python Packages](https://www.activestate.com/resources/quick-reads/how-to-uninstall-python-packages/)，ActiveState
