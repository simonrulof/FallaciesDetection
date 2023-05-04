import Assets
from Assets.Predicats_Raisonnements import form_predicats_raisonnements
from Assets.ACEToDRS import transformACEToDRS

ACE_FILE_NAME = "ACE_SENTENCES"

if __name__ == '__main__':
    # ETAPE 0 : METTRE EN FORME LES PREDICATS ET RAISONNEMENTS
    listNameSentences, listPredicates, listReasoning = form_predicats_raisonnements(ACE_FILE_NAME)

    #ETAPE 1 : TRANSFORMER LES PHRASES ACE EN DRS
    DRS_ListPredicates = transformACEToDRS(listPredicates)
    DRS_listReasoning = transformACEToDRS(listReasoning)


    # ETAPE 2 : verifier le raisonnement
