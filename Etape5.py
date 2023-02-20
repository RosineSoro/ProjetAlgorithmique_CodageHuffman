from Etape1 import *
from Etape2 import *
from Etape3 import*
from Etape4 import *

def Moyenne (file_name,root, code, liste):
    liste_char = codeFinal(file_name,root,code,liste)[0]
    code_final = codeFinal(file_name,root,code,liste)[1]
    moyenne = len(code_final)/len(liste_char)
    return moyenne


print(Moyenne(fileName,tree[0],code,list_nodes))