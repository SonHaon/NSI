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
    print(f"signe : {signe}")
    resultat.append(signe)
    resultat_norme.append(signe)

    binaire = reel2bin(nombre)
    mantisse = binaire.replace(".","")
    print(f"mantisse : {mantisse}")
    resultat.append(mantisse)
    print(f"mantisse tronquée : {mantisse[1:]}")
    resultat_norme.append(mantisse[1:])

    exposant=dec_vers_bin(len(binaire.split(".")[0])-1)[2:]
    print(f"exposant sans décalage : {exposant}")
    




    return " ".join(resultat)," ".join(resultat_norme)










print(reel2bin(-1024.25))
print(bin2reel("10000000000.01"))