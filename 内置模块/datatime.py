#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/19 23:09
# @Author  : maojx
# @Site    : 
# @File    : datatime.py
# @Software: PyCharm

"""
datatime是Python处理日期和时间的标准库.
"""

# 获取当前日期和时间

from datetime import datetime

now = datetime.now()
print(now)
print(type(now))

# 获取制定的日期和时间
dt = datetime(2017, 6, 11, 23, 10, 10)
print(dt)

"""
在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
"""
# datetime转换为timestamp
now = datetime.now()
print(now.timestamp())

# timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# timestamp转换成UTC的标准时区的时间：
t = 1489937133.706406
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # UTC标准时区时间

# str转换为datetime
# 通过datetime.strptime()实现把字符串格式化成datetime
cday = datetime.strptime('2016-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
now = datetime.now()
print(now.strftime('%a,%b %d %H:%M'))

# datetime加减
# 对日期和时间进行加减实际上就可以把datetime往后或往前计算
# 得到新的datetime。加减可以直接用+和-运算符 需要导入timedelta这个类
from datetime import timedelta

now = datetime.now()
now = now + timedelta(hours=10)
print(now)
now = now + timedelta(days=1)
print(now)
now = now + timedelta(days=2, hours=12)
print(now)

# ps:datetime表示的时间需要时区信息才能确定一个特定的时间,否则只能视为本地时间。
# 如果要存储datetime,最佳方法是将其转换为tiemstamp再存储,因为timestamp的值与时区完全无关
