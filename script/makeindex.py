# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'weiyanshum@gmail.com'
__create__  = '2023-07-20'
__file__    = 'makeindex.py'
__license__ = '2023 All rights reserved.'
__doc__     = 'Automatic index.md detection for each path.'
#####################################################################

import os,sys,optparse,datetime

dirname, filename = os.path.split(os.path.abspath(__file__))
sys.path.append(dirname)

if sys.version_info < (3, 0):
    sys.exit('请使用 Python 3.6+ 执行本程序！')

if len(sys.argv) == 1:
    os.system("python3 %s -h " % (sys.argv[0]))
    sys.exit()

def __main__():
    usage = "usage: python3 %prog [options] \n\nExample:\n"
    usage = usage + "    python3 %prog -d docs"
    usage = usage + "\n\nDescription:\n"
    usage = usage + "    1. 自动检测每个目录是否存在 md 结尾的文件，如果没有，自动生成 index.md。\n"
    usage = usage + "    3. -d 默认 docs。"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-d", "--dir", dest="dir", default="docs", help="输入指定的目录。")
    parser.add_option("-r", "--run", dest="run", action="store_true", default=False, help="执行缺失 index.md 生成(默认不开启)。")

    opts, args = parser.parse_args()
    docdir     = opts.dir.strip()
    mkindex    = opts.run

    #获取当前时间
    nowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    subdirs = [os.path.join(root, dir) for root, dirs, files in os.walk(docdir) for dir in dirs]
    for each_dir in subdirs:
        md_file_list = [file for file in os.listdir(each_dir) if file.endswith(".md")]
        if len(md_file_list) == 0:
            if mkindex:
                with open (os.path.join(each_dir, "index.md"), "w") as IN:
                    IN.write("本文件于 %s 自动生成！" % nowTime)
                    print("Success Create " + os.path.join(each_dir, "index.md !"))
            else:
                print(os.path.join(each_dir, "index.md"))

if __name__ == "__main__":
    __main__()
