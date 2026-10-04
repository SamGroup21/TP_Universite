# TD 1 Exercices1

# def main() :



#     nombre =  int(input("saisir la valeur "))
#     if nombre != 0 :
#         carre = nombre*nombre
#         carre = (carre*10) + 25
#         return carre

#     else :
#         print("imposssible")


# if __name__=="__main__":
#         resultat = main()

# print(resultat)

# A: oui son resultat est exacte
# B Non elle n'a pas raison car deja partant de notre exemple on a pris 2 et on a obtenu 65 qui est impaire ensuite on ne peut pas
# trouver une valeur paire car à chaque fois on a addtioner 25 a la valeur trouver apres la multipplication par 10
# C : Oui c'est vrai parceque le carre d'un nombre;que ça soit positive ou negatif est toujours positive

# D :

# def square(a: float) -> float:
#     return a * a

# def calculer(x: float) -> float:
#     resultat = square(x) * 10 + 25
#     return resultat

# # Programme principal
# nombre = float(input("Entrez un nombre : "))
# resultat = calculer(nombre)
# print("Le résultat est :", resultat)

# Exercice 2 :

# def addition(a: float, b: float) -> float:
#     a_saisi = input("saisir la valeur de a : ")
#     b_saisi = input("saisir la valeur de b : ")
#     if len(a_saisi) < 2 or len(b_saisi) < 2:
#         print("impossible de calculer la somme car la valeur de a ou b est inferieur a 2")
#     else:
#         a = float(a_saisi)
#         b = float(b_saisi)
#         return a + b

# def resultat(a, b):
#     resu = addition(a, b)
#     print('a=', a, 'b=', b, 'le resultat :', resu)
#     return resu

# print(resultat())

# Question B :

# def saisieInt(min_val: int, max_val: int) -> int:
#     valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
#     while valeur < min_val or valeur > max_val:
#         print("Valeur incorrecte, réessayez.")
#         valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
#     return valeur

# # Test
# n = saisieInt(1, 10)
# print("Valeur saisie :", n)


# QUESTION C :

def intercaler(a: int, b: int) -> int:
    dizaine = a // 10
    unite = a % 10
    return dizaine * 1000 + b * 10 + unite

def saisieInt(min_val: int, max_val: int) -> int:
    valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
    while valeur < min_val or valeur > max_val:
        print("Valeur incorrecte, réessayez.")
        valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
    return valeur

# Programme principal
a = saisieInt(10, 99)
b = saisieInt(10, 99)
resultat = intercaler(a, b)
print("Le résultat est :", resultat)


# EXERCICE D :
def intercaler(a: int, b: int) -> int:
    dizaine = a // 10
    unite = a % 10
    return dizaine * 1000 + b * 10 + unite

def saisieInt(min_val: int, max_val: int) -> int:
    valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
    while valeur < min_val or valeur > max_val:
        print("Valeur incorrecte, réessayez.")
        valeur = int(input(f"Entrez un entier entre {min_val} et {max_val} : "))
    return valeur

# Programme principal
a = saisieInt(10, 99)
b = saisieInt(10, 99)
resultat = intercaler(a, b)
print("Le résultat est :", resultat)

#  FICHE DE TD 2 :

# Exercice 1 :

def valeurAbsolue(x: float) -> float:
    if x < 0:
        return -x
    else:
        return x
print(valeurAbsolue(-7.5))  
print(valeurAbsolue(3.2))  


# Exercice 2 :
# QUESTION B :

def resoudreEquation(a: float, b: float) -> float:
    if a == 0:
        print("Pas de solution unique (a = 0)")
        return None
    else:
        x = -b / a
        return x
    
    
# QUESTION C :

def resoudreEquationSecondDegre(a: float, b: float, c: float):
    delta = b * b - 4 * a * c

    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("Deux solutions :", x1, x2)
        return x1, x2
    elif delta == 0:
        x0 = -b / (2 * a)
        print("Une solution double :", x0)
        return x0
    else:
        print("Pas de solution réelle")
        return None


resoudreEquationSecondDegre(1, -3, 2)  
resoudreEquationSecondDegre(1, 2, 1)  
resoudreEquationSecondDegre(1, 0, 1) 

# OU ENCORE :

from math import sqrt, pow

def resoudreEquationSecondDegre(a: float, b: float, c: float):
    delta = pow(b, 2) - 4 * a * c

    if delta > 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("Deux solutions :", x1, x2)
        return x1, x2
    elif delta == 0:
        x0 = -b / (2 * a)
        print("Une solution double :", x0)
        return x0
    else:
        print("Pas de solution réelle")
        return None

resoudreEquationSecondDegre(5, -3, 6) 
resoudreEquationSecondDegre(2, 2, 1)
resoudreEquationSecondDegre(1, 0, 1)


from math import sqrt, pow

