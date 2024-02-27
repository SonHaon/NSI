import os
import platform
from math import sqrt
from pathlib import Path

path = Path(__file__).parent
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)
clear()


listeDePoints =[{'attributs': [2,3],'classe':'R'},
                {'attributs': [-1,5],'classe': 'B'},
                {'attributs': [3,3],'classe': 'B'},
                {'attributs': [3,0],'classe': 'R'},
                {'attributs': [6,5],'classe': 'R'},
                {'attributs': [-2,4],'classe': 'R'},
                {'attributs': [-1,-1],'classe': 'B'},
                {'attributs': [0,0],'classe': 'R'},
                {'attributs': [1,1],'classe': 'B'},
                {'attributs': [0,2],'classe':'B'} ]
cible ={'attributs': [2,1]}




def distance(elements1,elements2):
    assert len(elements1)==len(elements2),"il faut que les elements ait la même longueur"
    somme=0
    for i in range(len(elements1)):
        somme+=(elements2[i]-elements1[i])**2
    return sqrt(somme)

def distances_min(dataset,cible,k):
    min=[]
    for element in dataset:
        min.append((distance(element["attributs"],cible["attributs"]),element["classe"]))
    min.sort()
    result=[min[each][1] for each in range(k)]
    return result

print(distances_min(listeDePoints,cible,5))


def max_classe(classe):
    result={}
    for a in classe:
        try:
            result[a]+=1
        except:
            result[a]=1
    return result
print(max_classe(['B','R','R','B','R']))


def knn(dataset,cible,k):
    classes=distances_min(dataset,cible,k)
    nb_classe = max_classe(classes)
    return max(nb_classe)

print(knn(listeDePoints,cible,5))