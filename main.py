from random import random

def si_contient(liste, caractere):
    return caractere in liste  

def si_dans_mot(char, word):
    for i in word:
        if char == i:
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



def selection_mot():
    file = open('dictionnaire.txt', mode='r', encoding='utf8')

    content = file.read()
    file.close()

    lines = content.splitlines()
    selected_idx = int(random() * len(lines))
    return lines[selected_idx].split(';')[0]

def partie_terminee(mot_a_trouver, lettres_trouvees):
    for lettre in mot_a_trouver:
        if lettre not in lettres_trouvees:
            return False
    return True  


