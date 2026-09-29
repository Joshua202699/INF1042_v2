"""Utiliser count() et index() avec un tuple."""
t = (1, 2, 2, 2, 3)
print("Tuple :", t)
print("Nombre de 2 :", t.count(2))
print("Position du premier 3 :", t.index(3))

# index() produit ValueError si la valeur n'existe pas.
# print(t.index(99))
