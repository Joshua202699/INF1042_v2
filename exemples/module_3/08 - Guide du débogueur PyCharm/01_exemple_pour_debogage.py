"""
Exemple à utiliser avec le débogueur PyCharm.

Suggestions :
1. Placez un breakpoint sur la ligne `total = addition(total, i)`.
2. Lancez le mode Debug.
3. Utilisez Step Over (F8) pour avancer ligne par ligne.
4. Utilisez Step Into (F7) sur `addition(...)`.
5. Observez `i`, `total`, `a`, `b` et `resultat`.
6. Essayez un breakpoint conditionnel : i > 3.
"""

def addition(a, b):
    resultat = a + b
    return resultat


total = 0

for i in range(1, 6):
    total = addition(total, i)
    print(f"Après i={i}, total={total}")

print("Total final :", total)
