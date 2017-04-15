#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/19 23:57
# @Author  : maojx
# @Site    : 
# @File    : collection.py
# @Software: PyCharm

"""
collections是Python内建的一个集合模块，提供了许多有用的集合类
"""

# namedtuple 表示坐标

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print(p.x)

# deque 使用list存储数据时,按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储,数据量大的时候,插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表,合适用于队列和栈：

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# deque除了实现list的append()和pop()外,还支持appendleft()
# 和popleft(),这样就可以非常高效地往头部添加或删除元素。


# defaultdaict 使用dict时,如果引用的key不存在，就会抛出keyError。如果希望key不存在时，
# 返回一个默认值,就可以用defaultdict:
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # key1存在
print(dd['key2'])  # key2不存在，返回默认值"N/A"

# OrderedDict使用dict时,key是无序的。子啊对dict做迭代时，我们无法确定
# key的顺序。如果要保持key的顺序,可以用OrderedDict:
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # dict的key是无序的
od = OrderedDict[('a', 1), ('b', 2), ('c', 3)]
print(od)  # OrderedDict的key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# OrderedDict的Key会按照插入的顺序排列,不是Key本身排序
# OrderedDict可以实现一个FIFO(先进先出)的dict,当容量超出
# 限制时,先删除最早添加的key：

from collections import OrderedDict


class LastUpdatedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove', last)
        if containsKey:
            del self[key]
            print('set', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter是一个简单的计数器,例如统计字符出现的个数：
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

# Counter实际上也是dict的一个子类,上面的结果可以看出,字符
