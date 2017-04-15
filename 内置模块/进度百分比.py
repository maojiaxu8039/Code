# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/13 12:34
# @Author  : maojx
# @Site    : 
# @File    : 进度百分比.py
# @Software: PyCharm
import sys
import time


def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = '\r%d%%' % (rate_num,)
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(0, 100):
        time.sleep(0.1)
        view_bar(i, 100)
