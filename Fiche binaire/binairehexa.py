hexadecimal=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
binaire=["0000","0001","0010","0011","0100","0101","0110","0111","1000","1001","1010","1011","1100","1101","1110","1111",]

def bin_vers_hex(binaire:str)->str:
    binaire=binaire[2:]
    chiffre=0
    resultat=["0x"]
    a=0
    for i in range(round(len(binaire)/4)):
        for g in range(4):
            a+=1
            if a<=len(binaire):
                chiffre+=int(binaire[-a])*2**g
        resultat.insert(1,hexadecimal[chiffre])
        chiffre=0
    return "".join(resultat)
def hex_vers_bin(hexa:str)->str:
    hexa=hexa[2:]
    resultat=["0b"]
    for chiffre in hexa:
        resultat.append(str(int(binaire[hexadecimal.index(chiffre)])))
    return "".join(resultat)
def bin_vers_dec(binaire:str)->str:
    binaire=binaire[2:]
    resultat=0
    for i in range(len(binaire)):
        resultat+=int(binaire[-(i+1)])*2**i
    return str(resultat)
def dec_vers_bin(nb:str)->str:
    nb=int(nb)
    resultat=["0b"]
    while nb>=1:
        nb,reste=int(nb//2),nb%2
        resultat.insert(1,str(reste))
    return "".join(resultat)

def n_vers_m(nb:str,n,m)->str:
    nb=list(nb)
    nb.reverse()
    nb="".join(nb)
    resultat=0
    i=0
    for chiffre in nb:
        resultat+=int(chiffre)*n**i
        i+=1
    nb=resultat
    resultat=[f"base {m} : "]
    while nb>=1:
        nb,reste=int(nb//m),nb%m
        resultat.insert(1,str(hexadecimal[reste]))
    return "".join(resultat)
def somme_binaire(nb1,nb2):
    nb1=nb1[2:]
    nb2=nb2[2:]
    resultat=["0b"]
    retenu=0
    if len(nb1)>len(nb2):
        nb=len(nb1)
        nb2="0"*(len(nb1)-len(nb2))+nb2
    elif len(nb2)>len(nb1):
        nb=len(nb2)
        nb1="0"*(len(nb2)-len(nb1))+nb1
    else:
        nb=len(nb1)
    for i in range(nb):
        i+=1
        somme=int(nb1[-i])+int(nb2[-i])+retenu
        if somme>1:
            somme-=2
            retenu=1
        else:
            retenu=0
        resultat.insert(1,str(somme))
    resultat.insert(1,str(retenu))

    return "".join(resultat)

#print(bin_vers_hex("0b101101"))
#print(hex_vers_bin("0x2D"))
#print(dec_vers_bin("45"))
#print(bin_vers_dec("0b101101"))

#print(n_vers_m("204",6,16))
#print(somme_binaire("0b101101","0b11011"))