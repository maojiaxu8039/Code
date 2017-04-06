#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/18 1:25
# @Author  : maojx
# @Site    : 
# @File    : 文件操作.py
# @Software: PyCharm

"""
操作文件
1、打开文件
2、操作文件
"""

'''
文件句柄 = open('文件路径', '模式')
注：python中打开文件有两种方式，即：open(...) 和  file(...) ，本质上前者在内部会调用后者来进行文件操作，推荐使用 open。
打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件
r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）
rb
wb
ab

'''
# 读文件
file = open('文件路径', '标识符')
file.read()
file.close()

# with语句自动调用close()方法
with open('文件路径', '标识符') as file:
    print(file.read())
# python2.7之后with又支持同时对多个文件的上下文进行管理
with open('文件路径', '标识符') as file, open('文件路径2', '标识符') as file1:
    pass

# read()一次性读取最方便;不确定文件大小read(size)比较保险；如果是配置文件调用readlines()最方便
for line in file.readines():
    print(line.strip())  # 把末尾的\n去掉

# 读取二进制文件
file = open('文件路径', 'rb')
file.read()

# 字符编码要读取非UTF-8编码的文件需要给open()函数传入encoding参数
file = open('文件路径', 'r', encoding='gbk')

# 遇到编码不规范的文件遇到UnicdeDecodeError,因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
file = open('文件路径', 'r', encoding='gbk', errors='ignore')

# 写文件
file = open('文件路径', 'w')

file.write('Hello word!')
file.close()
