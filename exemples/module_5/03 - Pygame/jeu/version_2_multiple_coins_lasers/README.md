# Version 2 — Projet Pygame avec plusieurs pièces et lasers

Cette version ajoute des éléments au projet de départ :

- plusieurs pièces stockées dans une liste `coins`
- une liste `pending_coin_spawns` pour attendre 2 secondes avant de remplacer une pièce ramassée
- une liste `lasers` pour les lasers tirés par le joueur
- `Espace` pour tirer un laser
- chaque laser est dessiné comme une ligne de 30 pixels
- les lasers se déplacent à 2 fois la vitesse du joueur

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
- `Espace` = tirer un laser
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

## Fonctionnement des pièces

Les pièces sont stockées dans une liste :

```python
coins = [new_coin_rect() for _ in range(INITIAL_COIN_COUNT)]
```

Quand le joueur touche une pièce, elle est retirée de la liste, le score augmente, puis un minuteur de 2 secondes est ajouté :

```python
coins.remove(coin)
pending_coin_spawns.append(COIN_RESPAWN_DELAY)
```

Quand le minuteur arrive à 0, une nouvelle pièce est ajoutée.

## Fonctionnement des lasers

Le joueur garde en mémoire sa dernière direction de déplacement dans `aim_direction`.

Quand le joueur appuie sur `Espace`, un laser est ajouté à la liste `lasers` :

```python
lasers.append(create_laser(player))
```

Chaque laser avance dans sa direction à 2 fois la vitesse du joueur :

```python
laser_speed = player.speed * LASER_SPEED_MULTIPLIER
```
