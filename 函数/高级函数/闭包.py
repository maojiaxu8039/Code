#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/15 11:22
# @Author  : maojx
# @Site    : 
# @File    : 闭包.py
# @Software: PyCharm
"""
http://python.jobbole.com/82624/
http://www.cnblogs.com/JohnABC/p/4076855.html
"""


# 什么是闭包
# 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)
# 一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B给你。这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量
def line_conf(a):
    def line(x):
        return 2 * x + a

    return line  # return a function object


my_line = line_conf(3)
print(my_line(5))


# 闭包的实现
# a.闭包就是为了不动原函数里面的代码，还要给它增加‘功能性’的一种手段。
# b.通过外面的一层层的函数传递的参数，让最内层的函数可以直接调用外层函数所有参数，从而实现不动原函数的代码，增加新功能的办法。
# 在python中，修饰器就是最好的体现：

# 闭包的原理
# 在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。环境变量取值被保存在函数对象的__closure__属性中
def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line.__closure__)
# __closure__里包含了一个元组(tuple)。这个元组中的每个元素是cell类型的对象。
# 我们看到第一个cell包含的就是整数15，也就是我们创建闭包时的环境变量b的取值。
print(my_line.__closure__[0].cell_contents)

# 闭包的作用

# 用途1，当闭包执行完后，仍然能够保持住当前的运行环境。
# 用途2，闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用，我们可以修改外部的变量，闭包根据这个变量展现出不同的功能。

# 闭包使用注意事项
# 1、闭包中是不能修改外部作用域的局部变量的
# 2、返回函数不要引用任何循环变量，或者后续会发生变化的变量
