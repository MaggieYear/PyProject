#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game_execute import GameExecute
from vote_execute import VoteExecute
import random
from key_word import KeyWords


class GameRun:
    """游戏控制器"""

    # 单例模式
    # 游戏核心模块
    gameExecute = GameExecute()

    # 投票和判断输赢模块
    voteExecute = VoteExecute()

    def __int__(self):
        self.player_count = 0  #玩家数量
        self.user_list = []
        self.cur_user = None #当前玩家对象
        self.cur_id = 0 #当前玩家id
        self.keyword_index = 0  #当局游戏关键字索引

    def inputGamePlayer(self):
        # 输入游戏人数
        user_count = input('请输入游戏人数：')
        if user_count >= 7:
            self.player_count = user_count
            return True
        else:
            print '游戏人数不足七位！'
            return False

    #开始游戏
    def startGame(self):
        # 询问游戏是否开始
        is_start = input("现在开始?")

        if cmp(is_start, 'yes') == 0:
            # 开始游戏
            print "游戏开始啦！"
            return True
        else:
            return False

    #分配角色和关键字
    def assignRole(self):

        # 关键字模块
        keyWord = KeyWords()
        self.keyword_index = keyWord.index

        # 分配角色（不显示）
        _user_list = self.gameExecute.createUser(self.player_count)
        # 分配关键词
        user_list = self.gameExecute.createKeyWord(_user_list, keyWord.index)

        # 当前用户的id
        user_id = random.randint(0, (self.player_count - 1))

        user = user_list[user_id]
        print str(user_id) + '你的关键词：' + str(user.key_word)

        self.cur_id = user_id
        self.cur_user = user
        self.user_list = user_list

    #玩家发言
    def playerDisplay(self):
        # 发言
        user_talk = raw_input("请发言：")

        print (str(self.cur_id) + ":" + user_talk)

        # 其他玩家发言
        self.gameExecute.userTalk(self.user_list , self.cur_id, self.keyword_index)

    #玩家投票
    def playerVote(self):
        # 投票
        cur_vote = input('请投票：')

        result = self.voteExecute.castVote(self.cur_user, cur_vote)

        # 模拟其他玩家投票
        for other_user in self.user_list:
            self.voteExecute.simulateCastVote(other_user.id, self.user_list)

    #分析投票结果（输赢判断）
    def analysisVote(self):
        # 分析投票结果

        vote = self.voteExecute.analysisVote()
        if vote is None:
            # 平票
            # 不淘汰进入下一轮
            print "下一轮>>>>>>>"
            return True

        else:
            # 判断当前用户角色
            if vote[0] == self.cur_id:
                if self.cur_user.role_id == 1:
                    # 卧底
                    print "你是卧底，已被找出，平民胜利！"
                else:
                    print "你是平民还被淘汰了！好冤！"

                return False

            else:
                # 判断剩下多少玩家
                if len(self.user_list) == 2:
                    print "只剩下两个人啦，卧底胜利！"
                    is_continue = False
                    return False
                else:
                    # 核对user列表，删掉已经删除的。
                    for user in self.user_list:
                        if vote[0] == user.id:
                            print str(user.id) + "被淘汰了"
                            self.user_list.remove(user)
                            if len(self.user_list) == 2:
                                print "只剩下两个人啦，卧底胜利！"
                                is_continue = False
                                break
                    print "剩下" + str(len(self.user_list)) + "个玩家"
                    # 接着下一轮
                    print "下一轮>>>>>>>"
                    return True

    def run(self):
        print "---------prepare for game-------------"

        while True:
            # 输入玩家数量
            result = self.inputGamePlayer()
            if result:
                result = self.startGame()
                if result:
                    # 游戏开始
                    # 分配角色和关键字
                    self.assignRole()

                    while True:
                        # 玩家发言
                        self.playerDisplay()
                        #玩家投票
                        self.playerVote()
                        #分析投票结果
                        result = self.analysisVote()
                        if result is False:
                            break
                        else:
                            continue
                else:
                    #游戏不开始，跳出
                    break
            else:
                #玩家数量不足，继续输入
                continue



if __name__ == '__main__':
    gameRun = GameRun()
    gameRun.run()