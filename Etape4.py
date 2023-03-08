from Etape1 import *
from Etape2 import *
from Etape3 import*
import os


def TauxCompression(file_name):  
   ''' Fonction qui calcule le taux de compression du fichier donne en parametre
   ''' 
   #je recupere la taille du fichier compresse
   texteCompresseSize = os.path.getsize(file_name + "_comp.bin")
   print('Taille de '+ file_name + "_comp.bin" +' :', texteCompresseSize, 'bits')

   #je recupere la taille du fichier original
   texteOriginalSize = os.path.getsize(file_name + ".txt") 
   print('Taille de '+ file_name + ".txt" +' :', texteOriginalSize, 'bits')

   #je calcule le taux avec la formule donnée dans le sujet
   amount = 1 - texteCompresseSize/texteOriginalSize
   print("Le taux est de :" ,round(amount,3))


###Tests###
TauxCompression(fileName)
print("\n")


