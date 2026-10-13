"""
Exemple 11 — Niveaux et difficulté progressive

Quand le score atteint l'objectif du niveau,
on augmente un ou deux paramètres seulement.
"""

level = 1
score = 0
level_goal = 50
enemy_speed = 120
spawn_rate = 2.0  # secondes entre les apparitions

print("Simulation de progression")
print("-------------------------")

for points in [10, 15, 20, 15, 30, 50]:
    score += points
    print(f"Score : {score} / objectif {level_goal}")

    if score >= level_goal:
        level += 1
        level_goal += 50
        enemy_speed += 40
        spawn_rate = max(0.5, spawn_rate - 0.2)

        print("NIVEAU SUPÉRIEUR !")
        print("Niveau :", level)
        print("Vitesse ennemis :", enemy_speed)
        print("Temps entre apparitions :", spawn_rate)
        print()
