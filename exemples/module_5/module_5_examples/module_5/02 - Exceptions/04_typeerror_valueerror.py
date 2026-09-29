"""
Exemple 4 — TypeError et ValueError

TypeError : le type de donnée ne convient pas à l'opération.
ValueError : le type est accepté, mais la valeur n'est pas valide.
"""

exemples = ["abc", "12", "12.5"]

for texte in exemples:
    try:
        print("Conversion de", repr(texte), "→", int(texte))
    except ValueError:
        print(repr(texte), "n'est pas une chaîne qui représente un entier.")

try:
    resultat = "2" + 2
except TypeError as erreur:
    print("TypeError capturée :", erreur)
