"""Calculer des statistiques simples sur une liste."""
notes = [12, 15, 9, 18, 15, 12]

if notes:  # Évite une division par zéro si la liste est vide.
    moyenne = sum(notes) / len(notes)
    print(f"Moyenne : {moyenne:.2f}")
    print("Minimum :", min(notes))
    print("Maximum :", max(notes))
else:
    print("La liste est vide.")
