#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/15 15:54
# @Author  : maojx
# @Site    : 
# @File    : 偏函数.py
# @Software: PyCharm
"""
python的functools模块提供了很多有用的功能,其中一个就是偏函数。
"""
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
int('12345')
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换
int('12345', base=2)


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)


# 这样，我们转换二进制就非常方便了：
int2('1000000')
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools

int2 = functools.partial(int, base=2)
int2('1000000')
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
