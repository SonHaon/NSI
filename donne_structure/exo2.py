import os,platform,math
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)

clear()




def verif_mdp(mdp):
    s = 0
    isonup = False
    isondown = False
    have_caractere_special = False
    for i in mdp:
        s += 1
    if s < 8:
        mdp = input("Tapez un nouveau mot de passe car celui ci n'a pas assez de caractères.")
    for i in mdp:
        if i.isupper():
            isonup = True
        if i.islower():
            isondown = True
    if not isonup:
        mdp = input("Tapez un nouveau mot de passe car celui ci n'a pas de majuscules.")
    if not isondown:
        mdp = input("Tapez un nouveau mot de passe car celui ci n'a pas de minuscules.")
    for i in mdp:
        if i in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', '.', ',', '?', '/', '`', '~']:
            have_caractere_special = True
    if not have_caractere_special:
        mdp = input("Tapez un nouveau mot de passe car celui ci n'a pas de caractère spécial.")


# verif_mdp("OOIoiehff@")



def nb_mot1(phrase:str):
    mots=phrase.split(" ")
    return len(mots)

def nb_mot2(phrase:str):
    nb_epace=0
    for lettre in phrase:
        if lettre ==" ":
            nb_epace+=1
    return nb_epace+1

# print(nb_mot1("Le petit chat est mort"))
# print(nb_mot2("Le petit chat est mort"))


personnes = {
    "Jean Aymar": {"taille": 178,"pays": "USA", "age": 31,"sexe": "H"},
    "Clio Patre": {"pays": "Portugal","age": 32,"sexe": "F", "taille": 179},
    "Delphine Jalon": {"pays": "France","sexe": "F","age": 19, "taille": 169},
    "Pietro Silvani": {"age": 74,"pays": "Italie", "taille": 170,"sexe": "H"},
    "Paco Roig": {"taille": 176,"pays": "Espagne","sexe": "H","age": 45},
}

def info_pers(nom:str):
    if nom in personnes:
        return personnes.get(nom)["age"]
    else:
        return None
    
def info_pers2(nom:str,info):
    if nom in personnes:
        return personnes.get(nom)[info]
    else:
        return None
    
def moyenne_taille():
    nb_pers=len(personnes)
    taille=0
    for pers in personnes:
        taille+=personnes[pers]["taille"]
    return taille/nb_pers

# print(info_pers("Jean Aymarz"))
# print(info_pers2("Jean Aymar","pays"))
# print(moyenne_taille())


def milieu_point(points):
    p1,p2=points
    p3=( (p1[0]+p2[0])/2, (p1[1]+p2[1])/2 )
    return p3

# print(milieu_point(((2,4),(5,7))))

def distance_points(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

# print(distance_points((1,1),(3,3)))




todo_list={
    "faire les courses":True,
    "ranger le garage":False,
    "completer exercice 4":False
}

def nb_tache_nonfait():
    nb=0
    for tache,fait in todo_list.items():
        if not fait:
            nb+=1
    return nb

etat={True:"V",False:"F"}


# • + pour ajouter une tâche. Le programme demande
# ensuite le nom de la tâche ;
# • —suivi d'un numéropourretirerlatâchecorrespondante;
# • v suivi d'un numéro pour changer le statut fait/ à faire
# de la tâche correspondante ;
# ? pour afficher seulement les tâches restant à faire.



def main():
    while True:
        show()
        print("+ pour ajouter une tâche.\n— suivi d'un numéro pour retirer la tâche correspondante\nv suivi d'un numéro pour changer le statut fait/ à faire\n? pour afficher seulement les tâches restant à faire.")
        todo=input("Que faire ? : ")
        if todo=="+":
            add_task()
        if todo=="-":
            remove_task()
        if todo=="v":
            change_task()
        if todo=="?":
            show2()
        if todo=="99":
            clear()
            break

def show():
    clear()
    global todo_list
    a=1
    for tache,fait in todo_list.items():
        print(f"{a}) {etat[fait]} {tache}")
        a+=1

def show2():
    clear()
    global todo_list
    a=1
    for tache,fait in todo_list.items():
        if not fait:
            print(f"{a}) {etat[fait]} {tache}")
        a+=1
    input()

def add_task():
    clear()
    show()
    global todo_list
    task=input("tache a effectuer : ")
    todo_list[task]=False

def remove_task():
    clear()
    global todo_list
    show()
    num=input("Numero de la tache : ")
    a=1
    for tache in todo_list:
        if a==int(num):
            todo_list.pop(tache)
            break
        a+=1

def change_task():
    clear()
    global todo_list
    show()
    num=input("Numero de la tache : ")
    a=1
    for tache in todo_list:
        if a==int(num):
            todo_list[tache]=not todo_list[tache]
            break
        a+=1

main()