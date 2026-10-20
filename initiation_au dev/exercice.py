# TRAVAIL  DEMANDE 

def grilleVide(nbligne:int,nbcolonne:int) -> list :
    resultat = []
    liste= []
        
    for j in range(0,nbcolonne) :
        liste.append(0)
    for i in range(0,nbligne):
        resultat.append(liste)
        
    return resultat
    
def initialiseGrille(g) :
    
    n = int(input("combien de cellule vous voulez mettre"))
    for i in range(n) :
        l = int(input("a quel position ligne"))
        c = int(input("a quel postion colonne"))
        g[l][c]=1
    return g


def afficher(g) :
    l=len(g)
    c=len(g[0])
    for i in range(l) :
        
        for j in range(c) :
            print(g[i][j],end= " ")
            
        print()
afficher(grilleVide(3,3) )     
afficher(initialiseGrille(grilleVide(3,3)))
        
     
            
    


    