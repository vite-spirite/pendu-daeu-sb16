def demander_saisi():
  saisie = input("proposez une lettre : ")

  while len(saisie) != 1 or not saisie.isalpha():
      print("veillez saisir une seule lettre.")
      saisie = input("proposez une lettre : ")

  return saisie.lower()
