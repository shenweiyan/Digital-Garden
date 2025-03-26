from datetime import datetime
from material.plugins.blog.structure import Archive

"""
def on_page_markdown(markdown, *, page, config, files):
    if isinstance(page, Archive):
        page.meta["template"] = "my-custom-template.html"
"""

def on_config(config, **kwargs):
    config.copyright = f"版权所有 © 2023-{datetime.now().year} <a href=\"https://github.com/orgs/BioITee/discussions\" target=\"_blank\">BioIT 爱好者</a> | <a href=\"http://beian.miit.gov.cn/\" target=\"_blank\" rel=\"noopener\">粤ICP备16023717号</a>"
