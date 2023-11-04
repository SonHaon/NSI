response=input("A vous de jouer : ")
a,b=response.split(" ")
if (a=="4" and b=="7") or (a=="7" and b=="4"):
    print("Coulé")
elif a=="4" or b == "4" or a=="7" or b=="7":
    print("En vue")
else:
    print("dans l'eau")
while True:
    response=input("Nouvel essai : ")
    if response=="s":
        print("arrêt de la partie")
        break
    a,b=response.split(" ")
    if (a=="4" and b=="7") or (a=="7" and b=="4"):
        print("Coulé")
        break
    elif a=="4" or b == "4" or a=="7" or b=="7":
        print("En vue")
    else:
        print("dans l'eau")