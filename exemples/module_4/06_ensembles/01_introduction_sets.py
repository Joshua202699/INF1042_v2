"""Créer et modifier un ensemble (set)."""
couleurs = {"rouge", "vert", "bleu"}
print("Départ :", couleurs)

couleurs.add("jaune")
print("Après add :", couleurs)

couleurs.remove("vert")
print("Après remove :", couleurs)

# Un set n'utilise pas d'index : couleurs[0] est invalide.
