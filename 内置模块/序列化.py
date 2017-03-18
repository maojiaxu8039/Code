#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 10:29
# @Author  : maojx
# @Site    : 
# @File    : 序列化.py
# @Software: PyCharm
"""
什么是序列化
把变量从内存中编程可存储或传输的过程称之为序列化在Python中叫pickling
把变量内容从序列化的对象重新读导内存里称之为反序列化，即unpikling

用于序列化的两个模块
json,用于字符串和python数据类型间进行转换
pickle，用于python特有的类型和python的数据类型间进行转换

json和pickle模块都提供了四个功能：dumps、dump、loads、load
"""
'''
使用pickle把对象序列化并写入导文件
pickle.dumps()方法把任意对象序列化成一个byte
'''

import pickle

d = dict(name='bob', age=20, score=88)
pickle.dumps(d)

'''
pickle.dump()直接把对象序列化后写入一个file-like Object
'''
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

'''
当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
'''
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python

'''
json dumps()方法返回一个str，内容就是标准的JSON
dump()方法可以直接把JSON写入一个file-like Object
'''

import json

d = dict(name='Bob', age=20, score=88)
json.dumps(d)

'''
要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
'''
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

# 由于json标准规定json编码是utf-8，所以我们总能正确地在Python的Str与字符串之间转换

'''
json序列化类
'''

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }


s = Student('Bob', 20, 88)
print(json.dumps(s, default=Student.student2dict))

'''
我们可以把任意class的实例变成dict：
因为通常class的实例都有一个__dict__的属性，它就是一个dict
'''
print(json.dumps(s, default=lambda obj: obj.__dict__))

'''
如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
然后，我们传入的object_hook函数负责把dict转换为Student实例
'''


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
