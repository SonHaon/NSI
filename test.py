#binaire="101101"
#print(binaire)
#resultat=0
#for i in range(len(binaire)):
#    print(i, binaire[-(i+1)],int(binaire[-i])*2**i)
#    resultat+=int(binaire[-(i+1)])*2**i
#print(resultat)


print("zjoifdqjhoz"[1:])


for i in range(limite):
        decimal=str(int(decimal)*2)
        if int(decimal)>=10**chiffre_decimal:
            chiffre=decimal[0]
            decimal=int(decimal[1:])
        else:
            chiffre="0"
        resultat.append(chiffre)
        if int(decimal)==0:
            break