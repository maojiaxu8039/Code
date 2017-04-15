#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/14 11:45
# @Author  : maojx
# @Site    : 
# @File    : reduce.py
# @Software: PyCharm
"""
reduce 把以后函数作用在一个序列[x1,x2,x3...]上，这个函数必须接受两个参数，
reduce把结果积雪和序列的下一个元素做累积计算，其效果是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""
from functools import reduce


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
