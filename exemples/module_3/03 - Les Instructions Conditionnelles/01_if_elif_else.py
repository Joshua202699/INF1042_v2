"""
Exemple 1 — if / elif / else

Python teste les conditions de haut en bas.
Dans une chaîne if/elif/else, un seul bloc est exécuté.
"""

note = int(input("Entrez votre note : "))

if note >= 60:
    print("Réussite")
elif note >= 50:
    print("Rattrapage")
else:
    print("Échec")
