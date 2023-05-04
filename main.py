import os


ACE_FILE_NAME_PREDICATS = ""
ACE_FILE_NAME_RESONNEMENTS = ""

if __name__ == '__main__':
    # ETAPE 0 : METTRE EN FORME LES PREDICATS ET RAISONNEMENTS
    liste_predicats, liste_raisonnements = form_predicats_raisonnements()


    #ETAPE 1 : TRANSFORMER LES PHRASES ACE EN DRS
    DRS_predicats = transformACEToDRS(liste_predicats)
    DRS_raisonnements = transformACEToDRS(liste_raisonnements)


    # ETAPE 2 : verifier le raisonnement
