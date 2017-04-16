#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 13:13
# @Author  : maojx
# @Site    : 
# @File    : 多重继承.py
# @Software: PyCharm

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
from socketserver import TCPServer, ForkingMixIn, UDPServer, ThreadingMixIn


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass


# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass


# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。


"""
Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，
而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
"""


# 比如，编写一个多进程模式的TCP服务，定义如下：
class MyTCPServer(TCPServer, ForkingMixIn):
    pass


# 编写一个多线程模式的UDP服务，定义如下：
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass

# 如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#    pass
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。
