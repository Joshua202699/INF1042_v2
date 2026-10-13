"""Créer un tuple et comprendre l'immutabilité."""
point = (10, 20)
print("Tuple :", point)
print("Type :", type(point))
print("Premier élément :", point[0])

# Un tuple est immuable : on ne peut pas remplacer un élément.
# Décommente la ligne suivante pour observer la TypeError :
# point[0] = 15
