"""Modifier une clé existante et ajouter une nouvelle clé."""
notes = {"math": 78, "science": 91}
print("Départ :", notes)

notes["math"] = 82       # La clé existe : modification.
notes["histoire"] = 88   # La clé n'existe pas : ajout.
print("Après changements :", notes)

# Lire une clé absente avec [] produit KeyError.
# print(notes["anglais"])

# get() permet une lecture plus sécuritaire.
print("Anglais :", notes.get("anglais", "Aucune note"))
