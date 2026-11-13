# # TP 1 : MATHEMATHIQUE DISCRETE :

# # EXERCICE 1 :
    
#     # a :
# # fonction entier(x:reel)
# #    si x>= 0 :
# #        retourner int(x)
# #     sinon si x<0 :
# #        p=int(x)-1
# #        retourner p

# # b:
    
# def entier(x:float) -> float :
#         if x >= 0 :
#             return int(x)
#         elif x < 0 :
#             p = int(x) -1
#         return p

# # print(entier(5000 ))

# # c :

# # Fonction per(x : réel) : entier
# # Début
# #     Si 0 ≤ x < 1 Alors
# #         Retourner 0
# #     Sinon Si -1 < x < 0 Alors
# #         Retourner -1
# #     Sinon Si x ≥ 1 Alors
# #         Retourner 1 + per(x - 1)
# #     Sinon
# #         Retourner -1 + per(x + 1)
# #     FinSi
# # Fin
# # avec la recursivité :

# # d:
# def per(x:float) -> float :
#     if 0<= x < 1 :
#         return 0
#     elif -1<x<0 :
#         return -1
#     elif x>= 1 :
#         return 1 + per(x-1)
#     else :
#         return -1 + per(x+1)

# # print(per(-9.5))

# # E:

# # Fonction point(x : réel) : entier
# # Variables
# #     p, seuil : entier
# # Début
# #     Si x >= 40 Alors
# #         p ← 5
# #         seuil ← 50

# #         Tant que x >= seuil Faire
# #             p ← p + 5
# #             seuil ← seuil + 10
# #         Fin Tant que

# #         Retourner p
# #     FinSi
# # Fin


# # F :

# def point(x) :
#     if x >=40 :
#         p = 5
#         seuil = 50
#         while x >= seuil :
#             p = p + 5
#             seuil = seuil + 10
#         return p

# # print(point(108))
# # EXERCICE 2 :

# # A :

# # Fonction quotient(x : entier, y : entier) : entier
# # Début
# #     Si y = 0 Alors
# #         Retourner "infini"
# #     Sinon
# #         Retourner x DIV y
# #     FinSi
# # Fin


# # B:
        
# def quotient(x,y) -> int :
    
#     if y == 0 :
#         return "infini"

#     else :
#         return x//y
        
    
# # print(quotient(8,3))

# # b :

# def reste(x, y):
#     r = x 
#     while r >= y :
#         r = r-y
        
#     return r

# # print(reste(7,4))
    
# # c :

# def de(x:float,y:float) -> float :
#     r= x
#     q = 0
#     while r >= y :
#         r =r-y
#         q +=1
#     return r,q
# # print(de(13,4))  

# # EXERCICE 3 :

# # a : 

# # Fonction minimum(liste : liste de réels) : réel
# # Variables
# #     min : réel
# #     i : entier
# # Début
# #     min ← liste[0]

# #     Pour i allant de 0 à longueur(liste) - 1 Faire
# #         Si min > liste[i] Alors
# #             min ← liste[i]
# #         FinSi
# #     FinPour

# #     Retourner min
# # Fin

# # B:

# def minimum(liste:list) -> float :
#     # liste = []
#     # liste = [0]
#     min = liste[0]
#     for i in range(len(liste)) :
#         if min > liste[i] :
#             min = liste[i]
#     return min
        
            

# # print(minimum([5,2,7,1,-9]))

# # C:

# # Fonction maximum(liste : liste de réels) : réel
# # Variables
# #     max : réel
# #     i : entier
# # Début
# #     max ← liste[0]

# #     Pour i allant de 0 à longueur(liste) - 1 Faire
# #         Si max < liste[i] Alors
# #             max ← liste[i]
# #         FinSi
# #     FinPour

# #     Retourner max
# # Fin


# # D :

# def maximum(liste:list) -> float :
#     max = liste[0]
#     for i in range(len(liste)) :
#         if max < liste[i] :
#             max = liste[i]
#     return max
        
            

# # print(maximum([5,2,7,1,-9]))

# # E :

# # Fonction appartient(liste : liste d'entiers) : booléen
# # Variables
# #     nombre : entier
# #     i : entier
# # Début
# #     Écrire("Saisis un nombre : ")
# #     Lire(nombre)

# #     Pour i allant de 0 à longueur(liste) - 1 Faire
# #         Si nombre = liste[i] Alors
# #             Retourner Vrai
# #         FinSi
# #     FinPour

# #     Retourner Faux
# # Fin


# # f :

# def appartient(liste : list) -> bool :
#     nombre  = int(input("saisi un nombre "))
#     for i in range(len(liste)):
#         if nombre == liste[i] :
#             return True
    
#     return False
# print(appartient([5,2,7,1,-9]))

# # ou encore : 
    
# def appartient(liste :list) -> float :
#     nombre = int(input("saisi un nombre "))
#     for element in liste :
#         if element == nombre :
#             return True
#     else :
#         return False
    
# print(appartient([5,2,7,1,-9]))

    

# if __name__ == "__main__":
#     appartient([5,2,7,1,-9])
    
  

# a = [1,2,3,5,4,6]
# b = a
# b.append(7)
# d = a.copy()
# print(id(a))
# print(id(b))
# print(id(d))

# d = {"nom":"samuel","prenom ": "ninziza"}
# d.update({"ville":"maubeuge"})

# for x in d :
#     print(d)
def trie() -> bool :
    
    a = [3,5,3,5,4,6]

    for i in range(0,5) :
        if a[i]>a[i+1] :
            return False
    return True
      
print(trie())
# # del(a[1])
# # a.pop(1)
# a.remove(0)
# print(a)


