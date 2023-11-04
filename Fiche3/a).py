texte = input("texte : ")
nb_e = 0
for lettre in texte:
    if lettre=="e":
        nb_e+=1
print(f"il y a {nb_e} e dans le texte")