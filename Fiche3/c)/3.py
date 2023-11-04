def evo_capital(somme,taux,nb_annee):
    for i in range(nb_annee):
        somme*=taux/100+1
    return somme

print(evo_capital(2000,2,20))