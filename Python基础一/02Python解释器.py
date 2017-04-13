#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 10:10
# @Author  : maojx
# @Site    : 
# @File    : 02Python解释器.py
# @Software: PyCharm
"""
如果在linux想要类似于执行shell脚本一样执行python脚本，例： ./hello.py ，那么就需要在 hello.py 文件的头部指定解释器，如下：
#!/usr/bin/env python
print ("hello,world")

如此一来，执行： ./hello.py 即可
ps：执行前需给予 hello.py 执行权限，chmod 755 hello.py
"""