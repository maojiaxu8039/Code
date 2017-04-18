#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/17 18:14
# @Author  : maojx
# @Site    : 
# @File    : 分布式进程.py
# @Software: PyCharm
"""
在Thread和Process中，应当优选Process，
因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
"""

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的列队
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册导网络上,calleble参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000,设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.radint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result列队读取结果
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭
manager.shutdown()
print('master exit')
"""
创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
"""
import time, sys, queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue,所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器,也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 端口和验证吗注意保持与task_mester.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')

# 从网络链接
m.connect()

# 获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task列队取任务,并把结果写入result列队:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

print('worker exit')


