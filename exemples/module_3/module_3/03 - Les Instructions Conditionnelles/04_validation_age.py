"""
Exemple 4 — Saisie et décision

input() fournit du texte.
int() transforme ce texte en entier avant la comparaison.
"""

age = int(input("Votre âge : "))

if age >= 18:
    print("Accès autorisé")
else:
    print("Accès restreint")
