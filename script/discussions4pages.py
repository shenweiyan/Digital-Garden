# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'shen@weiyan.tech'
__create__  = '2024-03-22'
__file__    = 'discussions4pages.py'
__license__ = '2024 All rights reserved.'
__doc__     = '把特定的 Discussions 转化成指定页面.'
#####################################################################

import optparse
from slugify import slugify
from pathlib import Path

def __main__():
    usage = "usage: python3 %prog [options] \n\nExample:\n"
    usage = usage + "    python3 %prog -i Discussions.txt -o docs"
    usage = usage + "\n\nDescription:\n"
    usage = usage + "    1. 把 Discussions 转成 mkdocs 特定页面，以 md 格式保存。\n"
    usage = usage + "    2. 特定页面主要包括 flinks/message/readme。"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-i", "--input", dest="input", help="Discussions input file.")
    parser.add_option("-o", "--outdir", dest="outdir", default='docs', help="Output directory (%default).")

    opts, args = parser.parse_args()
    inputFile  = opts.input
    outputDir  = opts.outdir

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

            if int(discussion_number) == 5:
                #友情链接
                flinks_md  = Path(outputDir).joinpath('flinks/index.md')
                flinks_dir = flinks_md.parent
                if not flinks_dir.exists():
                    flinks_dir.mkdir(parents=True, exist_ok=True)
                f_metadata = ( f'---\n'
                               f'title: 友情链接\n'
                               f'author: 沈维燕\n'
                               f'date: 2023-07-24\n'
                               f'updated: 2024-03-21\n'
                               f'---\n\n')
                with open(flinks_md, "w") as FMD:
                    FMD.write(f_metadata)
                    FMD.write(discussion_body)
                    FMD.write(comments)

            elif int(discussion_number) == 16:
                #留言
                message_md  = Path(outputDir).joinpath('message/index.md')
                message_dir = message_md.parent
                if not message_dir.exists():
                    message_dir.mkdir(parents=True, exist_ok=True)
                m_metadata = ( f'---\n'
                               f'title: 给作者留言\n'
                               f'author: 沈维燕\n'
                               f'date: 2023-07-24\n'
                               f'updated: 2024-03-21\n'
                               f'---\n\n')
                with open(message_md, "w") as MMD:
                    MMD.write(m_metadata)
                    MMD.write(discussion_body)
                    MMD.write(comments)
            
            elif int(discussion_number) == 4:
                #关于
                readme_md  = Path(outputDir).joinpath('readme/index.md')
                readme_dir = readme_md.parent
                if not readme_dir.exists():
                    readme_dir.mkdir(parents=True, exist_ok=True)
                r_metadata = ( f'---\n'
                               f'title: 作者与站点\n'
                               f'author: 沈维燕\n'
                               f'date: 2023-07-24\n'
                               f'updated: 2024-03-21\n'
                               f'---\n\n')
                with open(readme_md, "w") as RMD:
                    RMD.write(r_metadata)
                    RMD.write(discussion_body)
                    RMD.write(comments)
            else:
                continue

if __name__ == "__main__":
    __main__()
