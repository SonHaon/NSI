def population_bacterie():
    t=0
    pop_init=100000
    pop=pop_init
    while pop < pop_init*2:
        pop+=10.5
        t+=1
    return f"la population a doublé en {t} heures"


def population_bacterie2(seuil):
    t=0
    pop=100000
    while pop < seuil:
        pop+=10.5
        t+=1
    return f"la population a atteint le seuil de {seuil} en {t} heures"


def population_bacterie3(pop_init,seuil):
    if pop_init>=seuil:
        return "la population est déjà supérieur ou égal au seuil"
    t=0
    pop=pop_init
    while pop < seuil:
        pop+=10.5
        t+=1
    return f"la population est passé de {pop_init} à {seuil} en {t} heures"

print(population_bacterie3(100000,200000))