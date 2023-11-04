from math import sqrt
import time

def racine_carre(nombre,decimal_ask):
    decimal=0
    a_test=1
    test_oui=1
    while decimal<decimal_ask:
        i=0
        stop=False
        while stop==False:
            a_test=test_oui+i/10**decimal
            test=a_test**2
            if test==nombre:
                test_oui=a_test
                break
            elif test > nombre:
                test_oui=test_oui+(i-1)/10**decimal
                stop=True
            i+=1
        decimal+=1
    if float(round(test_oui)) == test_oui:
        return int(test_oui)
    return test_oui

nombre=float(input("nombre : "))
decimal=float(input("decimal : "))

print("voila la racine calculé : ",racine_carre(nombre,decimal))
print("racine calculé avec sqrt: ",sqrt(nombre))