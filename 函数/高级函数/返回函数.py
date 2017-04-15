#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/15 10:13
# @Author  : maojx
# @Site    : 
# @File    : 返回函数.py
# @Software: PyCharm
"""
函数作为返回值
高级函数除了可以接受函数作为参数外,还可以把函数作为结果值返回。
"""


# 我们实现一个可变的求和。通常情况下，求和函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
        return ax


# 如果不需要立刻求和,而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
