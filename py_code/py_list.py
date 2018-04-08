# -*- coding:utf-8 -*-

'''
   @author: xt
   @data : 2016-7-4
   @capacity: 列表推导式
   [表达式 for 变量 in 列表]   或者  [表达式 for 变量 in 列表 if 条件]
   表达式:
   [表达式 for 变量 in 列表 if <条件> else if <条件>]
'''


li = range(1, 10)

print [x**2 for x in li]

print [x**2 for x in li if x > 5]

# 字典强转成列表 {'a':'b'} --list-->[('a','b')]
print [(x, x*10) for x in li]
print dict([(x, x*10) for x in li])


print [(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8]

vec = [2, 4, 6]

vec2 = [4, 3, -9]

sq = [vec[i]+vec2[i] for i in range(len(vec))]
print sq

print [x*y for x in [1, 2, 3] for y in [1, 2, 3]]

testList = [1, 2, 3, 4]

print('.....')

def mul2(x):
    return x*2
print [mul2(i) for i in testList]