from Etape2 import *
from Etape1 import *


def codeChar (root, code, liste):
    # Créer le code binaire
    code = code + str (root.branch)

    dicoChar = {}

    # Si le noeud contient un enfant gauche ou droit, alors ce n'est pas une feuille et il faut rappeler la fonction
    if root.leftChild != None:
        codeChar(root.leftChild,code,liste)

    if root.rightChild != None:
        codeChar(root.rightChild,code,liste)

    # Si le noeud n'a pas d'enfant, c'est une feuille.
    # On peut donc l'ajouter dans le dictionnaire et lui affecter son code binaire
    if root.leftChild == None and  root.rightChild == None :
        dicoChar[root.label] = code
        # Je crée une liste de dictionnaire
        liste.append(dicoChar)
    
    return liste

#Pour recuperer les caracteres du texte, je fais appel a la fonction alphabet_non_reduit de letape1
def codeFinal(file_name,root, code, liste):
    liste_char = alphabet_non_reduit(file_name)
    liste_code_char = codeChar(root,code,liste)
    code_final = ''
    for i in range(len(liste_char)):
        for dico in liste_code_char:
            for key,code_char in dico.items():
                if liste_char[i] == key :
                    liste_char[i] = code_char
    
    for code in liste_char:
          code_final = code_final + code

     #faire un affichage joli avec retour à la ligne
    return liste_char, code_final

def Compression (code_final,file_name): # comprendre ce que ça fait
    texteCompresse = int(code_final, base=2).to_bytes((len(code_final)+7)//8, byteorder='big') 

    nouveau_fichier= open(file_name + "_comp.bin", "wb")
    nouveau_fichier.write(texteCompresse)
    nouveau_fichier.close()
    return texteCompresse








dico = alphabet_final(fileName)
#print(dico)
list_node = create_liste_node(dico)
#print(list_node)
#print(insert (list_node, ('!', 1), ('B', 1), ('!B',2)))
tree = add_and_remove_node(list_node)
#print(tree)

#print(printTree(tree[0]))
code= ""

list_nodes = []
list_nodes = codeChar(tree[0], code, list_nodes)

print(list_nodes)
print(alphabet_non_reduit(fileName))
#print(codeFinal('texteemma.txt',tree[0],code,list_nodes))
code_final = codeFinal(fileName,tree[0],code,list_nodes)[1]
print (code_final)
#texteCompresse = int(code_final, base=2).to_bytes((len(code_final)+7)//8, byteorder='big') 
print(Compression(code_final,fileName))

