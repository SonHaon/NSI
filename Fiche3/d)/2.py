def evo_capital(somme,taux,valeur):
    duree=0
    while somme < valeur:
        duree+=1
        somme*=1+taux/100
    return duree

print(evo_capital(2000,2,3000))