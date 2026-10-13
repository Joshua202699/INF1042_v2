"""
Exemple 5 — IndexError et KeyError

IndexError : index inexistant dans une liste ou un tuple.
KeyError : clé inexistante dans un dictionnaire.
"""

nombres = [4, 8, 15]

def lire_index(index):
    try:
        print("nombres[", index, "] =", nombres[index], sep="")
    except IndexError:
        print("Index inexistant :", index)

lire_index(1)
lire_index(10)

eleve = {"nom": "Tremblay", "note": 88}

try:
    print("Prénom :", eleve["prenom"])
except KeyError:
    print("La clé 'prenom' n'existe pas dans le dictionnaire.")
    print("Clés disponibles :", list(eleve.keys()))
