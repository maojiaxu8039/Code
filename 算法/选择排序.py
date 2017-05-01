#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/30 13:15
# @Author  : maojx
# @Site    : 
# @File    : 选择排序.py
# @Software: PyCharm

"""
选择排序
找到列表里面的最小值跟前面值进行交换
时间复杂度O(n2)
"""

import random

arry = []
for i in range(20):
    arry.append(random.randrange(1000))


# 选择排序(普通版)
def selection_sort1(data):
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]


# 选择排序(优化版)
# 优化小循环比较一次就的交换一次 定以一个下标记住小循环循环完成的最小值的下标
# 再大循环外进行一次交换
def selection_sort2(data):
    for i in range(len(data) - 1):
        smallest_index = i
        for j in range(i, len(data)):
            if data[smallest_index] > data[j]:
                smallest_index = j
        data[i], data[smallest_index] = data[smallest_index], data[i]


selection_sort1(arry)
print(arry)
selection_sort2(arry)
print(arry)
