# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

import os
import subprocess
import optparse
import requests
import pytz
from datetime import datetime
from pathlib import Path
from git import Repo

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
    usage  = "usage: python3 %prog [options] \n\nExample:\n"
    usage  = usage + "    python3 %prog -r shenweiyan/Digital-Garden -t ghp_m8Iu12345abcdsfm6HzB"
    usage  = usage + "\n\nDescription:\n"
    usage  = usage + "    1. 比较 Discussions 是否变动, 以确认下一步部署。\n"
    usage  = usage + "    2. 默认生成 docs/diff.txt, 内容为前后两个 discussions 文件 diff 的结果。"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-r', '--repo', help="GitHub repository name with namespace.")
    parser.add_option('-t', '--token', help='GitHub token.')
    parser.add_option('-a', '--afile', default='docs/discussions.old.txt', help='Exists discussions txt file (default=%default).')
    parser.add_option('-b', '--bfile', default='docs/discussions.new.txt', help='Before discussions txt file (default=%default).')
    parser.add_option('-m', '--mode', default='debug', help='Running mode ( debug|deploy ) (default=%default).')

    opts, args = parser.parse_args()
    gh_repo    = opts.repo
    gh_token   = opts.token
    afile      = opts.afile
    bfile      = opts.bfile
    mtype      = opts.mode

    diff_txt = 'docs/diff.txt'

    # 获取一个时区对象（例如，北京的时区）
    beijing_timezone = pytz.timezone('Asia/Shanghai')
    # 使用时区对象将当前时间转换为具有时区信息的时间
    beijing_time = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(beijing_timezone)

    gh_owner     = gh_repo.split("/")[0]
    gh_repo_name = gh_repo.split("/")[-1]

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

    keys_to_remove = ['body', 'bodyText', 'bodyHTML', 'comments']
    with open(bfile, "w") as OUT:
        for each_discussion in allDiscussions:
            for key in keys_to_remove:
                each_discussion.pop(key, None)  # 安全删除多个键
            OUT.write(str(each_discussion)+"\n")

    if not os.path.exists(afile) or not os.path.exists(bfile):  
        print("错误: 文件不存在，请检查路径。")  
        exit() 
    else:
        content_a, content_o = "", ""
        # 读取文件内容
        with open(afile, 'r') as f:
            content_a = f.read()

        with open(bfile, 'r') as f:
            content_b = f.read()

        # 比较文件内容, 不管内容是否一样都把结果写入 doc/diff.txt
        cmd = f"diff {bfile} {afile}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if content_a != content_b:  
            message = f"Add Changes By GitHub Actions: {beijing_time} (CST/UTC-8)"
            with open(diff_txt, 'w') as DIFF1:
                if result.stdout:
                    DIFF1.write(result.stdout)
                else:
                    DIFF1.write(f"diff {bfile} {afile} 结果为空?")

            if mtype == "deploy":
                """
                print(f"# 内容不一致: 把 {bfile} 内容写入 {afile}!")
                os.replace(bfile, afile)  
                print(f"# 执行 git 提交")
                repo = Repo()
                g = repo.git
                g.add("--all")
                g.commit(f"-m {message}")
                g.push()
                """
                print("Skip push!")
            else:
                print(f"# 内容不一致: diff {afile} {bfile} 可看到区别")
        else:
            with open(diff_txt, 'w') as DIFF2:
                if result.stdout:
                    DIFF2.write(result.stdout)
                else:
                    DIFF2.write("")
                    print(f"提示: {bfile} 和 {afile} 文件内容相同，无需替换。")
       
if __name__ == "__main__":
    __main__()
