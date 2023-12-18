import os,platform,time
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)

clear()

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
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
    if not cLettre.lower() in alphabet:
        return cLettre
    lettre = alphabet.index(cLettre.lower())+iDecalage
    while lettre>(len(alphabet)-1):lettre-len(alphabet)
    if cLettre.isupper():
        return (alphabet[lettre])
    else:
        return (alphabet[lettre]).lower()

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



# print(encode_cesar_lettre2("A",43))
# print(encode_cesar_lettre2("b",43))
# print(encode_cesar_lettre2("C",43))
# print(encode_cesar_lettre2(" ",43))
# print(encode_cesar_lettre2("!",43))
# print(encode_cesar("couCou C'est Moi !",146))
# print(decode_cesar(encode_cesar("couCou C'est Moi !",146),146))

print(code_cesar("24,0ô'!38584ô,à0&&0-4?24ô'08 ô,4ô2!34ô4 aô-4,0a8c4c4'4?aô 8'&,4ôhô20 4-ôé",33,False))
