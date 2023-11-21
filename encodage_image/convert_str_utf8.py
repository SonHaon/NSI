def str_vers_utf8(message: str) -> str:
    """
    Prend en argument un message sous forme de chaîne de caractères
    Renvoie le message encodé selon le code utf-8 et exprimé comme un
    nombre binaire (ex: '0b00011001')
    """
    resultat=""
    for lettre in message:
        binaire=bin(ord(lettre))[2:]
        if len(binaire)<=7:
            binaire=f"{'0'*(8-len(binaire))}{binaire}"
        elif len(binaire)<=11:
            binaire=f"110{'0'*(11-len(binaire))}{binaire[:-6]} 10{binaire[-6:]}"
        elif len(binaire)<=16:
            binaire=f"1110{'0'*(16-len(binaire))}{binaire[:-12]} 10{binaire[:-6][-6:]} 10{binaire[-6:]}"
        elif len(binaire)<=21:
            binaire=f"11110{'0'*(21-len(binaire))}{binaire[:-18]} 10{binaire[:-6][-12:]} 10{binaire[:-6][-6:]} 10{binaire[-6:]}"
        resultat=resultat+binaire+" "
    return resultat.replace(" ","")

def utf8_vers_str(message_utf8: str) -> str:
    """
    Prend en argument un message encodé selon le code utf-8 et exprimé
    comme un nombre binaire (ex: '0b00011001')
    Renvoie le message encodé sous forme de chaîne de caractères
    """
    message_utf8=message_utf8.replace(" ","")
    message=""
    while len(message_utf8)>0:
        if message_utf8[:1]=="0":
            caractere=chr(int(message_utf8[:8],2))
            message_utf8=message_utf8[8:]
        elif message_utf8[:3]=="110":
            binaire=""
            binaire=binaire+message_utf8[:8][3:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            caractere=chr(int(binaire,2))
        elif message_utf8[:4]=="1110":
            binaire=""
            binaire=binaire+message_utf8[:8][4:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            caractere=chr(int(binaire,2))
        elif message_utf8[:5]=="11110":
            binaire=""
            binaire=binaire+message_utf8[:8][5:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            binaire=binaire+message_utf8[:8][2:]
            message_utf8=message_utf8[8:]
            caractere=chr(int(binaire,2))
        message=message+caractere

    return message
