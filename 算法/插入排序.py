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


def insertion_sort(data):
    # 数组第一个值不需要循环
    for i in range(1, len(data)):
        position = i  # 刚开始往左走的第一个位置
        current_val = data[i]  # 先把当前值存起来
        # 因为子循环不确定循环的次数所以用while条件来控制
        while position > 0 and current_val < data[position - 1]:
            # 如果保存值比 当前比较值小就把当前值往后赋值一位
            data[position] = data[position - 1]
            position -= 1
        data[position] = current_val


# 创建一个不规则数组
import random

arry = []
# 循环20次
for i in range(20):
    # 每次生成一个随机数
    arry.append(random.randrange(1000))

# 调用插入排序
insertion_sort(arry)
print(arry)
