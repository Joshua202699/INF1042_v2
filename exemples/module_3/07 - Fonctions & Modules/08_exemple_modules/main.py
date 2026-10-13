"""
Exemple multi-fichiers — Modules

Placez main.py, affichage.py et calcul.py dans le même dossier,
puis exécutez CE fichier.
"""

import affichage
import calcul

affichage.bonjour()
affichage.separateur()

resultat = calcul.addition(5, 3)
print("5 + 3 =", resultat)

produit = calcul.multiplication(4, 6)
print("4 × 6 =", produit)
