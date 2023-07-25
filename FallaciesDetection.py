import Assets.GlobalVar as GlobalVar
from Assets.PrologManager import PrologManager
from Assets.Setup import setup
from Assets.ACEToDRS import transformACEToDRS


if __name__ == '__main__':
    setup()

    #STAGE 1 : TRANSFORM ACE SENTENCES TO DRS
    DRS = transformACEToDRS(GlobalVar.ACE_FILE_INPUT)

    #STAGE 1.5 : SHOW HOW THE DRS IS SEEN
    DRS.display()

    #STAGE 2 : TRANSFORM DRS TO PROLOG
    reasonnings, goal = DRS.DRSProlog()

    print(reasonnings, goal)

    #STAGE 3 : COMMUNICATE WITH PROLOG TO GET THE RESULT
    result = PrologManager.launchProlog(reasonnings, goal)

    #the result contains differents possible schemes. Note that if a non-fallacy sheme is valid, then the result is automatically not a fallacy.
    print(result)
    print(result[0]['X'][0][0]) # just to show how to get the scheme name.