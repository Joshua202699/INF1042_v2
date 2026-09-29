"""
Exemple 6 — Choix aléatoire et condition

random.choice() choisit un élément dans une collection.
"""

import random

options = ["Pierre", "Papier", "Ciseaux"]
choix = random.choice(options)

print("Choix de l'ordinateur :", choix)

if choix == "Pierre":
    print("L'ordinateur a joué Pierre.")
elif choix == "Papier":
    print("L'ordinateur a joué Papier.")
else:
    print("L'ordinateur a joué Ciseaux.")
