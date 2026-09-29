"""Découper une liste avec [début:fin:pas]."""
nombres = list(range(10))
print("Original :", nombres)
print("Index 0 à 2 :", nombres[0:3])  # fin=3 est exclue
print("Un élément sur deux :", nombres[::2])
print("Liste inversée :", nombres[::-1])
