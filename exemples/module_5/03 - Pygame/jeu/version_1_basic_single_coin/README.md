# Version 1 — Projet Pygame de base avec WASD

Cette version contient le projet de départ simple :

- un fichier principal `main.py`
- une classe `Player` dans `player.py`
- déplacement avec les touches `WASD`
- une seule pièce à ramasser
- score qui augmente quand le joueur touche la pièce
- pause avec `Échap`
- affichage des boîtes de collision avec `F1`

## Lancer le projet

```bash
python -m pip install -r requirements.txt
python main.py
```

## Contrôles

- `W` = déplacer vers le haut
- `A` = déplacer vers la gauche
- `S` = déplacer vers le bas
- `D` = déplacer vers la droite
- `Échap` = mettre en pause / reprendre
- `F1` = afficher / cacher les boîtes de collision

## Structure du projet

```text
main.py
player.py
settings.py
requirements.txt
assets/images/player_idle.png
assets/images/player_run_right_1.png
assets/images/player_run_right_2.png
snippets/code_snippets.md
```

## Notes

- L’animation de course vers la gauche est créée en retournant horizontalement les images de course vers la droite dans `player.py`.
- Le déplacement utilise `dt`, donc la vitesse est mesurée en pixels par seconde.
- La boucle principale suit cette structure : événements → mise à jour → dessin → affichage.
