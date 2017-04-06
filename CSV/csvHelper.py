#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/30 22:11
# @Author  : maojx
# @Site    : 
# @File    : csvHelper.py
# @Software: PyCharm

import csv
import os

# 可以递归创建目录
os.makedirs('headerRemoved', exist_ok=True)
# 列出目录下的所有文件和目录
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print(csvFilename)

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
