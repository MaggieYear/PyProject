# -*- coding:utf-8 -*-

# a ='str'
# if a:
#     raise NameError('cuowu')
#
# def name(x,b=1):
#     pass

l = range(1, 11)  # 1-10
l2 = range(11, 21)  # 11-20
print len(l)
print len(l2)
print l
print l2
# 函数过程方
li = []
for x in l:
    if x > 5:
        li.append(x)
print li


def index(x, y):
    return x+y

print [x for x in l if x > 5]
print [l[x]+l2[x] for x in range(len(l))]  # 3.x -->list(tuple(1,11))
# print map(index(x, y), l, l2)
