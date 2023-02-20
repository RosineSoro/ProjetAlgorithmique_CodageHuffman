from Etape1 import *
from Etape2 import *
from Etape3 import*
import os


def TauxCompression(file_name):   
   texteCompresseSize = os.path.getsize(file_name + "_comp.bin")
   print('Taille de '+ file_name + "_comp.bin" +' :', texteCompresseSize, 'bits')

   texteOriginalSize = os.path.getsize(file_name) 
   print('Taille de '+ file_name + ".txt" +' :', texteOriginalSize, 'bits')

   amount = 1 - texteCompresseSize/texteOriginalSize
   print("Le taux est de :" ,round(amount,3))


TauxCompression(fileName)

