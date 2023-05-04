def form_predicats_raisonnements(ACE_FILE_NAME):
    file = open(ACE_FILE_NAME, "r")

    listNameSentences = []
    listPredicates = []
    listReasoning = []

    i = 0

    line = file.readline()
    while line[:-1:] != '':
        listNameSentences.append(line[:-2:])

        listPredicates.append([])
        line = file.readline()
        while line[:-1:] != '':
            listPredicates[i].append(line[:-1:])
            line = file.readline()

        listReasoning.append([])
        line = file.readline()
        while line[:-1:] != '':
            listReasoning[i].append(line[:-1:])
            line = file.readline()

        file.readline()
        line = file.readline()

        i+= 1
    return listNameSentences, listPredicates, listReasoning