from Etape2 import *
from Etape1 import *


def codeChar (root, code, liste):
    '''Cette fonction permet la creation du code binaire de chaque caractère
    Elle prend en parametre le noeud racine de l arbre, un code binaire qui est initalement une chaine de caractere vide 
    et une liste initialement vide egalement puis retourne une liste de dictionnaires
    '''
    code = code + str (root.branch)

    dicoChar = {}

    # Si le noeud a un enfant gauche ou droit, alors rappeler la fonction car ce n'est pas une feuille
    if root.leftChild != None:
        codeChar(root.leftChild,code,liste)

    if root.rightChild != None:
        codeChar(root.rightChild,code,liste)

    # Si le noeud est une feuille, on l'ajoute dans le dictionnaire comme la cle et on lui affecte son code binaire comme valeur de la cle
    if root.leftChild == None and  root.rightChild == None :
        dicoChar[root.label] = code

        # creation de la liste de dictionnaire
        liste.append(dicoChar)
    
    return liste


def codeFinal(liste_char,liste_code_char):
    '''
    Prend en parametre une liste de caractere et une liste de code des caractres
    retourne la concatenation des codes 
    '''


    #Pour recuperer les caracteres du texte, je fais appel a la fonction getText de letape 1
    #Pour les codes des caractères, je fais appel à la fonction codeChar de l etape 3
    
    
    code_final = ''

    #Je parcours la liste_char avec des indices pour pouvoir remplacer les caracteres par leur code
    #Je parcours la liste des dictionnaires pour m interesser a chaque dictionnaire
    #Puis je compare le charactere avec la cle du dictionnaire, s il y a egalite, je remplace le charactere par son code
    for i in range(len(liste_char)):
        for dico in liste_code_char:
            for key,code_char in dico.items():
                if liste_char[i] == key :
                    liste_char[i] = code_char
    
    # je concatene les codes pour obtenir le code final
    for code in liste_char:
          code_final = code_final + code

    return liste_char, code_final


def Compression (code_final,file_name): 
    ''' 
    Prend en parametre le nom d un fichier et le code final de tous les caracteres du fichier
    Permet de compresser le fichier donné en parametre
    Retourne le fichier compressé
    '''
    texteCompresse = int(code_final, base=2).to_bytes((len(code_final)+7)//8, byteorder='big') 
     
    # creation ou suppression et creation du fichier compresse 
    nouveau_fichier= open(file_name + "_comp.bin", "wb")
    nouveau_fichier.write(texteCompresse)
    nouveau_fichier.close()
    return ("fichier créé avec succes") 







####Tests####

#affichage de la liste des codes
code= ""
list_codes = []
list_code_char = codeChar(root[0], code, list_codes)
print("list_code_char : ",list_code_char, "\n")

#affichage du code final
print("code_final : ",codeFinal(texte,list_code_char)[1],"\n")

#compression
code_final = codeFinal(texte,list_code_char)[1]
print(Compression(code_final,fileName),"\n")



