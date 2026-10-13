"""Modifier indirectement un tuple en passant par une liste."""
t = (1, 2, 3)
print("Tuple original :", t)

liste_temporaire = list(t)
liste_temporaire[1] = 99

t_modifie = tuple(liste_temporaire)
print("Nouveau tuple :", t_modifie)
print("L'original existe toujours :", t)
