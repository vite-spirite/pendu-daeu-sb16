# Projet Jeu du Pendu — Classe Inversée

Ce dépôt contient le code source et la documentation pour le projet du jeu du pendu en Python dans le cadre du cours.

---

## 📐 Architecture du projet

Pour garder un code clair et structuré, le programme est découpé en 4 fonctions principales :

- `selection_mot()` : Choisit un mot au hasard depuis le fichier `dictionnaire.txt`.
- `calcule_indice(mot, lettres_trouvees)` : Génère la chaîne d'affichage avec les lettres devinées et les tirets.
- `valider_saisie(saisie, mot)` : Vérifie la validité de l'entrée utilisateur.
- `partie_terminee(vies, mot, lettres_trouvees)` : Contrôle les conditions de fin (victoire ou défaite).

### Algorigramme de la boucle de jeu

![Algorigramme du jeu du pendu](algorigramme.png)

---

## 🚀 Comment contribuer au projet ?

Nous utilisons **GitHub Codespaces** pour pouvoir coder et tester directement depuis le navigateur sans aucune installation local.

### 1. Lancer l'environnement de développement

1. En haut de cette page, cliquez sur le bouton **`<> Code`**.
2. Allez dans l'onglet **Codespaces**.
3. Cliquez sur **Create codespace on main**.

### 2. Tester le code

Dans l'éditeur qui s'ouvre, ouvrez le terminal en bas de l'écran et lancez :

```bash
python main.py
```
