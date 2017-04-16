#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 12:00
# @Author  : maojx
# @Site    : 
# @File    : 使用__slots__.py
# @Software: PyCharm
# 当我们定义了一个class,创建了一个class的实例后,我们可以给该实例绑定任何属性和方法,这就是动态语言的灵活性。先定义class：
class Student(object):
    pass


# 尝试给实例绑定一个属性
s = Student()
s.name = 'Micheal'
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实力绑定一个方法
s.set_age(25)  # 调用实例方法
s.age

# 但是,给一个实力绑定的方法，对另一个实例是不起作用的
s2 = Student()
s2.set_age(25)


def set_score(self, score):
    self.score = score


# 上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
Student.set_score = set_score

s.set_score(100)
s.score
s2.set_score(99)
s2.score


# __slots__
# ，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性name
s.age = 25
s.score = 99
"""
由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
"""
