#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/14 17:09
# @Author  : maojx
# @Site    : 
# @File    : sorted.py
# @Software: PyCharm
from operator import itemgetter

"""
排序算法

"""
# python内置的sorted()函数就可以对list进排序：
sorted([36, 5, -12, -9, 21])

# sorted()函数也是一个高级函数，它还可以接收一个key函数来实现自定义的排序,例如按绝对值大小排序：
sorted([36, 5, -12, -9, 21], key=abs)

# 给sorted传入key函数,即可实现忽略大小写的培训：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

# 要进行反向排序,不必改动key函数,可以传入第三个参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reversed=True)

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
