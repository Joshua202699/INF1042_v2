"""Supprimer les doublons d'une liste avec set()."""
nombres = [1, 2, 2, 3, 3, 3, 4]
uniques = set(nombres)
print("Original :", nombres)
print("Sans doublons :", uniques)

# Si on reconvertit en liste, l'ordre original n'est pas garanti.
liste_unique = list(uniques)
print("Reconversi en liste :", liste_unique)
