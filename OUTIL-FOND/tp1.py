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

            
# Exercice 2 :

def mineur(A,i,j) :
    nb_ligne = len(A)
    nb_colonne = len(A[0])
    
    resulat = []
    for r in range(0,nb_ligne) :
        if r!=i :
            nouv_ligne = []
            for c in range(nb_colonne) :
                if c!=j :
                    nouv_ligne = nouv_ligne + [A[r][c]]
            resulat.append(nouv_ligne)
    return resulat
        
       
    
print(mineur([[1,2,2],[1,3,-2],[3,5,8]],0,1))

#Exercice 3 :


        
                
                
            