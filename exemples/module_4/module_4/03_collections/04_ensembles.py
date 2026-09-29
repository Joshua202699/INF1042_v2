"""Exemple de set : supprimer les doublons et tester l'appartenance."""

nombres = [1, 2, 2, 3, 3, 3, 4]
uniques = set(nombres)

print("Liste originale :", nombres)
print("Valeurs uniques :", uniques)

# L'opérateur in vérifie si une valeur est présente.
print("Est-ce que 3 est présent?", 3 in uniques)
