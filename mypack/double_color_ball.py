#!/usr/bin/env python
#coding:utf-8
import random
import time
import os

"""
1、生成六个不同随机数值的红色球（1-33）。
2、生成一个随机数值的蓝色球（1-16）
3、时间生成类
4、文件写出类
5、主方法

"""

class CreateBall:
    """双色球生成类"""
    def __init__(self,obj):
        self.color = obj.color
        self.count = obj.count
        self.range = obj.range
        self.flag = obj.flag

    @staticmethod
    def random_number(self):
        return random.randint(self.range[0], self.range[1])

    #[(9, 'red'), (19, 'red'), (22, 'red'), (27, 'red'), (27, 'red'), (31, 'red')]
    def create_ball(self):
        list = []
        while self.count > 0:
            number = CreateBall.random_number(self)
            if number not in list:
                list.append((number,self.color))
                self.count -= 1
        #对列表进行排序
        list = sorted(list)
        return list

    #[1, 2, 3, 10, 20, 24]
    def create_simple_ball(self):
        list = []
        while self.count > 0:
            number = CreateBall.random_number(self)
            if number not in list:
                list.append(number)
                self.count -= 1
        #对列表进行排序
        list = sorted(list)
        return list

class RedBall:
    """红色球类"""
    def __init__(self):
        self.color = 'red'
        self.count = 6
        self.range = [1,33]
        self.flag = ''

class BlueBall:
    """蓝色球类"""
    def __init__(self):
        self.color='blue'
        self.count = 1
        self.range = [1, 16]
        self.flag = '+'

def getLocalTime():
    # localtime = time.localtime(time.time())
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current time:", localtime)
    return localtime

#写到文件里
def save( path, filename, content):
    if not os.path.exists(path):
        os.makedirs(path)

    file_path = path + '/' + filename
    f = open(file_path, 'a+')
    f.write(content)
    f.close()

def run():
    # 一个存放双色球的列表
    list = []
    # 生成六个红色球，放到列表里
    red_list = CreateBall(RedBall()).create_simple_ball()

    #生成一个蓝色球，放到列表里
    blue_list = CreateBall(BlueBall()).create_simple_ball()
    #标记蓝色球
    blue_list[0] = BlueBall().flag + str(blue_list[0])

    list = red_list + blue_list
    print list
    #获得当前时间
    current_time = getLocalTime()
    content = "[" + current_time + "]\n" + str(list) +"\n"

    path = 'ball'
    filename = 'colorball.txt'
    #写出到文件
    save( path, filename,content)

if __name__ == '__main__':
    run()
