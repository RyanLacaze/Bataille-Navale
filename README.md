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

![Capture d'écran 2025-01-15 124905](https://github.com/user-attachments/assets/e228fce3-be84-4d50-802b-8e80d6e64221)

2. Bateaux

Ensuite, je défini des caractéristiques pour la classe bateau.

![Capture d'écran 2025-01-15 125828](https://github.com/user-attachments/assets/62ad5ea0-1576-46ed-b531-dd578b14dce7)

3. Grille

Pour la grille, Elle se créer via deux variables, x pour la longueur et y pour la largeur.

![Capture d'écran 2025-01-15 130135](https://github.com/user-attachments/assets/9f6e5a78-0230-4185-a09a-ae3f4b25a541)
![Capture d'écran 2025-01-15 130143](https://github.com/user-attachments/assets/27d9dfb4-7e91-4acb-b0ff-89629938f3dd)

L'intéraction avec la grille se fera avec des boutons.

![Capture d'écran 2025-01-15 130719](https://github.com/user-attachments/assets/ed773c94-d96b-4f54-b18f-846415942a41)

4. Placer les bateaux

Maintenat que la grille à été créer, il faut placer les bateaux.

![Capture d'écran 2025-01-15 233906](https://github.com/user-attachments/assets/74cb1768-dade-4857-a0cb-7275e08bb968)

5. Gestions des tirs

Pour les tirs, il faut signifié si un bateau est touché ou si le tir est raté.

![Capture d'écran 2025-01-15 231558](https://github.com/user-attachments/assets/33a91455-810a-49cf-af36-173ef389023b)

Si un tir touche un bateau, le bouton devient rouge et si le tir est raté, le bouton devient bleu foncé.

![Capture d'écran 2025-01-15 231632](https://github.com/user-attachments/assets/b60797ae-f3f9-4d4c-8d0d-052b54631065)

6. Gestion de l'ordinateur

Pour l'ordinateur, il aura sa propre grille ainsi que son propre placement de bateau et sa propre gestion des tirs.

![Capture d'écran 2025-01-15 232300](https://github.com/user-attachments/assets/176e22eb-b011-44ba-a1d2-d2ad02b55929)

Les tirs de l'ordinateur seront aléatoires de 1 à 10 que se soit verticalement ou horizontalement.

![Capture d'écran 2025-01-15 232530](https://github.com/user-attachments/assets/b636ba6d-7678-4b4b-ab5d-0fec4867ceff)

7. Lancer le code

Le code est une boucle continue qui sera appelé dans le main.

![Capture d'écran 2025-01-15 233042](https://github.com/user-attachments/assets/cd8606b0-a736-4196-b89b-4e8d3f86fc1d)
