"""Utiliser une liste 2D : une liste contenant d'autres listes."""
grille = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Deux index : [ligne][colonne].
print("Élément ligne 1, colonne 2 :", grille[1][2])  # 6

# Calculer la somme de chaque ligne.
sommes = []
for ligne in grille:
    sommes.append(sum(ligne))

print("Sommes des lignes :", sommes)
