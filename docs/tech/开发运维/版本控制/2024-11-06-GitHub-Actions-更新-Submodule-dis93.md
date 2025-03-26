---
title: GitHub Actions 更新 Submodule
number: 93
slug: discussions-93/
url: https://github.com/shenweiyan/Digital-Garden/discussions/93
date: 2024-11-06
authors: [shenweiyan]
categories: 
  - 1.3-折腾
labels: ['1.3.18-版本控制']
---

怎么通过 GitHub Actions 实时更新 Git 仓库中的子模块（submodules）。

<!-- more -->

```yaml
name: Send submodule updates to parent repo

on:
  push:
    branches: 
      - main

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
        with: 
          repository: xxx/parent_xxx
          token: ${{ secrets.PRIVATE_TOKEN_GITHUB }}

      - name: Pull & update submodules recursively
        run: |
          git submodule update --init --recursive
          git submodule update --recursive --remote
      - name: Commit
        run: |
          git config user.email "actions@github.com"
          git config user.name "GitHub Actions - update submodules"
          git add --all
          git commit -m "Update submodules" || echo "No changes to commit"
          git push
```

1. `git submodule update --init --recursive`

这个命令用于初始化并更新仓库中的子模块。具体来说：

- `--init` 参数会初始化在 `.gitmodules` 文件中指定的每个子模块的配置信息，但不会更新子模块的内容。这个步骤是必须的，因为 Git 不会自动初始化子模块的配置信息。
- `--recursive` 参数确保命令递归地应用于任何嵌套的子模块。这意味着如果子模块本身还包含子模块，这些子模块也会被初始化。

简而言之，这个命令会初始化仓库中所有（包括嵌套的）子模块的配置，并更新它们到在父仓库中记录的提交。

2. `git submodule update --recursive --remote`

这个命令用于更新仓库中的子模块到它们的远程仓库中的最新状态（或指定的分支/标签）。具体来说：

- `--recursive` 的作用与上述命令相同，确保命令递归地应用于所有嵌套的子模块。
- `--remot`e 参数指示 Git 更新每个子模块到其远程仓库的当前分支的最新提交。如果没有指定分支，则默认为在 `.gitmodules ` 文件中为每个子模块指定的分支。

注意，这个命令并不会改变父仓库中记录的子模块的提交。它只是更新了子模块的工作目录和索引，以匹配远程仓库的最新状态。如果你想在父仓库中记录这些更新，你需要在子模块中执行提交，然后回到父仓库中，添加子模块的变更并提交。

3. 总结

- `git submodule update --init --recursive` 用于初始化并更新子模块到父仓库中记录的提交。
- `git submodule update --recursive --remote` 用于将子模块更新到其远程仓库的最新状态，但不会在父仓库中记录这些更新。


<script src="https://giscus.app/client.js"
	data-repo="shenweiyan/Digital-Garden"
	data-repo-id="R_kgDOKgxWlg"
	data-mapping="number"
	data-term="93"
	data-reactions-enabled="1"
	data-emit-metadata="0"
	data-input-position="bottom"
	data-theme="light"
	data-lang="zh-CN"
	crossorigin="anonymous"
	async>
</script>
