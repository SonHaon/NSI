from random import randint
dico_lettre={
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9
}

def create_map() -> list:
    map=[["~","~","~","~","~","~","~","~","~","~",]]*10
    return map

def view_map(map:list) -> None:
    print("  A B C D E F G H I J")
    a=0
    for ligne in map:
        print(f"{a} ",end="")
        a+=1
        print(" ".join(ligne))

def edit_case(map,x,y,new_caractere):
    ligne_entiere=map[y].copy()
    ligne_entiere[x]=new_caractere
    map[y]=ligne_entiere
    return map

def create_ship(map:list,nb_ship) -> list:
    for i in range(nb_ship):
        ligne=randint(0,9)
        colonne=randint(0,9)
        print(colonne,ligne)
        edit_case(map,colonne,ligne,"b")
    return map

def is_touche(map,x,y):
    if map[y][x] =="b":
        return True
    else:
        return False

def ask_case():
    rep = input("Ou voulez-vous tirer : ")
    x,y=rep[0],rep[1]
    return dico_lettre[x],int(y)

def Game(nb_ship_init):
    nb_ship=nb_ship_init
    map_player=create_map()
    map_ship=map_player.copy()
    map_ship=create_ship(map_ship,nb_ship)
    view_map(map_player)
    nb_tour=0
    while True:
        nb_tour += 1
        x,y=ask_case()
        if is_touche(map_ship,x,y):
            map_player = edit_case(map_player,x,y,"e")
            map_ship = edit_case(map_ship,x,y,"e")
            view_map(map_player)
            print("Bravo vous avez touché un bateau !")
            nb_ship-=1
            if nb_ship==0:
                break
        else:
            map_player = edit_case(map_player,x,y,"¤")
            map_ship = edit_case(map_ship,x,y,"¤")
            view_map(map_player)
            print("Il n'y avait rien ici dommage")
    view_map(map_player)
    print(f"Bravo vous avez détruit tout les {nb_ship_init} bateaux ennemis en {nb_tour} essais")





print("Nouvelle partie !")
nb_ship=int(input("Combien de bateau ennemi voulez-vous : "))
print("Très bien lancement de la partie \nvoila le terrain")
Game(nb_ship)