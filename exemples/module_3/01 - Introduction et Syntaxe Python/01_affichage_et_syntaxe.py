"""
Exemple 1 — Affichage et syntaxe de base

Objectifs :
- utiliser print()
- observer la sensibilité à la casse
- comprendre l'importance de l'indentation
"""

print("Bonjour Collège Boréal !")

# Une condition crée un bloc de code.
# Les instructions qui appartiennent au bloc sont indentées.
if True:
    print("Cette ligne est indentée de 4 espaces.")
    print("Elle fait donc partie du bloc if.")

print("Cette ligne n'est plus dans le bloc if.")

# Python est sensible à la casse :
nom = "Alex"
print(nom)

# print(Nom)  # Décommenter provoquerait NameError :
#             # 'Nom' et 'nom' sont deux identificateurs différents.
