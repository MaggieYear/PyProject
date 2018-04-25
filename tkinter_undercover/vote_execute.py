#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yekiki'
import random

"""
（1）分配平民词语和卧底词语
（2）玩家依次发言
（3）投票认为谁是卧底
（4）得到票数最多的玩家出局，如果最高票数有两个，则进行下一轮。
（5）出局玩家刚好是卧底则平民胜利，如果出局玩家是平民则被冤死继续下一轮。
（6）当剩下的玩家只有两个并且有卧底时，卧底胜利。
"""

class VoteExecute:
    """投票和输赢机制模块"""

    def __init__(self):
        self._vote_dict = {}

    @property
    def vote_dict(self):
        return self._vote_dict

    @vote_dict.setter
    def vote_dict(self, vote_dict):
        self._vote_dict = vote_dict

    # 投票
    def cast_vote(self, user_id, vote_num):
        vote_dict = self.vote_dict

        # 判断投票是否为当前ID
        if user_id == vote_num:
            return False
        else:
            # self.vote_num = vote_num
            if vote_dict. has_key(vote_num) is False:
                vote_dict[vote_num] = 1
            else:
                vote_dict[vote_num] += 1
            self.vote_dict = vote_dict
            # print '---------------'
            # print self.vote_dict
            return True

    # 模拟其他用户投票
    def simulate_cast_vote(self, user_id, user_list):

        random_index = random.randint(0, len(user_list)-1)
        # 模拟票
        tmp_vote = user_list[random_index].id
        if tmp_vote != user_id:
            self.cast_vote(user_id, tmp_vote)
            return str(user_id) + "号玩家正在投票" + str(tmp_vote)
        else:
            # print 'simulate_cast_vote~~~~~~~~~~~~'
            return None


    # 分析投票结果
    def analysis_vote(self):
        # 对投票结果进行排序,字典转成list
        vote_list = sorted(self.vote_dict.items(), key=lambda item: item[1])

        # 取出最后一个元素（票数最多的）
        max_index = len(vote_list)-1
        max_vote = vote_list[max_index]
        print '票数最多'
        print max_vote
        # 取出倒数第二个元素，判断是否平票
        max_index2 = len(vote_list) - 2
        max_vote2 = vote_list[max_index2]
        print '票数第二多'
        print max_vote2
        if max_vote2[1] == max_vote[1]:  # 判断是否平票
            return None
        else:
            return max_vote

    # 对票数进行清零
    def clear_vote(self):
        self.vote_dict = {}
