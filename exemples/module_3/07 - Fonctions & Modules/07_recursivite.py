"""
Exemple 7 — Récursivité

Une fonction récursive s'appelle elle-même.
Elle doit avoir un cas de base qui arrête les appels.
"""

def factorielle(n):
    print("Appel de factorielle(", n, ")", sep="")

    if n <= 1:
        print("Cas de base atteint.")
        return 1

    resultat = n * factorielle(n - 1)
    print(f"Retour pour n={n} : {resultat}")
    return resultat


print("Résultat final :", factorielle(5))
