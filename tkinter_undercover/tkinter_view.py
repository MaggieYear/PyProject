#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter_run import GameRun
from str_utils import StrUtils
import tkMessageBox
import time
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

class GameView:
    """ 游戏绘制 """
    game_run = GameRun()
    #字符判断
    str_utils = StrUtils()

    def __init__(self):
        pass
        self.root = None
        self.input_text = None
        self.player_count = 0
        self.descr_text = None
        self.vote_text = None
        self.keyword_des = None
        self.user_list = None

    def draw(self):
        root = Tk()
        # 根窗口
        root.title('window with command')  # 主窗口标题
        root.geometry('400x400')  # 主窗口大小，中间的为英文字母x
        # 窗口尺寸固定
        # root.resizable(False, False)

        # 创建frame容器
        # frmT = Frame(width=400, height=200, bg='white')
        # frmB = Frame(width=400, height=200, bg='grey')
        #
        # frmT.grid(row=0, column=0,padx=1,pady=3)
        # frmB.grid(row=2, column=0)

        self.root = root
        # 绘制各种组件

        # 玩家数量文本框
        self.draw_input_count()

        # 开始按键
        self.draw_start()

        #结束按键
        self.draw_stop()

        # 用户发言文本框和按键
        self.play_talk_draw()
        # 用户投票文本框和按键
        self.draw_vote_button()
        # 输出文本框，显示运行内容
        self.draw_display(root)
        # 事件循环
        root.mainloop()

    # 开始按键
    def draw_start(self):
        # 次级窗口
        com = Button(self.root, text='开始游戏', command=self.start)
        com.pack(side=LEFT,expand=YES)  # 次级窗口的位置摆放位置
        com.place(relx=0.68, rely=0.6, anchor=NW)

    # 结束游戏按键
    def draw_stop(self):
        # 次级窗口
        com = Button(self.root, text='结束游戏', command=self.stop)
        com.pack(side=LEFT, expand=YES)  # 次级窗口的位置摆放位置
        com.place(relx=0.5, rely=0.93, anchor=CENTER)

    #开始按键触发事件
    def start(self):
        player_count = self.input_text.get()

        # 判断输入是否 为数字
        result = self.str_utils.is_number( unicode(player_count) )

        if result:
            player_count = int(player_count)
            if int(player_count) < 7:
                # 弹出窗口提示：游戏人数不足7人
                self.show_content('游戏人数不足7人')
                tkMessageBox.showinfo("提示", "游戏人数不足7人")
            else:
                self.game_run.player_count = player_count
                self.run()
        else:
            tkMessageBox.showinfo("提示", "请输入数字！")

    # 结束游戏按键触发事件
    def stop(self):
        exit()

    def get_player_count(self):
        player_count = self.input_text.get()
        player_count = int(player_count)
        if int(player_count) < 7:
            # 弹出窗口提示：游戏人数不足7人
            self.show_content('游戏人数不足7人')
            tkMessageBox.showinfo("提示", "游戏人数不足7人")
            return 0
        else:
            self.player_count = player_count
            return player_count

    # 玩家数量文本框
    def draw_input_count(self):
        label = Label(self.root, text="玩家数量(>=7)")
        label.pack(side=LEFT)
        label.place(relx=0.07, rely=0.6, anchor=NW)

        input_text = StringVar()
        input_player = Entry(self.root, textvariable=input_text)
        input_text.set("")
        input_player.pack(side=LEFT)
        input_player.place(relx=0.3, rely=0.6, anchor=NW)
        self.input_text = input_text

    # 投票文本框和按键
    def draw_vote_button(self):
        label = Label(self.root, text="投给哪个玩家：")
        label.pack()
        label.place(relx=0.07, rely=0.8, anchor=NW)

        vote_text = StringVar()
        input_vote = Entry(self.root, textvariable=vote_text)
        vote_text.set("")
        input_vote.pack(side=LEFT)
        input_vote.place(relx=0.3, rely=0.8, anchor=NW)
        self.vote_text = vote_text

        # 次级窗口
        com = Button(self.root, text='投票', command=self.vote_button_event)
        com.pack(side=LEFT)  # 次级窗口的位置摆放位置
        com.place(relx=0.68, rely=0.8, anchor=NW)

    # 用户发言文本框
    def play_talk_draw(self):
        label = Label(self.root, text="请描述关键字：")
        label.pack(side=LEFT)
        label.place(relx=0.07, rely=0.7, anchor=NW)

        descr_text = StringVar()
        input_descript = Entry(self.root, textvariable=descr_text)
        descr_text.set("")
        input_descript.pack(side=LEFT)
        input_descript.place(relx=0.3, rely=0.7, anchor=NW)
        self.descr_text = descr_text

        # 次级窗口
        com = Button(self.root, text='发言', command=self.player_talk)
        com.pack(side=LEFT)  # 次级窗口的位置摆放位置
        com.place(relx=0.68, rely=0.7, anchor=NW)

    # 发言按键
    def player_talk(self):
        keyword_des = self.descr_text.get()
        if keyword_des is '' or keyword_des is None:
            self.show_content('请输入描述！')
        else:
            self.keyword_des = keyword_des
            print keyword_des
            # 显示发言
            self.show_content('您的发言：' + keyword_des)
            # 模拟其他玩家发言
            self.user_list = self.game_run.user_list
            # 其他玩家发言
            content_list = self.game_run.user_talk()
            for content in content_list:
                self.show_content(str(content[0]) + '号玩家的发言：' + content[1])
                time.sleep(1)
            self.show_content("请投票>>>>>")

    # 投票按键
    def vote_button_event(self):
        vote_num = self.vote_text.get()

        # 判断输入是否 为数字
        result = self.str_utils.is_number( unicode(vote_num) )
        if result:
            vote_num = int(vote_num)
            #当前玩家数量
            cur_players = len(self.game_run.user_list)
            print '当前玩家数量' + str(cur_players)
            # 判断玩家号是否存在
            if cur_players < vote_num:
                tkMessageBox.showinfo("提示", "玩家号不存在！")
                return
            #判断是否给自己投票
            if self.game_run.cur_id == vote_num:
                tkMessageBox.showinfo("提示", "请不要投票给自己！")
                return

            # 当前玩家投票
            result = self.game_run.player_vote(vote_num)
            if result:
                self.show_content('您投给了'+ str(vote_num) +'号玩家')
            # 模拟其他玩家投票
            for other_user in self.user_list:
                content = self.game_run.simulateCastVote(other_user.id)
                if content is not None:
                    self.show_content(content)

            # 分析投票结果
            result = self.analysis_vote()
            if result is False:
                self.show_content("游戏结束>>>>>")
                return
            else:
                pass
        else:
            tkMessageBox.showinfo("提示", "请输入数字！")
            return

    # 输出文本框，显示运行内容
    def draw_display(self, root):
        text1 = Text(root, width=50, height=15)
        # INSERT索引表示在光标处插入
        # text1.insert(1.0, 'I Love\n')
        # END索引号表示在最后插入
        # text1.insert(END, content + '\n')
        text1.place(relx=0.5, rely=0.07, anchor=CENTER)
        text1.pack()
        self.display_text = text1

    # 输出到文本框
    def show_content(self, content):
        self.display_text.insert(END, content + '\n')
        self.display_text.pack()

    def analysis_vote(self):

        vote = self.game_run.analysis_vote()

        if vote is None:
            # 平票
            # 不淘汰进入下一轮
            print "下一轮>>>>>>>"
            self.show_content("平局继续下一轮>>>>>")
            self.show_content("请继续描述您的关键词>>>>>")
            return True

        else:
            # 判断当前用户角色
            if vote[0] == self.game_run.cur_id:
                if self.game_run.cur_user.role_id == 1:
                    # 卧底
                    self.show_content("你是卧底，已被找出，平民胜利！")
                else:
                    print "你是平民还被淘汰了！好冤！"
                    self.show_content("你是平民还被淘汰了！好冤！")

            else:
                # 判断剩下多少玩家
                if len(self.game_run.user_list) == 2:
                    print "只剩下两个人啦，卧底胜利！"
                    self.show_content("只剩下两个人啦，卧底胜利！")

                else:
                    remain_user = len(self.game_run.user_list)
                    print "剩下" + str(remain_user) + "个玩家"
                    # 核对user列表，删掉已经删除的。
                    for user in self.game_run.user_list:
                        if vote[0] == user.id:
                            print str(user.id) + "号玩家被淘汰了"
                            self.show_content(str(user.id) + "号玩家被淘汰了")
                            self.user_list.remove(user)
                            if remain_user == 2:
                                print "只剩下两个人啦，卧底胜利！"
                                self.show_content("只剩下两个人啦，卧底胜利！")
                                break
                    print "下一轮>>>>>>>"

                    # 接着下一轮
                    self.show_content("剩下" + str(len(self.user_list)) + "个玩家")
                    self.show_content("继续下一轮>>>>>")
                    self.show_content("请继续描述您的关键词>>>>>")

    def run(self):

        print "---------prepare for game-------------"

        # 获得玩家数量
        player_count = self.get_player_count()

        if player_count != 0:
            self.game_run.player_count = player_count
            # 游戏开始
            # 分配角色和关键字
            user_keyword = self.game_run.assign_role()

            # 提示当前玩家关键字
            self.show_content('您获得的关键字是：' + user_keyword)
            self.show_content("请输入描述>>>>>>>")

if __name__ == '__main__':
    game_view = GameView()
    # 绘制窗体和组件
    game_view.draw()


