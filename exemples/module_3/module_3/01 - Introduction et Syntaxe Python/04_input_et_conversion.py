"""
Exemple 4 — input() et conversion

input() retourne TOUJOURS une chaîne de caractères (str).
Pour calculer avec une saisie numérique, il faut la convertir.
"""

age_texte = input("Entrez votre âge : ")

print("Valeur reçue :", age_texte)
print("Type reçu :", type(age_texte))

age = int(age_texte)

print("Après int() :", age)
print("Nouveau type :", type(age))
print("Dans 5 ans, vous aurez", age + 5, "ans.")
