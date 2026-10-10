# def entier(x:float) -> float :
#     if x >= 0 :
#         return int(x)
#     elif x < 0 :
#         p = int(x) -1
#     return p

# print(entier(5000 ))


# avec la recursivité :

# def per(x:float) -> float :
#     if 0<= x < 1 :
#         return 0
#     elif -1<x<0 :
#         return -1
#     elif x>= 1 :
#         return 1 + per(x-1)
#     else :
#         return -1 + per(x+1)

# print(per(-9.5))

# def point(x) :
#     if x >=40 :
#         p = 5
#         seuil = 50
#         while x >= seuil :
#             p = p + 5
#             seuil = seuil + 10
#         return p

# print(point(108))

# ou encore  :

# def point(x) :
#     if x >= 40 :
#         return 5 * ((x-40)/10) + 5
    
#     else :
#         return 0
# print(point(40))
        
def quotient(x,y) -> int :
    if y == 0 :
        return "infini"
    else :
        res = int(x/y)
        return res
    
print(quotient(8,3))
   


