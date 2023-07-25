import Assets.GlobalVar as GlobalVar
from Assets.PrologManager import PrologManager
from Assets.Setup import setup
from Assets.ACEToDRS import transformACEToDRS


if __name__ == '__main__':
    setup()

    #ETAPE 1 : TRANSFORMER LES PHRASES ACE EN DRS
    DRS = transformACEToDRS(GlobalVar.ACE_FILE_INPUT)


    DRS.display()

    #ETAPE 2 : TRANSFORMER LES PHRASES DRS EN PROLOG
    reasonnings, goal = DRS.DRSProlog()

    print(reasonnings, goal)

    #ETAPE 3 : PARLER AVEC PROLOG
    result = PrologManager.launchProlog(reasonnings, goal)

    print(result)