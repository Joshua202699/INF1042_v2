"""
Exemple 2 — int()

int() transforme une représentation valide d'un entier en int.
Sur un float, int() tronque vers zéro.
"""

age_texte = "42"
age = int(age_texte)
print(age + 8)

prix = 19.99
print("int(19.99) =", int(prix))
print("int(-3.9) =", int(-3.9))

binaire = "1010"
valeur = int(binaire, 2)
print('int("1010", 2) =', valeur)

# Ces conversions produiraient ValueError :
# int("12.5")
# int("abc")
