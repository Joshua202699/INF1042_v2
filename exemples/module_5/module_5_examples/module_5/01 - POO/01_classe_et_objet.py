"""
Exemple 1 — Classe et objet

Objectif : comprendre les deux mots les plus importants de la POO.

Classe : un plan, un modèle, une recette.
Objet  : un exemplaire concret créé à partir de la classe.
"""


class Personne:
    """Classe vide pour représenter une personne."""
    pass


# p1 et p2 sont deux objets différents, créés avec le même plan.
p1 = Personne()
p2 = Personne()

print("Type de p1 :", type(p1))
print("p1 est-il le même objet que p2 ?", p1 is p2)
print("Même classe, mais deux objets différents.")


def a_faire_plus_tard():
    # pass signifie : « je laisse ce bloc vide pour l'instant ».
    # Python exige au moins une instruction dans un bloc.
    pass
