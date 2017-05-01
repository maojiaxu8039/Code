#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/30 13:55
# @Author  : maojx
# @Site    : 
# @File    : 插入排序.py
# @Software: PyCharm
"""
从一个数组循环取出一个值并把这个值跟之前取出的值做比较如果这个值比之前取出的值小那么就跟列表之前的值做比较
只到找到一个大于的值插入这个位置。
时间复杂度O(n2)
"""
# 创建一个不规则数组
import random

arry = []
# 循环20次
for i in range(20):
    # 每次生成一个随机数
    arry.append(random.randrange(1000))


def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            data[j + i] = data[j]
            j = j - 1
        data[j + 1] = tmp


# 调用插入排序
insert_sort(arry)
print(arry)


# 优化可以用二分查找
