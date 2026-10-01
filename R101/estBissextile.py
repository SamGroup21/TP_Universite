# def estBissextile (x) :
#     est_bissextille = True
#     non_bissextille = False

#     year = 0
#     if year%4 == 0 and year%100 !=0 or year%400 == 0 :
#         return est_bissextille
#     else :
#         return non_bissextille


# from estBissextile import estBissextile

# def testerBissextile():

#     if(estBissextile(2016)):
#       print("test de 2016 OK")
#     else:
#       print("test de 2016 ECHEC")
#     if(estBissextile(2008)):
#       print("test de 2008 OK")
#     else:
#       print("test de 2008 ECHEC")
#     if(not estBissextile(1900)):
#       print("test de 1900 OK")
#     else:
#        print("test de 1900 ECHEC")
#     if(estBissextile(2000)):
#        print("test de 2000 OK")
#     else:
#        print("test de 2000 ECHEC")

# def prog():
#     testerBissextile()
    


# QUESTION B :

def moisValide(x=0) :

   if 1<=x<=12 :
      return True
   else :
      return False 

   

def testerMoisValide ():
   if (moisValide(1)) :
      print("teste de 1 Ok")
   else : 
      print("test de 1 Echec")
   if (moisValide(2)):
      print("test de 2 Ok")
   else :
      print("test de 2 Echec")

   if (moisValide(3)) :
      print("teste de 3 Ok")
   else :
      print("test de 3 echec")

   if (moisValide(4)) :
      print("test de 4 ok")
   else :
      print("test de 4 echec")

   if (moisValide(12)) :
      print('test de 12 ok')
   else :
      print("test de 12 echec")


def prog() :
   testerMoisValide()

if(__name__=="__main__"):
   prog()


   
   
   
     
   








