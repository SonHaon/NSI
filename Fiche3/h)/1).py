a,b=input("A vous de jouer : ").split(" ")
if (a=="4" and b=="7") or (a=="7" and b=="4"):
    print("Coulé")
elif a=="4" or b == "4" or a=="7" or b=="7":
    print("En vue")
else:
    print("dans l'eau")