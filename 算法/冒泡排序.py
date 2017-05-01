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

#冒泡排序
def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                temp = data[j + 1]
                data[j + 1] = data[j]
                data[j] = temp


# 创建一个不规则数组
import random

arry = []
# 循环20次
for i in range(20):
    # 每次生成一个随机数
    arry.append(random.randrange(1000))

#调用冒泡排序
bubble_sort(arry)
print(arry)
