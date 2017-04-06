#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 21:34
# @Author  : maojx
# @Site    : 
# @File    : csv操作.py
# @Software: PyCharm

import csv

# 创建一个Reader对象,Reader对像让你迭代遍历CSV文件中的每一行
exampleFiel = open('./example.csv')
exampleReader = csv.reader(exampleFiel)
exampleData = list(exampleReader)
print(exampleData)

print(exampleData[0][0])

# for 循环中从Reader对象读取数据这样避免将正规文件一次性装入内存中
exampleFiel = open('./example.csv')
exampleReader = csv.reader(exampleFiel)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + '' + str(row))

# ps 需要为open()函数的newline关键字参数传入一个空字符串，如果忘记设置行距将有两倍
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'bam'])
outputWriter.writerow(['Hello,word!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
