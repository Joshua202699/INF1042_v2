"""
Exemple 5 — Pourquoi l'ordre des conditions compte

On teste généralement les conditions les plus exigeantes en premier.
"""

note = int(input("Note sur 100 : "))

if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
elif note >= 60:
    print("Réussite")
else:
    print("À améliorer")

# Si on testait note >= 60 en premier,
# une note de 95 entrerait immédiatement dans ce premier bloc.
