def partie_terminee(mot_a_trouver, lettres_trouvees):
    for lettre in mot_a_trouver:
        if lettre not in lettres_trouvees:
            return False
    return True  