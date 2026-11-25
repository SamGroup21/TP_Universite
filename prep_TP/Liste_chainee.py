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

    
    
prog()
    
    

    










