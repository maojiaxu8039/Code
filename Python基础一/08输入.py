#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 10:32
# @Author  : maojx
# @Site    : 
# @File    : 08输入.py
# @Software: PyCharm

# 将用户输入的内容赋值给 name 变量
name = input("请输入用户名：")

# 打印输入的内容
print(name)

# 输入密码时，如果想要不可见，需要利用getpass 模块中的 getpass方法，即：
import getpass

# 将用户输入的内容赋值给 name 变量
pwd = getpass.getpass("请输入密码：")

# 打印输入的内容
print(pwd)
