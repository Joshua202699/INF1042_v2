"""Parcourir les clés, valeurs et paires d'un dictionnaire."""
notes = {"math": 82, "science": 91, "histoire": 88}

print("Clés :")
for matiere in notes.keys():
    print("-", matiere)

print("\nValeurs :")
for note in notes.values():
    print("-", note)

print("\nPaires clé-valeur :")
for matiere, note in notes.items():
    print(f"{matiere} : {note}")
