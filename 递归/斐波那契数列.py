#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 11:53
# @Author  : maojx
# @Site    : 
# @File    : 斐波那契数列.py
# @Software: PyCharm
"""
斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377，610，987，1597，2584，4181，6765，10946，17711，28657，46368
"""


def func(arg1, arg2):
    if arg1 == 0:
        print(arg1, arg2)
    arg3 = arg1 + arg2
    print(arg3)
    func(arg2, arg3)


func(0, 1)
