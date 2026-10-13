"""
Exemple 3 — else et finally

else s'exécute seulement si le try réussit.
finally s'exécute toujours, qu'il y ait une erreur ou non.
"""

texte = input("Entrez votre âge : ")

try:
    age = int(texte)
except ValueError:
    print("Veuillez entrer un nombre.")
else:
    print(f"Âge valide : {age}")
    print("Le bloc else s'exécute seulement s'il n'y a pas eu d'erreur.")
finally:
    print("Fin de la vérification.")
    print("Le bloc finally s'exécute toujours.")
