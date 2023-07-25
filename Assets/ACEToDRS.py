import os
from Assets.DRSController import DRSController
def transformACEToDRS(ACE_FILE):

    file = open(ACE_FILE, 'r')
    sentences = file.read()
    file.close()

    os.system("./APE/ape.exe -text \"" + sentences + "\" -solo drspp > .temp")

    temp = open(".temp", "r")
    DRS = DRSController(temp.read())
    temp.close()

    os.system("rm .temp")

    return DRS