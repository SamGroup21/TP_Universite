from Liste_chainee import *

def insertAfter(elt,val) :
    
    


def  InsertInSorted(liste,val) :
    if liste.nb==0 :              #on verifie la longuer de la liste
        ajouterValeur(liste,val)    # s'il est vide, on ajoute des valeur
    else :
        liste.nb=liste.nb + 1       # s'il ya deja des valeur on parcour notre chaine
        if  liste.tete.valeur > val :
            tmp = liste.tete
            liste.tete=Element(val)
            liste.tete.suivant=tmp
        else :
            insertAfter(liste.tete,val)


def prog() :
    
    ma_liste = Liste()
    ajouterValeur(ma_liste,6)
    ajouterValeur(ma_liste,7)
    afficherListe(ma_liste)
    InsertInSorted(ma_liste,5)
    InsertInSorted(ma_liste,6)
    InsertInSorted(ma_liste,2)
if __name__=="__main__" :
    
    prog()