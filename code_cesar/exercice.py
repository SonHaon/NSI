import os,platform,time,math
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)

clear()

alphabet_simple=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','à','ù','é','è','ê','ï','ô','0','1','2','3','4','5','6','7','8','9','.',',','\'','?','!','&','#','-',' ']




def encode_cesar_lettre(cLettre: str, iDecalage: int) ->str:
    """
    renvoie la lettre encodé en code cesar aver un decalage de idecalage
    """
    assert type(cLettre)==str, "la lettre doit etre un string"
    assert len(cLettre)==1, "la lettre doit etre une seul lettre"
    assert type(iDecalage)==int, "le decalage doit etre un entier"
    if not (ord(cLettre.upper())<=90 and ord(cLettre.upper())>=65):
        return cLettre
    lettre=ord(cLettre.upper())+iDecalage
    while lettre>90:lettre-=26
    while lettre<65:lettre+=26
    if cLettre.isupper():
        return chr(lettre)
    else:
        return chr(lettre).lower()

def encode_cesar_lettre_alphabet(cLettre: str, iDecalage: int) ->str:

    """
    renvoie la lettre encodé en code cesar aver un decalage de idecalage
    """
    assert type(cLettre)==str, "la lettre doit etre un string"
    assert len(cLettre)==1, "la lettre doit etre une seul lettre"
    assert type(iDecalage)==int, "le decalage doit etre un entier"
    if not cLettre.lower() in alphabet_simple:
        return cLettre
    lettre = alphabet_simple.index(cLettre.lower())+iDecalage
    while lettre>(len(alphabet_simple)-1):lettre-=len(alphabet_simple)
    if cLettre.isupper():
        return (alphabet_simple[lettre])
    else:
        return (alphabet_simple[lettre]).lower()

def encode_cesar(strMessage: str, iDecalage: int) -> str:
    """
    blabla
    """
    assert type(strMessage)==str, "le message doit etre un string"
    assert type(iDecalage)==int, "le decalage doit etre un entier"
    message=""
    for lettre in strMessage:
        message+=encode_cesar_lettre_alphabet(lettre,iDecalage)
    return message

def decode_cesar(strMessage: str, iDecalage: int) -> str:
    """
    blabla
    """
    assert type(strMessage)==str, "le message doit etre un string"
    assert type(iDecalage)==int, "le decalage doit etre un entier"
    message=""
    for lettre in strMessage:
        message+=encode_cesar_lettre_alphabet(lettre,-iDecalage)
    return message

def code_cesar(strMessage: str, iDecalage: int,encodage:bool):
    if encodage:
        return encode_cesar(strMessage,iDecalage)
    else:
        return decode_cesar(strMessage,iDecalage)



# print(encode_cesar_lettre_alphabet("A",1))
# print(encode_cesar_lettre_alphabet("b",43))
# print(encode_cesar_lettre_alphabet("C",43))
# print(encode_cesar_lettre_alphabet(" ",43))
# print(encode_cesar_lettre_alphabet("!",43))
# print(encode_cesar("couCou C'est Moi !",146))
# print(decode_cesar(encode_cesar("couCou C'est Moi !",146),146))

# print(code_cesar("24,0ô'!38584ô,à0&&0-4?24ô'08 ô,4ô2!34ô4 aô-4,0a8c4c4'4?aô 8'&,4ôhô20 4-ôé",33,False))

def code_Vigenere(strMessage: str, strCle: str) -> str:
    while len(strCle)<len(strMessage):
        strCle+=strCle
    mess=""
    for i in range(len(strMessage)):
        intCle=alphabet_simple.index(strCle[i].lower())
        mess+=encode_cesar_lettre_alphabet(strMessage[i].lower(),intCle)

    return mess

def decode_Vigenere(strMessage: str, strCle: str) -> str:
    while len(strCle)<len(strMessage):
        strCle+=strCle
    mess=""
    for i in range(len(strMessage)):
        intCle=alphabet_simple.index(strCle[i].lower())
        mess+=encode_cesar_lettre_alphabet(strMessage[i].lower(),-intCle)

    return mess

# print(code_Vigenere("CHIFFRE DE VIGENERE","BACHELIER"))
# print(decode_Vigenere("dhkmjcm uf xpkpviif","BACHELIER"))


