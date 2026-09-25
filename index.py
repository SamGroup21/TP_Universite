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

listeTest = [12,36,25,36,16,36,15,25,41,78,97,45,36,89]
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

etudiants = {
     "nom": "Niyonkuru", "prenom": "David",
     "nom": "Irakoze", "prenom": "Aline",
     "nom": "Nkurunziza", "prenom": "Kevin",
     "nom": "Hakizimana", "prenom": "Samuel",
     "nom": "Uwimana", "prenom": "Grace"
}

def note_etudiant() :
    for etudiant in etudiants:
        nom = etudiant["nom"]
        prenom = etudiant["pernom"]
        note = int(input(f"saisir les note du {nom},{prenom}"))
        etudiants["note"] = note

    return etudiants

   

def prog() :
    resu = note_etudiant()
    print(resu)

prog()



    




        





          
          


          











