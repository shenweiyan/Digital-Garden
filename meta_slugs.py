# -*- coding:utf-8 -*-
# vim:et:ts=4:sw=4:
#!/usr/bin/env python

"""
Via: https://github.com/squidfunk/mkdocs-material/discussions/5161

MkDocs hook to replace destination urls with custom slugs

The main issue of this feature is the fact that the front matter header is loaded 
for each page sequentially in the on_page_markdown event. To avoid issues with 
internal link references it's required to read the front matter before the MkDocs 
event. This duplicates the read task, so it decreases overall performance relative
to the amount of files.

Current limitations:
- Primitive collision check for slugs and files, doesn't check if a file has a slug that voids the collision
- `use_directory_urls` was always True during testing, the hook will not handle False :shrug:

Licence MIT 2024 Kamil Krzyśków (HRY)
"""

import os
from mkdocs.plugins import get_plugin_logger
from mkdocs.utils import meta

log = get_plugin_logger("meta_slugs")


class SlugCollision:
    """Container class to handle the slug collision logic"""

    file_urls: dict[str, str]
    """Dict mapping of file urls to file paths of the original file urls"""

    slug_urls: dict[str, str]
    """Dict mapping of slug urls to file paths of the custom meta slugs"""

    def __init__(self):
        self.file_urls = {}
        self.slug_urls = {}

    def is_valid(self, slug: str) -> bool:
        """Check the slug string for errors and check for collisions"""

        if slug is None:
            return False

        if not isinstance(slug, str):
            log.error(f"'slug' has to be a string not {type(slug)}")
            return False

        if slug.startswith("/") or not slug.endswith("/"):
            log.warning(f"'slug': '{slug}' can't start with a '/' and has to end with a '/'")
            return False

        if "\\" in slug:
            log.error(f"'slug' can't be a Windows path with '\\'")
            return False

        if slug in self.file_urls:
            log.warning(f"'slug': '{slug}' collides with the file: {self.file_urls[slug]}")
            return False

        if slug in self.slug_urls:
            log.warning(f"'slug': '{slug}' was already used in the file: {self.slug_urls[slug]}")
            return False

        return True


def on_files(files, config, **__):
    slug_collision = SlugCollision()

    # First load the ulrs
    for file in files:
        if file.is_documentation_page():
            slug_collision.file_urls[file.url] = file.abs_src_path

    # Second process the meta
    for file in files:
        if not file.is_documentation_page():
            continue

        slug = _load_meta(file).get("slug")

        if not slug_collision.is_valid(slug):
            continue

        # TODO Add handling for `use_directory_urls`
        file.url = slug
        file.dest_uri = slug + "index.html"
        file.abs_dest_path = os.path.normpath(os.path.join(config["site_dir"], file.dest_uri))

        slug_collision.slug_urls[slug] = file.abs_src_path


def _load_meta(file):
    """Local copy of mkdocs.structure.pages.Page.read_source"""

    try:
        with open(file.abs_src_path, encoding="utf-8-sig", errors="strict") as f:
            source = f.read()
        _, file_meta = meta.get_data(source)
        return file_meta
    except OSError:
        log.error(f"File not found: {self.file.src_path}")
        raise
    except ValueError:
        log.error(f"Encoding error reading file: {self.file.src_path}")
        raise
