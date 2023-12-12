import os,platform
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)

clear()

def encode_cesar_lettre(cLettre: str, iDecalage: int) ->str:
    """
    renvoie la lettre encodé en code cesar aver un decalage de idecalage
    """
    assert type(cLettre)==str, "la lettre doit etre un string"
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
    
def encode_cesar(strMessage: str, iDecalage: int) -> str:
    
    

print(encode_cesar_lettre("A",43))
print(encode_cesar_lettre("b",43))
print(encode_cesar_lettre("C",43))
print(encode_cesar_lettre(" ",43))
print(encode_cesar_lettre("!",43))
