"""
Exemple 1 — Fonctions et principe DRY

DRY = Don't Repeat Yourself.
Une fonction permet de regrouper une tâche sous un nom
et de la réutiliser plusieurs fois.
"""

def afficher_table(n):
    print(f"Table de {n}")
    for i in range(0, 11):
        print(n, "×", i, "=", n * i)


afficher_table(1)
print()
afficher_table(2)
