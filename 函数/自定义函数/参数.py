#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 15:42
# @Author  : maojx
# @Site    : 
# @File    : 参数.py
# @Software: PyCharm
"""
函数的有三中不同的参数：
普通参数
默认参数
动态参数
"""


# ######### 定义函数 #########
# name叫做函数func的形式参数,简称:形参
def func(name):
    print(name)


# ######### 执行函数 #########
# 'maojiaxu'叫做函数func的实际参数,简称实参
func('maojiaxu')


# age=18参数赋值为默认参数 默认参数需要放在参数列表最后
def func(name, age=18):
    print("%s:%s" % (name, age))


# 指定参数
func('wupeiqi', 19)
# 使用默认参数
func('alex')


# 动态参数*args
def func(*args):
    print(args)


# 执行方式一
func(11, 33, 4, 4454, 5)

# 执行方式二
li = [11, 2, 2, 3, 3, 4, 54]
func(*li)


# 动态参数**kwargs
def func(**kwargs):
    print(kwargs)


# 执行方式一
func(name="maojiaxu", age=18)

# 执行方式二
li = {'name': 'maojiaxu', 'age': 18, 'gender': 'male'}
func(**li)


# 动态参数*args, **kwargs 可以接收任何值
def func(*args, **kwargs):
    print(args)
    print(kwargs)
