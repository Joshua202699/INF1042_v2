"""
Exemple 5 — Validation avec try / except

La conversion et la validation sont deux choses différentes :
- convertir = changer le type
- valider = vérifier que la saisie est acceptable
"""

saisie = input("Entrez un nombre entier : ").strip()

try:
    nombre = int(saisie)
    print("Conversion réussie :", nombre)
except ValueError:
    print("Saisie invalide : veuillez entrer un entier.")

# try/except accepte correctement les nombres négatifs,
# contrairement à un simple test avec .isdigit().
