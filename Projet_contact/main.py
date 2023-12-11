import json,os
from pathlib import Path
path= Path(__file__).parent

os.system("cls")

with os.open((path / "contact.json"),"r") as file:
    contact=json.load(file)
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
    
def voir_contact(id=None,prenom=None,tel=None):
    global contact
    infos=[]
    width=os.get_terminal_size().columns-1
    if id!=None:
        info=[f"***** Contact {id} : "+" "*(width-len(f"***** Contact {id} : ")-5)+"*****"]
        for inf in contact[id]:
            info.append(f"***** {inf} : {contact[id][inf]}"+" "*(width-len(f"***** {inf} : {contact[id][inf]}")-5)+"*****")
        info="\n".join(info)
        infos.append(info)
    elif prenom != None:
        for id in contact:
            if contact[id]["prenom"]==prenom:
                info=[f"***** Contact {id} : "+" "*(width-len(f"***** Contact {id} : ")-5)+"*****"]
                for inf in contact[id]:
                    info.append(f"***** {inf} : {contact[id][inf]}"+" "*(width-len(f"***** {inf} : {contact[id][inf]}")-5)+"*****")
                info="\n".join(info)
                infos.append(info)
    elif tel != None:
        for id in contact:
            if contact[id]["tel"]==tel:
                info=[f"***** Contact {id} : "+" "*(width-len(f"***** Contact {id} : ")-5)+"*****"]
                for inf in contact[id]:
                    info.append(f"***** {inf} : {contact[id][inf]}"+" "*(width-len(f"***** {inf} : {contact[id][inf]}")-5)+"*****")
                info="\n".join(info)
                infos.append(info)
    else:
        for id in contact:
            info=[f"***** Contact {id} : "+" "*(width-len(f"***** Contact {id} : ")-5)+"*****"]
            for inf in contact[id]:
                info.append(f"***** {inf} : {contact[id][inf]}"+" "*(width-len(f"***** {inf} : {contact[id][inf]}")-5)+"*****")
            info="\n".join(info)
            infos.append(info)
    print("*"*width)
    print("\n**************************************************\n".join(infos))
    print("*"*width)
    input()
    os.system("cls")
    
def menu():
    while True:
        os.system("cls")
        print("1) ajouter un contact")
        print("2) retirer un contact")
        print("3) modifier un contact")
        print("4) chercher un contact par le nom")
        print("5) voir les contacts")
        print("99) sortir du programme")
        a=input("choisir une option : ")
        os.system("cls")
        if a=="1":
            ajout_contact()
        elif a=="4":
            prenom=input("prénom du contact a rechercher : ")
            voir_contact(prenom=prenom)
        elif a=="5":
            voir_contact()
        elif a=="99":
            os.system("cls")
            break

            
    

menu()