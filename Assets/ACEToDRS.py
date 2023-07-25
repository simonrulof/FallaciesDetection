import os
from Assets.DRSController import DRSController


def transformACEToDRS(ACE_FILE):
    """
    Return a DRSController of the ACE from the input name-file.
    @param ACE_FILE: Name of the input file that contains the ACE text.
    @return: DRS of the ACE text.
    """


    # Read the entirety of the file.
    file = open(ACE_FILE, 'r')
    sentences = file.read()
    file.close()

    # translating it from ACE to DRS using APE and putting it on a temporary file.
    os.system("./APE/ape.exe -text \"" + sentences + "\" -solo drspp > .temp")

    # convert the temporary file to a DRSController tu use after.
    temp = open(".temp", "r")
    DRS = DRSController(temp.read())
    temp.close()

    # deleting the temporary file.
    os.system("rm .temp")

    return DRS