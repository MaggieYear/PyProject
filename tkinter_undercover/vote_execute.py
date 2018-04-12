#!/usr/bin/env python
# -*- coding: utf-8 -*-

from user_role import User
import operator
import random

"""
投票的引擎
1、模拟玩家投票
2、汇总票数
3、淘汰票数最多的玩家，出局玩家是卧底，则平民胜利。
4、判断剩余角色人数，游戏定局
    当剩两个玩家且有卧底时，卧底胜利
"""

class VoteExecute:

    def __init__(self):
        self.user_id = 0
        self._vote_num = 0
        self.vote_dict = {}

    @property
    def vote_num(self):
        return self._vote_num

    #投票
    def castVote(self,user_id,vote_num):

        #判断投票是否为当前ID
        if user_id == vote_num:
            return False
        else:
            self._vote_num = vote_num
            if self.vote_dict.has_key(vote_num) is False:
                self.vote_dict[vote_num] = 1
            else:
                self.vote_dict[vote_num] += 1

            #print self.vote_dict
        return True

    #模拟其他用户投票
    def simulateCastVote(self,user_id,user_list):

        random_index = random.randint(0,len(user_list)-1)
        # 模拟票
        tmp_vote = user_list[random_index].id
        if tmp_vote != user_id:
            print str(user_id) + "玩家正在投票" + str(tmp_vote)
            self.castVote(user_id, tmp_vote)

    #分析投票结果
    def analysisVote(self,cur_id):
        #对投票结果进行排序,字典转成list
        vote_list = sorted(self.vote_dict.items(),key=lambda item:item[1])
        #取出最后一个元素（票数最多的）
        max_index = len(vote_list)-1
        max_vote = vote_list[max_index]
        print max_vote

        # 判断是否是当前玩家
        if max_vote[0] == cur_id:
            print "当前玩家被淘汰"
            return None
        else:
            print "其他玩家被淘汰"
            return max_vote #（3,2）user_id为3的用户获得2票

if __name__ == '__main__':

    voteExecute = VoteExecute()

    user = User(1,0)
    vote_num = 4
    result = voteExecute.castVote(user.id,vote_num)
    print result

    user = User(2, 0)
    vote_num = 5
    result = voteExecute.castVote(user.id,vote_num)
    print result

    user = User(3, 1)
    vote_num = 4
    result = voteExecute.castVote(user.id,vote_num)
    print result

    #分析投票结果
    cur_id = 3  #当前用户ID
    user_list = voteExecute.analysisVote(cur_id)
    if user_list is None:
        print "游戏结束"
        #判断当前用户角色
        if user.role_id == 1:
            #卧底
            print "卧底已被找出，平民胜利！"
    else:
        #判断剩下多少玩家
        if len(user_list) == 2:
            print "只剩下两个人啦，卧底胜利！"
        else:
            #接着下一轮
            pass
