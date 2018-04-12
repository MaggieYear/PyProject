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

        for _user in user_list:

            if _user.role_id == 1:
                # 卧底
                _user.key_word = self.undercover_word
            else:
                # 平民
                _user.key_word = self.civilian_word
            user_list[_user.id] = _user

        self.user_list = user_list
        return user_list

    #分配带角色的玩家
    def createUser(self,user_count):
        undercover_count = 1
        civilian_count = user_count - 1
        #当前id (0, user_count-1)
        cur_id = 0

        #分配卧底
        user = User(cur_id,1)
        self.user_list.append(user)
        cur_id += 1

        #分配平民角色
        for civilian_count in range(0, civilian_count):
            user = User(cur_id, 0)
            self.user_list.append(user)
            cur_id += 1
            civilian_count -= 1
        print str(cur_id) + '总用户数' + str(len(self.user_list))

        return self.user_list

    #模拟玩家发言
    def userTalk(self,user_list,cur_user_id):

        for user in user_list:
            if user.id != cur_user_id:
                content = user.talk()
                time.sleep(2)
                print (str(user.id) + ":" + content)







