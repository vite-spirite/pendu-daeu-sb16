from si_dans_mot import si_dans_mot

def calcule_indice(mot, lettre_trouvees):
    indice = ""

    for lettre in mot:
        if lettre in lettre_trouvees:
            indice += lettre
        else:
            indice += "-"

    return indice 


print(calcule_indice("aeaeaeae", ['e']))