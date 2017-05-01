#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/1 20:44
# @Author  : maojx
# @Site    : 
# @File    : 希尔排序.py
# @Software: PyCharm
"""
希尔排序
相当于多次分组的插入排序
时间复杂度O((1+T)n)
"""


def shell_sort(data):
    # gap是间隔值
    gap = len(data) // 2
    while gap >= 1:
        # 从间隔到最后
        for i in range(gap, len(data)):
            # 取出要比较的值放到tmp
            tmp = data[i]
            # 前一个要比较的值的下标
            j = i - gap
            # 如果间隔值比前一个要比较的值小
            while j >= 0 and tmp < data[j]:
                # 就把前一个比较值付给现在间隔值
                data[j + gap] = data[j]
                # 获取前面的间隔gap的值准备比较
                j -= gap
            # 把比较的值重新放入数组里
            data[j + gap] = tmp
        # 把间隔值再除2
        gap /= 2
