"""
Exemple 6 — Éviter une boucle infinie

La condition d'une boucle while doit finir par devenir False.
"""

# Version incorrecte — laissée en commentaire :
#
# x = 0
# while x < 5:
#     print(x)
#     # x ne change jamais -> boucle infinie

# Version correcte :
x = 0

while x < 5:
    print(x)
    x += 1

print("La boucle s'est arrêtée parce que x vaut maintenant", x)
