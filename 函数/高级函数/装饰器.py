#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 16:49
# @Author  : maojx
# @Site    : 
# @File    : 装饰器.py
# @Software: PyCharm
"""
装饰器是一个著名的设计模式,经常被用于有切面需求的场景,较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能
"""

# 由于函数也是一个对象,而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
import functools


def now():
    print('2017-07-01')


f = now
f()
# 函数对象有一个__name__属性,可以拿到函数的名字：
print(now.__name__)


# 现在我们要增强now函数的功能,比如,在函数调用前后自动打印日志,但又不希望修改now()函数的定义,在这种代码运行期间动态增加的功能方式
# 称之为装饰器(Decorator)
# 本质上decorator就是一个返回函数的高阶函数。所以我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
    def wrapper(*args, **kw):
        print('call%s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


# 观察log因为它是一个decortaor所以接受一个函数作为参数,并返回一个函数。我们要借助于Python的@语法,把decorator
# 置于函数的定义处
@log
def now(*args, **kwgs):
    print('2017-7-17')


now()


# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now = log('execute')(now)
# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
# 它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


# 装饰器的问题写法
def log(text):
    def warpper(func):
        print('%s %s():' % (text, func.__name__))
        return func

    return warpper


@log('hello')
def now():
    print('2017-04-13')

# 没有执行now() 方法就输出了hello now()了 原因程序一执行就执行了第一次验证。所以正确写法应该再嵌套一个函数。
