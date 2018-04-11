#!/usr/bin/env python
# -*- coding: utf-8 -*-
from user_role import User
from user_role import Role
import time

"""
（1）分配平民词语和卧底词语
（2）玩家依次发言
（3）根据发言投票认为谁是卧底
（4）得到票数最多的玩家出局
（5）出局玩家刚好是卧底则平民胜利，如果出局玩家是平民则被冤死并继续第2步，当剩下的平民只有1个卧底时胜利。
"""

class GameExecute:

    def __init__(self):
        self.undercover_count = 0
        self.undercover_word = ""
        self.civilian_count = 0
        self.civilian_word = ""
        self.user_list = []
    """
    游戏启动引擎
    """
    #生成关键词(面对角色的单例模式）
    def createKeyWord(self,user_list):
        self.undercover_word = "狗子"
        self.civilian_word = "柴狗"
        for user in user_list:

            if user.role_id == 1:
                # 卧底
                user.key_word = self.undercover_word
            else:
                # 平民
                user.key_word = self.civilian_word
            user_list[user.id] = user
        return user_list

    #分配带角色的玩家
    def createUser(self,user_count):
        undercover_count = 0
        civilian_count = 0
        if user_count % 2 == 0:
            # 玩家数为偶数
            #  角色用户对半分
            undercover_count = (user_count / 2)
            civilian_count = (user_count / 2)
        else:
            undercover_count = (user_count / 2)
            civilian_count =  undercover_count + 1

        cur_id = user_count
        for  undercover_count in range(0, undercover_count):
            user = User(cur_id,1)
            self.user_list.append(user)
            cur_id -= 1
        print str(cur_id) + '卧底数'+str(len(self.user_list))

        for civilian_count in range(0, civilian_count):
            user = User(cur_id, 0)
            self.user_list.append(user)
            cur_id -= 1
        print str(cur_id) + '总用户数' + str(len(self.user_list))

        return self.user_list

    #其他玩家发言
    def userTalk(self,user_list,cur_user_id):

        for user in user_list:
            if user.id != cur_user_id:
                content = user.talk()
                time.sleep(2)
                print (str(user.id) + ":" + content)







