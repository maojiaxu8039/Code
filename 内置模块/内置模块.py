#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 9:36
# @Author  : maojx
# @Site    : 
# @File    : 内置模块.py
# @Software: PyCharm
"""
什么是模块

模块，用一堆代码实现某个功能的代码集合

类似域函数式编程和面向过程编程，函数式编程则完成一个功能，其他 代码用来调用即可，
提供了代码的重用性和代码间的耦合。而对于一个复杂的功能来说，可能需要多个函数才能完成
(函数可以在不同的.py文件中),n个.py文件组成的代码集合就称为模块。
"""

"""
安装模块
pip install  模块名
"""

"""
导入模块
import module
from module.xx.xx import xx
from module.xx.xx import xx as rename
from module.xx.xx import *

导入模块其实就是告诉Python解释器区解释那个py文件
导入一个py文件，解释器解释该py文件
导入一个包，解释器解释该包下的_init_.py文件
"""

# 默认情况下，python解释器会搜索当前目录，所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：、
import sys

sys.path
print(sys.path)

# 添加自己的搜索目录有两种方法：
# 1、直接修改sys.path,要添加搜索目录；
sys.path.append('/User/micheal/my_py_scripts')  # 第二种方法是设置环境变量PYTHONPATH,该环境变量的内容被自动添加导模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径,Python自己本身的搜索路径不受影响。

# 获取当前文件的路径
print(__file__)
