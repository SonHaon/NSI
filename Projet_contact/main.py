import json,os,platform
from pathlib import Path
path= Path(__file__).parent
file_contact=path / "contact.json"

def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)



with open((file_contact)) as file:
    contact:list=json.load(file)
def ajout_contact():
    global contact
    id=len(contact)
    nom=input("nom : ")
    prenom=input("prénom : ")
    naissance=input("date de naissance : ")
    addresse=input("addresse : ")
    ville=input("ville : ")
    code_postal=input("code postal : ")
    tel=input("numéro de tel : ")
    email=input("email : ")
    contact[str(id)]={
        "nom":nom,
        "prenom":prenom,
        "naissance":naissance,
        "addresse":addresse,
        "ville":ville,
        "code_postal":code_postal,
        "tel":tel,
        "email":email}

def supprimmer_contact():
    global contact
    clear()
    nom=input("nom : ")
    if nom=="":nom=None
    prenom=input("prénom : ")
    if prenom=="":prenom=None
    tel=input("numéro de tel : ")
    if tel=="":tel=None
    ids=search_contact(prenom,nom,tel)
    if ids==[]:
        print('aucun contact trouvé')
    contact.pop(ids[0])



    

def search_contact(prenom=None,nom=None,tel=None)->list:
    global contact
    infos=[]
    if prenom != None:
        for id in contact:
            if contact[id]["prenom"]==prenom:
                if not id in infos:
                    infos.append(id)
    if nom != None:
        for id in contact:
            if contact[id]["nom"]==nom:
                if not id in infos:
                    infos.append(id)
    elif tel != None:
        for id in contact:
            if contact[id]["tel"]==tel:
                if not id in infos:
                    infos.append(id)
    else:
        for id in contact:
            if not id in infos:
                infos.append(id)

    return infos

def voir_contact(id=None,prenom=None,nom=None,tel=None):
    global contact
    infos=[]
    width=os.get_terminal_size().columns-1
    if id!=None:
        info=[f"***** Contact {id} : "+" "*(width-len(f"***** Contact {id} : ")-5)+"*****"]
        for inf in contact[id]:
            info.append(f"***** {inf} : {contact[id][inf]}"+" "*(width-len(f"***** {inf} : {contact[id][inf]}")-5)+"*****")
        info="\n".join(info)
        infos.append(info)
    else:
        liste=search_contact(prenom,nom,tel)
        for id in liste:
            info=[f"*****"+" "*((width-len(f"***** Contact {id} : ")-5)//2)+f"Contact {id} : "+" "*((width-len(f"***** Contact {id} : ")-5)//2)+"*****"]
            for inf in contact[id]:
                info.append(f"*****"+" "*((width-len(f"***** {inf} : {contact[id][inf]}")-5)//2)+f"{inf} : {contact[id][inf]}"+" "*((width-len(f"***** {inf} : {contact[id][inf]}")-5)//2)+"*****")
            info="\n".join(info)
            infos.append(info)
    print("*"*width)
    print(("\n"+"*"*width+"\n").join(infos))
    print("*"*width)
    input()
    clear()
    
def menu():
    global contact
    while True:
        clear()
        print("1) ajouter un contact")
        print("2) retirer un contact")
        print("3) modifier un contact")
        print("4) chercher un contact par le nom")
        print("5) voir les contacts")
        print("99) sortir du programme")
        a=input("choisir une option : ")
        clear()
        if a=="1":
            ajout_contact()
        if a=="2":
            supprimmer_contact()
        elif a=="4":
            prenom=input("prénom du contact a rechercher : ")
            voir_contact(prenom=prenom)
        elif a=="5":
            voir_contact()
        elif a=="99":
            with open(file_contact,"w") as file:
                file.write(json.dumps(contact))
            clear()
            break

            
    

menu()