import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np


class DRSController:

    def __init__(self, string_DRS):
        self.string = string_DRS
        self.tabDRS = self.string.split("\n")


    def setupBaseData(self, content):
        lines = content.split("\n")
        numberLines = len(lines)+1

        maxChar = 0
        iTab = []
        i = 0
        for line in lines:
            if maxChar < len(line):
                maxChar = len(line)
            if line[0:3] == "   ":
                iTab.append(i)
                for j in range(i, len(lines)):
                    lines[j] = lines[j][3:]
            i+=1

        maxChar = maxChar + 2 * len(iTab)
        return lines, numberLines, maxChar, iTab

    def setupCanva(self, w, x, y, width, height, sizeFirstFrame, title):
        w.configure(width=width, height=height, background="white")

        w.create_rectangle(1+x, 1+y, x + width, y + sizeFirstFrame, fill="white", outline='black')
        w.create_rectangle(1+x, 1+y + sizeFirstFrame, x + width, y + height, fill="white", outline='black')

        w.create_text(x + width / 2, y + sizeFirstFrame / 2, text=title, )


    def configSubCanvas(self, w: tkinter.Canvas, x: int, y: int, title: str, content, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=9, heightLetter=17):
        """
        CONFIGURE UN CANVA SANS SOUS CANVA (canva minimal)
        """


        ## RECUPERATION DES DONNEES NECESSAIRES
        lines, numberLines, maxChar, iTab = self.setupBaseData(content)

        width = max(minWidth, maxChar * widthLetter)
        height = sizeFirstFrame + numberLines * heightLetter + 2 * padx + len(iTab) * (2*widthLetter)


        ## SETUP DU CANVA + CADRES PRINCIPAUX
        self.setupCanva(w, x, y, width, height, sizeFirstFrame, title)

        ## AFFICHAGE DES TEXTES TITRE ET CONTENT + CADRES
        decSquare = 5
        content = ""
        decX = 0
        decY = 0
        count = 0
        for i in range(len(lines)):
            if i in iTab:
                w.create_text(x + padx + decX, y + pady + sizeFirstFrame + decY, text=content, anchor="nw")
                decX = decX + padx
                decY = (3*i) * widthLetter
                count+=1
                w.create_rectangle(x + decX, y + pady + sizeFirstFrame + decY + decSquare, width - decX, height - count*widthLetter)
                content = ""
            content = content + "\n" + lines[i]

        w.create_text(x + padx + decX, y + pady + sizeFirstFrame + decY, text=content, anchor="nw")


        return w

    def configCanvas(self, w, subCanvas, x: int, y: int, title: str, content: str, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=9, heightLetter=17):
        """
        permet de
        """

        ## RECUPERATION DES DONNEES NECESSAIRES
        lines, numberLines, maxChar, iTab = self.setupBaseData(content)

        widthSubCanvas = 0
        heightSubCanvas = 0
        for canva in subCanvas:
            widthSubCanvas += canva.winfo_reqwidth()
            heightSubCanvas = max(heightSubCanvas, canva.winfo_reqheight())

        width = max(max(minWidth, maxChar * widthLetter), widthSubCanvas + (1+len(subCanvas))*padx)
        heightWithoutSubCanvas = sizeFirstFrame + numberLines * heightLetter + 2 * pady + len(iTab) * (2*widthLetter)
        height = heightWithoutSubCanvas + heightSubCanvas + pady

        ## SETUP DU CANVA + CADRES PRINCIPAUX
        self.setupCanva(w, x, y, width, height, sizeFirstFrame, title)

        ## AFFICHAGE DES TEXTES TITRE ET CONTENT + CADRES
        decSquare = 5
        content = ""
        decX = 0
        decY = 0
        count = 0
        for i in range(len(lines)):
            if i in iTab:
                w.create_text(x + padx + decX, y + pady + sizeFirstFrame + decY, text=content, anchor="nw")
                decX = decX + padx
                decY = (3*i) * widthLetter
                count+=1
                w.create_rectangle(x + decX, y + pady + sizeFirstFrame + decY + decSquare, width - decX, y + heightWithoutSubCanvas - count * decSquare)
                content = ""
            content = content + "\n" + lines[i]

        w.create_text(x + padx + decX, y + pady + sizeFirstFrame + decY, text=content, anchor="nw")


        ## AFFICHAGE DES SOUS CANVAS DANS CE CANVAS
        dec = 0
        for canva in subCanvas[::-1]:
            canva.place(x=x + padx + dec, y=y + heightWithoutSubCanvas + heightSubCanvas/2, anchor='w')
            dec += x + padx + canva.winfo_reqwidth()

        return w

    def configLinksCanvas(self, w, txt, widthLetter=11, heightLetter=17):
        width = len(txt) * widthLetter
        height = heightLetter
        w.configure(width=width, height=height, background="white", border=0)

        w.create_text(1, 1, text=txt, anchor="nw")



    def toLogic(self):
        pass

    def display(self):
        """
        fonction qui affiche sous une fenetre Tkinter le code DRS formaté.
        """



        lines = self.string.split("\n")

        titles = []
        contents = []
        links = []

        for line in lines:
            dec = 0
            if line:
                while line[0:4] == "    ":
                    line = line[4:]
                    dec += 1
                    if not line:
                        break

                if line == '=>' or line == 'v' or line == 'NO' or line == 'NAF' or line == 'CAN' or line == 'MUST' \
                        or line == 'SHOULD' or line == 'MAY' or line == 'QUESTION' or line == 'COMMAND':
                    links.append((line, len(titles)))

                elif 64 < ord(line[0]) < 91:
                    links.append((line[0], len(titles)))

                elif line[0] == '[':
                    if titles == []:
                        titles.append((line[1:-1], -1, dec))
                    else:
                        for i in range(len(titles)-1, -1, -1):
                            if titles[i][1] == dec-2:
                                titles.append((line[1:-1], i, dec))
                                break

                    contents.append([])

                else:
                    for i in range(len(titles)-1, -1, -1):
                        if titles[i][2] == dec:
                            contents[i].append(line)
                            break


        master = Tk()
        mainFrame = Frame(master)

        canvas = []
        for i in range(len(titles)):
            if titles[i][1] == -1:
                canvas.append(Canvas(mainFrame))
            else:
                canvas.append(Canvas(canvas[titles[i][1]]))

        canvasLinks = []
        for i in range(len(links)):
            canvasLinks.append(Canvas(canvas[titles[links[i][1]][1]]))



        titles = titles[::-1]
        contents = contents[::-1]
        links = links[::-1]
        for i in range(len(contents)):
            contents[i] = "\n".join(contents[i])
        canvas = canvas[::-1]
        canvasLinks = canvasLinks[::-1]

        for i in range(len(canvasLinks)):
            self.configLinksCanvas(canvasLinks[i], links[i][0])



        dec = -1


        for i in range(len(titles)):
            if titles[i][2] >= dec:
                self.configSubCanvas(canvas[i], 0, 0, title=titles[i][0], content=contents[i])
            else:
                listSubCanvas = []
                for j in range(i):
                    if titles[j][1] == len(titles) - i - 1:
                        listSubCanvas.append(canvas[j])
                        for k in range(len(links)):
                            if -1+len(titles)-links[k][1] == j:
                                listSubCanvas.append(canvasLinks[k])


                self.configCanvas(canvas[i], listSubCanvas, 0, 0, title=titles[i][0], content=contents[i])
            dec = titles[i][2]

        canvas[-1].pack()
        mainFrame.pack(anchor="nw")
        master.mainloop()









        """

        master = Tk()
        frameTest = Frame(master)
        baseCanvas = Canvas(frameTest)
        subCanva = Canvas(baseCanvas)
        subCanva2 = Canvas(frameTest)

        self.configSubCanvas(subCanva, 0, 0, title="title", content="aaaaaaaahahaha")
        self.configSubCanvas(subCanva2, 0, 0, title="title", content="aaaaaaaahabbbbbbbbbbbbbbb\nbbb\nbbbbbbbbbbbbb\nbbb\nbbbbbbbbbbbbb\nbbb\nbbbbbbbhaha")
        self.configCanvas(baseCanvas,[subCanva, subCanva2], 0, 0, title="title", content="aaaaaaaahahaha")

        subCanva2.pack()
        frameTest.pack(anchor="n")
        master.mainloop()

        """