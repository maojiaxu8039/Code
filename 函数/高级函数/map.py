#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/14 11:04
# @Author  : maojx
# @Site    : 
# @File    : map.py
# @Software: PyCharm
"""
map()函数接受两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用导序列的每个对象，并把结果作为新的Iterator
返回
"""


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
list(r)
