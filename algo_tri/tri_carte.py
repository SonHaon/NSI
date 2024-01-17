from random import shuffle,randrange
from pathlib import Path
from itertools import count
import os,platform
path = Path(__file__).parent
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)
clear()
carte = [5,2,7,3,1]
# carte= [randrange(0,10) for i in range (5)]
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

# def tri(carte:list):
#     carte2=carte.copy()
#     for i in range(len(carte)):
#         temp=carte2[i]
#         carte.remove(temp)
#         carte.append(None)
#         a=len(carte)-2
#         while temp<carte[a] and a>=0:
#             carte[a+1],carte[a]=carte[a],carte[a+1]
#             a-=1
#         carte[a+1]=temp

#     return carte

def trier(l): 
    for i in range(len(l)): 
        for j in range(0, len(l) - i - 1): 
            if l[j] > l[j + 1]: 
                l[j], l[j + 1] = l[j + 1], l[j] 
    return l 
 
                
def trier_decroissant(l): 
    for i in range(len(l)): 
        for j in range(0, len(l) - i - 1): 
            if l[j] < l[j + 1]: 
                l[j], l[j + 1] = l[j + 1], l[j] 
    return l 

def tri_décroissant(carte:list):
    carte2=carte.copy()
    for i in range(len(carte)):
        temp=carte2[i]
        carte.remove(temp)
        carte.append(None)
        a=1
        while temp>carte[a] and a<=0:
            carte[a+1],carte[a]=carte[a],carte[a+1]
            a-=1
        carte[a]=temp

    return carte

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

def tri_bulle(liste):
    n = len(liste)
    for i in range(n-1):
        for j in range(n-i-1):
             if liste[j] >liste[j+1]:
                  liste[j], liste[j+1] = liste[j+1], liste[j]
    
    return liste

for i in count(0):
    print(i)

print(tri_bulle(carte))