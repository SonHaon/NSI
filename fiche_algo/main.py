from random import shuffle,randrange
from pathlib import Path
from itertools import count
import os,platform,math
path = Path(__file__).parent
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)
clear()
carte= [randrange(0,10) for i in range (5)]

def trier(l): 
    for i in range(len(l)): 
        for j in range(0, len(l) - i - 1): 
            if l[j] > l[j + 1]: 
                l[j], l[j + 1] = l[j + 1], l[j] 
    return l 

# notes = [9,10, 10.5,15.5,7 ,7 ,2.5,16,7,12.5,13,13,9.5,4,12,10.5,19,6.5 , 13, 8.5]
# def moyenne_note(notes:list):
#     return sum(notes)/len(notes)
# print(moyenne_note(notes))

# def est_dedans(liste:list,valeur):
#     for element in liste:
#         if element==valeur:
#             return True
#     return False
# print(est_dedans(notes,123))

# def nb_fois(liste:list,valeur):
#     nb=0
#     for element in liste:
#         if element==valeur:
#             nb+=1
#     return nb
# print(nb_fois(notes,7))

# def longeur(liste):
#     nb=0
#     for element in liste:
#         nb+=1
#     return nb
# print(longeur(notes))

def est_present_dans(tableau_trie,valeur):
    print(tableau_trie)
    milieu=tableau_trie[len(tableau_trie)//2]

    for i in range(len(tableau_trie)):
        if milieu==valeur:
            return True
        if milieu>valeur:
            milieu=tableau_trie[len(tableau_trie[::milieu])//2]
        else:
            milieu=tableau_trie[len(tableau_trie[milieu::])//2]
    return False
    
# print(est_present_dans(trier(carte),6))

def rechdic(liste,valeur):
    indices_inferieur=0
    indices_superieur=len(liste)-1
    print("début :",indices_inferieur,indices_superieur)

    while indices_inferieur<=indices_superieur:
        milieu=(indices_inferieur+indices_superieur)//2

        if liste[milieu]>valeur:
            indices_superieur=milieu-1
        elif liste[milieu]<valeur:
            indices_inferieur=milieu+1
        else:
            return f"élément {valeur} présent a l'indice {milieu}"
    return "élément absent"

# print(rechdic(trier(carte),6))

def f(x):
    return math.cos(x)-x

def recherche_sd_dicho(debut,fin,p):
    while True:
        milieu=(debut+fin)/2
        # print(milieu,f(milieu))
        if round(f(milieu),p)==0.0:
            return f"{milieu} et {round(f(milieu),p+1)}"
        elif f(milieu)>0.0:
            debut=milieu
        elif f(milieu<0.0):
            fin=milieu

def recherche_sd_dicho2(debut,fin,p):
    milieu=(debut+fin)/2
    while fin-debut>10**-p:
        milieu=(debut+fin)/2
        if f(milieu)>0.0:
            debut=milieu
        elif f(milieu<0.0):
            fin=milieu
    return f"{debut},{fin},{milieu} et {round(f(milieu),p+1)}"

print(recherche_sd_dicho(0,4,4))
print(recherche_sd_dicho2(0,4,4))