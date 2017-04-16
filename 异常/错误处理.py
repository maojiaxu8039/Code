#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 17:59
# @Author  : maojx
# @Site    : 
# @File    : 错误处理.py
# @Software: PyCharm

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
# 则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
# 如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，
# foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦。

# Python内置的logging模块可以非常容易地记录错误信息：

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')


# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

# 抛出错误
# 用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')
"""
其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

"""


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')