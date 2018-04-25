#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yekiki'
from user_role import User
from key_word import KeyWords
import random

"""
（1）分配平民词语和卧底词语
（2）玩家依次发言
（3）投票认为谁是卧底
（4）得到票数最多的玩家出局，如果最高票数有两个，则进行下一轮。
（5）出局玩家刚好是卧底则平民胜利，如果出局玩家是平民则被冤死继续下一轮。
（6）当剩下的玩家只有两个并且有卧底时，卧底胜利。

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
    # 生成关键词(面对角色的单例模式）
    def create_keyword(self, user_list, keyword_index):
        key_word = KeyWords()
        self.civilian_word = key_word.key_word[keyword_index][0]
        self.undercover_word = key_word.key_word[keyword_index][1]

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

    # 分配带角色的玩家
    def create_user(self, user_count):

        civilian_count = user_count - 1
        # 当前id (0, user_count-1)
        cur_id = 0

        # 分配卧底
        user = User(cur_id, 1)
        self.user_list.append(user)
        cur_id += 1

        # 分配平民角色
        for civilian_count in range(0, civilian_count):
            user = User(cur_id, 0)
            self.user_list.append(user)
            cur_id += 1
            civilian_count -= 1
        # print str(cur_id) + '总用户数' + str(len(self.user_list))

        return self.user_list

    # 模拟玩家发言
    def user_talk(self, user_list, cur_user_id, keyword_index):
        # 存放发言的列表（发言要唯一，不重复）

        content_tuple = ()
        temp_list = []
        content_list = []
        key_word = KeyWords()
        contents = key_word.getKeyContent(keyword_index)  # list
        for user in user_list:
            # 除了当前玩家，其他玩家发言
            if user.id == cur_user_id:
                continue
            else:
                flag = True
                while flag:
                    words = contents[user.role_id]  # 元祖
                    index = random.randint(0, (len(words) - 1))
                    content = words[index]
                    # 如果和已经发言的描述重复，则继续模拟发言
                    if content not in temp_list:
                        content_tuple = (user.id, content)
                        temp_list.append(content)
                        content_list.append(content_tuple)
                        flag = False
        return content_list


