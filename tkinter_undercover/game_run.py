#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game_execute import GameExecute
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
                user_list = gameExecute.createUser(user_count)

                #分配关键词
                user_list = gameExecute.createKeyWord(user_list)

                # 当前用户的id
                user_id = random.randint(0, (user_count - 1))
                #print '当前用户id：' + str(user_id)
                user = user_list[user_id]
                print '关键词：' + str(user.key_word)

                print '------------'
                for u in user_list:
                    print ">>" + str(u.id)
                print '------------'
                #发言
                user_talk = raw_input("请发言：")

                print (str(user_id) + ":" + user_talk)
               # print ("玩家" + str(user.id) + "发言：" + user_talk)
                #其他玩家发言
                gameExecute.userTalk(user_list,user_id)

            else:
                break