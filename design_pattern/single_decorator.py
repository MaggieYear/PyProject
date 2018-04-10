#!/usr/bin/env python
#coding:utf-8
from functools import wraps

def singleton(cls):
    instance = {}
    @wraps(cls)
    def getinstance(*args,**kw):
        if cls not in instance:
            instance[cls] = cls(*args,**kw)
        return instance[cls]
    return getinstance

@singleton
class MyClass(object):
    """
    定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，
    该函数会判断某个类是否在字典 instances 中，
    如果不存在，则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，
    否则，直接返回 instances[cls]。
    """
    a = 1


