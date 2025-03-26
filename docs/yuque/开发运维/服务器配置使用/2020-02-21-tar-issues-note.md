---
title: tar 打包的一些注意问题
urlname: 2020-02-21-tar-issues-note
author: 章鱼猫先生
date: 2020-02-21
updated: "2021-06-25 10:54:07"
---

对于需要打包压缩的目录、文件，如果该目录或者文件不可读，将会引发 Permission denied 的错误。

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fmpxm2Evzh8ZNYFQ3QnjgoP3fNn2.png)

如果需要检查一个目录打包是否出现因为权限导致的异常，可以检查 log 日志是否存在  failure/Permission denied/error 等关键字。

```bash
tar zvcf 2014060503104SSQ.tar.gz 2014060503104SSQ 1>2014060503104SSQ.log 2>&1
grep -i failure 2014060503104SSQ.log
```

![comment.gif](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlMO8jnjfaW7QalT7nyPkxQ4d37w.gif)
