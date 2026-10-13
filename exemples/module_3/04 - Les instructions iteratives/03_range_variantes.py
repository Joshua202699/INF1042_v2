"""
Exemple 3 — Les formes de range()

range(stop)
range(start, stop)
range(start, stop, step)
"""

print("range(5) :")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 7) :")
for i in range(2, 7):
    print(i, end=" ")
print()

print("range(2, 10, 2) :")
for i in range(2, 10, 2):
    print(i, end=" ")
print()

print("Décompte range(5, 0, -1) :")
for i in range(5, 0, -1):
    print(i, end=" ")
print()
