"""
Exemple 3 — Identificateurs et mots-clés

Un identificateur est le nom donné à une variable, une fonction, etc.
Un mot-clé est un mot réservé par la syntaxe de Python.
"""

# Noms valides :
nom_complet = "Marie Tremblay"
age_etudiant = 17
note_1 = 88

print(nom_complet, age_etudiant, note_1)

# Noms invalides — ils restent en commentaires pour que ce fichier fonctionne :
# 1er_nom = "Erreur"      # ne peut pas commencer par un chiffre
# nom-complet = "Erreur"  # le tiret '-' est interprété comme une soustraction
# class = "Erreur"        # 'class' est un mot-clé Python

# Convention recommandée : snake_case
nombre_de_vies = 3
print("Nombre de vies :", nombre_de_vies)
