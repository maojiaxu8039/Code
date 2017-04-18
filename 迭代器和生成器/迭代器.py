#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/17 16:49
# @Author  : maojx
# @Site    : 
# @File    : 迭代器.py
# @Software: PyCharm
"""
在Python中，for循环可以用于Python中的任何类型，包括列表、元祖等等，实际上，for循环可用于任何“可迭代对象”，这其实就是迭代器
迭代器是一个实现了迭代器协议的对象，Python中的迭代器协议就是有next方法的对象会前进到下一结果，而在一系列结果的末尾是，则会引发StopIteration。任何这类的对象在Python中都可以用for循环或其他遍历工具迭代，迭代工具内部会在每次迭代时调用next方法，并且捕捉StopIteration异常来确定何时离开。
使用迭代器一个显而易见的好处就是：每次只从对象中读取一条数据，不会造成内存的过大开销。
"""
"""
可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：
"""
from collections import Iterable

isinstance([], Iterable)
"""
而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象：
"""
from collections import Iterator

isinstance([], Iterator)

"""
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
"""
isinstance(iter([]), Iterator)

"""
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
"""
