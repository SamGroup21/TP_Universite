class Element:
    def __init__(self,v,s=None):
        self.valeur = v
        self.suivant = s
class Liste:
    def __init__(self):
        self.tete = None
        self.nb = 0
        
def setValeur(elt:Element, v):
    elt.valeur = v
    
def setSuivant(elt:Element, succ:Element):
    elt.suivant = succ
    
def ajouterValeur(lst:Liste,v)->Liste:
    lst.nb = lst.nb+1
    if lst.tete == None:
        lst.tete=Element(v)
        return lst   
    elt = lst.tete   
    while elt.suivant!=None:
        elt = elt.suivant
    nouv = Element(v)
    elt.suivant = nouv
    return lst

def afficherListe(lst:Liste):
    print("[ ",end="")
    elt = lst.tete
    while elt!=None :
        print(elt.valeur,end="")
        elt = elt.suivant
        if(elt!=None):
            print(", ",end="")
    print("]")
    
def longueurListe(lst:Liste)->int:
    return lst.nb

def getAt(lst:Liste,n:int):
    if(n>lst.nb) or n<1:
        return None
    cpt = 1
    elt = lst.tete
    while cpt<n:
        elt = elt.suivant
        cpt = cpt + 1
    return elt.valeur

def delAt(lst:Liste,n:int):
    if(n>lst.nb) or n<1:
        return None
    lst.nb = lst.nb - 1
    if n==1:
        val=lst.tete.valeur
        lst.tete = lst.tete.suivant
        return val
    cpt = 1
    elt = lst.tete
    while cpt<n-1:
        elt = elt.suivant
        cpt = cpt + 1
    val = elt.suivant.valeur
    suiv = elt.suivant.suivant
    elt.suivant = suiv
    return val


#class Instant :
    #def __init__(self,heure= 0,minute = 0,seconde= 0) :
   #     self.h = heure
  #      self.m= minute
 #       self.s= seconde
        
#toto = Instant(12,45,52)
#print(toto.h,toto.m,toto.s)
#titi= Instant(50)
#print(titi.h,titi.m,titi.s)

#question a et b

# FICHE DE TD 11 :


class Instant :
    def __init__(self,heure = 0,minute= 0,seconde = 0) :
        self.h = heure
        self.m= minute
        self.s= seconde
        
    def __str__(i) :             #methode : fonction qu'on appele a prtie de l'objet
            return f"{i.h:02}: {i.m:02}:{i.s:02}"         
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
    
    
    

#toto = read_Instant()
toto = Instant(12,50,23)
print(toto.__str__())
#print_Instant(toto)
#print_Instant(toto.toStr)
print(f"{toto.isValid}")


    

    









def prog() :
    print("")
if __name__=="__main__" :
    
    prog()

