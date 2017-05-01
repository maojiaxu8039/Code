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
import time


# 定义时间装饰器
def cal_time(func):
    def wrapper(*args, **kwargs):
        ti = time.time()
        x = func(*args, **kwargs)
        ti2 = time.time()
        print("Time cost", ti2 - ti)
        return x

    return wrapper


arry = [326, 128, 343, 169, 471, 184, 279, 347, 285, 544, 426]


def quick_sort_x(data, left, right):
    # 当左坐标大于右坐标代表排序完成
    if left < right:
        # 获取一轮排序后的中间值
        mid = partition(data, left, right)
        # 通过中间值拆分左边继续下一轮排序 递归
        quick_sort_x(data, left, mid - 1)
        # 通过中间值拆分右边继续下一轮排序 递归
        quick_sort_x(data, mid + 1, right)


def partition(data, left, right):
    #  把左边的值找一个地方存起来留出一个空位
    tmp = data[left]
    while left < right:
        # 开始从右向左寻找
        while left < right and data[right] >= tmp:
            right -= 1
        # 当找到比这个数小的值存到左边空位上
        data[left] = data[right]
        # 开始从左向右寻找
        while left < right and data[left] <= tmp:
            left += 1
        # 当找到比这个数大的值存到右边的空位上
        data[right] = data[left]
    # 最后把开始的值存到数组保留的空位上
    data[left] = tmp
    # 返回当前中间值的下标
    return left


@cal_time  # 装饰器直接写在包含递归的方法上出问题只能先调用递归方法
def quick_sort(data):
    return quick_sort_x(data, 0, len(data) - 1)


quick_sort(arry)
print(arry)


@cal_time
# 系统的快速排序 使用c写的所以速度快
def sys_sort(data):
    return data.sort()


# 如果需要设置系统最大递归数
import sys

sys.setrecursionlimit(100000)
