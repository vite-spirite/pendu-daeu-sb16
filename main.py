from random import random

def si_contient(liste, caractere):
    return caractere in liste  

def si_dans_mot(caractere, mot):
    for i in mot:
        if caractere == i:
            return True

    return False

def demander_saisi():
  saisie = input("proposez une lettre : ")

  while len(saisie) != 1 or not saisie.isalpha():
      print("veillez saisir une seule lettre.")
      saisie = input("proposez une lettre : ")

  return saisie.lower()

def selection_mot():
    file = open('dictionnaire.txt', mode='r', encoding='utf8')

    content = file.read()
    file.close()

    lines = content.splitlines()
    selected_idx = int(random() * len(lines))
    return lines[selected_idx].split(';')[0]

def calcule_indice(mot, lettre_trouvees):
    indice = ""

    for lettre in mot:
        if si_contient(lettre_trouvees, lettre):
            indice += lettre
        else:
            indice += "_"

    return indice 


def partie_terminee(mot_a_trouver, lettres_trouvees):
    for lettre in mot_a_trouver:
        if not si_contient(lettres_trouvees, lettre):
            return False
    return True  


mot_a_trouver = selection_mot()
lettres_trouves = []
lettres_incorrects = []
vie = 5
trouve = False

print("Mot à trouver:", calcule_indice(mot_a_trouver, lettres_trouves))

while vie > 0 and not trouve:
    saisie = demander_saisi()

    if si_dans_mot(saisie, mot_a_trouver):
        if not si_contient(lettres_trouves, saisie):
            lettres_trouves.append(saisie)
    else:
        if not si_contient(lettres_incorrects, saisie):
            lettres_incorrects.append(saisie)
            vie -= 1

    trouve = partie_terminee(mot_a_trouver, lettres_trouves)

    print('============================================')
    print("Il vous reste", vie, "vies.")
    print("Lettres incorrects:", lettres_incorrects)
    print(calcule_indice(mot_a_trouver, lettres_trouves))

print('============================================')
if trouve:
    print("Vous avez gangé.")
else:
    print("Vous avez perdu.")

print("Le mot à trouver été:", mot_a_trouver)