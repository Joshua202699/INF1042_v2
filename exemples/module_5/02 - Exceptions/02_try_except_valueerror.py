"""
Exemple 2 — try / except

try : code qui pourrait provoquer une erreur.
except : code qui réagit à un type précis d'erreur.
"""

texte = input("Entrez votre âge : ")

try:
    age = int(texte)
    print("Âge dans 5 ans :", age + 5)
except ValueError:
    print("Veuillez entrer un nombre entier valide.")

print("Le programme continue au lieu de s'arrêter brusquement.")
