#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 12:33
# @Author  : maojx
# @Site    : 
# @File    : virtualenv.py
# @Software: PyCharm
"""
1.使不同应用开放环境独立
2.环境升级不影响其他应用，也不会影响全局的python环境
3.塔可以防止系统中出现包管理混乱和版本的冲突

安装virtualenv
pip install virtualenv
安装目录就是当前所在文件夹下

启动virtualenv
activate.bat

停止virtualenv
deactivate.bat

pip install virtualenvwrapper-win
mkvirtualenv testvir2


查看有多少虚拟环境
workon

进入其中的一个虚拟环境
workon testvir2

退出虚拟环境
deactivate

查看虚拟环境有什么包
pip list

"""
