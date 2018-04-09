#!/usr/bin/env python
#coding:utf-8

class A:
    def foo(self):
        print "duck A"

class B(A):
    def foo(self):
        print "duck B"

class C(A):
    def foo(self):
        print "duck C"

class D(A):
    pass

class E:
    def foo(self):
        print "like a duck"

def test(obj):
    obj.foo()


a = A()
b = B()
c = C()
d = D()
e = E()

test(a)
test(b)
test(c)
test(d)
test(e)

"""
d 没有继承A,d不是鸭子，但是它也有foo方法，它也能像鸭子一样游泳、嘎嘎叫，所以d 也能视为鸭子，和a,b,c变量一样。
鸭子类型也就是，不管继承什么，是什么变量，只要能像鸭子一样游泳、嘎嘎叫，就是鸭子。
"""