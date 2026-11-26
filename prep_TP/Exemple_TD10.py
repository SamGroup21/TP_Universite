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


# def prog() :
    
#     ma_liste = Liste()
#     ajouterValeur(ma_liste,6)
#     ajouterValeur(ma_liste,7)
#     afficherListe(ma_liste)
#     InsertInSorted(ma_liste,5)
#     InsertInSorted(ma_liste,6)
#     InsertInSorted(ma_liste,2)


# FICHE DE TD 11 :


class Instant :
    def __init__(self,heure = 0,minute= 0,seconde = 0) :
        self.h = heure
        self.m= minute
        self.s= seconde
        
    def __str__(i) :             #methode : fonction qu'on appele a prtie de l'objet
            return f"{i.h:02}: {i.m:02}:{i.s:02}"    
        
# question b :
     
def read_Instant() :
    
    heure =int(input(" entrer l'heure : "))
    minute = int(input("entrer les minute : "))
    seconde= int(input("entrer les secondes : "))
    
    return Instant(heure,minute,seconde)

#QUESTION D :

def isValid(self)->bool :
    return 0<=self.h<=24 and 0<=self.m<=60 and 0<=self.s<=60


def __add__(self,another :Instant) ->  :
    
    s = self.s +another.s
    if(s>59) :
        rem=1
        s=s-60
    else :
        rm = 0
        
    m = self.m +another.m + rm
    if(m>59) :
        rm=1
        s= s-60
        
    else :
        rm = 0
        m = self.m+another.m + rm

        


#QUESTION C

def print_Instant(i :Instant) -> None :
    print(f"{i.h:02}: {i.m:02}:{i.s:02}")
    
#QUESTION E :    

def estPlusRecent(t1,t2)-> bool :
    if t1.h < t2.h :
        return False
    elif t1.h > t2.h :
        return True
    elif t1.m < t2.m :
        return False
    elif t1.m > t2.m :
        return True
    elif t1.s < t2.s :
        return False
    else :
        return True
    
#QUESTION G :
    
def duree(debut,fin) :
    debut = debut.h*3600+debut.m*60+debut.s
    fin = fin.h*3600+fin.m*60+fin.s
    diff = abs(debut-fin)
    diff_h = diff//3600
    diff = diff%3600
    diff_m = diff//60
    diff_s = diff %60
    return Instant(diff_h,diff_m,diff_s)
    
    
def fonc(a,b,operation:str) :
    a=int(input("entrer a : "))
    b=int(input("entre b : "))
    operation = input("quel est l'operation")
    
    if operation == "+" :
        return a+b
    elif operation == "-" :
        return a-b
    elif operation == "/" :
        return a/b
    else :
        return None
    

def prog() :
    #maintenant = read_Instant()
    #print_Instant(maintenant)
    #apres = read_Instant()
    #print_Instant(apres)
    #print(estPlusRecent(apres,maintenant))
    #temps = duree(maintenant,apres)
    #print_Instant(temps)
    
    print(fonc(0,0,'+'))

#class  Voiture :
    #nb_voiture_cree = 0
    #def __init__(self,marque) :
    #    self.marque= marque
   #     Voiture.nb_voiture_cree+=1
  #  def  afficher_marque(self) :
 #       print(f"la voiture est de marque {self.marque}")
    
#voiture1 = Voiture("Voxy")
#voiture2 = Voiture("Noah")
#print(voiture1.marque)
#print(voiture2.marque)
#print(Voiture.nb_voiture_cree)
#print(voiture1.afficher_marque())
#print(Voiture.afficher_marque(voiture2))


class Etudiant :
    def __init__(self,nom,prenom,age,moyenne,promotion) :
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
        self.promotion = promotion
        
def saisir_information () :
    nom = input("entre le nom de l'etudiant : ")
    prenom = input("entre le prenom de l'etudiant : ")
    age = int(input("entre l'anne de naissance : "))
    moyenne = float(input("entre la moyenne de l'etudiant : "))
    promotion = int(input("il est de quel promotion 1 ou 2 : "))
    
    while promotion !=1 and promotion !=2:
        raise "erreur la promotion est 1 ou 2"
        promotion = int(input("il est de quel promotion 1 ou 2 : "))
        
    nouvel_etudiant = Etudiant(nom,prenom,age,moyenne,promotion)
    
    return nouvel_etudiant
        
