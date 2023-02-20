
from Etape1 import *

class Node ():
    def __init__(self, label , occurence, leftChild = None, rightChild =None):
        self.label = label
        self.occur = occurence
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.branch = ''

    def __repr__(self) :
        return  '(' + str(self.label)  + "," + str(self.occur) +')'
    
    

def insert (liste, a,b,c):
    '''insere l'element x dans la liste qui est supposee triee et retire les elements a et b
    a,b et x etant des noeuds'''
    liste.remove(a)
    liste.remove(b)
    liste.append(c)
    new_liste = sorted(liste, key=lambda x: x.occur)
    return new_liste
    
        




    
def create_liste_node(dico):
    ''' récupère l'alphabet sous forme de liste de tuple et crée les nouveux noeuds jusqu'à obtenir 1 seul tuple'''
    liste_node = []
    liste_node = [(Node(char,occur)) for char,occur in dico.items()]
    return liste_node
    

def add_and_remove_node(new_liste_node):

    new_label = ''
    new_occur = 0
    new_leftChild = None
    new_rightChild = None
    new_node = None


    while len(new_liste_node) > 1:
       new_label =  str(new_liste_node[0].label) + str(new_liste_node[1].label) 
       new_occur = new_liste_node[0].occur+ new_liste_node[1].occur

       new_leftChild = new_liste_node[0]
       new_rightChild = new_liste_node[1]
       new_leftChild.branch = 0
       new_rightChild.branch = 1

       new_node = Node(new_label,new_occur,new_leftChild,new_rightChild)
       new_liste_node = insert (new_liste_node,new_liste_node[0], new_liste_node[1],new_node)

       new_liste_node = add_and_remove_node(new_liste_node)
    return new_liste_node
          
    
'''class Btree():
       def __init__(self, root):
            self.root = root'''
        

def printTree(root):
    if root!=None:
        return [root.label, printTree(root.leftChild),printTree(root.rightChild)]


dico = alphabet_final(fileName)
#print(dico)
list_node = create_liste_node(dico)
#print(list_node)
#print(insert (list_node, ('!', 1), ('B', 1), ('!B',2)))
#tree = add_and_remove_node(list_node)
#print(tree)

#print(printTree(tree[0]))