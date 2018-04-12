#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
root = Tk()

#鼠标左击事件
def callback(event):
    frame.focus_set()
    print 'clicked at:', event.x,event.y

#键盘事件
def key(event):
    print "pressed:", repr(event.char)

#关闭窗口时的弹出窗口事件
def closeWindow():
    if tkMessageBox.askokcancel('Quit',"Do you want to exit"):
        root.destroy()

frame = Frame(root,width=100,height=100)
frame.bind('<Button-1>',callback)   #鼠标左击事件
frame.bind('<Key>',key)  #键盘事件
frame.pack()

#协议监听关闭窗口时的弹出窗口事件
root.protocol('WM_DELETE_WINDOW',closeWindow)
root.mainloop()