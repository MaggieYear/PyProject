#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game_execute import GameExecute
from vote_execute import VoteExecute
import random


"""游戏控制器"""

if __name__ == '__main__':
    print "---------prepare for game-------------"

    while True:

        # 输入游戏人数
        user_count = input('请输入游戏人数：')

        if user_count < 3 :
            print '游戏人数不足三位！'
            continue
        else:
            #询问游戏是否开始
            is_start = input("现在开始?")
            print('is_start:' + is_start)
            print( cmp(is_start, "yes"))
            if cmp(is_start,'yes') == 0:
                #开始游戏
                print "游戏开始啦！"

                gameExecute = GameExecute()
                #分配角色（不显示）
                _user_list = gameExecute.createUser(user_count)
                #分配关键词
                user_list = gameExecute.createKeyWord(_user_list)

                # 当前用户的id
                user_id = random.randint(0, (user_count - 1))
                #print '当前用户id：' + str(user_id)
                user = user_list[user_id]
                print str(user_id) + '你的关键词：' + str(user.key_word)

                is_continue = True

                while is_continue:
                    #发言
                    user_talk = raw_input("请发言：")

                    print (str(user_id) + ":" + user_talk)
                   # print ("玩家" + str(user.id) + "发言：" + user_talk)
                    #其他玩家发言
                    gameExecute.userTalk(user_list,user_id)

                    #投票
                    cur_vote = input('请投票：')
                    voteExecute = VoteExecute()

                    result = voteExecute.castVote(user, cur_vote)

                    #模拟其他玩家投票
                    for other_user in user_list:
                        voteExecute.simulateCastVote(other_user.id, user_list)

                    # 分析投票结果
                    vote = voteExecute.analysisVote(user_id)
                    if vote is None:
                        # 判断当前用户角色
                        if user.role_id == 1:
                            # 卧底
                            print "你是卧底，已被找出，平民胜利！"
                        else:
                            print "你是平民还被淘汰了！好冤！"

                        print "游戏结束"
                        is_continue = False
                        break
                    else:
                        # 判断剩下多少玩家
                        if len(user_list) == 2:
                            print "只剩下两个人啦，卧底胜利！"
                            is_continue = False
                            break
                        else:
                            #核对user列表，删掉已经删除的。
                            for user in user_list:
                                if vote[0] == user.id:
                                    print str(user.id) + "被淘汰了"
                                    user_list.remove(user)
                                    if len(user_list) == 2:
                                        print "只剩下两个人啦，卧底胜利！"
                                        is_continue = False
                                        break
                            print "剩下" + str(len(user_list)) + "个玩家"
                            # 接着下一轮
                            print "下一轮>>>>>>>"

            else:
                pass