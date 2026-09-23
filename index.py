# TD 1 Exercices1

def main() :



    nombre =  int(input("saisir la valeur "))
    if nombre != 0 :
        carre = nombre*nombre
        carre = (carre*10) + 25
        return carre

    else :
        print("imposssible")
    

if __name__=="__main__":
        resultat = main()

print(resultat)

# A: oui son resultat est exacte
# B Non elle n'a pas raison car deja partant de notre exemple on a pris 2 et on a obtenu 65 qui est impaire ensuite on ne peut pas 
# trouver une valeur paire car à chaque fois on a addtioner 25 a la valeur trouver apres la multipplication par 10
# C : Oui c'est vrai parceque le carre d'un nombre;que ça soit positive ou negatif est toujours positive


 
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