def afficher_etudiant(liste_etudiant):
    for etudiant in liste_etudiant :
        print(f"Nom : {etudiant.nom}, Prenom : {etudiant.prenom}, Age : {etudiant.age},Moyenne : {etudiant.moyenne}, Promotion : {etudiant.promotion}")
    return 

def ajouter_etudiant(liste) :
    autre_etudiant = saisir_information()
    liste.append(autre_etudiant)
    return liste

def recherche_etudiant(liste) :
    n = input("vous cherchez quel etudiant : ")
    for i in range(len(liste)) :
        if liste[i].nom == n :
            print(f"l'etudiant {n} est sur l'indice {i}")
            return i
    print(f"l'etudiant {n} n'est pas dans la liste")
    return -1
        
def retrait_etudiant(liste) :
    indice = recherche_etudiant()
    if indice != -1 :
        del liste[indice]
        print("l'etudiant est supprimé")
            
    return liste
        
# liste = []
# #etudiant1 = saisir_information()
# #liste.append(etudiant1)
# ajouter_etudiant(liste)
# afficher_etudianat(liste)
# ajouter_etudiant(liste)
# afficher_etudiant(liste)
# #recherche_etudiant(liste)
# retrait_etudiant(liste)



# FICHE  DE TP 5 :INITIATION AU DEVELOPPEMENT :


class Etudiant :
    def __init__(self,nom,prenom,anne_naissance,moyenne,promotion) :
        self.nom = nom
        self.prenom = prenom
        self.anne_naissance = anne_naissance
        self.moyenne = moyenne
        self.promotion = promotion
        


def saisir_information() :
    nom = input("entrer le nom de l'etudiant : ")
    prenom = input("entre le prenom de l'etudiant : ")
    anne_naissance = int(input("entrer l'anne de naissance de l'etudiant : "))
    moyenne = int(input("entrer la moyenne de l'etudiant : "  ))
    promotion = int(input("il est de quel promotion (1 ou 2) :"))
    
    while promotion !=1 and promotion !=2 :
        promotion = int(input("il est de quel promotion (1 ou 2) :"))
        
    nouvel_etudiant = Etudiant(nom, prenom, anne_naissance,moyenne,promotion)
    
    return nouvel_etudiant


def afficher_etudiant(liste_etudiant) :
    for etudiant in liste_etudiant :
        print(f"Nom : {etudiant.nom}, Prenom : {etudiant.prenom},Anne de naissance : {etudiant.anne_naissance},Moyenne : {etudiant.moyenne}, Promotion : {etudiant.promotion}")
        
    return



def ajouter_etudiant(liste) :
    autre_etudiant = saisir_information()
    liste.append(autre_etudiant)
    
    return liste

def rechercher_etudiant(liste,qui) :
    taille = len(liste)
    for i in range(taille) :
        if liste[i].nom == qui :
            print(f"l'etudiant {qui} est sur l'indice {i}")
        
    return -1

def retrait_etudiant(liste,suprimme) :
    indice = rechercher_etudiant(liste,suprimme)
    if indice != -1 :
       del liste[indice]
       print("l'etudiant à ete supprimé")
            
    return liste

def trier_etudiant(liste) :
    n = len(liste)
    
    for i in range(n) :
        indice_max = i
        for j in range(i+1,n) :
            if liste[j].moyenne > liste[indice_max].moyenne :
               indice_max = j
               
        liste[i],liste[indice_max] = liste[indice_max],liste[i]
               
    return liste

def major_promotion() :
    
    
    





def prog():
    #etudiant1 = Etudiant("Isaac","Ibrahim",2000,50,2)
    #print(etudiant1.nom)
    #print(etudiant1.prenom)
    liste = []
    liste.append(saisir_information())
    afficher_etudiant(liste)
    ajouter_etudiant(liste)
    afficher_etudiant(liste)
    #qui = input("vous chercher qui : ")
    #rechercher_etudiant(liste,qui)
    #suprimme = input("on supprime qui : ")
    #retrait_etudiant(liste,suprimme)
    trier_etudiant(liste)
    
    
prog()
    
    
    
    
    
    
    
    






 


    
