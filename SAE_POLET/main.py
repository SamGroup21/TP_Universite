import sys
import pygame as pg
import random
# 1. IMPORTATION DU MODULE MM COMME DEMANDÉ PAR L'ÉNONCÉ
import mm 

# Initialisation du moteur Pygame
pg.init()

# Définition des dimensions (Largeur = 800, Hauteur = 1000 pour le plateau vertical)
largeur, hauteur = 800, 1000
fenetre = None

def afficherIHM():
    global fenetre
    # Pygame prend (largeur, hauteur) en paramètre
    fenetre = pg.display.set_mode((largeur, hauteur))
    pg.display.set_caption("Bienvenu sur notre page de Jeux")
    
    # ÉTAPES D'AFFICHAGE DE L'ENSEMBLE DE L'IHM (Utilisation des variables/fonctions de mm.py)
    fenetre.fill(mm.Blanc)          # On colore le fond en utilisant mm.Blanc
    mm.afficherPlateau(fenetre)      # On dessine le plateau de mm.py
    mm.afficherChoixCouleur(fenetre) # On dessine la palette de couleurs de mm.py

def executer_mastermind():
    # Affichage initial de l'IHM
    afficherIHM()
    
    # Génération de la combinaison secrète (5 couleurs aléatoires)
    # On pioche dans le tableau TabCouleur qui appartient à mm.py
    secret = [random.choice(mm.TabCouleur) for _ in range(5)]
    
    # Pour tester ton code, tu peux décommenter la ligne ci-dessous pour voir le secret s'afficher en haut :
    # mm.afficherSecret(fenetre, secret)
    
    ligne_actuelle = 1
    en_cours = True 
    
    # BOUCLE PRINCIPALE DU JEU
    while en_cours:
        # Gestion des événements système (clic sur la croix pour fermer)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                en_cours = False
                pg.quit()
                sys.exit()

        # Si le joueur n'a pas dépassé les 15 essais réglementaires
        if ligne_actuelle <= 15:
            # Appel de la fonction de mm.py pour récupérer les clics du joueur
            proposition = mm.construireProposition(fenetre, ligne_actuelle)
            
            # --- CALCUL DU SCORE (Pions bien placés / mal placés) ---
            bien_place = 0
            mal_place = 0
            
            secret_copie = list(secret)
            prop_copie = list(proposition)
            
            # 1er passage : détection des pions bien placés (mêmes places)
            for i in range(5):
                if prop_copie[i] == secret_copie[i]:
                    bien_place += 1
                    secret_copie[i] = None
                    prop_copie[i] = None
            
            # 2e passage : détection des pions mal placés (bonne couleur, mauvaise place)
            for i in range(5):
                if prop_copie[i] is not None:
                    if prop_copie[i] in secret_copie:
                        mal_place += 1
                        secret_copie[secret_copie.index(prop_copie[i])] = None
            
            # Envoi du résultat à la fonction d'affichage de mm.py
            # res[0] = bien placés, res[1] = mal placés
            res = (bien_place, mal_place)
            mm.afficherResultat(fenetre, res, ligne_actuelle)
            
            # --- VÉRIFICATION DE LA CONDITION DE VICTOIRE ---
            if bien_place == 5:
                print("Félicitations, vous avez gagné !")
                mm.afficherSecret(fenetre, secret) # On révèle le secret final
                en_cours = False
            else:
                # On passe à la tentative suivante (ligne du dessous)
                ligne_actuelle += 1
        else:
            print("Partie terminée, vous avez épuisé vos 15 essais.")
            mm.afficherSecret(fenetre, secret) # On révèle le secret perdu
            en_cours = False

    # Boucle de fin : maintient la fenêtre ouverte pour contempler le résultat
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

# Lancement officiel du programme principal
executer_mastermind()

