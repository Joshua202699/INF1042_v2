"""
Exemple 2 — Boucle de jeu

Chaque image suit la même structure :
1. Lire les événements
2. Mettre à jour l'état du jeu
3. Dessiner
4. Afficher l'image
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60
BACKGROUND = (20, 22, 35)
PLAYER_COLOR = (80, 180, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boucle de jeu")
clock = pygame.time.Clock()

player = pygame.Rect(380, 230, 40, 40)
paused = False
running = True

while running:
    dt = clock.tick(FPS) / 1000

    # 1. Événements ponctuels
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused

    # 2. Mise à jour continue
    if not paused:
        keys = pygame.key.get_pressed()
        speed = 250
        if keys[pygame.K_LEFT]:
            player.x -= speed * dt
        if keys[pygame.K_RIGHT]:
            player.x += speed * dt
        if keys[pygame.K_UP]:
            player.y -= speed * dt
        if keys[pygame.K_DOWN]:
            player.y += speed * dt

    # 3. Dessin
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, PLAYER_COLOR, player)

    # 4. Affichage
    pygame.display.flip()

pygame.quit()
