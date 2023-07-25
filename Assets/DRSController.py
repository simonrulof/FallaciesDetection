import tkinter
from tkinter import *
from tkinter import ttk
import numpy as np


class DRSController:

    def __init__(self, string_DRS):
        self.DRSString = string_DRS
        self.tabDRS = self.DRSString.split("\n")

    def toString(self):
        return self.DRSString





    def getDRSString(self):
        return self.DRSString

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



        lines = self.DRSString.split("\n")

        titles = []
        contents = []
        links = []

        for line in lines:
            dec = 0
            if line:
                while line[0:3] == "   ":
                    line = line[3:]
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

    def isPropertyPresent(self, line, output):
        if len(output) == 0:
            return ""
        for property in output:
            if property[1][0:8] == 'property':
                context = property[1].split(',')
                lineContext = line.split(',')
                if len(context) == len(lineContext):
                    count = 0
                    for i in range(1,len(context)):
                        if context[i] == lineContext[i]:
                            count+=1
                    if count == len(context)-1:
                        return lineContext[0][9:] + "-" + context[0][9:]
        return ""

    def isPredicatePresent(self, line, output):
        if len(output) == 0:
            return line
        for predicate in output:
            if predicate[1][0:9] == 'predicate':
                context = predicate[1].split(',')
                lineContext = line.split(',')
                if len(context) == len(lineContext):
                    count = 0
                    for i in range(1,len(context)):
                        if context[i] == lineContext[i]:
                            count+=1
                    if count == len(context)-1:
                        newLine = line
                        newLine = newLine.replace('(' + lineContext[0].split('(')[1] + ',', '(' + context[0].split('(')[1] + ',')
                        newLine = newLine.replace(',' + lineContext[0].split('(')[1] + ',', ',' + context[0].split('(')[1] + ',')
                        newLine = newLine.replace(',' + lineContext[0].split('(')[1] + ')', ',' + context[0].split('(')[1] + ')')
                        return newLine

        return line


    def sortDRSString(self, str):
        lines = str.split('\n')
        strOut = ''
        decLines = []
        decMax = 0
        for line in lines:
            if len(line) > 0:
                dec = 0
                while line[0] == ' ':
                    line = line[1:]
                    dec += 1
                if dec > decMax:
                    decMax = dec
                decLines.append(dec)

        for i in range(decMax+1):
            for j in range(len(decLines)):
                if decLines[j] == i:
                    strOut = strOut + i*' ' + lines[j] + '\n'

        return strOut

    def DRSProlog(self):

        str = self.DRSString

        lines = str.split('\n')
        for i in range(len(lines)-1, -1, -1):
            if len(lines[i]) > 0:
                lineSplit = lines[i].split('(')
                lineSplit[0] += 'tag'
                lines[i] = '('.join(lineSplit)
                break
        str = '\n'.join(lines)

        str = self.sortDRSString(str)

        output = []

        strsplit = str.split('\n')
        for line in strsplit:
            if len(line) > 1:
                dec = 0
                while line[0] == ' ':
                    line = line[1:]
                    dec+=1
                if line[0] != '[':
                    line = line.split('-')[0]
                    if line[0:8] == "property":
                        change = self.isPropertyPresent(line, output)
                        if change == "":
                            output.append((dec,line))
                        else:
                            fromTo = change.split('-')
                            for i in range(len(strsplit)):
                                strsplit[i] = strsplit[i].replace('(' + fromTo[0] + ',', '(' + fromTo[1] + ',')
                                strsplit[i] = strsplit[i].replace(',' + fromTo[0] + ',', ',' + fromTo[1] + ',')
                                strsplit[i] = strsplit[i].replace(',' + fromTo[0] + ')', ',' + fromTo[1] + ')')
                    elif line[0:9] == "predicate":
                        newLine = self.isPredicatePresent(line, output)
                        output.append((dec,newLine))
                    else:
                        output.append((dec, line))



        max = output[0][0]
        for i in output:
            if max < i[0]:
                max = i[0]


        while max >= 0:
            i = len(output)-1
            while i >= 0:
                if (output[i][1] == '∼' or output[i][1] == '¬' or output[i][1].isupper()) and output[i][0] == max:
                    if output[i][1] == '∼' :
                        sentence = 'notProvable('
                    if output[i][1] == '¬' :
                        sentence = 'not('
                    else:
                        sentence = output[i][1] + '('
                    j = i + 1
                    while j<len(output):
                        sentence = sentence + output[j][1] + ','
                        fronti = j
                        j+=1

                    sentence = sentence[:-1:] + ')'

                    output = output[:i] + [(output[i][0], sentence)]

                if (output[i][1] == '=>' or output[i][1] == 'v') and output[i][0] == max:
                    if output[i][1] == '=>':
                        sentence = 'implies(['
                    if output[i][1] == 'v':
                        sentence = 'OR(['
                    j = i-1
                    predicates = []
                    while j>=0 and output[j][0] == output[i][0]:
                        predicates.append(output[j][1] + ',')
                        j-=1

                    backi = j+1

                    for predicate in predicates[::-1]:
                        sentence = sentence + predicate

                    sentence = sentence[:-1:] + '],['

                    j = i+1
                    while j<len(output):
                        sentence = sentence + output[j][1] + ','
                        fronti = j
                        j+=1

                    sentence = sentence[:-1:] + '])'

                    output = output[:backi] + [(output[i][0], sentence)]
                    i = backi
                i-=1
            max-=1

        retour = []
        for i in output:
            if i[1].find('tag') == -1:
                retour.append(i[1].replace('[', '').replace(']', '').lower())
            else:
                concl = i[1].replace('tag', '').replace('[', '').replace(']', '').lower()

        return (retour, concl)