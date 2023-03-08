from Etape1 import *
from Etape2 import *
from Etape3 import*
from Etape4 import *

def Moyenne (file_name,root, code, liste):
    '''
    fonction qui calcule et retourne le nombre moyen de bits
    '''
    liste_char = codeFinal(texte,list_code_char)[0]
    code_final = codeFinal(texte,list_code_char)[1]
    moyenne = len(code_final)/len(liste_char)
    return moyenne


print("Moyenne: ",Moyenne(fileName,root[0],code,list_codes), "\n")