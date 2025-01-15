Bonjour, je suis Ryan Lacaze.

Voici le jeu de la bataille navale en python avec tkinter comme interface graphique où le joueur affronte l'ordinateur.

Sommaire :
1. Importation
2. Bateaux
3. Grille
4. Placer les bateaux
5. Gestion des tirs
6. Gestion de l'ordinateur
7. Lancer le code

1. Importation 

Pour commencer, j'importe la bibliothèque de l'interface graphique tkinter ainsi que la bibliothèque random car il y aura besoin d'aléatoire pour le jeu.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20124905.png")

2. Bateaux

Ensuite, je défini des caractéristiques pour la classe bateau.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20125828.png")

3. Grille

Pour la grille, Elle se créer via deux variables, x pour la longueur et y pour la largeur.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20130135.png")
![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20130143.png")

L'intéraction avec la grille se fera avec des boutons.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20130719.png")

4. Placer les bateaux

Maintenat que la grille à été créer, il faut placer les bateaux.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20130719.png")

5. Gestionss des tirs

Pour les tirs, il faut signifié si un bateau est touché ou si le tir est raté.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20231558.png")

Si un tir touche un bateau, le bouton devient rouge et si le tir est raté, le bouton devient bleu foncé.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20231632.png")

6. Gestion de l'odrinateur

Pour l'ordinateur, il aura sa propre grille ainsi que son propre placement de bateau et sa propre gestion des tirs.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20232300.png")

Les tirs de l'ordinateur seront aléatoires de 1 à 10 que se soit verticalement ou horizontalement.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20232530.png")

7. Lancer le code

Le code est une boucle continue qui sera appelé dans le main.

![Alt text]("file:///C:/Users/ryanl/OneDrive/Images/Captures%20d%E2%80%99%C3%A9cran/Capture%20d'%C3%A9cran%202025-01-15%20233042.png")

