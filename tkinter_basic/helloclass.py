__author__ = 'kiki'

from Tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Hello World", fg='red',command=frame.quit())

        self.button.pack()

        self.hiButton = Button(frame, text="Say hi", command=self.say_hi())

        self.hiButton.pack()

    def say_hi(self):
        print("hi")


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
