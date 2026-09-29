"""Indexation positive, négative et modification d'une liste."""
couleurs = ["rouge", "vert", "bleu"]
print("Avant :", couleurs)
print("Index 0 :", couleurs[0])
print("Index -1 :", couleurs[-1])

# Une liste est mutable : on peut remplacer une valeur.
couleurs[1] = "jaune"
print("Après modification :", couleurs)

# Exemple d'erreur à ne pas exécuter :
# print(couleurs[10])  # IndexError
