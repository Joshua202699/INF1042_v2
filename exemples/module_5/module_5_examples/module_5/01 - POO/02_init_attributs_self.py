"""
Exemple 2 — __init__, attributs et self

__init__ est appelée automatiquement quand on crée un objet.
self représente l'objet en train d'être construit ou utilisé.
Un attribut est une donnée attachée à un objet : self.nom, self.age, etc.
"""


class Personne:
    def __init__(self, nom, age):
        self.nom = nom      # attribut de l'objet
        self.age = age      # autre attribut de l'objet


p = Personne("Maya", 16)

print("Nom :", p.nom)
print("Âge :", p.age)

# On peut créer plusieurs objets avec des valeurs différentes.
autre = Personne("Noah", 15)
print("Autre personne :", autre.nom, autre.age)
