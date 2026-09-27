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

Nous utilisons **GitHub Codespaces** pour pouvoir coder et tester directement depuis le navigateur sans aucune installation locale.

### 1. Lancer l'environnement de développement

1. En haut de cette page, cliquez sur le bouton vert **`<> Code`**.
2. Allez dans l'onglet **Codespaces**.
3. Cliquez sur **Create codespace on main**.
4. _(Patientez quelques secondes au premier démarrage : l'environnement et l'extension Python s'installent automatiquement grâce au devcontainer)._

### 2. Tester le code

Dans l'éditeur qui s'ouvre, vous pouvez exécuter le script soit :

- En cliquant sur l'icône **Play (▶)** en haut à droite.
- En ouvrant le terminal en bas de l'écran (`Terminal` ➔ `New Terminal`) et en tapant :
    ```bash
    python main.py
    ```

## 💾 Comment valider et envoyer vos modifications (Commit & Push)

> ⚠️ **IMPORTANT :** Enregistrer votre fichier (`Ctrl + S`) garde vos modifications dans votre Codespace privé, mais **ne les publie pas** sur le dépôt partagé du groupe ! Pour que tout le monde voie votre code, il faut obligatoirement faire un **Commit** et un **Push**.

Voici la marche à suivre pas-à-pas dans Codespaces :

1. **Ouvrir le panneau Git :** Dans le menu vertical tout à gauche, cliquez sur l'icône **Source Control** (les 3 petits ronds reliés par des lignes, ou raccourci `Ctrl + Shift + G`).
2. **Écrire un message de commit :** Dans la zone de texte sous _Message_, écrivez une phrase courte décrivant ce que vous avez fait (ex: `Ajout de la fonction selection_mot` ou `Correction bug saisie`).
3. **Valider le commit :** Cliquez sur le bouton bleu **Commit** (ou faites `Ctrl + Enter`).
4. **Envoyer sur GitHub (Push) :** Cliquez sur le bouton bleu **Sync Changes** (ou **Push**) qui apparaît juste après pour envoyer vos changements sur le dépôt commun.

Une fois ces étapes faites, votre code est sauvegardé en ligne et visible par toute l'équipe !
