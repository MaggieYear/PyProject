#!/usr/bin/env python
#coding:utf-8

#装饰器
def deco(a_class):
    class NewClass:
        def __init__(self,age,color):
            self.wrapped = a_class(age)
            self.color = color

        def display(self):
            print(self.color)
            print(self.wrapped.age)

    return NewClass

#装饰器装饰类
@deco
class Cat:
    def __init__(self,age):
        self.age = age

    def display(self):
        print(self.age)

if __name__ == '__main__':
    c = Cat(12,'black')
    c.display()