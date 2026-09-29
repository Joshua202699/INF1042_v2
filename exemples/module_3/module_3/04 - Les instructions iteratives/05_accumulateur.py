"""
Exemple 5 — Accumulateur

Un accumulateur est une variable dont la valeur est modifiée
à répétition pour construire progressivement un résultat.
"""

somme = 0

while somme < 20:
    print(f"Somme avant ajout : {somme}")
    somme += 5

print(f"Valeur finale : {somme}")
