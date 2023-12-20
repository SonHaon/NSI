import csv,os,platform,collections
from pathlib import Path
path = Path(__file__).parent
def clear():
    """
    Clear the console
    """
    command = 'cls' if platform.system().lower().startswith('win') else 'clear'
    os.system(command)



def lecture_csv_en_listes(nom_du_fichier: str, delimiteur: str)->list:
    """
    :param delimiteur: type str: le délimiteur : ‘,’ ou ‘;’
    renvoie une liste contenant toutes les données du fichier csv, chaque
    donnée étant stockée sous forme de liste
    """
    with open(path / nom_du_fichier, 'r') as mon_fichier :
        contenu = csv.reader(mon_fichier, delimiter=';')
        header=next(contenu)

        elements = list()
        for ligne in contenu:
            elements.append(ligne)
    # elements est une liste de listes
    for element in elements:
        print(element)

def lecture_csv_en_dictionnaire(nom_du_fichier: str, delimiteur: str)-> list:
    """
    :param nom_du_fichier: type str: Le nom du fichier à ouvrir
    :param delimiteur: type str: le délimiteur : ‘,’ ou ‘ ;’
    :return: type list: liste contenant toutes les données du fichier csv,
    chaque donnée étant stockée sous forme de dictionnaire
    """
    mon_fichier = open(path/nom_du_fichier)
    contenu = csv.DictReader(mon_fichier, delimiter = delimiteur)
    elements = []
    for ligne in contenu:
        elements.append(ligne) # elements est une liste de dictionnaires
    mon_fichier.close()
    return elements

def lecture_csv_en_tuples_nommes(nom_du_fichier: str, delimiteur: str)-> list:
    """
    :param delimiteur: type str: le délimiteur : ‘,’ ou ‘;’
    renvoie une liste contenant toutes les données du fichier csv, chaque
    donnée étant stockée sous forme de liste
    """
    with open(path / nom_du_fichier, 'r') as mon_fichier :
        contenu = csv.reader(mon_fichier, delimiter=';')
        header=next(contenu)
        createur_de_tuple_nomme = collections.namedtuple(nom_du_fichier.split(".")[0], header)

        elements = list()
        for ligne in contenu:
            tuple=createur_de_tuple_nomme(*ligne)
            elements.append(tuple)
    # elements est une liste de listes
    for element in elements:
        print(element)



clear()
# print(lecture_csv_en_listes("fruits.txt",";"))
# print(lecture_csv_en_dictionnaire("fruits.txt",";"))
print(lecture_csv_en_tuples_nommes("fruits.txt",";"))
