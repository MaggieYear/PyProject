#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yekiki'
from game_execute import GameExecute
from vote_execute import VoteExecute
import random
from key_word import KeyWords

class GameRun:
    """游戏控制器"""

    def __init__(self):
        self.player_count = 0  # 玩家数量
        self.user_list = []
        self.cur_user = None  # 当前玩家对象
        self.cur_id = 0  # 当前玩家id
        self.keyword_index = 0  # 当局游戏关键字索引
        # 单例模式
        # 游戏核心模块
        self.gameExecute = GameExecute()
        # 投票和判断输赢模块
        self.voteExecute = VoteExecute()

    # 分配角色和关键字
    def assign_role(self):

        # 关键字模块
        key_word = KeyWords()
        self.keyword_index = key_word.index

        # 分配角色（不显示）
        _user_list = self.gameExecute.create_user(self.player_count)
        # 分配关键词
        user_list = self.gameExecute.create_keyword(_user_list, key_word.index)

        # 当前用户的id
        user_id = random.randint(0, (self.player_count - 1))

        user = user_list[user_id]

        self.cur_id = user_id
        self.cur_user = user
        self.user_list = user_list

        return user.key_word

    # 玩家发言
    def user_talk(self):
        content_list = self.gameExecute.user_talk(self.user_list, self.cur_id, self.keyword_index)
        return content_list

    # 玩家投票
    def player_vote(self, vote_num):
        result = self.voteExecute.cast_vote(self.cur_id, vote_num)
        return result

    # 模拟其他玩家投票
    def simulate_cast_vote(self, user_id):
        vote_content = self.voteExecute.simulate_cast_vote(user_id, self.user_list)
        return vote_content

    # 分析投票结果（输赢判断）
    def analysis_vote(self):
        # 分析投票结果
        vote = self.voteExecute.analysis_vote()
        return vote

    # 对票数进行清零
    def clear(self):
        self.voteExecute.clear_vote()
