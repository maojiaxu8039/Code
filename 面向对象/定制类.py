#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 13:25
# @Author  : maojx
# @Site    : 
# @File    : 定制类.py
# @Software: PyCharm
"""
__str__
"""


class Student(object):
    def __init__(self, name):
        self.name = name


print(Student('Michael'))


# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
class Stundent(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('Michael'))
# 但是细心的朋友会发现直接敲变量不用print打印出来的实例还是不好看：
s = Student('Michael')


# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name=%s)' % self.name

    __repr__ = __str__


"""
__iter__
"""


# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象,返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

"""
__getitem__
"""


# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# 现在，就可以按下标访问数列的任意一项了：
f = Fib()
f[0]

"""
__getattr__
"""


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)


class Chain(object):
    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)
"""
__call__
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用实例.方法()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
"""


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()  # self参数不要传入

# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
callable(Student())
callable([1, 2, 3])