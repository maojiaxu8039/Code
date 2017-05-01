#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/30 14:59
# @Author  : maojx
# @Site    : 
# @File    : 快速排序.py
# @Software: PyCharm
"""
快速排序

"""


def quick_sort(data, start, end):
    # 起始如果大于等于结束循环停止
    if start >= end:
        return
    # 设置K为数组的起始值
    K = data[start]
    # 数组的开始下标
    left_flag = start
    # 数组的结束下标
    right_flag = end
    # 当结开始下标跟结束下标重合 经过这一个循环数组右边都是大于起始值的无需集合左边都是小于起始值的无序集合
    while left_flag < right_flag:
        # 当前值从右向左找到小于等于起始值 获取当前值的下标
        while left_flag < right_flag and data[right_flag] > K:
            right_flag -= 1
        # 把当前值跟起始值调换
        temp = data[left_flag]
        data[left_flag] = data[right_flag]
        data[right_flag] = temp
        # 再当前之从左向右寻找 找到大于起始值 获取当前只的下标
        while left_flag < right_flag and data[left_flag] <= K:  # 开始往右寻找
            left_flag += 1
        # 把当前值跟起始值调换
        temp = data[left_flag]
        data[left_flag] = data[right_flag]
        data[right_flag] = temp
    print(data)

    # 开始把问题拆分采用递归继续排序
    # 这个时候的left_flag=right_flag为第一次循环的中间值
    quick_sort(data, start, left_flag - 1)
    quick_sort(data, left_flag + 1, end)


arry = [326, 128, 343, 169, 471, 184, 279, 347, 285, 544, 426]
# 循环20次

# 调用快速排序
quick_sort(arry, 0, len(arry) - 1)
print(arry)
