"""
Exemple 5 — Petit exercice de synthèse

On combine :
- int et float
- conversions
- division
- modulo
"""

age = 17
taille = 1.75

print("age :", age, type(age))
print("taille :", taille, type(taille))

entier = 10
decimal = float(entier)
print("10 converti en float :", decimal)

valeur = 15.9
tronquee = int(valeur)
print("15.9 converti en int :", tronquee)

print("15 / 4  =", 15 / 4)
print("15 // 4 =", 15 // 4)
print("15 % 4  =", 15 % 4)

print("Relation vérifiée ?",
      15 == (15 // 4) * 4 + (15 % 4))
