---
title: Windows 增强型终端 MobaXterm 
urlname: 2019-07-01-mobaxterm
author: 章鱼猫先生
date: 2019-07-01
updated: "2024-08-07"
---

MobaXterm 又名 MobaXVT，是一款增强型终端、X 服务器和 Unix 命令集（GNU/ Cygwin）工具箱。MobaXterm 可以开启多个终端视窗，以最新的 X 服务器为基础的 [X.Org](http://X.Org)，可以轻松地来试用 Unix/Linux 上的 GNU Unix 命令。这样一来，我们可以不用安装虚拟机来试用虚拟环境，然后只要通过 MobaXterm 就可以使用大多数的 linux 命令。

MobaXterm 还有很强的扩展能力，可以集成插件来运行 Emacs、Fontforge、Gcc, G++ and development tools、MPlayer、Perl、Curl、Corkscrew、 Tcl / Tk / Expect、 Screen、 Png2Ico 、 NEdit  Midnight Commander 等程序。

MobaXterm 分免费开源版和收费专业版。官网提供 MobaXterm 的免费开源版 "Home Edition" 下载, 免费开源版又分便捷版(解压即用)和安装版(需要一步步安装)。

MobaXterm 免费版（persional）和专业版（Professional）除了 sessions 数、SSH tunnels 数和其他一些定制化配置外限制外，免费版在终端底部还多了一个 "UNREGISTERED VERSION" 提示。

- Peronnal Edition      
  ![mobaxterm_personal](https://kg.weiyan.cc/2024/08/mobaxterm_personal.png)

- Professional Edition      
  ![mobaxterm_professional](https://kg.weiyan.cc/2024/08/mobaxterm_professional.png)

## 1. 主要功能

- 支持各种连接 SSH，X11，RDP，VNC，FTP，MOSH

- 支持 Unix 命令（bash，ls，cat，sed，grep，awk，rsync，…）

- 连接 SSH 终端后支持 SFTP 传输文件

- 各种丰富的插件（git/dig/aria2…）

- 可运行 Windows 或软件

### 1.1. 内建多标签和多终端分屏

MobaXterm 内置多标签页、横向纵向 2 分屏和田字形 4 分屏，用于一个窗口内管理多个连接。管理多台服务器不必开多个窗口。      
![mobaxterm-split-mode](https://kg.weiyan.cc/2024/08/mobaxterm-split-mode.png)

### 1.2. 内建 SFTP 文件传输

如果用 SSH 连接远程主机，则左侧就会自动启动 SFTP 连接，列出服务器上的文件列表，无需任何配置。可以直接上传下载，更方便的是，还可以让文件列表的当前目录，直接跟随终端当前目录同步切换！          
![mobaxterm-sftp](https://kg.weiyan.cc/2024/08/mobaxterm-sftp.png)

### 1.3. 内建 X server

MobaXterm 内建了一个 X server，可以直接执行远程端的 X 窗口程序。也是随着 SSH 连接自动发挥作用，无需任何配置。      
![mobaxterm-x-server](https://kg.weiyan.cc/2024/08/mobaxterm-x-server.png)

### 1.4. 支持远程桌面

直接支持 VNC/RDP/Xdmcp 远程桌面,如果真的需要完整的远程桌面了，也无需多种客户端，一个软件即可对付所有的需求。Windows 服务器管理员特别推荐。      
![mobaxterm-vnc](https://kg.weiyan.cc/2024/08/mobaxterm-vnc.png)

### 1.5. 更加友好的串口连接设置

MobaXterm 不仅支持串口连接，并且直接提供下拉框选择串口号和波特率，选择串口号时还会自动显示串口设备的名称。这一点对于开源硬件玩家是相当幸福的。            
![mobaxterm-serial](https://kg.weiyan.cc/2024/08/mobaxterm-serial.png)

## 2. 使用介绍

### 2.1. 下载

我们使用免费开源版的便携版为例。(<http://mobaxterm.mobatek.net/download-home-edition.html>)。下载位置如下图所示。      
![mobaxterm-home-edition](https://kg.weiyan.cc/2024/08/mobaxterm-home-edition.png) 

下载后解压文件，运行 MobaXterm_Personal_xx.xx.exe 即可。第一次打开会自解压，会比较慢，后续就正常了。

### 2.2. SSH 连接

1. 打开软件后，点击左上角的 Session（会话控制），在弹出的窗口中选择 SSH：      
   ![mobaxterm-session-ssh](https://kg.weiyan.cc/2024/08/mobaxterm-session-ssh.png)

2. 在新的窗口输入账号和密码，即可登陆主机。此时界面主要分两块，左边的是主机的文件，右边是终端。勾选左下角的 "Follow terminal folder" 可以让两个的工作路径保持一致。      
   ![mobaxterm-follow-terminal-folder](https://kg.weiyan.cc/2024/08/mobaxterm-follow-terminal-folder.png)

## 3. 常用设置

**注意任何配置修改后都需要重启下 MobaXterm，否则不会生效。**

### 3.1. 取消自动关闭连接

MobaXterm 使用 ssh 直接连接远程主机，或者通过跳板机登陆远程服务器可能会出现一段时候不操作就会自动关闭连接。要解决这个过一会就断开连接的问题，我们需要在勾选 Setting 下的 SSH Keepalive 选项。      
![mobaxterm-ssh-keepalive](https://kg.weiyan.cc/2024/08/mobaxterm-ssh-keepalive.png)

### 3.2. 保存临时文件

MobaXterm 会产生临时文件，但是临时文件随时可能被删除或丢失，建议指定文件夹作为 `/home` 和 `/root` 目录，以免出现异常。打开 Settings – Configuration – Genernal 进行设置，如下截图。      
![mobaxterm-genernal](https://kg.weiyan.cc/2024/08/mobaxterm-genernal.png)

### 3.3. 使用 Windows 环境变量

在 MobaXterm 23.x 及以上版本中发现 `Use Windows PATH environment` 在设置中已经找不到，MabaXterm 的 [Changelog](https://mobaxterm.mobatek.net/download-home-edition.html) 中也没发现有什么移除之类的说明。

如果您 Windows 下安装了 node、Python 等环境，发现相关命令无法在 MobaXterm 使用，可通过打开 **Settings** – **Configuration** – **Terminal** – **使用 Windows 环境变量**，如下截图进行设置。      
![mobaxterm-win-path-env](https://kg.weiyan.cc/2024/08/mobaxterm-win-path-env.png)

### 3.4. 右键快速复制粘贴

如果需要鼠标右键快速复制粘贴，把 "**Paste using right-click**" 勾选上，然后重启 MobaXterm。      
![mobaxterm-right-click](https://kg.weiyan.cc/2024/08/mobaxterm-right-click.png)

除了 ssh/telnet/rsh 等多种远程会话，支持录制和回放键盘宏，支持多终端分屏显示等功能以外，MobaXterm 还支持 xdmcp/vnc 访问远程桌面以及本地 bash 或者 cmd 等诸多功能，无法一一介绍，欢迎大家用自行去探索研究。

### 3.5 设置 Terminal 窗口大小

![mobaxterm-terminal-size](https://kg.weiyan.cc/2024/08/mobaxterm-terminal-size.png)

### 3.5 SSH browser 消失不显示

某些用户可能在 MobaXTerm 中看不到文件浏览器窗格。这可能是也可能不是由于 Windows 防火墙提示用户允许/拒绝 MobaXTerm 访问公共和/或专用网络时所采取的操作所致。

解决此问题的方法是在创建/启动 MobaXTerm 会话时要求 MobaXTerm 使用 SCP 文件传输协议而不是 SFTP 协议（参考 [mikecroucher/Intro_to_HPC#2](https://github.com/mikecroucher/Intro_to_HPC/issues/2)）：      
![mobaxterm-ssh-browser-type](https://kg.weiyan.cc/2024/08/mobaxterm-ssh-browser-type.png)

## 4. 参考资料

- [Windows 全能终端神器——MobaXterm](https://www.isharebest.com/mobaxterm.htm)，爱上分享，博客

- [Windows 终端神器 MobaXterm & 常用设置](https://www.dabiaoseo.com/212.html)，Xiaoz，2017.12.28
