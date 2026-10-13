"""Filtrer une liste avec une boucle for et une condition."""
valeurs = [3, -1, 4, -2, 0, 5, -9]
positifs = []

for valeur in valeurs:
    if valeur >= 0:
        positifs.append(valeur)

print("Valeurs originales :", valeurs)
print("Valeurs >= 0 :", positifs)
