import tkinter
from tkinter import *
from tkinter import ttk


class DRSController:

    def __init__(self, string_DRS):
        self.string = string_DRS
        self.tabDRS = self.string.split("\n")

    def createCanvas(self, frame, x: int, y: int, title: str, content: str, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=8, heightLetter=16):
        lines = content.split("\n")
        numberLines = len(lines)+1

        maxChar = 0
        for line in lines:
            if maxChar < len(line):
                maxChar = len(line)

        width = max(minWidth, maxChar * widthLetter)
        height = sizeFirstFrame + numberLines * heightLetter + 2 * padx
        w = Canvas(frame, width=width, height=height)

        w.create_rectangle(x, y, x + width, y + sizeFirstFrame, fill="white", outline='black')
        w.create_rectangle(x, y + sizeFirstFrame, x + width, y + height, fill="white", outline='black')

        w.create_text(x + width / 2, y + sizeFirstFrame / 2, text=title, )
        w.create_text(x + padx, y + pady + sizeFirstFrame, text=content, anchor="nw")

        return w

    def createSubCanvas(self, frame: tkinter.Canvas, x: int, y: int, title: str, content: str, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=8, heightLetter=16):
        w = self.createCanvas(frame, x, y, title=title, content=content, padx=padx, pady=pady, sizeFirstFrame=sizeFirstFrame, minWidth=minWidth, widthLetter=widthLetter, heightLetter=heightLetter)
        print(frame.winfo_reqheight())
        print(w.winfo_reqheight() + pady)
        frame.configure(width=max(w.winfo_reqwidth() + 2 * padx, frame.winfo_reqwidth()), height=frame.winfo_reqheight() + pady + w.winfo_reqheight())
        print(frame.winfo_reqheight())
        w.pack(anchor="sw")

    def toLogic(self):
        pass

    def dsplay(self):
        master = Tk()
        frameTest = Frame(master)
        w = self.createCanvas(frameTest, 0, 0, title="a", content="content")
        subCanvas = self.createSubCanvas(w, 0, 0, title="b", content="aaaaaaaaa")
        w.pack()
        frameTest.pack()
        master.mainloop()
