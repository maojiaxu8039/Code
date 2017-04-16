#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/19 12:41
# @Author  : maojx
# @Site    : 
# @File    : 封装.py
# @Software: PyCharm
def log(text):
    def warpper(func):
        print('%s %s():' % (text, func.__name__))
        return func

    return warpper


@log('hello')
def now():
    print('2017-04-13')
