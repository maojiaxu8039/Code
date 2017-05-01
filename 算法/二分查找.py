#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 11:52
# @Author  : maojx
# @Site    : 
# @File    : 二分查找.py
# @Software: PyCharm
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

@cal_time
def bin_searvch(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return


import random

"""
修改二分查找代码，输入学生id，输出该学生在列表中的下标，并输出完整学生信息。
"""

@cal_time
# 生成测试数组字典
def random_list(n):
    result = []
    ids = list(range(1001, 1001 + n))
    a1 = ['zhao', 'qian', 'sun', 'li']
    a2 = ['li', 'hao', ]
    a3 = ['qiang', 'guo']
    for i in range(n):
        age = random.randint(18, 60)
        id = ids[i]
        name = random.choice(a1) + random.choice(a2) + random.choice(a3)
        result.append({'id': id, 'name': name, 'age': age})
    return result

@cal_time
def binary_chop(data_set, val):
    """

    :param data_set: 需要查找的数组
    :param val: 查找的值
    :return:
    """
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid]['id'] == val:
            return data_set[mid]
        elif data_set[mid]['id'] < val:
            low = mid + 1
        else:
            high = mid - 1


student_list = random_list(100)
a = binary_chop(student_list, 1002)
print(a)
