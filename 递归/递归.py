#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 9:39
# @Author  : maojx
# @Site    : 
# @File    : 递归.py
# @Software: PyCharm

def calc(n):
    print(n)
    if n / 2 > 1:
        res = calc(n / 2)
        return res


calc(10)
