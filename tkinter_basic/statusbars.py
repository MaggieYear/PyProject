#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
status = Label(root,text='我要显示的内容',bd=1,relief=SUNKEN,anchor=W)  #W-west-左边
status.pack(side=BOTTOM, fill=X)
root.mainloop()