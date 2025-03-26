---
title: Python 3.6 不能产生 libpython3.6m.so 文件
number: 106
slug: discussions-106/
url: https://github.com/shenweiyan/Digital-Garden/discussions/106
date: 2025-03-21
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.5-Python']
---

在 Python-3.6.9 中测试 `Cheetah` 包的时候遇到了找不到 `libpython3.6m.so.1.0` 静态库，记录一下填坑。

<!-- more -->

```bash
$ python3 -c "import Cheetah._namemapper; print(Cheetah._namemapper.file)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: libpython3.6m.so.1.0: cannot open shared object file: No such file or directory
```

编译第三方静态库，在 `configure` 阶段需要增加 `--enable-shared CFLAGS=-fPIC` 参数！
```bash
./configure --prefix=/usr/local/python3 --enable-optimizations --enable-shared CFLAGS=-fPIC
```

在安装后，才会在 `/usr/local/python3/lib` 目录下产生 `libpython3.6m.so` 和 `libpython3.6m.so.1.0` 两个文件。如果不加上面的添加，产生的文件是 `libpython3.6m.a`。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="106"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