def resoudreEquationSecondDegre(a: float, b: float, c: float):
    delta = pow(b, 2) - 4 * a * c

    if delta > 0:
        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        print("Deux solutions :", x1, x2)
        return x1, x2
    elif delta == 0:
        x0 = -b / (2 * a)
        print("Une solution double :", x0)
        return x0
    else:
        print("Pas de solution réelle")
        return None

print("Résolution de a*x^2 + b*x + c = 0")
a = float(input("Entrez a : "))
b = float(input("Entrez b : "))
c = float(input("Entrez c : "))

resoudreEquationSecondDegre(a, b, c)


# EXERCICE 3 :

# QUESTION A :

def estEquilateral(a: float, b: float, c: float) -> bool:
    if a == b and b == c:
        return True
    else:
        return False

print(estEquilateral(5, 5, 5))  
print(estEquilateral(3, 4, 5)) 

# QUESTION B :

def estIsocele(a: float, b: float, c: float) -> bool:
    if a == b or b == c or a == c:
        return True
    else:
        return False

print(estIsocele(7, 5, 8))  
print(estIsocele(9, 4, 2))  

# QUESTION C :

def estRectangle(a: float, b: float, c: float) -> bool:

    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        return True
    else:
        return False

# Tests
print(estRectangle(3, 4, 5))
print(estRectangle(2, 2, 2))  

# QUESTION D :

def estEquilateral(a: float, b: float, c: float) -> bool:
    return a == b and b == c

def estRectangle(a: float, b: float, c: float) -> bool:
    return (a*a == b*b + c*c or
            b*b == a*a + c*c or
            c*c == a*a + b*b)

def estIsocele(a: float, b: float, c: float) -> bool:
    return a == b or b == c or a == c

# Programme principal
a = float(input("Entrez le côté a : "))
b = float(input("Entrez le côté b : "))
c = float(input("Entrez le côté c : "))

if estEquilateral(a, b, c):
    print("Le triangle est équilatéral")
elif estRectangle(a, b, c):
    print("Le triangle est rectangle")
elif estIsocele(a, b, c):
    print("Le triangle est isocèle")
else:
    print("Le triangle est quelconque")
    
    
# FICHE DE TD 3 :

# EXERCICE 1 :

# Ligne d'en-tête
print("X", end="\t")
for j in range(11):
    print(j, end="\t")
print()  # retour à la ligne

# Lignes de la table
for i in range(11):
    print(i, end="\t")
    for j in range(11):
        print(i * j, end="\t")
    print()  # retour à la ligne après chaque ligne i
    
    
# EXERCICE 2 :
    
def afficherTriangle(c: int):
    for i in range(1, c + 1):
        nbEtoiles = c - i + 1
        nbPoints = i - 1
        print("*" * nbEtoiles + "." * nbPoints)


afficherTriangle(6)

# FICHE DE TD 4 :

# EXERCICE 1 :
# QUESTION A :

def puissanceIteratif(x: float, n: int) -> float:
    resultat = 1
    for i in range(n):
        resultat = resultat * x
    return resultat

print(puissanceIteratif(2, 5))

# QUESTION B:

def puissanceRecursif(x: float, n: int) -> float:
    if n == 0:
        return 1
    else:
        return x * puissanceRecursif(x, n - 1)


print(puissanceRecursif(2, 9)) 


