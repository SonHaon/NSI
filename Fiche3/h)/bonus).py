response=input("A vous de jouer : ")
essai=0
while True:
    essai+=1
    a,b=response.split(" ")
    if (a=="4" and b=="7") or (a=="7" and b=="4"):
        print("Coulé")
        break
    elif a=="4" or b == "4" or a=="7" or b=="7":
        print("En vue")
    else:
        print("dans l'eau")
    if input("Rejouer ?")=="n":
        break
    response=input("Nouvel essai : ")

print(f"Vous avez fait {essai} essais\nAu revoir !")