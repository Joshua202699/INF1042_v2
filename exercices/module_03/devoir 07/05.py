import math
def aire_cercle(diametre):
    rayon = diametre / 2
    aire = math.pi * rayon**2
    return aire
print(aire_cercle(10))