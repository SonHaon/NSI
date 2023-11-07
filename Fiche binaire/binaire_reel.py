from binairehexa import *

limite=50

def dec_bin_apres_virgule(decimal:int):
    resultat=[]
    for i in range(limite):
        decimal=float("0."+str(decimal))*2
        chiffre,decimal=str(decimal).split(".")
        resultat.append(chiffre)
        if int(decimal)==0:
            break
    return "".join(resultat)
def reel2bin(nombre:float)->str:
    print(nombre)
    signe=""
    if nombre<0:
        signe="-"
        nombre=abs(nombre)
    entier,decimal=str(nombre).split(".")
    entier,decimal=int(entier),int(decimal)
    return f"{signe}{dec_vers_bin(entier)[2:]}.{dec_bin_apres_virgule(decimal)}"
def bin2reel(binaire:str)->float:
    entier=binaire.split(".")[0]
    resultat=0.0
    i=len(entier)-1
    binaire=binaire.replace(".","")
    for chiffre in binaire:
        resultat+= float(chiffre)*2**i
        i-=1
    return resultat

def rep_bin_reel(nombre:float,bits_exposant:int,bits_mantisse:int)->str:
    resultat,resultat_norme=[],[]
    signe=0
    if nombre<0:
        signe=1
        nombre=abs(nombre)
    print(str(nombre))
    print(f"signe : {signe}")
    resultat.append(str(signe))
    resultat_norme.append(str(signe))

    binaire = reel2bin(nombre)
    mantisse = (binaire.replace(".","")+"0"*bits_mantisse)[:bits_mantisse]
    print(f"mantisse : {mantisse}")
    resultat.append(mantisse)
    mantisse_tronquee=(mantisse[1:]+"0"*bits_mantisse)[:bits_mantisse]
    print(f"mantisse tronquée : {mantisse_tronquee}")
    resultat_norme.append(mantisse_tronquee)

    exposant=("0"*bits_exposant+dec_vers_bin(len(binaire.split(".")[0])-1)[2:])[-bits_exposant:]
    print(f"exposant sans décalage : {exposant}")
    resultat.insert(1,exposant)
    exposant_decalage=("0"*bits_exposant+somme_binaire("0b"+exposant,"0b1111111")[2:])[-bits_exposant:]
    print(f"exposant avec décalage : {exposant_decalage}")
    resultat_norme.insert(1,exposant_decalage)



    




    return " ".join(resultat)," ".join(resultat_norme)








print(rep_bin_reel(67.0,8,23))

# print(reel2bin(-1024.25))
# print(bin2reel("10000000000.01"))