def puissanceRapide(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n % 2 == 0:
        demi = puissanceRapide(x, n // 2)
        return demi * demi
    else:
        demi = puissanceRapide(x, n // 2)
        return x * demi * demi


print(puissanceRapide(2, 10))

# puissanceRapide est bien plus performant

# EXERCICE 2 :

# QUESTION A :


def divise(a: int, b: int) -> bool:
    return a % b == 0

print(divise(10, 2)) 
print(divise(10, 3))  
print(divise(9, 3)) 

















#  CHERCHER LA LISTE TRIE ET LA LISTE NON TRIE

# listeTest = [12,36,25,36,16,36,15,25,41,78,98,45,36,89]
# listeTriee = [1,3,5,6,7,9,12,16,17,19,20]

# def chercher_trie(nbr,l) :
#      ind = 0
#      while ind < len(l) and l[ind] <= nbr:
#           if l[ind] == nbr :
#                return ind
#           ind = ind + 1

#      return -1


# def progr() :
#     n = int(input('vous cherchez quel valeur '))
#     resu = chercher_trie(n,listeTriee)
#     if(resu == -1) :
#           print("la valeur",n,"ne se trouve pas dans la liste")

#     else :
#          print("la valeur",n,"se trouve a l'indice",resu)


# progr()


# listeTest = [12,36,25,36,16,36,15,25,41,78,98,45,36,89]
# listeTriee = [1,3,5,6,7,9,12,16,17,19,20]

# def chercher_trie(nbr,l) :
#      ind = 0
#      while ind < len(l) and l[ind] <= nbr:
#           if l[ind] == nbr :
#                return ind
#           ind = ind + 1

#      return -1


# def search(nbr,l,bmin=0,bmax=None) :
#     if bmax == None :
#         bmax = len(l)-1
#     if bmin > bmax or nbr < l[bmin] or nbr > l[bmax] :
#          return -1

#     m = (bmax - bmin) // 2
#     if l[m] == nbr :
#          return m
#     elif l[m] > nbr :
#          return search(nbr,l,bmin,m-1)
#     else :
#          return search(nbr,l,bmax,m+1)

# def progr() :

#     n = int(input('vous cherchez quel valeur '))
    # resu = chercher_trie(n,listeTriee)
    # if(resu == -1) :
    #       print("la valeur",n,"ne se trouve pas dans la liste")

    # else :
    #      print("la valeur",n,"se trouve a l'indice",resu)


# progr()




# TD 5 EXERCICE 2 :

# listeTest = [12,36,25,36,16,36,15,25,41,78,97,45,36,89]
# listeTriee = [1,3,5,6,7,9,12,16,17,19,20]

# Question A :

# def nombre_occ_T(n,l) :
#      cpt= 0
#      for i in l :
#           if(i == n) :
#                cpt = cpt +1
#      return cpt

# def prog() :
#      nbr = int(input("saisir le nombre\n"))
#      resu = nombre_occ_T(nbr,12)
#      print("le nombre d'occurence de",nbr,"dans la liste trie est :",resu)


# QUESTION C :

# def nombre_min_max(l) :
#      max = l[0]
#      min = l[0]
#      for i in l :
#           if(i>max) :
#                max = l
#           if(i<min) :
#                min = l
#      return min,max

# def prog(l) :
#      min,max = nombre_min_max(l)
#      print("le nombre mini est",min,"le nombre maxi est:",max)

# prog()

# EXERCICE 3
# QUESTION A :

# def moyenne(liste: list) :
#      somme = 0
#      for i in listeTest :
#           somme = somme + i
#           i = i + 1

#      return somme/len(listeTest)

# def prog():
#      resu = moyenne(listeTest)

#      print("La moyenne de la liste ",listeTest,"est",resu)

# prog()

# QUESTION B :

# l = [12,36,25,36,16,36,15,25,41,78,97,45,36,89]
# l1 = [1,3,5,6,7,9,12,16,17,19,20]
# l2 = [12,52,15,25,36,98,45,5,6,5,66,56,56,4,6]
# l3 = [5,4,1,2,3,6,5,4,7,8,9,12,23,36,54,7,5,5]

# def somme (l1,l2) :
#     resultat = []
#     for i in range(0,len(l1)) :
#         resultat.append(l1[i] + l2[i])

#     return resultat

# def prog() :
#     resu = moyenne(l3)
#     print("la somme de la liste est :",resu)
#     print("La somme est",somme(l,l1))

# prog()

# QUESTION C :

# def somme (l1,l2) :
#     resultat = []
#     for i in range(0,len(l1)) :
#         resultat.append(l1[i] + l2[i])

#     return resultat

# def doublon(liste) :
#     listeresu = []
#     for i in liste :
#         if i not in listeresu :
#             listeresu.append(i)

#     return listeresu

# def prog() :
#     resu = moyenne(l3)
#     print("la somme de la liste est :",resu)
#     print("La somme est",somme(l,l1))

# prog()

# QUESTION D :

# l1 = [1,3,5,6,7,9,12,16,17,19,20,25,36,12,6,4]
# l2 = [12,52,15,25,36,98,45,5,6,5,66,56,56,4,6]

# def elt_commun(l1,l2) :
#     liste_commun = []
#     for i in l1 :
#         if i in l2 :
#             liste_commun.append(i)

#     return liste_commun

# def prog() :
#     resu = elt_commun(l1,l2)
#     print("La liste commun entre les deux lign est",resu)

# prog()

# ou encore :
# l1 = [1, 3, 5, 6, 7, 9, 12, 16, 17, 19, 20, 25, 36, 12, 6, 4]
# l2 = [12, 52, 15, 25, 36, 98, 45, 5, 6, 5, 66, 56, 56, 4, 6]


# def elt_commun():
#     liste_commun = []

#     for i in l1:
#         for j in l2:
#             if i == j:
#                 liste_commun.append(i)

#     return liste_commun



# def prog():
#     resu = elt_commun()
#     print("La liste des éléments communs entre les deux listes et :", resu)


# prog()

# TD 6 EXERCICE 1 :

# QUESTION A :

# etudiants = {
#      "nom": "Niyonkuru", "prenom": "David",
#      "nom": "Irakoze", "prenom": "Aline",
#      "nom": "Nkurunziza", "prenom": "Kevin",
#      "nom": "Hakizimana", "prenom": "Samuel",
#      "nom": "Uwimana", "prenom": "Grace"
# }

# def note_etudiant() :
#     for etudiant in etudiants:
#         nom = etudiant["nom"]
#         prenom = etudiant["pernom"]
#         note = int(input(f"saisir les note du {nom},{prenom}"))
#         etudiants["note"] = note

#     return etudiants



# def prog() :
#     resu = note_etudiant()
#     print(resu)

# prog()






























