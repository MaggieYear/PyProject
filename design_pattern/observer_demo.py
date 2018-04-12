#!/usr/bin/env python
#coding:utf-8

# observer pattern

class subject():
    def __init__(self, dat):
        self.listobj = list()  # 主题中的列表变量用来存储观察者
        self.dat = dat  # 主题中的数据变化时，需要通知观察者

    def registerObject(self, obj):
        self.listobj.append(obj)  # 实现订阅主题的函数

    def removeObject(self, obj):
        pass

    def notifyObservers(self):  # 通知各个观察者数据已经发生变化，观察者相应需要更新自己的数据
        for i in range(len(self.listobj)):
            self.listobj[i].update()

    def setdat(self, new_dat):  # 设置数据
        if self.dat != new_dat:
            self.dat = new_dat
            self.notifyObservers() #数据一旦改动，就通知观察者


class observer():  # 观察者
    def __init__(self, sub):  # 观察者初始化时，需要订阅主题
        self.sub = sub
        self.sub.registerObject(self)
        self.updateContent = self.sub.dat

    def update(self):  # 观察者更新
        self.updateContent = self.sub.dat

    def display(self,index):
        print "-------读者"+str(index)+"-----------"
        print self.updateContent


if __name__ == "__main__":
    su = subject('新报纸')
    ob1 = observer(su)
    ob1.display(1)
    ob2 = observer(su)
    ob2.display(2)

    su.setdat('新杂志')
    ob1.display(1)
    ob2.display(2)