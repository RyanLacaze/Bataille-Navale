# Ce code à pour but de créer le jeu bataille navale
# et de pouvoir y jouer contre l'ordinateur

# importer les bibliothèques tkinter(interface graphique) et random(aléatoire)
import tkinter as tk
import random

# cette classe défini toutes les caractéristiques des bateaux
class Bateau:
    def __init__(self, nom, taille):
        self.nom = nom
        self.taille = taille
        self.positions = []
        self.toucher = []

    # Cette fonction vérifie si un bateau coule par rapport à sa longueur
    def est_coule(self):
        return len(self.toucher) == self.taille

# Cette classe défini les actions présentes dans la grille
class Plateau:
    def __init__(self, taille):
        self.taille = taille
        self.grille = [[None for _ in range(taille)] for _ in range(taille)]
        self.bateaux = []

    # Cette fonction ajoute les bateaux à différentes postions dans la grille
    def ajouter_bateau(self, bateau, positions):
        for x, y in positions:
            self.grille[x][y] = bateau
        bateau.positions = positions
        self.bateaux.append(bateau)

    # Cette fonction détaille la fonction tir
    def tir(self, x, y):
        cible = self.grille[x][y]
        if isinstance(cible, Bateau):  # Vérifie si la cible est un navire
            cible.toucher.append((x, y))
            return True, cible.est_coule()
        # La case est vide
        elif cible is None:
            self.grille[x][y] = "manqué"
            return False, False
        # La case a déjà été tirée
        return False, False

# Cette classe désigne la grille par rapport au nom
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.plateau = Plateau(10)

# Cette classe contient tous les éléments pour jouer à la bataille navale
class Bataille_navale:
    def __init__(self):
        self.joueur = Joueur("Joueur")
        self.ordi = Joueur("Ordinateur")
        self.fenetre = tk.Tk()
        self.fenetre.title("Bataille Navale")
        self.fenetre.config(bg="#7c88f5")
        self.fenetre.resizable(width=False, height=False)
        self.grille_joueur = []
        self.grille_ordi = []
        self.tour_joueur = True
        self.initialiser_interface()
        self.placer_bateaux_ordi()

    # Cette fonction contient l'interface graphiques (fenetre, frame, grille)
    def initialiser_interface(self):
        frame_joueur = tk.Frame(self.fenetre)
        frame_joueur.grid(row=1, column=1)
        frame_ordi = tk.Frame(self.fenetre)
        frame_ordi.grid(row=0, column=0)

        # Ajout des cases de 1 à 10 avec l'indice verticale
        for x in range(10):
            ligne_joueur = []
            ligne_ordi = []

            # Ajout des cases de 1 à 10 avec l'indice horizontale
            for y in range(10):
                # Ajout des boutons dans chaque cases de la grille du joueur
                bouton_joueur = tk.Button(frame_joueur, width=4, height=2, command=lambda x=x, y=y: self.placer_bateaux(x, y), bg="#9ba2ff")
                bouton_joueur.grid(row=x, column=y)
                ligne_joueur.append(bouton_joueur)

                # Ajout des boutons dans chaque cases de la grille de l'ordinateur
                bouton_ordi = tk.Button(frame_ordi, width=4, height=2, command=lambda x=x, y=y: self.tir_joueur(x, y), bg="#9ba2ff")
                bouton_ordi.grid(row=x, column=y)
                ligne_ordi.append(bouton_ordi)

            self.grille_joueur.append(ligne_joueur)
            self.grille_ordi.append(ligne_ordi)

    # Cette fonction place les bateux dans la grille de l'ordinateur
    def placer_bateaux_ordi(self):
        tailles_bateaux = [5, 4, 3, 3, 2, 2]
        for taille in tailles_bateaux:
            place = False
            while not place:
                orientation = random.choice(["horizontal", "vertical"])
                x = random.randint(0, self.ordi.plateau.taille - 1)
                y = random.randint(0, self.ordi.plateau.taille - 1)
                positions = []
                for i in range(taille):
                    if orientation == "horizontal":
                        positions.append((x, y + i))
                    else:
                        positions.append((x + i, y))

                if self.positions_valides(self.ordi.plateau, positions):
                    bateau = Bateau(f"Bateau-{taille}", taille)
                    self.ordi.plateau.ajouter_bateau(bateau, positions)
                    print(f"Bateau {bateau.nom} placé : {positions}")
                    place = True

    # ctte fonction vérifie que la positions des bateaux est valides
    def positions_valides(self, plateau, positions):
        for x, y in positions:
            if x < 0 or x >= plateau.taille or y < 0 or y >= plateau.taille or plateau.grille[x][y]:
                return False
        return True

    def placer_bateaux(self, x, y):
        # Logique de placement manuel du joueur
        pass

    # Cette fonction détaille les actions lié aux tirs du joueur
    def tir_joueur(self, x, y):
        if not self.tour_joueur:
            return
        touche, coule = self.ordi.plateau.tir(x, y)
        bouton = self.grille_ordi[x][y]

        # Changement de couleur des boutons
        if touche:
            bouton.config(bg="#f2372b")
            if coule:
                print("Bateau coulé!")
        else:
            bouton.config(bg="#2a34d3")

        self.tour_joueur = False
        self.tir_ordi()

    # Cette fonction détaille les actions lié aux tirs du l'ordinateur, celui-ci tir de manière aléatoire
    def tir_ordi(self):
        x, y = random.randint(0, 9), random.randint(0, 9)
        touche, coule = self.joueur.plateau.tir(x, y)
        bouton = self.grille_joueur[x][y]

        # Changement de couleur des boutons
        if touche:
            bouton.config(bg="#f2372b")
        else:
            bouton.config(bg="#2a34d3")

        self.tour_joueur = True

    # lance le code en boucle
    def run(self):
        self.fenetre.mainloop()

# Appeler dans le main
if __name__ == "__main__":
    jeu = Bataille_navale()
    jeu.run()
