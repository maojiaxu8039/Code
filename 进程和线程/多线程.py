#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/21 14:07
# @Author  : maojx
# @Site    : 
# @File    : 多线程.py
# @Software: PyCharm

"""
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
"""
"""
直接调用
"""
import threading
import time


def sayhi(num):  # 定义每个线程要运行的函数

    print("running on number:%s" % num)

    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
    t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
    '''
    循环创建多线程
    t_list = []
    for i in range(10):
        t = threading.Thread(target=sayhi, args[i,])
        t.start()
        t_list.append(t)
    for i in t_list:
        i.join()

    '''

    t1.start()  # 启动线程
    t2.start()  # 启动另一个线程

    print(t1.getName())  # 获取线程名
    print(t2.getName())

"""
继承式调用
"""
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  # 定义每个线程要运行的函数

        print("running on number:%s" % self.num)

        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

"""
多线程锁
"""
lock = threading.lock()  # 创建锁
lock.acquire()  # 获取锁
lock.release()  # 释放
