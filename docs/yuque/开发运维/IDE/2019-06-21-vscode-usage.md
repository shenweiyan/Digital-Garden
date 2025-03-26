---
title: VS Code 常见配置与使用技巧总结
urlname: 2019-06-21-vscode-usage
author: 章鱼猫先生
date: 2019-06-21
updated: "2021-06-25 10:39:11"
---

版本: 1.35.1 (user setup)

## 1. 通过配置文件设置

VS Code 的配置文件默认为：settings.json，我们可以通过下面的方式打开该文件进行自定义配置：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiQpFgBEIolE-e8XjD_AitEdsgLL.png)
打开 settings.json 方式一：VSCode 1.35.1 (user setup)

![setting_json.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FrWX9_lPP0-n29Fbt0YCjhH1lGCx.png)
打开 settings.json 方式一：VSCode 1.44.2 (user setup)

![setting-json-2.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FlNR1bfqK0awTbl_v9-Ls0VBTnAM.png)
打开 settings.json 方式二：VSCode 1.44.2 (user setup)

- **C:\Users\[USER_NAMD]\AppData\Roaming\Code\User\settings.json**

```json
{
  "editor.minimap.enabled": false,
  "editor.fontSize": 12,
  "workbench.statusBar.feedback.visible": false,
  "terminal.integrated.shell.windows": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
  "workbench.colorTheme": "Visual Studio Dark",
  "[python]": {},
  "breadcrumbs.enabled": false,
  "workbench.editor.centeredLayoutAutoResize": false,
  "editor.wordWrap": "on",
  "editor.minimap.showSlider": "always",
  "window.menuBarVisibility": "visible",
  "workbench.sideBar.location": "left",
  "editor.accessibilitySupport": "off",
  //显示头部导航栏
  "workbench.editor.showTabs": true,
  "window.zoomLevel": 0,
  //Ctrl+滚轮实现代码的缩放
  "editor.mouseWheelZoom": true,
  "workbench.editor.tabSizing": "shrink"
}
```

## 2. 编辑器选项卡

当 vscode 打开很多文件，如果 "**设置 → 工作台 → 编辑器管理 →Tab Sizing**" 为 "**fit**"，编辑器选项卡将使用滚动隐藏的方式显示，想要显示打开的编辑器可以使用 `edt`  的命令或者设置 "**Show All Editors**" 的快捷键。
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Ft_EfS30x1vrL1Ft7K6lkd_eA_YR.png)

![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fj4ZWfs1Fr8FKzr1CJT3diOfhNPn.png)

也可以将  "**设置 → 工作台 → 编辑器管理 →Tab Sizing**" 设置为 "**shrink**"：
![image.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fqdqhb4OB-bsYflxkB0q0zjTuVml.png)

## 3. 禁用 Tab 转换为空格

VS Code 中会默认把 Tab 键转换成 4 个空格，当然你也可以自己定义转换的空格数。或者你也可以禁止把 Tab 键转换为空格，具体设置如下截图：**“设置”**→**“常规设置”**→**“Editor:Tab Size”**→**“Editor:Insert Spaces”。**
![vscode-tab-setting.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/Fh2kGbIFaOvMRPjTwzCabQGCs0wo.png)


## 4. 无法创建和打开任何文件

VSCode 无法创建和打开任何问题文件，重装和重启后都没办法解决，异常信息如下“**Unable to open 'xxx': Assertion Failed: argument is undefined or null**”。
![vscode-open-error.png](https://shub.weiyan.tech/yuque/elog-cookbook-img/FiK6VE11khUrbPvNtU-YYLOIRfUt.png)
解决方法参考：
[Windows: Both insider and normal version: Unable to open ‘xxx’: Assertion Failed: argument is undefined or null · Issue #93679 · microsoft/vscode](https://github.com/microsoft/vscode/issues/93679)

> I just had the same issue and this is how I fixed:
> go to -> **C:\Users\[USER_NAMD]\AppData\Roaming\Code\User\settings.json**
> and look for `"editor.quickSuggestions": null`. Change the value to either `false` or `true` .
