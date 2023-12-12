def exo2(nb_chaine):
    liste=[]
    for i in range(nb_chaine):
        string=list(input())
        string.reverse()
        liste.append(str(string))
    liste.reverse()
    return liste

def suppr_voyelle(mot:str):
    a_suppr=["a","e","i","o","u","y"," "]
    for lettre in a_suppr:
        mot=mot.replace(lettre,"")

    return mot



print(suppr_voyelle("salut c'est moi"))