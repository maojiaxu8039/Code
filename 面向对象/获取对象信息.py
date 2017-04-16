#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 10:34
# @Author  : maojx
# @Site    : 
# @File    : 获取对象信息.py
# @Software: PyCharm
# 我们来判断对象类型，使用type()函数
type(123)
# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types


def fn():
    pass


type(fn) == types.FunctionType

type(abs) == types.BuiltinFunctionType

types(lambda x: x) == type.LambdaType

type((x for x in range(10))) == types.GeneratorType

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
# 能用type()判断的基本类型也可以用isinstance()判断：
isinstance('a', str)
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
isinstance([1, 2, 3], (list, tuple))


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：


# 配合getattr()、setattr()以及hasattr(),我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
hasattr(obj, 'x')  # 有属性'x'吗
obj.x
hasattr(obj, 'y')  # 有属性'y'吗
setattr(obj, 'y', 19)  # 设置一个属性y
hasattr(obj, 'y')
obj.y

# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# 可以传入一个default参数，如果属性不存在，就返回默认值：
getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404

# 也可以获得对象的方法：
hasattr(obj, 'power')  # 有属性power吗
getattr(obj, 'power')  # 获取属性power
fn = getattr(obj, 'power')  # 获取户型power并赋值到变量fn
