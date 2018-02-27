---
title: python实现简易音乐播放器②
date: 2018-02-27
tags: python
categories: python
---

# python实现简易音乐播放器②

---

## 测试环境

python 3.6

win10

## 代码功能

① 输入歌曲名称后 播放相应的歌曲

② 可以暂停音乐

③ 界面右侧显示歌词

④ 可以在线播放音乐，也可以播放本地音乐

## 使用的库

`pygame、tkinter、subprocess、os、sys、requests、re`

此外，还需要使用到`ffmpeg`来进行歌曲转码，安装过程参考[这里](https://zh.wikihow.com/%E5%9C%A8Windows%E4%B8%8A%E5%AE%89%E8%A3%85FFmpeg%E7%A8%8B%E5%BA%8F)。

## 结果展示

初始：

![](http://119.29.89.242/image/python_music2_1.PNG)


输入歌名后，点击播放：

![](http://119.29.89.242/image/python_music2_2.PNG)


之后我们就可以听到歌曲了

## 代码运行方法

将全部文件[下载](https://github.com/lhx1228/MusicPlayer)下来，放入同一个文件运行`start.py`即可。



