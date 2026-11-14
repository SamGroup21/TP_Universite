# TRAVAIL  DEMANDE 

def grilleVide(nbligne:int,nbcolonne:int) -> list :
    resultat = []
        
    for i in range(0,nbligne) :
        liste= []
        for j in range(0,nbcolonne):
           liste.append(0)
        resultat.append(liste)
        
    return resultat

# print(grilleVide(4,4))
    
def initialiseGrille(g) :
    
    n = int(input("combien de cellule vous voulez mettre"))
    for i in range(n) :
        l = int(input("a quel position ligne "))
        c = int(input("a quel postion colonne "))
        g[l][c]= 1
    return g


def afficher(g) :
    l=len(g)
    c=len(g[0])
    for i in range(l) :
        
        for j in range(c) :
            print(g[i][j],end= " ")
            
        print()
# afficher(grilleVide(3,3))     
# afficher(initialiseGrille(grilleVide(5,5)))

def nbVoisin(gr:initialiseGrille,li,co) -> int :
    cpt = 0
    nb_ligne = len(gr)
    nb_colonne = len(gr[0]) if nb_ligne> 0 else 0
    for i in range(li - 1,li + 2) :
        for j in range(co-1,co+2) :
            if 0 <= i <= nb_ligne  and 0<= j<nb_colonne :
                while (gr[i][j]) == 1 :
                    cpt += 1
                    
    return cpt



# ou encore :

def nbVoisin(grille:list[list[int]],l :int,c:int) -> int :
    cpt : int = 0
    for i in range(l-1,l+2) :
        for j in range(c-1,c-2) :
            if not (i ==l and j == c) and (0<=i<len(grille) and 0<=j<len(grille[0])) :
                cpt += grille[i][j]
                
    return cpt
            
# def main() :

def nextGeneration(grille:list[list[int]]) ->list[list[int]] :
    nbL = len(grille)
    nbC = len(grille[0])
    newG = initialiseGrille(nbL,nbC)
    for i in range(nbL) :
        for j in range(nbC) :
            v = nbVoisin(grille,i,j)
            if (grille[i][j]== 1) and (2<=v<=3) :
                newG[i][j] = 1
            else :
                if(v==3) :
                    newG[i][j] = 1
    return newG

# def main() :


    
def affichageModeTexte(grille:list[list[int]]) -> list[list[int]] :
    nombre = int(input("combien de cellule vous voulez mettre "))
    for i in range(nombre) :
        li = int(input("quel position ligne"))
        co= int(input("quel position collone"))
        grille[li][co] = '|*|'
        for ligne in range(len(grille)) :
            for colonne in range(len(grille(ligne))) :
                if grille[ligne][colonne] == 0 :
                    print("| |")
                    
                    
                    




            

    
                
    
                 
                
        
     
            
    


    