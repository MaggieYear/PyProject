#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Yekiki'
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
        self.descr_text = None
        self.vote_text = None
        self.keyword_des = None
        self.user_list = None
        self.is_talk = 0
        self.is_voting = 0
        self._game_run = GameRun()

    @property
    def game_run(self):
        return self._game_run

    @game_run.setter
    def game_run(self, game_run):
        self._game_run = game_run

    def init_param(self):
        self.user_list = None
        self.is_talk = 0
        self.is_voting = 0

    def draw(self):
        root = Tk()
        # 根窗口
        root.title('谁是卧底')  # 主窗口标题
        root.geometry('400x400')  # 主窗口大小，中间的为英文字母x
        # 窗口尺寸固定
        # root.resizable(False, False)

        self.root = root
        # 绘制各种组件

        # 玩家数量文本框
        self.draw_input_count()

        # 开始按键
        self.draw_start()

        # 结束按键
        self.draw_stop()

        # 用户发言文本框和按键
        self.play_talk_draw()
        # 用户投票文本框和按键
        self.draw_vote_button()
        # 输出文本框，显示运行内容
        self.draw_display(root)

        # 绘制标签（关键字和ID)
        self.draw_label()

        # 事件循环
        root.mainloop()

    # 开始按键
    def draw_start(self):
        com = Button(self.root, text='开始游戏', command=self.start)
        com.pack(side=LEFT,expand=YES)
        com.place(relx=0.68, rely=0.6, anchor=NW)  # 坐标位置

    # 结束游戏按键
    def draw_stop(self):
        com = Button(self.root, text='结束游戏', command=self.stop)
        com.pack(side=LEFT, expand=YES)
        com.place(relx=0.5, rely=0.93, anchor=CENTER)

    # 开始按键触发事件
    def start(self):

        # 先判断游戏是否正在进行
        if self.game_is_run() is True:
            if tkMessageBox.askyesnocancel('提示','游戏正在进行，确定要重新开始游戏？') is not True:
                return
            else:
                # 游戏重新开始
                self.game_reset()

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
        self.game_reset()
        self.show_content("游戏结束！>>>>>")
        self.show_content("请输入玩家数量，然后开始游戏>>>>>")

    def get_player_count(self):
        player_count = self.input_text.get()
        player_count = int(player_count)
        if int(player_count) < 7:
            # 弹出窗口提示：游戏人数不足7人
            self.show_content('游戏人数不足7人')
            tkMessageBox.showinfo("提示", "游戏人数不足7人")
            return 0
        else:
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

        com = Button(self.root, text='投票', command=self.vote_button_event)
        com.pack(side=LEFT)
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

        # 判断游戏是否在进行
        if self.game_is_run() is False:
            self.show_content("游戏尚未开始>>>>>")
            self.show_content("请输入玩家数量，然后开始游戏>>>>>")
            return

        # 判断是否正在投票
        if self.player_is_voting() is True:
            self.show_content("投票尚未完成，请不要发言>>>>>")
            return
        keyword_des = self.descr_text.get()
        if keyword_des is '' or keyword_des is None:
            self.show_content('请输入描述！')
        else:
            self.keyword_des = keyword_des
            # 显示发言
            self.show_content('您的发言：' + keyword_des)
            # 模拟其他玩家发言
            self.user_list = self.game_run.user_list
            # 其他玩家发言
            content_list = self.game_run.user_talk()
            for content in content_list:
                self.show_content(str(content[0]) + '号玩家的发言：' + content[1])
                # time.sleep(1)
            self.is_talk = 0
            self.show_content("请投票>>>>>")
            self.is_voting = 1

    # 投票按键
    def vote_button_event(self):

        # 判断游戏是否在进行
        if self.game_is_run() is False:
            self.show_content("游戏尚未开始>>>>>")
            self.show_content("请输入玩家数量，然后开始游戏>>>>>")
            return
        # 判断现在是否发言在进行
        if self.player_is_talk() is True:
            self.show_content("发言尚未完成，请不要投票>>>>>")
            return
        vote_num = self.vote_text.get()

        # 判断输入是否 为数字
        result = self.str_utils.is_number( unicode(vote_num) )
        if result:
            vote_num = int(vote_num)

            # 当前玩家数量
            cur_players = len(self.game_run.user_list)
            # print '当前玩家数量' + str(cur_players)

            is_exist = False
            for user in self.game_run.user_list:
                if vote_num == user.id:
                    is_exist = True
            # 判断玩家号是否存在
            if is_exist is False:
                tkMessageBox.showinfo("提示", "玩家号不存在！")
                return
            # 判断是否给自己投票
            if self.game_run.cur_id == vote_num:
                tkMessageBox.showinfo("提示", "请不要投票给自己！")
                return

            # 当前玩家投票
            result = self.game_run.player_vote(vote_num)
            if result:
                self.show_content('您投给了' + str(vote_num) + '号玩家')
            # 模拟其他玩家投票
            for other_user in self.game_run.user_list:
                if self.game_run.cur_id == other_user.id:
                    continue
                else:
                    content = None
                    # 如果获得的投票信息一直为空，就一直获取直到不为空
                    while content is None:
                        content = self.game_run.simulate_cast_vote(other_user.id)
                    self.show_content(content)
            self.is_voting = 0

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
        game_rule="""游戏规则：\n游戏有卧底和平民 2 种身份。\n 游戏根据在场人数大部分玩家拿到同一词语，其余玩家拿到与之相关的另一词语。\n每人每轮用一句话描述自己拿到的词语，既不能让卧底察觉，也要给同伴以暗示。\n每轮描述完毕，所有在场的人投票选出怀疑谁是卧底，得票最多的人出局。\n若卧底全部出局，则游戏结束。若卧底未全部出局，游戏继续。并反复此流程。\n若卧底撑到最后一轮（剩余总人数小于卧底初始人数的二倍时），则卧底获胜，反之，则平民胜利。\n
        """
        text1.insert(END, game_rule + '\n')
        text1.pack()
        self.display_text = text1

    # 输出到文本框
    def show_content(self, content):
        self.display_text.insert(END, content + '\n')
        self.display_text.pack()

    # 绘制标签（关键字和ID)
    def draw_label(self):
        label = Label(self.root, text="您的关键字：")
        label.pack(side=LEFT)
        label.place(relx=0.07, rely=0.52, anchor=NW)

        label = Label(self.root, text="您的ID：")
        label.pack(side=LEFT)
        label.place(relx=0.53, rely=0.52, anchor=NW)

    # 显示玩家关键字
    def show_keyword(self, keyword):
        label = Label(self.root, text=keyword)
        label.pack(side=LEFT)
        label.place(relx=0.26, rely=0.52, anchor=NW)

    # 显示玩家ID
    def show_id(self, id):
        label = Label(self.root, text=str(id))
        label.pack(side=LEFT)
        label.place(relx=0.66, rely=0.52, anchor=NW)

    # 分析票数
    def analysis_vote(self):

        vote = self.game_run.analysis_vote()

        if vote is None:
            # 平票
            # 不淘汰进入下一轮
            # print "下一轮>>>>>>>"
            self.show_content("平局继续下一轮>>>>>")
            self.show_content("请继续描述您的关键词>>>>>")
            self.is_talk = 1
            self.game_run.clear()
            return True

        else:
            remain_user = len(self.game_run.user_list)

            # 判断当前用户角色
            if vote[0] == self.game_run.cur_id:
                if self.game_run.cur_user.role_id == 1:
                    # 卧底
                    self.show_content("你是卧底，已被找出，平民胜利！")
                    self.game_reset()
                    self.show_content("游戏结束！>>>>>")
                    self.show_content("请输入玩家数量，然后开始游戏>>>>>")

                else:
                    # print "你是平民还被淘汰了！好冤！"
                    self.show_content("你是平民还被淘汰了！好冤！")
                    # 判断剩余玩家数等于2
                    if self.remain_player_2(remain_user-1) is False:
                        self.game_reset()
                        self.show_content("游戏结束！>>>>>")
                        self.show_content("请输入玩家数量，然后开始游戏>>>>>")

            else:
                # 判断剩余玩家是否为2
                if self.remain_player_2(remain_user) is False:

                    # print "剩下" + str(remain_user) + "个玩家"
                    # 核对user列表，删掉已经删除的。
                    for user in self.game_run.user_list:
                        if vote[0] == user.id:
                            print str(user.id) + "号玩家被淘汰了"
                            self.show_content(str(user.id) + "号玩家被淘汰了")
                            self.game_run.user_list.remove(user)
                            if self.remain_player_2(remain_user-1) is True:
                                break
                    # print "下一轮>>>>>>>"

                    # 接着下一轮
                    self.show_content("剩下" + str(len(self.user_list)) + "个玩家")
                    self.show_content("继续下一轮>>>>>")
                    self.game_run.clear()
                    self.show_content("请继续描述您的关键词>>>>>")
                    self.is_talk = 1

    # 当玩家数为2的行动
    def remain_player_2(self, remain_user):
        if remain_user == 2:
            # print "只剩下两个人啦，卧底胜利！"
            self.show_content("只剩下两个人啦，卧底胜利！")
            self.game_reset()
            self.show_content("游戏结束！>>>>>")
            self.show_content("请输入玩家数量，然后开始游戏>>>>>")
            return True
        else:
            return False

    # 游戏重置
    def game_reset(self):
        self.game_run = GameRun()
        self.game_run.__init__()
        self.init_param()

    # 判断游戏是否进行
    def game_is_run(self):
        cur_user_count = len(self.game_run.user_list)
        if cur_user_count < 2:
            return False
        else:
            return True

    # 判断现在是否发言在进行
    def player_is_talk(self):
        if self.is_talk == 1:
            return True
        else:
            return False

    # 判断现在是否投票在进行
    def player_is_voting(self):
        if self.is_voting == 1:
            return True
        else:
            return False

    def run(self):

        # print "---------prepare for game-------------"
        self.show_content("游戏开始了>>>>>>")
        # 获得玩家数量
        player_count = self.get_player_count()

        if player_count != 0:
            self.game_run.player_count = player_count
            # 游戏开始
            # 分配角色和关键字
            user_keyword = self.game_run.assign_role()

            # self.show_content('您的ID是：' + str(self.game_run.cur_id))
            self.show_id(self.game_run.cur_id)
            # 提示当前玩家关键字
            # self.show_content('您获得的关键字是：' + user_keyword)
            self.show_keyword(user_keyword)
            self.show_content("请输入描述>>>>>>>")
            self.is_talk = 1

if __name__ == '__main__':
    game_view = GameView()
    # 绘制窗体和组件
    game_view.draw()


