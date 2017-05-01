#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/1 20:02
# @Author  : maojx
# @Site    : 
# @File    : 归并排序.py
# @Software: PyCharm

"""
现在有两段有序的列表，如何将其合成为一个有序的列表
"""


def merge(data, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    # 判断两个都有数
    while i < mid and j <= high:
        # 如果哪个数小就先把至存到数组里
        if data[i] < data[j]:
            ltmp.append(data[i])
            print(ltmp)
            i += 1
        else:
            ltmp.append(data[j])
            print(ltmp)
            j += 1
    # 判断上面的比较完剩下的如果哪个数组还有数就都循环添加的数组里
    while i <= mid:
        ltmp.append(data[i])
        i += 1
    while j <= high:
        ltmp.append(data[j])
        j += 1
    # 用切片把数组给写会原来数组里
    data[low:high + 1] = ltmp


data = [1, 4, 5, 6, 2, 3, 7, 8, 9]
merge(data, 0, 3, 8)
print(data)

"""
归并排序
一个列表
先分解将列表越分越小,直至分成一个元素。
一个元素是有序的
合并将两个有序列表归并,列表越来越大。
时间复杂度O(nlogn)
"""


def mergesort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        # 利用递归的特性 先把列表一直分解
        mergesort(li, low, mid)
        mergesort(li, mid + 1, high)
        # 递归往外出的时候开始合并
        merge(li, low, mid, high)
