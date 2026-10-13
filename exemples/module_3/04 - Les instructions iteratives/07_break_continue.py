"""
Exemple 7 — break et continue

continue : saute le reste de l'itération actuelle
break    : quitte complètement la boucle
"""

for i in range(1, 10):
    if i == 3:
        print("On saute 3.")
        continue

    if i == 7:
        print("On arrête avant d'afficher 7.")
        break

    print("Valeur affichée :", i)

print("Boucle terminée.")
