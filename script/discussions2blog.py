# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

######################################################################
__author__  = 'shen@weiyan.tech'
__create__  = '2024-01-10'
__file__    = 'discussion2blog.py'
__license__ = '2024 All rights reserved.'
__doc__     = 'Discussion to mkdocs blog.'
#####################################################################

import optparse
from slugify import slugify
from pathlib import Path

def __main__():
    usage = "usage: python3 %prog [options] \n\nExample:\n"
    usage = usage + "    python3 %prog -i Discussions.txt -o docs"
    usage = usage + "\n\nDescription:\n"
    usage = usage + "    1. 把 Discussions 转成博客的博文，以 md 格式保存。\n"
    usage = usage + "    2. 如果博文目录(outdir/blog/posts)不为空，则先删除目录下的 *.md 再生成新的 md 博文。"
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

    # 创建博文保存目录, 如目录存在则先删除目录下的 md
    blogPostsDir = Path(outputDir).joinpath('blog/posts')
    if blogPostsDir.exists():
        for filePath in Path(blogPostsDir).glob("*.md"):
            filePath.unlink()
    else:
        blogPostsDir.mkdir(parents=True, exist_ok=True)

    # 处理所有的 discussions
    year_blogs_dict = {}

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
                category_name = discussion_category.strip().split("-")[-1] 
            else:
                continue            

            slug_name   = f'discussions-{discussion_number}'
            create_date = discussion_createdAt[0:10]
            md_filename = create_date + "-" + slugify(discussion_title, allow_unicode=True, lowercase=False) + ".md"    #2023-10-18-xxxxx.md
            metadata    = ( f'---\n'
                            f'title: {discussion_title}\n'
                            f'number: {str(discussion_number)}\n'
                            f'slug: {slug_name}/\n'
                            f'url: {discussion_url}\n'
                            f'date: {discussion_createdAt[0:10]}\n'
                            f'authors: [{discussion_author}]\n'
                            f'categories: \n'
                            f'  - {category_name}\n'
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

            # 保存博客的输出结果
            savedBlogFile = blogPostsDir.joinpath(md_filename)
            with open(savedBlogFile, "w") as MD:
                MD.write(metadata)
                MD.write(discussion_body)
                MD.write(comments)

            create_year   = discussion_createdAt[0:4]
            blog_full_url = f'./{slug_name}'
            blog_title    = discussion_title
            if create_year in year_blogs_dict:
                year_blogs_dict[create_year].append([create_date, blog_title, blog_full_url])
            else:
                year_blogs_dict[create_year] = [[create_date, blog_title, blog_full_url]]

    # 博客的归档头部信息
    blog_index_meta = (f'---\n'
                       f'vssue: ""\n'
                       f'---\n\n'
                       f'# 博客文章\n\n'
                       f'这是首发于 [GitHub Discussions](https://github.com/shenweiyan/Digital-Garden/discussions)，并定期同步更新至 Material for MkDocs 本站点上的博客文章。\n\n'
                       f'??? "本站点所有博客文章归档"\n\n')

    # 保存博客的主页面输出结果
    savedBlogIndex =  Path(outputDir).joinpath('blog/index.md') 

    with open(savedBlogIndex, "w") as BlogIndex:
        BlogIndex.write(blog_index_meta)
        for year in sorted(year_blogs_dict.keys(), reverse=True):
            # 按照年份从大到小排序
            BlogIndex.write(f'    === "{year}"\n')
            for each_blog in sorted(year_blogs_dict[year], key=lambda date: date[0], reverse=True):
                # 按照创建时间从大到小排序
                BlogIndex.write(f'        - {each_blog[0]} [{each_blog[1]}]({each_blog[2]}) \n')

if __name__ == "__main__":
    __main__()
