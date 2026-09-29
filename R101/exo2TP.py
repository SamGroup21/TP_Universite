# # EXERCICE 3 :
# def f(a:int, b:int)->None:
#     c:int
#     c=a
#     a=b
#     b=c

# def prog()->None:
#     a:int
#     b:int
#     a=5
#     b=10
#     print("a= ",a," b= ",b)
#     f(a,b)
#     print("a= ",a," b= ",b)

# if(__name__=="__main__"):

#   prog()
# # EXERCICES 4 :

from random import randint


# def faireTrouver( val):
#    n = 2
#    score = 0
#    while n != val :
#         n = int(input("saisir la valeur de votre choix "))
#         score = score +1

#         if n < val :
#             print("la valeur est trop petit ")

#         elif n > val :
#             print("la valeur est plus grand ")

#         else :
#             return score

# def progPrincipal():
#     val = randint(1,99)
#     score = faireTrouver(val)
#     print("Bravo, vous avez trouve en ", score, "coups")

# if (__name__=="__main__"):
#       progPrincipal()

# # EXERCICE 5 :

# def devinerNombre():
#     print("Pensez à un nombre entre 1 et 99")
#     bas = 1
#     haut = 99
#     coups = 0
#     trouve = False

#     while not trouve and bas <= haut:
        
#         proposition = (bas + haut) // 2
#         coups += 1
        
#         print(f"\nMon essai : Est-ce que c'est {proposition} ?")
#         reponse = int(input("Répondez :\n  1 : Trop petit\n  2 : Trop grand\n  3 : Trouvé !\nVotre choix : "))

#         if reponse == 1:
            
#             bas = proposition + 1
#         elif reponse == 2:
           
#             haut = proposition - 1
#         elif reponse == 3:
#             print(f"\n J'ai gagné ! J'ai trouvé votre nombre en {coups} coups.")
#             trouve = True
#         else:
#             print(" Réponse invalide. Veuillez entrer 1, 2 ou 3.")
#             coups -= 1  

#     if not trouve:
#         print("\n🤔 Attendez, il y a une contradiction dans vos réponses !")

# if __name__ == "__main__":
#     devinerNombre()  

# OU ENCORE :

def devinerNombre():
    print("Pensez à un nombre entre 1 et 99...")
    bas = 1
    haut = 99
    score = 0
    trouve = False

    while not trouve and bas <= haut:
        
        proposition = randint(bas,haut)
        score += 1
        
        print(f"\nMon essai : Est-ce que c'est {proposition} ?")
        reponse = int(input("Répondez :\n  1 : Trop petit\n  2 : Trop grand\n  3 : Trouvé !\nVotre choix : "))

        if reponse == 1:
            bas = proposition + 1


        elif reponse == 2 :
            haut = proposition -1
        elif reponse != 1 or reponse!= 2 or reponse!= 3 :
            print("desole vous saisie le mauvais choix")
        else :
            print("bravo vous avez trouver la valeur ",score,"tentatives")

        return
             



         
if __name__ == "__main__":
    devinerNombre()
    





    
  


      






         



   