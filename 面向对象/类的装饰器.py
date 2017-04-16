#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/19 15:03
# @Author  : maojx
# @Site    : 
# @File    : 类的方法.py
# @Software: PyCharm
"""
类的装饰器
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.num = None

    hobbie = "meat"

    @classmethod  # 类方法 静态方法中不能访问当前实例变量，但可以访问类变量
    def talk(self):
        print("%s is talking" % self.hobbie)

    @staticmethod  # 静态方法 静态方法中不能访问当前实例或类的变量 可以通过传值
    def walk():
        print("%s is walking" % Animal.hobbie)

    @property  # 类属性 Python内置的@property装饰器就是负责把一个方法变成属性调用的
    def habit(self):
        print("%s is habit" % self.name)

    @property
    def totalPlayers(self):
        return self.num

    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @totalPlayers.setter  # 给totalplayer方法 增加set属性
    def totalPlayers(self, num):
        self.num = num
        print("total players:", self.num)


# ps：普通方法不能被直接被调用
Animal.talk()  # 类方法可以直接被调用
Animal.walk()  # 静态方法可以直接被调用
d = Animal("Sanjang")
d.talk()  # 类方法可以实例化调用
d.walk()  # 静态方法可以实例化调用
d.totalPlayers = 3
