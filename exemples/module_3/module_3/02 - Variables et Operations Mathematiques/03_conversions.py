"""
Exemple 3 — Conversion de types

int() convertit vers un entier.
float() convertit vers un nombre décimal.
"""

a = 5
b = float(a)
print(a, "->", b, "|", type(b))

x = 7.8
y = int(x)
print(x, "->", y, "| int() tronque vers zéro")

texte_prix = "19.99"
prix_num = float(texte_prix)

print("Texte :", texte_prix, "|", type(texte_prix))
print("Nombre :", prix_num, "|", type(prix_num))
print("Deux articles coûtent :", prix_num * 2)

print("round(7.8) =", round(7.8))
print("int(7.8) =", int(7.8))
