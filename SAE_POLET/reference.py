import sys
import pygame 

# 1. Initialisation de Pygame
pygame.init()

# 2. Paramètres de la fenêtre
largeur, hauteur = 700, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mon premier programme Pygame")

# 3. Définition des couleurs (RGB)
NOIR = (125, 100, 100)
BLANC = (255, 255, 255)
ROUGE = (255, 50, 30)
GREEN = (0,  255, 255)

# 4. Horloge pour gérer les FPS (images par seconde)
horloge = pygame.time.Clock()

# Coordonnées et taille du carré
x, y = 350, 250
taille = 50
vitesse = 5

# 5. Boucle principale du jeu
en_cours = True
while en_cours:
  # Gestion des événements (fermeture de la fenêtre, clavier, souris)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      en_cours = False

  # Gestion des touches du clavier appuyées
  touches = pygame.key.get_pressed()
  if touches[pygame.K_LEFT]:
    x -= vitesse
  if touches[pygame.K_RIGHT]:
    x += vitesse
  if touches[pygame.K_UP]:
    y -= vitesse
  if touches[pygame.K_DOWN]:
    y += vitesse

  # Remplissage de l'arrière-plan (efface l'image précédente)
  fenetre.fill(GREEN)

  # Dessin d'un rectangle rouge
  pygame.draw.rect(fenetre, ROUGE, (x, y, taille, taille))

  # Mise à jour complète de l'affichage
  pygame.display.flip()

  # Limitation à 60 images par seconde
  horloge.tick(60)

# 6. Fermeture propre de Pygame
pygame.quit()
sys.exit()








# PROPOSITION  : 


# def afficherChoixCouleur(f:pg.Surface)->None:
#     for i in range(len(TabCouleur)):
#         pg.draw.circle(f,TabCouleur[i],[75,80+40*i],15)
#         pg.draw.circle(f,Noir,[75,80+40*i],15,1)
    
#     # Correction ici : le "pg.dra" coupé a été retiré pour éviter un plantage
#     pg.draw.circle(f,Marron,[75,80+40*9],15)
#     pg.draw.circle(f,Noir,[75,80+40*9],15,1)
#     pg.display.update()


# def afficherIHM():
#     global fenetre
#     # weigth (largeur) en premier, height (hauteur) en deuxième dans set_mode
#     fenetre = pg.display.set_mode((weigth, height))
#     pg.display.set_caption("Bienvenu sur notre page de Jeux")


# # --- NOUVELLE BOUCLE PRINCIPALE POUR LE MASTERMIND ---

# def jouer_mastermind():
#     # 1. On prépare la fenêtre de jeu
#     afficherIHM()
    
#     # 2. On remplit le fond en blanc pour effacer le noir de départ
#     fenetre.fill(Blanc)
    
#     # 3. On dessine les éléments fixes du Mastermind
#     afficherPlateau(fenetre)
#     afficherChoixCouleur(fenetre)
    
#     # 4. Génération du code SECRET de l'ordinateur (5 couleurs aléatoires)
#     # On choisit 5 couleurs au hasard parmi ton tableau TabCouleur
#     secret = [random.choice(TabCouleur) for _ in range(5)]
    
#     # Optionnel pour tricher/tester : On affiche le secret tout en haut
#     # afficherSecret(fenetre, secret)
    
#     print("Le code secret a été généré ! À vous de jouer.")

#     ligne_actuelle = 1
#     partie_en_cours = True

#     # Boucle principale du Mastermind
#     while partie_en_cours:
        
#         # Gestion de la fermeture de la fenêtre si le joueur clique sur la croix
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 return

#         # Si le joueur n'a pas dépassé les 15 essais maximum
#         if ligne_actuelle <= 15:
#             print(f"--- Essai numéro {ligne_actuelle} ---")
            
#             # Appel de TA fonction : elle bloque le jeu tant que le joueur 
#             # n'a pas cliqué sur 5 pions, puis elle renvoie la liste des couleurs choisies
#             proposition = construireProposition(fenetre, ligne_actuelle)
            
#             # --- LOGIQUE DE VÉRIFICATION (Le score) ---
#             # res[0] = pions bien placés (Blancs), res[1] = pions mal placés (Noirs)
#             bien_place = 0
#             mal_place = 0
            
#             # Copie pour ne pas détruire les listes originales pendant la vérification
#             secret_copie = list(secret)
#             prop_copie = list(proposition)
            
#             # Premier passage : on cherche les pions BIEN PLACÉS
#             for i in range(5):
#                 if prop_copie[i] == secret_copie[i]:
#                     bien_place += 1
#                     secret_copie[i] = None # On marque le pion comme "traité"
#                     prop_copie[i] = None
            
#             # Deuxième passage : on cherche les pions MAL PLACÉS parmi le reste
#             for i in range(5):
#                 if prop_copie[i] is not None:
#                     if prop_copie[i] in secret_copie:
#                         mal_place += 1
#                         # Retirer la première occurrence trouvée dans la copie du secret
#                         secret_copie[secret_copie.index(prop_copie[i])] = None
            
#             res = (bien_place, mal_place)
            
#             # Appel de TA fonction : affiche les petits cercles blancs et noirs de score
#             afficherResultat(fenetre, res, ligne_actuelle)
            
#             # --- VÉRIFICATION DE LA VICTOIRE OU DÉFAITE ---
#             if bien_place == 5:
#                 print("Félicitations ! Vous avez gagné !")
#                 # On révèle le secret tout en haut
#                 afficherSecret(fenetre, secret)
#                 partie_en_cours = False
#             else:
#                 # On passe à la ligne suivante pour l'essai suivant
#                 ligne_actuelle += 1
                
#         else:
#             print("Dommage, vous avez épuisé vos 15 essais. Partie perdue !")
#             # On montre la solution au joueur
#             afficherSecret(fenetre, secret)
#             partie_en_cours = False

#     # Une fois la partie finie (gagnée ou perdue), on laisse la fenêtre ouverte
#     # pour que le joueur puisse voir son résultat, jusqu'à ce qu'il ferme le jeu.
#     attente = True
#     while attente:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 attente = False
                
#     pg.quit()

# # --- LANCEMENT DU JEU ---
# jouer_mastermind()




    




    

    

        
