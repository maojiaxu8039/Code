#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 14:40
# @Author  : maojx
# @Site    : 
# @File    : 枚举类.py
# @Software: PyCharm

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份
# JAN = 1
# FEB = 2
# MAR = 3
# ...
# NOV = 11
# DEC = 12
# 好处是简单，缺点是类型是int，并且仍然是变量

# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。
# Python提供了Enum类来实现这个功能：
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Feb.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun.value)


# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。
