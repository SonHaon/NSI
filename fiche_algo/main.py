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



notes = [9,10, 10.5,15.5,7 ,7 ,2.5,16,7,12.5,13,13,9.5,4,12,10.5,19,6.5 , 13, 8.5]
def moyenne_note(notes:list):
    return sum(notes)/len(notes)
print(moyenne_note(notes))

def est_dedans(liste:list,valeur):
    for element in liste:
        if element==valeur:
            return True
    return False
print(est_dedans(notes,123))

def nb_fois(liste:list,valeur):
    nb=0
    for element in liste:
        if element==valeur:
            nb+=1
    return nb
print(nb_fois(notes,7))

def longeur(liste):
    nb=0
    for element in liste:
        nb+=1
    return nb
print(longeur(notes))