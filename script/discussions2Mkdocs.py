# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

import argparse
import requests
import os
import json
from slugify import slugify
from pathlib import Path

def stop_err(msg):
    sys.stderr.write('%s\n' % msg)
    sys.exit()

def gen_discussions_query(owner, repo_name, perPage, endCursor, first_n_threads):
    after_endCursor = ""
    if endCursor:
        after_endCursor = 'after: "%s"' % endCursor
    
    return f"""
    query {{
        repository(owner: "{owner}", name: "{repo_name}") {{
            discussions(
                orderBy: {{field: CREATED_AT, direction: DESC}}
                first: {perPage}
                {after_endCursor}) {{
                    nodes {{
                        title
                        number
                        url
                        createdAt
                        lastEditedAt
                        updatedAt
                        body
                        bodyText
                        bodyHTML
                        author {{
                            login
                        }}
                        category {{
                            name
                        }}
                        labels (first: 100) {{
                            nodes {{
                                name
                            }}
                        }} 
                        comments(first: {first_n_threads}) {{
                            nodes {{
                                body
                                author {{
                                    login
                                }}
                            }}
                        }}
                    }} # end nodes
                    pageInfo {{
                        hasNextPage
                        endCursor
                    }}
            }} # end discussions    
        }} # end discussions
    }} # end query
    """

def get_discussions(query, url, headers):
    response = requests.post(url, json={"query": query}, headers=headers)
    data = response.json()
    if data['data']['repository']['discussions'] is None:
        return ""
    else:
        return data['data']['repository']['discussions']

def __main__():
    parser = argparse.ArgumentParser(description="Fetch GitHub discussions data to mkdocs blog")
    parser.add_argument('-r', '--github_repo', help="GitHub repository name with namespace")
    parser.add_argument('-t', '--github_token', help='GitHub access token.')
    parser.add_argument('-o', '--outdir', default='docs', help='Output directory (%default).')
    args = parser.parse_args()

    gh_token = args.github_token
    gh_repo  = args.github_repo
    outdir   = args.outdir

    categoriesWhitelist = ['乱弹', '好玩', '资讯', '知识', '留言']

    gh_owner     = gh_repo.split("/")[0]
    gh_repo_name = gh_repo.split("/")[-1]

    # 创建博文保存目录, 如目录存在则先删除目录下的 md
    blog_posts_dir = Path(outdir).joinpath('blog/posts')
    if blog_posts_dir.exists():
        for file_path in Path(blog_posts_dir).glob("*.md"):
            file_path.unlink()
    else:
        blog_posts_dir.mkdir(parents=True, exist_ok=True)

    url = "https://api.github.com/graphql"
    headers = {"Authorization": f"Bearer %s" % gh_token}

    hasNextPage    = True
    allDiscussions = []
    endCursor      = ""  
    while hasNextPage:
        query          = gen_discussions_query(gh_owner, gh_repo_name, 5, endCursor, 10)
        results        = get_discussions(query, url, headers)
        discussions    = results['nodes']
        hasNextPage    = results['pageInfo']['hasNextPage']
        endCursor      = results['pageInfo']['endCursor']
        allDiscussions = allDiscussions + discussions

    for discussion in sorted(allDiscussions, key=lambda x: x['number']): #fix me
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
        discussion_category     = discussion['category']['name'].split('-')[-1]
        discussion_labels       = [label['name'] for label in discussion['labels']['nodes']] if discussion['labels']['nodes'] else []

        if not discussion_category in categoriesWhitelist:
            continue
        
        slug_name   = f'discussion-{discussion_number}'
        create_date = discussion_createdAt[0:10]
        md_filename = create_date + "-" + slugify(discussion_title, allow_unicode=True, lowercase=False) + ".md"    #2023-10-18-xxxxx.md
        metadata    = ( f'---\n'
                        f'title: {discussion_title}\n'
                        f'number: {str(discussion_number)}\n'
                        f'slug: {slug_name}\n'
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
        
        # 处理留言页面
        if int(discussion_number) == 16:
            saved_msg_file = Path(outdir).joinpath("message.md")
            with open(saved_msg_file, "w") as MSG:
                MSG.write("# 给作者留言\n\n")
                MSG.write(discussion_body)
                MSG.write(comments)
        else:
            # 保存博客的输出结果
            saved_blog_file = blog_posts_dir.joinpath(md_filename)
            with open(saved_blog_file, "w") as MD:
                MD.write(metadata)
                MD.write(discussion_body)
                MD.write(comments)       

if __name__ == "__main__":
    __main__()
