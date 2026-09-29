"""
Exemple 4 — Boucle while

Une boucle while comporte généralement :
1. une initialisation
2. une condition
3. une mise à jour
"""

# 1. Initialisation
compteur = 1

# 2. Condition
while compteur <= 5:
    print(f"Compteur : {compteur}")

    # 3. Mise à jour
    compteur += 1

print("Valeur finale :", compteur)
