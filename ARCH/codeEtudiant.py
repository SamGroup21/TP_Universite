
# TP 1 MATH DISCRETE AVEC LE PROF PHOILIPE MUNEBWE :

1.
# ALGORITHME :

# a. Entrée : un réel x
# Sortie : E(x)

# n ← 0
# Si x >= 0 :
#     Tant que n + 1 <= x :
#         n ← n + 1
# Sinon :
#     Tant que n > x :
#         n ← n - 1
# Renvoyer n

# b :
# def pe (x) :
#     n = 0
#     if x> 0 :
#         while n + 1 <= x :
#             n = n + 1

#     else :
#         while n > x :
#             n = n-1

#     return n

# print(pe(-8.5))

# c:
# algorithme :


# Fonction per(x) :
#     Si 0 <= x < 1 :
#         Renvoyer 0
#     Si x >= 1 :
#         Renvoyer 1 + per(x - 1)   
#     Sinon (x < 0) :
#         Renvoyer per(x + 1) - 1

# d :

# def per (x) :
#     if 0 <=x<1 :
#         return 0
#     if x >= 1 :
#         return 1 + per(x -1)
#     elif (x<0):
       
#        return per(x+1) - 1

# print(per(-2.3))

# Vérification : per(-2,3) = per(-1,3) − 1 = per(-0,3) − 2 = per(0,7) − 3 = 0 − 3 = -3.

# e :

# Entrée : un réel x ≥ 0
# Sortie : le nombre de points

# Si x < 40 :
#     Renvoyer 0
# Sinon :
#     t ← E(x / 10)
#     Renvoyer 5 × (t - 3)

# f :


# def euro(x) :
#     if x < 40 :
#         return 0
#     else :
#         tranche = x/10
   

#         return  5 * (tranche-3)

# print(euro(108))

# Question 2 :
# a :
# a,b,s,r :  reel
# r = a 
# s= 0
# tant que r > =b :
#    r = r - b
#    s = s +1

# a : pour trouver le quotient il suffit de predre le dividende moin le divideur et compte  le nombre de fois on a fait cette operation
# b : pour trouver le reste on regarde a le resultat de la dernier operation de r = r - b

#  retourne s, r 

# c :
def de(a, b):
    q = 0
    r = a
    while r >= b:
        r = r - b
        q = q + 1
    return q, r

print(de(10,3))

# Question 3 :





























