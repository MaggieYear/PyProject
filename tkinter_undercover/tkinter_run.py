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

    player_count = 0  # 玩家数量
    user_list = []
    cur_user = None  # 当前玩家对象
    cur_id = 0  # 当前玩家id
    keyword_index = 0  # 当局游戏关键字索引

    # def __int__(self):

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

    # 分析投票结果（输赢判断）
    def analysis_vote(self):
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

                    return False
                else:
                    # 核对user列表，删掉已经删除的。
                    for user in self.user_list:
                        if vote[0] == user.id:
                            print str(user.id) + "被淘汰了"
                            self.user_list.remove(user)
                            if len(self.user_list) == 2:
                                print "只剩下两个人啦，卧底胜利！"

                                break
                    print "剩下" + str(len(self.user_list)) + "个玩家"
                    # 接着下一轮
                    print "下一轮>>>>>>>"
                    return True

    def run(self):

        print "---------prepare for game-------------"

        # 绘制窗体和组件
        game_view = GameView()
        game_view.draw()
        # 获得玩家数量
        player_count = game_view.get_player_count()

        print player_count

        if player_count != 0:
            self.player_count = player_count
            # 游戏开始
            # 分配角色和关键字
            user_keyword = self.assign_role()
            # 提示当前玩家关键字
            game_view.display_message('您获得的关键字是：' + user_keyword )

            while True:
                # 玩家发言
                print "请输入描述>>>>>>>"
                game_view.player_talk()
                keyword_des = game_view.keyword_des

                # 玩家投票
                self.player_vote()
                # 分析投票结果
                result = self.analysis_vote()
                if result is False:
                    break
                else:
                    continue
if __name__ == '__main__':
    gameRun = GameRun()
    gameRun.run()
