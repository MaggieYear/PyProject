#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
（1）分配平民词语和卧底词语
（2）玩家依次发言
（3）根据发言投票认为谁是卧底
（4）得到票数最多的玩家出局
（5）出局玩家刚好是卧底则平民胜利，如果出局玩家是平民则被冤死并继续第2步，当剩下的平民只有1个卧底时胜利。
"""

class Role:

    """
    角色类
    卧底
    平民
    具有能力：分配关键字和发言
    """
    def __init__(self,key_word="",role_id = 0):
        self.key_word = key_word
        self.role_id = role_id  #平民-0；卧底-1；

    #发言
    def talk(self):
        if self.role_id == 0:
            #平民
            word_list = ["四条腿","会走的","人们都很喜欢","被用来称呼人","别人的男朋友","接地气的动物"]
            index = random.randint(0, len(word_list)-1)
            return word_list[index]
        elif self.role_id == 1:
            #卧底
            word_list = ["很好几种颜色","讨人喜欢","不太粘人","会看家护院","喜欢散步","喜欢同伴玩"]
            index = random.randint(0, len(word_list)-1)
            return word_list[index]
        else:
            return None

class User(Role):
    """
    用户类
    玩家
    """
    def __init__(self,id,role_id):
        self.id = id  #玩家id
        self.role_id = role_id

