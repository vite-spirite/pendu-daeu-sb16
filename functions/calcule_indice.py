from si_dans_mot import si_dans_mot

def calcule_indice(word, characters):
    indice = ""

    for i in word:
        if si_dans_mot(i, characters):
            indice += i
        else:
            indice += "_"

    return indice


print(calcule_indice("aeaeaeae", ['e']))