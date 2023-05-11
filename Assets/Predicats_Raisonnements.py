def form_predicates_reasoning(ACE_FILE):
    """

    :param ACE_FILE: file where ACE sentences are
    :return: list of the names of the sentences,
            list of the predicates for each sentence,
            list of the reasoning for each sentence
    """

    file = open(ACE_FILE, "r")

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

        i += 1

    file.close()
    return listNameSentences, listPredicates, listReasoning
