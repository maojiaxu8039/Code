#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 11:52
# @Author  : maojx
# @Site    : 
# @File    : 二维数组旋转.py
# @Software: PyCharm
"""
二维数组90度旋转
"""
# 创建一个二维数组
data = [[col for col in range(4)] for raw in range(4)]
for n in data:
    print(n)

print('\n')
# 外层循环
for i in range(len(data)):
    # 内层循环
    for j in range(i + 1, len(data)):
        # 交换数据
        data[i][j], data[j][i] = data[j][i], data[i][j]

for n in data:
    print(n)
