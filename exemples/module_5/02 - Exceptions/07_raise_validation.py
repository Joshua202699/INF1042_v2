"""
Exemple 7 — raise

raise permet de déclencher volontairement une exception
quand une règle importante est violée.
"""


def definir_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    return age


for valeur in [16, 0, -4]:
    try:
        print("Âge validé :", definir_age(valeur))
    except ValueError as erreur:
        print("Erreur :", erreur)
