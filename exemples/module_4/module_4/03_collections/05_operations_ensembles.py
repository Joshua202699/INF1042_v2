"""Comparer deux ensembles avec union, intersection et différence."""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A :", A)
print("B :", B)
print("Union A | B :", A | B)          # Tout ce qui est dans A ou B.
print("Intersection A & B :", A & B)  # Ce qui est dans A ET B.
print("Différence A - B :", A - B)    # Dans A, mais pas dans B.
