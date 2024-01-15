from random import shuffle
from pathlib import Path
import os,platform
path = Path(__file__).parent
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)
clear()
carte = [10,8,2,5,1,5,2,17,15,6]
carte_trie = [1,2,4,5,5,6,7,8,9,10]

def est_trie(liste):
    for i in range(len(liste)):
        try:
            if liste[i] <= liste[i+1]:
                pass
            else:
                return False
        except:
            pass
    return True

def tri(carte):
    for i in range(len(carte)):
        print(carte)
        if i<2:
            a=0
            while carte[i-a]>carte[i-1-a]:
                print(carte[i-1-a],carte[i-a])
                carte[i-1-a],carte[i-a]=carte[i-a],carte[i-1-a]
                a+=1
        else:
            if carte[i-1]>carte[i]:
                carte[i-1],carte[i]=carte[i],carte[i-1]

    print(carte)

def tri_singe(liste):
    a=0
    while not est_trie(liste):
        shuffle(liste)
        a+=1

    return len(liste),"element", a,"essai", liste

def tri_poste(liste):
    boites=[[] for _ in range(100)]
    for i in liste:
        boites[i].append(i)
    triee=[]
    for boite in boites:
        for element in boite:
            triee.append(element)
    return triee

print(tri_poste(carte))