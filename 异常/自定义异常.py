#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 9:44
# @Author  : maojx
# @Site    : 
# @File    : 自定义异常.py
# @Software: PyCharm
class customException(Exception):

    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise customException("自定义异常")
except customException as e:
    print(e)
