import pandas as pd



#1 Dermination de lalphabet et des frequences des caracteres

def getText (file_name):
    '''
      Retourne le texte contenu dans le fichier entre en parametre sous forme de liste. 
      Chaque element de cette liste est un caractre du texte.
      Possibilite d avoir des repetitions au niveau des elements si dans le texte le characteres sont utilises plusieurs fois
    '''
    
    with open(file_name + ".txt",'r',encoding="UTF-8") as fichier :
        Lignes = fichier.readlines()

    texte = []
    for i in range (len(Lignes)):
        for char in Lignes[i]:
                texte.append(char)
    fichier.close()

    return texte
    

def alphabet (file_name):
    '''
    retourne l alphabet utilisé pour écrire le texte contenu dans le fichier entre en parametre
    '''
    #pb: lalphabet change chaque fois quon lance le code
    alphabet = list(set(getText(file_name)))
    return alphabet 


def frequence(texte):
     '''
     Prend en paramètre un texte en forme de liste de caractere où chaque caractere est extrait d un texte.
     Permet de compter l occurence de chaque caractere dans le texte
     Retourne une liste de tuple constituee de deux elements : le 1er -> le charactere et le 2e -> l occurrence du charactere
     La frequence est retournee par ordre decroissant. Pour avoir la frequence par ordre croissante, voir fonction triFreq
     '''
     
     liste_frequence = []
     frequence = dict(pd.Series(texte).value_counts())
     for char, occur in frequence.items():
          liste_frequence.append((char,occur))
     return liste_frequence



def triFreq(myList):
        ''' Permet de trier une liste de tuple. 
        Le tuple etant constitue de 2 elements (le 1er est le caractere et le 2eme l occurence du caractere dans le texte ou il est extrait) 
        Retourne une liste triee de facon croissante en fonction de l occurence puis en fonction du code ASCII si deux caracteres ont la meme occurence
        '''
        list_length = len(myList)
        for i in range(0, list_length):
            for j in range(0, list_length-i-1):  
                if (myList[j][1] > myList[j + 1][1] or myList[j][1] == myList[j + 1][1] and myList[j][0] > myList[j + 1][0]):  
                    temp = myList[j]  
                    myList[j]= myList[j + 1]  
                    myList[j + 1]= temp  
        return myList

def save_frequence(liste_tri,file_name):
        '''
        Cree un fichier qui sauvegarde la frequence (occurence) de chaque caractere
        La fonction ecrase le fichier s il existe deja et en cree un nouveau.
        Il en cree un nouveau si le fichier n existe pas encore.
        Renvoie un message de confirmation quand le fichier est cree.
        '''
     
        new_file = open(file_name + "_freq.txt", "w" ,encoding="UTF-8")
        new_file.write(str(len(liste_tri))+ '\n')
        for tuple in liste_tri:
              new_file.write(tuple [0] + "  " + str(tuple[1]) + '\n')
        new_file.close()
        return ("Fichier créé avec succès")



#### Tests ####


# Avant de tester une fonction sur un fichier, il faut se placer dans le dossier contenant ce fichier texte (le dossier qui a pour nom le nom du fichier)
# Puis, il faut choisir parmi les fileName suivant en fonction du dossier où vous vous placerez
#Pour un affichage complet du début à la fin, après avoir realiser les deux # du haut, tout lancer à partir de l etape5

# Nom des fichiers pour les tester 

fileName = 'textesimple'
#fileName = 'alice'
#fileName = 'extraitalice'
#fileName = 'bonjour'

#Affichage du texte et de l alphabet
print("\n", "texte : ", getText(fileName), "\n")
print("alphabet :",alphabet(fileName), "\n")

#Affichage des frequences
texte = getText(fileName) 
print("frequence : ", frequence(texte), "\n")

#Affichage des frequences triees
freq = frequence(texte)
print ("frequence triee : ", triFreq(freq), "\n")

#Sauvegarde des frequences
liste_freq_triees = triFreq(freq)
print(save_frequence(liste_freq_triees,fileName), "\n")







        
        


