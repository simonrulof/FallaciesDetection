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
        """
        get differents data like the lines, number of lines, maximum number of char of a line and the shifth of each line.
        @param content: any text.
        @return: (lines, numberLines, maxChar, iTab)
        """
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

    def setupCanva(self, w,  width, height, sizeFirstFrame, title):
        """
        do the basic setups needed to make the canva works.
        @param w: the canva
        @param width: canva's width
        @param height: canva's height
        @param sizeFirstFrame:
        @param title: title of the box.
        """
        w.configure(width=width, height=height, background="white")

        w.create_rectangle(1, 1,width, sizeFirstFrame, fill="white", outline='black')
        w.create_rectangle(1, 1 + sizeFirstFrame, width, height, fill="white", outline='black')

        w.create_text(width / 2, sizeFirstFrame / 2, text=title, )

    def configSubCanvas(self, w: tkinter.Canvas, title: str, content, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=9, heightLetter=17):
        """
        configure a canvas without any sub canvas in it.
        @param w: precreated canva which will be modified
        @param title: title of the canva, of the "box"
        @param content: content in the canva, in the "box"
        @param padx: X-shift between the canva's border and the content.
        @param pady: Y-shift between the canva's border and the content.
        @param sizeFirstFrame: minimal height
        @param minWidth: minimal width
        @param widthLetter: width of letters
        @param heightLetter: heights of the letters
        @return: compeleted canva w.
        """
        ## RECOVERY OF NECESSARY DATA
        lines, numberLines, maxChar, iTab = self.setupBaseData(content)

        width = max(minWidth, maxChar * widthLetter)
        height = sizeFirstFrame + numberLines * heightLetter + 2 * padx + len(iTab) * (2*widthLetter)


        ## CANVA'S SETUP WITH MAIN FRAMES
        self.setupCanva(w, width, height, sizeFirstFrame, title)

        ## PRINTS OF THE TITLES AND CONTENTS
        decSquare = 5
        content = ""
        decX = 0
        decY = 0
        count = 0
        for i in range(len(lines)):
            if i in iTab:
                w.create_text(padx + decX, pady + sizeFirstFrame + decY, text=content, anchor="nw")
                decX = decX + padx
                decY = (3*i) * widthLetter
                count+=1
                w.create_rectangle(decX, pady + sizeFirstFrame + decY + decSquare, width - decX, height - count*widthLetter)
                content = ""
            content = content + "\n" + lines[i]

        w.create_text(padx + decX, pady + sizeFirstFrame + decY, text=content, anchor="nw")


        return w

    def configCanvas(self, w, subCanvas, title: str, content: str, padx=10, pady=10, sizeFirstFrame=25, minWidth=100, widthLetter=9, heightLetter=17):
        """
        configure a canvas with sub canvas in it.
        @param w: precreated canva which will be modified
        @param title: title of the canva, of the "box"
        @param content: content in the canva, in the "box"
        @param padx: X-shift between the canva's border and the content.
        @param pady: Y-shift between the canva's border and the content.
        @param sizeFirstFrame: minimal height
        @param minWidth: minimal width
        @param widthLetter: width of letters
        @param heightLetter: heights of the letters
        @return: compeleted canva w.
        """

        ## RECOVERY OF NECESSARY DATA
        lines, numberLines, maxChar, iTab = self.setupBaseData(content)

        widthSubCanvas = 0
        heightSubCanvas = 0
        for canva in subCanvas:
            widthSubCanvas += canva.winfo_reqwidth()
            heightSubCanvas = max(heightSubCanvas, canva.winfo_reqheight())

        width = max(max(minWidth, maxChar * widthLetter), widthSubCanvas + (1+len(subCanvas))*padx)
        heightWithoutSubCanvas = sizeFirstFrame + numberLines * heightLetter + 2 * pady + len(iTab) * (2*widthLetter)
        height = heightWithoutSubCanvas + heightSubCanvas + pady

        ## CANVA'S SETUP WITH MAIN FRAMES
        self.setupCanva(w, width, height, sizeFirstFrame, title)

        ## PRINTS OF THE TITLES AND CONTENTS
        decSquare = 5
        content = ""
        decX = 0
        decY = 0
        count = 0
        for i in range(len(lines)):
            if i in iTab:
                w.create_text(padx + decX, pady + sizeFirstFrame + decY, text=content, anchor="nw")
                decX = decX + padx
                decY = (3*i) * widthLetter
                count+=1
                w.create_rectangle(decX, pady + sizeFirstFrame + decY + decSquare, width - decX, heightWithoutSubCanvas - count * decSquare)
                content = ""
            content = content + "\n" + lines[i]

        w.create_text(padx + decX, pady + sizeFirstFrame + decY, text=content, anchor="nw")


        ## PRINTS OF EVERY SUB CANVAS IN THE CANVA
        dec = 0
        for canva in subCanvas[::-1]:
            canva.place(x=padx + dec, y=heightWithoutSubCanvas + heightSubCanvas/2, anchor='w')
            dec += padx + canva.winfo_reqwidth()

        return w

    def configLinksCanvas(self, w, txt, widthLetter=11, heightLetter=17):
        """
        configure a link's canvas
        @param w: the canva to configure
        @param txt: the link text
        @param widthLetter: width of the letters
        @param heightLetter: heights of the letters.
        """
        width = len(txt) * widthLetter
        height = heightLetter
        w.configure(width=width, height=height, background="white", border=0)

        w.create_text(1, 1, text=txt, anchor="nw")

    def toLogic(self):
        pass

    def display(self):
        """
        show on a Tkinter window the formated DRS code.
        """



        lines = self.DRSString.split("\n")

        titles = []
        contents = []
        links = []

        # checking each lines of the DRS code
        for line in lines:
            shift = 0
            if line:
                # removing the blank spaces and saving its shifts
                while line[0:3] == "   ":
                    line = line[3:]
                    shift += 1
                    if not line:
                        break

                # if the line is a special line (usually implications or AND mark), these lines are links between other lines, we stock them and they will use them later.
                if line == '=>' or line == 'v' or line == 'NO' or line == 'NAF' or line == 'CAN' or line == 'MUST' \
                        or line == 'SHOULD' or line == 'MAY' or line == 'QUESTION' or line == 'COMMAND':
                    links.append((line, len(titles)))

                # these are links too, they just are "custom" links that the user can do with ACE.
                elif 64 < ord(line[0]) < 91:
                    links.append((line[0], len(titles)))

                # if the line is a "case" title, we add it to the title list and use shift to know where theey are placed.
                elif line[0] == '[':
                    if titles == []:
                        titles.append((line[1:-1], -1, shift))
                    else:
                        for i in range(len(titles)-1, -1, -1):
                            if titles[i][1] == shift-2:
                                titles.append((line[1:-1], i, shift))
                                break

                    contents.append([])

                # if it's anything else, we add it on the content list using shift to know with which title it is.
                else:
                    for i in range(len(titles)-1, -1, -1):
                        if titles[i][2] == shift:
                            contents[i].append(line)
                            break

        print(contents)
        print(links)
        print(titles)

        # at this points, we have :
        #       contents : list of N list, N being the number of "box" and a content of a n-box is on the n-list.
        #           (ex : content of box number 2 is on the list contents[2]).
        #       links : contains the links between each boxes (there is not obligatorily a link between 2 boxes)
        #           (ex : links can contains ('=>', 2) which mean there is an implication mark just before box number 2).
        #       titles : list of N titles, it is basically the title of each box.


        # create the Tkinter window
        master = Tk()
        mainFrame = Frame(master)


        # for each "box" we create a sub-canvas which will be on the main mainFrame.
        canvas = []
        for i in range(len(titles)):
            if titles[i][1] == -1:
                canvas.append(Canvas(mainFrame))
            else:
                canvas.append(Canvas(canvas[titles[i][1]]))

        # we create a canva for each link too.
        canvasLinks = []
        for i in range(len(links)):
            canvasLinks.append(Canvas(canvas[titles[links[i][1]][1]]))


        # because there can be "boxes" on boxes", we have to work from the last boxes to the first one, because
        # to place a canva on another canva, the first canva must be completed.
        titles = titles[::-1]
        contents = contents[::-1]
        links = links[::-1]
        for i in range(len(contents)):
            contents[i] = "\n".join(contents[i])
        canvas = canvas[::-1]
        canvasLinks = canvasLinks[::-1]

        for i in range(len(canvasLinks)):
            self.configLinksCanvas(canvasLinks[i], links[i][0])



        # we first need to config each canvas in the right order.
        # we check with this if a box have another box in it. the config is a bit different if it has a box in it.
        # configSubCanvas will config a box without any boxes in it.
        # configCanvas will config a box with boxes in it.
        shift = -1
        for i in range(len(titles)):
            if titles[i][2] >= shift:
                self.configSubCanvas(canvas[i], title=titles[i][0], content=contents[i])
            else:
                listSubCanvas = []
                for j in range(i):
                    if titles[j][1] == len(titles) - i - 1:
                        listSubCanvas.append(canvas[j])
                        for k in range(len(links)):
                            if -1+len(titles)-links[k][1] == j:
                                listSubCanvas.append(canvasLinks[k])


                self.configCanvas(canvas[i], listSubCanvas, title=titles[i][0], content=contents[i])
            shift = titles[i][2]

        # last thing to do is pack the last box and show the result.
        canvas[-1].pack()
        mainFrame.pack(anchor="nw")
        master.mainloop()

    def isPropertyPresent(self, line, output):
        """
        check for a property in output if it is the same as the property in line. If it is the same,
        both identification letters are sent
        @param line: property needed to be checked
        @param output: all the lines processed before.
        @return: "" if there is not the same property before,
                 string of the previous identification letter and the new identification letter to change.
        """
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
        """
        check for a predicate in output if it is the same as the predicate in line. If it is the same, a new correct
        line with the first identification letter is created
        @param line: predicate needed to be checked
        @param output: all the lines processed before
        @return:line of there is no other same predicate, a new line with identification letter replaced if
        there is the same predicate before.
        """
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
        """
        sort string by shift.
        @param str: string to sort
        @return: sorted string
        """
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
        """
        from the DRSString, this function create the equivalence of the DRS in Prolog.
        @return: prolog reasonning and goal of the fallacy argumentation.
        """
        str = self.DRSString

        # ADDING THE "tag" ON THE LAST LINE IN A WAY TO KNOW WHERE IT WILL BE AT THE END.
        lines = str.split('\n')
        for i in range(len(lines)-1, -1, -1):
            if len(lines[i]) > 0:
                lineSplit = lines[i].split('(')
                lineSplit[0] += 'tag'
                lines[i] = '('.join(lineSplit)
                break
        str = '\n'.join(lines)


        # SORTING THE DRS BY THEIR SHIFTS.
        str = self.sortDRSString(str)

        output = []

        # READING LINE PER LINE, ERASING REDUNDANCY OF EVERY PROPERTIES AND PREDICATES
        strsplit = str.split('\n')
        for line in strsplit:
            if len(line) > 1:
                dec = 0
                while line[0] == ' ':
                    line = line[1:]
                    dec+=1
                if line[0] != '[':
                    line = line.split('-')[0]
                    # if the line is a property
                    if line[0:8] == "property":
                        # we see if we already seen the same property
                        change = self.isPropertyPresent(line, output)
                        # if we didnt saw any, we add it to the usual output.
                        if change == "":
                            output.append((dec,line))
                        # if we saw the same property we replace its identification letter to the previous one.
                        else:
                            fromTo = change.split('-')
                            for i in range(len(strsplit)):
                                strsplit[i] = strsplit[i].replace('(' + fromTo[0] + ',', '(' + fromTo[1] + ',')
                                strsplit[i] = strsplit[i].replace(',' + fromTo[0] + ',', ',' + fromTo[1] + ',')
                                strsplit[i] = strsplit[i].replace(',' + fromTo[0] + ')', ',' + fromTo[1] + ')')
                    # we do the same if the predicates, but we add them anyway after checking a previous one
                    # and changing the identification letter.
                    elif line[0:9] == "predicate":
                        newLine = self.isPredicatePresent(line, output)
                        output.append((dec,newLine))
                    else:
                        output.append((dec, line))


        # calculate the maximum shift of a sentence.
        max = output[0][0]
        for i in output:
            if max < i[0]:
                max = i[0]

        print(output)
        # starting from the most shifted sentences, checking and processing links beween two parts (like implies or AND)
        # and links to on part (like NOT, or '∼' or custom links from ACE).
        while max >= 0:
            i = len(output)-1
            while i >= 0:
                # if it is a link to one part only
                if (output[i][1] == '∼' or output[i][1] == '¬' or output[i][1].isupper()) and output[i][0] == max:
                    # we add the start of the Prolog input
                    if output[i][1] == '∼' :
                        sentence = 'notProvable('
                    if output[i][1] == '¬' :
                        sentence = 'not('
                    else:
                        sentence = output[i][1] + '('
                    j = i + 1

                    # we add the content of the "box" seen next to the link with the right shift.
                    # (BUG TO FIX HERE, STOP ON ENTERING ANOTHER BOX OF THE SAME SHIFT)
                    while j<len(output):
                        sentence = sentence + output[j][1] + ','
                        fronti = j
                        j+=1
                    sentence = sentence[:-1:] + ')'

                    output = output[:i] + [(output[i][0], sentence)]

                # if it is a link to 2 parts
                if (output[i][1] == '=>' or output[i][1] == 'v') and output[i][0] == max:
                    # we add the start of the Prolog input
                    if output[i][1] == '=>':
                        sentence = 'implies(['
                    #add the bein
                    if output[i][1] == 'v':
                        sentence = 'OR(['
                    j = i-1

                    # we add the content of the "box" seen before the link with the right shift.
                    predicates = []
                    while j>=0 and output[j][0] == output[i][0]:
                        predicates.append(output[j][1] + ',')
                        j-=1
                    backi = j+1
                    for predicate in predicates[::-1]:
                        sentence = sentence + predicate

                    sentence = sentence[:-1:] + '],['


                    # we add the content of the "box" seen next to the link with the right shift.
                    # (BUG TO FIX HERE, STOP ON ENTERING ANOTHER BOX OF THE SAME SHIFT)
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

        # last thing to do is differentiate the reasonning and the conclusion with the tag put at the beginning.
        reasonnings = []
        for i in output:
            if i[1].find('tag') == -1:
                reasonnings.append(i[1].replace('[', '').replace(']', '').lower())
            else:
                goal = i[1].replace('tag', '').replace('[', '').replace(']', '').lower()

        return (reasonnings, goal)