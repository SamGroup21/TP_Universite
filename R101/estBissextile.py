# A DETERMINER SI UNE ANNEE EST BISSEXTILE


# def estBissextile (x) :

#     year = 0
#     if year%4 == 0 and year%100 !=0 or year%400 == 0 :
#         return True
#     else :
#         return False


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
    


# QUESTION B : Determiner si un mois est valide

# def moisValide(x=0) :

#    if 1<=x<=12 :
#       return True
#    else :
#       return False 

   

# def testerMoisValide ():
#    if (moisValide(1)) :
#       print("teste de 1 Ok")
#    else : 
#       print("test de 1 Echec")
#    if (moisValide(2)):
#       print("test de 2 Ok")
#    else :
#       print("test de 2 Echec")

#    if (moisValide(3)) :
#       print("teste de 3 Ok")
#    else :
#       print("test de 3 echec")

#    if (moisValide(4)) :
#       print("test de 4 ok")
#    else :
#       print("test de 4 echec")

#    if (moisValide(12)) :
#       print('test de 12 ok')
#    else :
#       print("test de 12 echec")
def estBissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def nbJours (mois,annee) :
   if mois == 2 :
      if estBissextile(annee) :
         return 29
      else :
         return 28
   elif mois in [4,6,9,11] :
      return 30
   elif mois in [1,3,5,7,8,10,12] :
      return 31
   else :
      return 0


# QUESTION C : DETERMINER LE NOMBRE DE JOURS DANS UN MOIS :
def testerNbJours():
   if(nbJours(1,2000)==31):
      print("test de 01/2000 OK")
   else:
      print("test de 01/2000 ECHEC")
   if(nbJours(2,2000)==29):
      print("test de 02/2000 OK")
   else:
      print("test de 02/2000 ECHEC")
   if(nbJours(2,2001)==28):
      print("test de 02/2001 OK")
   else:
      print("test de 02/2001 ECHEC")
   if(nbJours(3,2000)==31):
      print("test de 03/2000 OK")
   else:
      print("test de 03/2000 ECHEC")
   if(nbJours(4,2000)==30):
      print("test de 04/2000 OK")
   else:
      print("test de 04/2000 ECHEC")
   if(nbJours(5,2000)==31):
      print("test de 05/2000 OK")
   else:
      print("test de 05/2000 ECHEC")
   if(nbJours(6,2000)==30):
      print("test de 06/2000 OK")
   else:
      print("test de 06/2000 ECHEC")
   if(nbJours(7,2000)==31):
      print("test de 07/2000 OK")
   else:
      print("test de 07/2000 ECHEC")
   if(nbJours(8,2000)==31):
      print("test de 08/2000 OK")
   else:
      print("test de 08/2000 ECHEC")
   if(nbJours(9,2000)==30):
      print("test de 09/2000 OK")
   else:
      print("test de 09/2000 ECHEC")
   if(nbJours(10,2000)==31):
      print("test de 10/2000 OK")
   else:
      print("test de 10/2000 ECHEC")
   if(nbJours(11,2000)==30):
      print("test de 11/2000 OK")
   else:
      print("test de 11/2000 ECHEC")
   if(nbJours(12,2000)==31):
      print("test de 12/2000 OK")
   else:
      print("test de 12/2000 ECHEC")
      
testerNbJours()


def dateValide(jour, mois, annee):
    # 1. Vérifier si le mois est valide (entre 1 et 12)
    if mois < 1 or mois > 12:
        return False

    # 2. Vérifier si le jour est valide (entre 1 et le max de jours du mois)
    if jour >= 1 and jour <= nbJours(mois, annee):
        return True
    else:
        return False
dateValide(29, 2, 2020)


# TP 3 :


   
   
     
   








