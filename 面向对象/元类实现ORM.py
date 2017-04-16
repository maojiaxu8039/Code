#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/16 15:39
# @Author  : maojx
# @Site    : 
# @File    : 元类实现ORM.py
# @Software: PyCharm

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


st = StringField(name='哈哈')


class ModelMetaclass(type):
    # 当前准备创建的类的对象,类的名字,类继承的父类集合,类的方法集合。
    def __new__(cls, name, bases, attrs):
        # 把表名保存到__table__中，这里简化为表名默认为类名
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


"""
当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，
如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类
也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
"""


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
            # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        sql = 'insert into %s(%s)VALUES (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# testing code:
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

user=User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
print(user.items())
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()
