#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 15:42
# @Author  : maojx
# @Site    : 
# @File    : 返回值.py
# @Software: PyCharm
"""
函数是一个功能块，该功能到底执行成功与否，需要通过返回值来告知调用者
def 发送短信():

    发送短信的代码...

    if 发送成功:
        return True
    else:
        return False


while True:

    # 每次执行发送短信函数，都会将返回值自动赋值给result
    # 之后，可以根据result来写日志，或重发等操作

    result = 发送短信()
    if result == False:
        记录日志，短信发送失败...
"""