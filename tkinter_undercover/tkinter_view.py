#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter_run import GameRun

class GameView():

    gameRun = GameRun()

    def __init__(self,root):
        self.root = root

    def frame(self,root,side):
        w = Frame(root)
        w.pack(side=side, expand=YES, fill=BOTH)
        return w

    def button(self,root, side, text, command=None):
        w = Button(root, text=text, command=command)
        w.pack(side=side, expand=YES, fill=BOTH)
        return w

    def draw(self):
        # 　根窗口
        self.root.title('Who is undercover')  # 主窗口标题
        self.root.geometry('400x200')  # 主窗口大小，中间的为英文字母x

        #绘制各种组件
        #玩家数量文本框
        self.inputPlayerCount()
        #开始按键
        self.drawStart()

        # 事件循环
        self.root.mainloop()

    # 开始按键
    def drawStart(self):
        com = Entry(self.root, text='游戏开始', command=self.start())  # 第一个参数root说明com按钮是root的孩子，text指按钮的名称，command指点击按钮时所执行的操作
        com.pack(side=BOTTOM)  # 次级窗口的位置摆放位置

    def start(self):
        print "start>>>"

    # 玩家数量文本框
    def inputPlayerCount(self):
        Label(self.root, text="玩家数量(>=7)").grid(row=0)
        input = Entry(self.root)
        input.grid(row=0, column=1)

        print input.get()

        com = Button(self.root, text='开始游戏', command=self.playernumber()).grid(row=3, column=0, sticky=W, pady=4)
        # 第一个参数root说明com按钮是root的孩子，text指按钮的名称，command指点击按钮时所执行的操作

        #Button(self.root, text='开始游戏', command=self.playernumber(input_player.get())).grid(row=3, column=0, sticky=W, pady=4)

        Button(self.root, text='结束游戏', command=self.root.quit).grid(row=3, column=1, sticky=W, pady=4)

    def playernumber(self):

        print("玩家数量>>")

class BackGround:
    """背景"""
    pass

class PlayerInput:
    """玩家人数文本框"""
    pass

class StartButton:
    """开始按键"""
    def __init__(self,cvns,start_point,w,h):
        self.cvns = cvns
        self.start_point = start_point
        self.w = w
        self.h = h

    def draw(self):
        self.ht.draw()
        self.hb.draw()


class StopButton:
    """结束按键"""
    pass

class VoteText:
    """投票号码文本框"""
    pass

class VoteButton:
    """投票按键"""
    pass

if __name__ == '__main__':
    root = Tk()
    gameView = GameView(root)
    gameView.draw()