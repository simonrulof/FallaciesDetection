import Assets.GlobalVar as GlobalVar


def setup():
    """
    set up the global variables from the config file
    global variables are :
        ACE_FILE_INPUT
        ACE_FILE_OUTPUT
    """

    # open the config file
    file = open("config", "r")

    # setting up all the global variables from the config file.
    line = file.readline()
    while line:
        data = line.split(' ')
        if data[0] == "ACE_FILE_INPUT=":
            GlobalVar.ACE_FILE_INPUT = data[1][:-1:]
        if data[0] == "ACE_FILE_OUTPUT=":
            GlobalVar.ACE_FILE_OUTPUT = data[1][:-1:]
        line = file.readline()
    file.close()
