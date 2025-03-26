---
title: Linux shell 编程笔记
urlname: 2020-01-13-shell-coding
author: 章鱼猫先生
date: 2020-01-13
updated: "2023-08-01 01:00:12"
---

基础性的语法不啰嗦了，记录一下比较容易忘记的一些点。

## Shell 示例脚本

```bash
#!/bin/sh
START=$(date +'%Y-%m-%d %H:%M:%S');
echo "Start: $START" >/home/shenweiyan/log.txt

for i in `find /data/database/onekp/nucl-v2/samples/ -name "*.fa"`;
do
    dir=`dirname $i`;
    fa=`basename $i`;
    cd $dir; makeblastdb -in $fa -dbtype nucl;
    echo $i >>/data/database/onekp/nucl-v2/memo/log;
done
END=$(date);echo "End: $END" >>/home/shenweiyan/log.txt
```

## Shell 程序模板

```shell
#!/bin/bash
set -e
# 设置程序参数的缺省值，少用参数即可运行
# Default parameter
input=input.txt
output=output.txt
database=database.txt
execute='TRUE'
# 程序功能描述，每次必改程序名、版本、时间等；版本更新要记录清楚，一般可用-h/-?来显示这部分
# Function for script description and usage
usage()
{
cat <<EOF >&2
Usage:
-------------------------------------------------------------------------------
Filename:    template.sh
Revision:    1.0
Date:        2017/6/24
Author:      Yong-Xin Liu
Email:       yxliu@genetics.ac.cn
Website:     http://bailab.genetics.ac.cn/
Description: This script is solve parameter read and default
Notes:       Function of this script
-------------------------------------------------------------------------------
Copyright:   2017 (c) Yong-Xin Liu
License:     GPL
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
If any changes are made to this script, please mail me a copy of the changes
-------------------------------------------------------------------------------
Version 1.0 2017/6/24
# 输入输出文件格式和示例，非常有用，不知道格式怎么准备文件呀
# Input files: input.txt, can inclue many file
# 1. input.txt, design of expriment
SampleID    BarcodeSequence    group
WT.1    TAGCTT    WT
WT.2    GGCTAC    WT
WT.3    CGCGCG    WT
# 2. database.txt, annotation of gene
ID    description
AT3G48300    Transcript factor
# Output file
1. Annotated samples & DE genes
Samples    ID    description
Wt    AT3G48300    Transcript factor
2. Volcano plot: vol_otu_SampleAvsSampleB.pdf
# 参数描述，写清功能的缺省值
OPTIONS:
    -d database file, default database.txt
    -i input file, recommend must give
    -o output file or output directory, default output.txt
    -h/? show help of script
Example:
    template.sh -i input.txt -d database.txt -o result.txt
EOF
}
# 解释命令行参数，是不是很面熟，其实是调用了perl语言的getopts包，
# Analysis parameter
while getopts "d:h:i:o:" OPTION
do
    case $OPTION in
        d)
            database=$OPTARG
            ;;
        h)
            usage
            exit 1
            ;;
        i)
            input=$OPTARG
            ;;
        o)
            output=$OPTARG
            ;;
        ?)
            usage
            exit 1
            ;;
    esac
done
# for 循环批量调用程序，如批量绘制热图
# 有多种批量输入文件的方式，以下N种任选其一，其它用#注释掉
for i in a.txt b.txt n.txt; do # 文件不多，手动放在in后用空格分开
for i in `seq 1 9`; do # 文字名为数字顺序，用seq命令生成连续数据，引用命令需反引
for i in `ls data/*.txt`; do # 匹配某类文件作为输入
for i in `cat list.txt`; do # 使用文本原为输入列表
for i in `cat list.txt|cut -f 1`; do # 指定某列作为输入文件名
    plot_heatmap.sh -i data/${i} -o heatmap/${i}.pdf
done
```

将以上代码保存为 template.sh，然后根据实际需要调整。

## Shell 语法与知识

### if 基础语法

```bash
if [ command ]; then
   符合该条件执行的语句
elif [ command ]; then
   符合该条件执行的语句
else
   符合该条件执行的语句
fi
```

### 文件与目录判断

```bash
[ -b FILE ] 如果 FILE 存在且是一个块特殊文件则为真。
[ -c FILE ] 如果 FILE 存在且是一个字特殊文件则为真。
[ -d DIR ]  如果 FILE 存在且是一个目录则为真。
[ -e FILE ] 如果 FILE 存在则为真。
[ -f FILE ] 如果 FILE 存在且是一个普通文件则为真。
[ -g FILE ] 如果 FILE 存在且已经设置了 SGID 则为真。
[ -k FILE ] 如果 FILE 存在且已经设置了粘制位则为真。
[ -p FILE ] 如果 FILE 存在且是一个名字管道(F如果O)则为真。
[ -r FILE ] 如果 FILE 存在且是可读的则为真。
[ -s FILE ] 如果 FILE 存在且大小不为0则为真。
[ -t FD ]   如果文件描述符 FD 打开且指向一个终端则为真。
[ -u FILE ] 如果 FILE 存在且设置了SUID (set user ID)则为真。
[ -w FILE ] 如果 FILE 存在且是可写的则为真。
[ -x FILE ] 如果 FILE 存在且是可执行的则为真。
[ -O FILE ] 如果 FILE 存在且属有效用户ID则为真。
[ -G FILE ] 如果 FILE 存在且属有效用户组则为真。
[ -L FILE ] 如果 FILE 存在且是一个符号连接则为真。
[ -N FILE ] 如果 FILE 存在 and has been mod如果ied since it was last read则为真。
[ -S FILE ] 如果 FILE 存在且是一个套接字则为真。
[ FILE1 -nt FILE2 ] 如果 FILE1 has been changed more recently than FILE2, or 如果 FILE1 exists and FILE2 does not则为真。
[ FILE1 -ot FILE2 ] 如果 FILE1 比 FILE2 要老, 或者 FILE2 存在且 FILE1 不存在则为真。
[ FILE1 -ef FILE2 ] 如果 FILE1 和 FILE2 指向相同的设备和节点号则为真。

[ -o OPTIONNAME ] 如果 shell选项 “OPTIONNAME” 开启则为真。
[ -z STRING ] “STRING” 的长度为零则为真。
[ -n STRING ] or [ STRING ] “STRING” 的长度为非零 non-zero则为真。
[ STRING1 == STRING2 ] 如果2个字符串相同。 “=” may be used instead of “==” for strict POSIX compliance则为真。
[ STRING1 != STRING2 ] 如果字符串不相等则为真。
[ STRING1 < STRING2 ] 如果 “STRING1” sorts before “STRING2” lexicographically in the current locale则为真。
[ STRING1 > STRING2 ] 如果 “STRING1” sorts after “STRING2” lexicographically in the current locale则为真。
[ ARG1 OP ARG2 ] “OP” is one of -eq, -ne, -lt, -le, -gt or -ge. These arithmetic binary operators return true if “ARG1” is equal to, not equal to, less than, less than or equal to, greater than, or greater than or equal to “ARG2”, respectively. “ARG1” and “ARG2” are integers.
```

## Bash Shell 实战示例

一些常见的 bash shell 实战示例。

### 排除当前行及下一行的内容

```shell
sed '/关键字/,+1d' file >file2
```

### 批量重命名文件

- 把 1.xtx，2.txt，...，26.txt 分别重命名为 a.txt，b.txt，...，z.txt。

```bash
n=1;for i in {a..z}.txt;do echo mv ${n}.txt $i.txt;n=$((n+1));done
```

### 字符出现次数统计

- 统计文档中每个字符出现的次数。

```bash
# 本脚本需要两个参数，第一个参数是要统计的文件，第二个参数是输出统计结果的文件。
#!/bin/sh

for line in `cat $1`; do
    count=`echo $line|wc -m`
    echo $count $line

    i=1;
    while [ "$i" -lt "$count" ]; do
        one_word=`echo $line|cut -c$i`
        #echo $i $one_word
        echo "$one_word" >>temp
        ((i++))
    done
done

sort temp|uniq -c|sort -k1nr > $2

rm -f temp
```

### 切割字符串并打印分割后的值

```bash
awk -F ',' '{for(i=1;i<=NF;i++){print $i}}'` file.txt
```
