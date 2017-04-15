#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/19 15:17
# @Author  : maojx
# @Site    : 
# @File    : 反射.py
# @Software: PyCharm

"""
反射就是通过字符串获取到内存地址。
http://www.cnblogs.com/feixuelove1009/p/5576206.html
http://python.jobbole.com/82110/

hasattr
getattr
setattr
delattr
"""

import sys


class WebServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print("Server is starting...")

    def stop(self):
        print("Server is Stopping...")

    def restart(self):
        self.stop()
        self.start()


def test_run(self, name):
    print("running...", name)


if __name__ == "__main__":
    server = WebServer('localhost', 8080)
    # hasattr 判断有没有
    if hasattr(server, sys.argv[1]):
        # 获取server.start内存地址
        func = getattr(server, sys.argv[1])
        func()
    # 把方法绑定到类里
    setattr(server, 'gun', test_run)
    server.gun(server, "maojiaxu")

    delattr(server, 'host')
    print(server.host)

    delattr(server, 'stop')
    print(server.stop)
