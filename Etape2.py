from Etape1 import *

class Node :

    def __init__(self, label , occurence, leftChild = None, rightChild = None):
        ''' constructeur d un noeud qui prend en parametre son etiquette (label+ occurrence) et ses enfants 
        Et lui attribut un une branche vide
        '''
        self.label = label
        self.occur = occurence
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.branch = ''

    def __repr__(self) :
        ''' permet l affichage du noeud '''
        return  '(' + str(self.label)  + "," + str(self.occur) +')'
    
    

def insert_and_remove(liste, a,b,c):
    '''
    La fonction prend en parametre une liste et 3 noeuds et retourne une liste
    Elle insere lelement c dans la liste qui est supposee triee tout en respectant l'ordre de tri puis retire les elements a et b
    '''
    liste.remove(a)
    liste.remove(b)
    liste.append(c)
    new_liste = sorted(liste, key=lambda x: x.occur)
    return new_liste
    
        
  
def create_liste_node(dico):
    '''
    Prend en parametre un dictionnaire (ordonne par ordre croissant) puis cree des noeuds pour chaque element du dictionnaire
    ayant pour etiquette la cle(label) et la valeur de la cle (occurence)
    Retourne une liste de noeuds
    '''

    liste_node = []
    liste_node = [(Node(char,occur)) for char,occur in dico.items()]
    return liste_node
    

def add_and_remove_node(new_liste_node):
    ''' 
    Prend en parametre une liste de noeud et la reduit grace a la fonction insert_and_remove jusqu a obtenir une liste ayant un seul noeud: le noeud racine
    Retourne une liste avec pour element le noeud racine
    '''

    new_label = ''
    new_occur = 0
    new_leftChild = None
    new_rightChild = None
    new_node = None

    #tant que la longueur de la liste est > 1 : creer un nouveau noeud avec avec les 2 premiers elements de la liste 
    while len(new_liste_node) > 1:
    
       #creation de l etiquette du nouveau noeud
       new_label =  str(new_liste_node[0].label) + str(new_liste_node[1].label) 
       new_occur = new_liste_node[0].occur+ new_liste_node[1].occur

       #affecte le 1er element de la liste comme etant le fils gauche et le 2nd comme etant le fils droit
       new_leftChild = new_liste_node[0]
       new_rightChild = new_liste_node[1]

       #affecte la branche 0 au fils gauche et la branche 1 au fils droit
       new_leftChild.branch = 0
       new_rightChild.branch = 1

       # cree un nouveau noeud ,supprime les 2 premiers noeuds de la liste noeud puis y rajoute le nouveau noeud 
       new_node = Node(new_label,new_occur,new_leftChild,new_rightChild)
       new_liste_node = insert_and_remove (new_liste_node,new_liste_node[0], new_liste_node[1],new_node)

       new_liste_node = add_and_remove_node(new_liste_node)

    return new_liste_node
          
    
def printTree(root):
    '''Gere l'affichage de l'arbre de l'ordre à avoir les fils de chaque noeud'''
    if root!=None:
        return [root.label, printTree(root.leftChild),printTree(root.rightChild)]
    

###Tests###

#affichage de la liste des noeuds
dico = dict(freq)
#print("dico",dico, "\n")
list_node = create_liste_node(dico)
print("list_node", list_node, "\n")

#affichage du noeud racine
root = add_and_remove_node(list_node)
print("root : ",root, "\n")

#affichage de l'arbre
print("tree : ",printTree(root[0]), "\n")

