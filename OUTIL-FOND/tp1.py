from time import time

# #Exercice 1




# def puissance1(x, n):
#     if n == 1:
#       return x
#     return x * puissance1(x, n - 1)

# def puissance2(x, n):
#     if n == 1:
#        return x
#     if n % 2 == 0:
#        return puissance2(x * x, n // 2)
#     return x * puissance2(x * x, (n - 1) // 2)


# td1 = time()
# p1 = puissance1(10,800)
# tf1 = time()
# print(td1)
# #print(tf1)
# T1 = tf1 - td1

# td2 = time()
# p1 = puissance2(10,800)
# print(td2)
# tf2 = time()
# #print(tf2)
# T2 = tf2 - td2

#print(T2)

#tfinal = T1/T2                

#print(tfinal)

            
# Exercice 2 : calcul du mineur d'une matrice

def mineur(A,i,j) :
    nb_ligne = len(A)
    nb_colonne = len(A[0])
    
    resultat = []
    for r in range(0,nb_ligne) :
        if r!=i :
            nouv_ligne = []
            for c in range(nb_colonne) :
                if c!=j :
                    nouv_ligne = nouv_ligne + [A[r][c]]
            #resultat.append(nouv_ligne)  ou encore :
            resultat = resultat + [nouv_ligne]
    return resultat
        
       
    
#print(mineur([[1,2,2],[1,3,-2],[3,5,8]],0,1))

#exercice 3 : calcul du determinant d'une matrice

def determinant(A:list[list[int]]) -> int: 
    nb_ligne= len(A)
    if nb_ligne == 1 :
        return A[0][0]
    # if nb_ligne == 2 :
    #     return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
#print(determinant([[1,-2],[3,5]]))

    #if nb_ligne > 2 :
        #return sum([(-1)**j * A[0][j] * determinant(mineur(A,0,j)) for j in range(nb_ligne)])
        
#print(determinant([[1,2,2],[1,3,-2],[3,5,8]]))  
    S = 0
    for j in range(nb_ligne) :
        if j % 2 == 0 :
            S = S + A[0][j] * determinant(mineur(A,0,j))
            
        elif j % 2 != 0 :
            S =S - A[0][j] * determinant(mineur(A,0,j))
    
    return S
#print(determinant([[1,2,2],[1,3,-2],[3,5,8]])) 

# exercice 4 : calcul le determinant par la methodde de Sarrus :

def determinant_sarrus(A:list[list[int]]) -> int:
    nb_ligne = len(A)
    if nb_ligne == 3 :
        return A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1] - A[0][2]*A[1][1]*A[2][0] - A[0][0]*A[1][2]*A[2][1] - A[0][1]*A[1][0]*A[2][2]
#print(determinant([[1,2,2],[1,3,-2],[3,5,8]]))  

# exercice 5 : 
# a : det_compte(A) : couple de deteminant et le nombre de fois on a multiplier pour l'obtenir

def det_compte(A:list[list[int]]) -> tuple[int,int]:
    nb_ligne = len(A)
    if nb_ligne == 1 :
        return (A[0][0], 0)
    else :
        compteur = 0
        S = 0
        for j in range(nb_ligne) :
            if j % 2 == 0 :
                        S = S + A[0][j] * determinant(mineur(A,0,j))
                        compteur = compteur + 1
            elif j % 2 != 0 :
                        S =S - A[0][j] * determinant(mineur(A,0,j))
                        compteur = compteur + 1
        return (S, compteur)
    
print(det_compte([[1,2,2],[1,3,-2],[3,5,8]])) 
        
    