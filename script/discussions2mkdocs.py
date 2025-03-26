# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'shen@weiyan.tech'
__create__  = '2024-01-11'
__file__    = 'discussions2mkdocs.py'
__license__ = '2024 All rights reserved.'
__doc__     = 'Discussion to mkdocs markdown files.'
#####################################################################

import optparse
import yaml
from slugify import slugify
from pathlib import Path

def __main__():
    usage = "usage: python3 %prog [options] \n\nExample:\n"
    usage = usage + "    python3 %prog -i Discussions.txt -c nav.yml -o docs"
    usage = usage + "\n\nDescription:\n"
    usage = usage + "    1. 把 Discussions 转成 MKdocs 的文章，以 md 格式保存。\n"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-i", "--input", dest="input", help="Discussions input file.")
    parser.add_option("-c", "--cate", dest="cate", help="Categories yaml input file.")
    parser.add_option("-o", "--outdir", dest="outdir", default='docs', help="Output directory (%default).")

    opts, args = parser.parse_args()
    inputFile  = opts.input
    cateFile   = opts.cate
    outputDir  = opts.outdir

    cateDict = {}
    with open(cateFile, "r") as YF:
        cateDict = yaml.safe_load(YF)

    discussionsDict = {}
    # 打开文件并读取内容
    dictFile = open(inputFile, 'r')
    # 解析 txt 中的字典数据
    discussionsDict = eval(dictFile.read())
    dictFile.close()

    # 处理所有的 discussions
    if 'nodes' in discussionsDict.keys():
        discussionsList = discussionsDict['nodes']
        for discussion in discussionsList:
            if not discussion:
                print("Null discussion!")
                continue
            discussion_title        = discussion['title']
            discussion_number       = discussion['number']
            discussion_url          = discussion['url']
            discussion_createdAt    = discussion['createdAt']
            discussion_lastEditedAt = discussion['lastEditedAt'] if discussion['lastEditedAt'] else 'None'
            discussion_updatedAt    = discussion['updatedAt']
            discussion_body         = discussion['body']
            discussion_author       = discussion['author']['login']
            discussion_category     = discussion['category']['name']
            discussion_labels       = [label['name'] for label in discussion['labels']['nodes']] if discussion['labels']['nodes'] else []

            if discussion_category.startswith('2.'):
                continue
        
            slug_name   = f'discussions-{discussion_number}'
            create_date = discussion_createdAt[0:10]
            md_filename = f'{create_date}-{slugify(discussion_title, allow_unicode=True, lowercase=False)}-dis{discussion_number}.md'
            metadata    = ( f'---\n'
                            f'title: {discussion_title}\n'
                            f'number: {str(discussion_number)}\n'
                            f'slug: {slug_name}/\n'
                            f'url: {discussion_url}\n'
                            f'date: {discussion_createdAt[0:10]}\n'
                            f'authors: [{discussion_author}]\n'
                            f'categories: \n'
                            f'  - {discussion_category}\n'
                            f'labels: {discussion_labels}\n'
                            f'---\n\n')
            
            # 使用 giscus 加载评论
            comments = ( f'\n\n<script src="https://giscus.app/client.js"\n'
                         f'\tdata-repo="shenweiyan/Digital-Garden"\n'
                         f'\tdata-repo-id="R_kgDOKgxWlg"\n'
                         f'\tdata-mapping="number"\n'
                         f'\tdata-term="{discussion_number}"\n'
                         f'\tdata-reactions-enabled="1"\n'
                         f'\tdata-emit-metadata="0"\n'
                         f'\tdata-input-position="bottom"\n'
                         f'\tdata-theme="light"\n'
                         f'\tdata-lang="zh-CN"\n'
                         f'\tcrossorigin="anonymous"\n'
                         f'\tasync>\n'
                         f'</script>\n')

            # 处理输出结果
            savedPostDir = ""
            for label in discussion_labels:
                label = label.strip()
                if label in cateDict.keys():
                    savedPostDir = cateDict[label]
                if savedPostDir:
                    break

            if savedPostDir:
                savedPostDir = Path(outputDir).joinpath(savedPostDir)
                # 如目录存在则先删除目录下对应的 *-dis.md, 否则创建 Posts 保存目录
                if savedPostDir.exists():
                    for md in savedPostDir.glob(f'*-dis{discussion_number}.md'):
                        md.unlink()
                else:
                    Path(savedPostDir).mkdir(parents=True, exist_ok=True) #如果目录不存在,先创建博文保存目录

                # 保存输出结果
                savedPostFile = Path(savedPostDir).joinpath(md_filename)
                print(savedPostFile)
                with open(savedPostFile, "w") as MD:
                    MD.write(metadata)
                    MD.write(discussion_body)
                    MD.write(comments)
            else:
                continue

if __name__ == "__main__":
    __main__()
