![icon0](https://github.com/XiQuedhm/Xbot/blob/main/.resources/icon_light.png "Xbot Icon")
<br>
![Icon1](https://img.shields.io/badge/Chat%20on-gitter%20or%20telegram-blue "Chat")
<br>
![Icon2](https://img.shields.io/badge/Language-Python-lightgrey "Language")
![Icon3](https://img.shields.io/badge/Licence-CC--BY--NC--SA%204.0-lightgrey "Licence")
<br>
一个使用Python制作的简单易用的QQ机器人框架

# Xbot
*  [English](https://github.com/XiQuedhm/Xbot/blob/main/README.md)
* [简体中文](https://github.com/XiQuedhm/Xbot/blob/main/README_zhcn.md)

# Contents
* [项目背景](#背景)
* [安装](#安装)
* [使用方法](#使用)
* [主要贡献者](#贡献者)
* [如何帮助开发](#如何帮助开发)
* [将来可能的功能](#开发中功能)
* [开源许可证](#licence)
## 背景
这个项目最初的目的是制作一个高拓展性，高可自定义性，高稳定性的自用框架
<br>
随着开发进度的推进，我越发觉得它也应该成为一个可以供其他人使用的框架，所以我创建了这个仓库
## 安装
### 依赖
* Python (≥ 3.8)
    * Flask
    * requests
* git
* pip
* zip
* unzip
* gzip

### 通用安装
你可以使用
```sh
cd
git clone https://github.com/XiQuedhm/Xbot.git
```
来安装`Xbot`，你也可以直接下载发行版中的文件自行解压
### Linux安装
如果你在`Linux`环境中，你也可以使用
```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/XiQuedhm/Xbot/main/tools/install.sh)"
```
来安装`Xbot`
## 使用
### Linux / MAC OS
`Xbot`直接使用源码与解释器运行
<br>
如果你`clone`在`~`目录，你可以直接使用`sh ./Xbot/bin/open.sh`来启动它。
<br>
把插件放置在`Xbot/plugins`目录下，插件将在启动时被自动加载
### Windows
先编辑`Xbot/tools/sysconfig.py`，把其中的`system_W`设置为`True`，其中的`py_Path`设置为你安装的`Python`的`bin`目录位置，然后手动运行`Xbot/tools/win_Fix.py`
<br>
开启时运行`Xbot/bin/open.bat`
<br>
把插件放置在`Xbot/plugins`目录下，插件将在启动时被自动加载
## 贡献者
### 以下排名不分先后
* 夏小白
* XiQuedhm233
##  如何帮助开发
## 开发中功能
## Licence