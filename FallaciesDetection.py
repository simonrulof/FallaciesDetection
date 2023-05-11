import Assets.GlobalVar as GlobalVar
from Assets.Setup import setup
from Assets.Predicats_Raisonnements import form_predicates_reasoning
from Assets.ACEToDRS import transformACEToDRS


if __name__ == '__main__':
    setup()

    # ETAPE 0 : METTRE EN FORME LES PREDICATS ET RAISONNEMENTS
    listNameSentences, listPredicates, listReasoning = form_predicates_reasoning(GlobalVar.ACE_FILE_INPUT)

    #ETAPE 1 : TRANSFORMER LES PHRASES ACE EN DRS
    DRS_ListPredicates = transformACEToDRS(listPredicates)
    DRS_listReasoning = transformACEToDRS(listReasoning)


    # ETAPE 2 : verifier le raisonnement
