"""Exemple de dictionnaire : accéder, modifier et ajouter des données."""

eleve = {"nom": "Ava", "note": 92, "niveau": 12}

print("Nom :", eleve["nom"])

# Une affectation à une clé existante modifie sa valeur.
eleve["note"] = 95

# Une affectation à une nouvelle clé crée une nouvelle paire clé-valeur.
eleve["ville"] = "Sudbury"

print("Dictionnaire mis à jour :", eleve)
