"""
Exemple 5 — Modulo (%)

Le modulo donne le RESTE d'une division entière.
Il est très utile pour tester si un nombre est pair ou impair.
"""

print("7 % 2 =", 7 % 2)
print("8 % 2 =", 8 % 2)
print("14 % 5 =", 14 % 5)

nombre = int(input("Entrez un nombre entier : "))

if nombre % 2 == 0:
    print(nombre, "est pair.")
else:
    print(nombre, "est impair.")
