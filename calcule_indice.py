def calcule_indice(mot, lettre_trouvees):
    indice = ""

    for lettre in mot:
        if lettre in lettre_trouvees:
            indice += lettre
        else:
            indice += "-"

    return indice 