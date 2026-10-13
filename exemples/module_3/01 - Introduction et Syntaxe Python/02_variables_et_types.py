"""
Exemple 2 — Variables et types de données

Une variable est un nom qui permet de référencer une valeur.
Python détermine automatiquement le type de la valeur assignée.
"""

age = 25
nom = "Boréal"
temperature = 21.5
est_inscrit = True

print("age =", age, "| type :", type(age))
print("nom =", nom, "| type :", type(nom))
print("temperature =", temperature, "| type :", type(temperature))
print("est_inscrit =", est_inscrit, "| type :", type(est_inscrit))

# Le symbole = est l'opérateur d'affectation.
# Il prend la valeur située à droite et l'associe au nom situé à gauche.
age = 26
print("Nouvel âge :", age)
