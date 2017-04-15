#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 1:24
# @Author  : maojx
# @Site    : 
# @File    : 内置函数.py
# @Software: PyCharm
"""
内置函数文档
https://docs.python.org/3/library/functions.html
"""
# map 遍历序列,对序列中每个元素进行操作,最终获取新的序列
from functools import reduce

li = [11, 22, 33]
new_list = map(lambda a: a + 100, li)
print(list(new_list))

li = [11, 22, 33]
sl = [1, 2, 3]
new_list = map(lambda a, b: a + b, li, sl)
print(list(new_list))

# filter 对于序列中的元素进行筛选，最终获取符合条件的序列
li = [11, 22, 33]
new_list = filter(lambda arg: arg > 22, li)
print(list(new_list))

# reduce 对于序列内所有元素进行累计操作
li = [11, 22, 33]
result = reduce(lambda arg1, arg2: arg1 + arg2, li)
print(result)