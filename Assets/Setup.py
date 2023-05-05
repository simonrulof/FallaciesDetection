import Assets.GlobalVar as GlobalVar


def setup():

    file = open("config", "r")

    line = file.readline()
    while line:
        data = line.split(' ')
        if data[0] == "ACE_FILE_NAME=":
            GlobalVar.ACE_FILE_NAME = data[1][:-1:]
        if data[0] == "ACE_FILE_OUTPUT=":
            GlobalVar.ACE_FILE_OUTPUT = data[1][:-1:]
        line = file.readline()

