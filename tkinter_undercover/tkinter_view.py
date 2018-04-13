#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter_run import GameRun
from game_execute import GameExecute
from vote_execute import VoteExecute
import tkMessageBox
import time

class GameView:
    """ 游戏绘制 """
    game_run = GameRun()

    # 游戏核心模块
    gameExecute = GameExecute()

    # 投票和判断输赢模块
    voteExecute = VoteExecute()

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
        self.draw_display()
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
        com = Button(self.root, text='结束游戏', command=self.start)
        com.pack(side=LEFT, expand=YES)  # 次级窗口的位置摆放位置
        com.place(relx=0.5, rely=0.93, anchor=CENTER)

    def start(self):
        player_count = self.input_text.get()
        player_count = int(player_count)
        if int(player_count) < 7:
            # 弹出窗口提示：游戏人数不足7人
            self.display_message('游戏人数不足7人')
            tkMessageBox.showinfo("提示", "游戏人数不足7人")
        else:
            self.game_run.player_count = player_count
            self.run()

    def get_player_count(self):
        player_count = self.input_text.get()
        player_count = int(player_count)
        if int(player_count) < 7:
            # 弹出窗口提示：游戏人数不足7人
            self.display_message('游戏人数不足7人')
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

    # 输出文本框，显示运行内容
    def draw_display(self):
        text1 = Text(self.root, width=50, height=15)
        # INSERT索引表示在光标处插入
        # text1.insert(1.0, 'I Love\n')
        # END索引号表示在最后插入
        # text1.insert(END, content + '\n')
        text1.place(relx=0.5, rely=0.07, anchor=CENTER)
        text1.pack()
        self.display_text = text1

    def show_content(self, content):
        self.display_text.insert(END, content + '\n')
        self.display_text.pack()

    # 发言按键
    def player_talk(self):
        keyword_des = self.descr_text.get()
        print keyword_des

        if keyword_des is '' or keyword_des is None:
            self.show_content('请输入描述！')
        else:
            self.keyword_des = keyword_des

            # 显示发言
            self.show_content('您的发言：'+keyword_des)
            # 模拟其他玩家发言
            self.user_list = self.game_run.user_list
            # 其他玩家发言
            content_list = self.gameExecute.user_talk(self.user_list, self.game_run.cur_id, self.game_run.keyword_index)
            for content in content_list:
                time.sleep(1)
                self.show_content(str(content[0]) + '玩家的发言：' + content[1])

            self.show_content("请投票>>>>>")

    # 投票按键
    def vote_button_event(self):
        vote_num = self.vote_text.get()
        # 当前玩家投票
        self.voteExecute.castVote(self.game_run.cur_id, vote_num)

        # 模拟其他玩家投票
        for other_user in self.user_list:
            print other_user is None
            content = self.voteExecute.simulateCastVote(other_user.id, self.user_list)
            print content

        # 分析投票结果
        result = self.game_run.analysis_vote()
        if result is False:
            self.show_content("继续下一轮>>>>>")
        else:
            self.show_content("游戏结束>>>>>")

    # 状态栏显示内容
    def bar_show(self, content):
        status = Label(self.root, text=content, bd=1, relief=SUNKEN, anchor=W)  # W-west-左边
        status.pack(side=BOTTOM, fill=X)

    # 打印消息
    def display_message(self, message):
        self.show_content(message)

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


