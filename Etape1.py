#1 Dermination de lalphabet et des frequences des caracteres

import pandas as pd

def alphabet_non_reduit (file_name):
    '''
    determination de l'alphabet à partir d'un fichier txt
    pour le moment, pas de majuscules autorisées dans le fichier
    '''
    
    with open(file_name,'r',encoding="UTF-8") as fichier :
        Lignes = fichier.readlines()
    #Lignes = []
    #for ligne in lignes :
        #Lignes.append(ligne.strip()) ça supprime les tabulations, donc à éviter
    alphabet_non_reduit = []
    for i in range (len(Lignes)):
        for char in Lignes[i]:
                alphabet_non_reduit.append(char)
    #alphabet_non_reduit = str(alphabet_non_reduit).lower()
    return alphabet_non_reduit


def frequence(file_name):
    liste = alphabet_non_reduit(file_name)
    frequence = dict(pd.Series(liste).value_counts())
    return frequence

def alphabet (file_name):
    '''pb: lalphabet change chaque fois quon lance le code'''
    alphabet = list(set(alphabet_non_reduit(file_name)))
    return alphabet 

def alphabet_final(file_name):
    new_alphabet_final = {}
    dico_frequence = frequence(file_name)
    alphabet_final = dict(sorted(dico_frequence.items(), key=lambda t: t[1]))

    liste_occur =[]
    for occur in alphabet_final.values():
        liste_occur.append (occur)
    liste_occur = list(set(liste_occur))

    liste_char =[]
    liste_occur_2 = []
    for val in (liste_occur):
        for char,occurenc in alphabet_final.items():
            if occurenc == val :
                liste_char.append(char)
                liste_occur_2.append(occurenc)

        for i in sorted(liste_char):
            for j in liste_occur_2 :
                new_alphabet_final[i] = j
                break

        liste_occur_2 = []
        liste_char = []
                  
    #return '\n' + str(new_alphabet_final) + '\n'
    return new_alphabet_final

def display(file_name):
    dico = alphabet_final(file_name)
    #print(str(dico))
    print(len(dico))
    for k,v in dico.items():
             print(k,v) #pk ça retourne None?

             #new_file = open(file_name + "_freq.txt", "w" ,encoding="UTF-8")
             #new_file.write(display(filename))
             #new_file.close()
        



#fileName = 'alice.txt'
fileName = 'texteemma.txt'
# fileName = 'extraitalice.txt'
# fileName = 'textesimple.txt'

#clsprint(alphabet_non_reduit (fileName))
#print(alphabet (fileName))
#print(frequence(fileName))
print(alphabet_final(fileName))
print(display(fileName))
#print(sorted(['a','d','c','b']))
#print(set([1,2,2,3,9,3,8]))
l = [0,1,4]
#for i in l:
     #l.remove(i)
l.remove(0)
l.remove(4)
#print(l)  





        
        


