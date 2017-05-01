# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 18:07
# @Author  : maojx
# @Site    : 
# @File    : 冒泡排序.py
# @Software: PyCharm

"""
冒泡排序
把无序的数组按照从小到大的顺序进行排序
时间复杂度O(n2)
"""
# 创建一个不规则数组
import random

arry = []
# 循环20次
for i in range(20):
    # 每次生成一个随机数
    arry.append(random.randrange(1000))


# 冒泡排序
def bubble_sort1(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


# 冒泡排序 如果没有交换那么排序已经完成。
def bubble_sort2(data):
    for i in range(len(data) - 1):
        exchange = False
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                exchange = True
        if not exchange:
            break


# 调用冒泡排序
bubble_sort1(arry)
print(arry)
bubble_sort2(arry)
print(arry)
