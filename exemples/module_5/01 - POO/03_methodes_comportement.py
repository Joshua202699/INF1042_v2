"""
Exemple 3 — Méthodes

Une méthode est une fonction définie DANS une classe.
Elle représente souvent un comportement de l'objet.
"""


class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."

    def anniversaire(self):
        self.age += 1
        return f"Bon anniversaire {self.nom} ! Tu as maintenant {self.age} ans."


p = Personne("Noah", 15)

print(p.se_presenter())
print(p.anniversaire())
print(p.se_presenter())
