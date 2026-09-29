"""
Exemple 8 — Ennemi avec poursuite horizontale simple

L'ennemi se déplace vers la position x du joueur.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ennemi qui poursuit")
clock = pygame.time.Clock()

player = pygame.Rect(150, 220, 45, 45)
enemy = pygame.Rect(600, 220, 50, 50)
enemy_speed = 140
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    speed = 260
    if keys[pygame.K_LEFT]: player.x -= speed * dt
    if keys[pygame.K_RIGHT]: player.x += speed * dt
    if keys[pygame.K_UP]: player.y -= speed * dt
    if keys[pygame.K_DOWN]: player.y += speed * dt

    if player.x < enemy.x:
        enemy.x -= enemy_speed * dt
    else:
        enemy.x += enemy_speed * dt

    screen.fill((22, 24, 34))
    pygame.draw.rect(screen, (80, 180, 255), player)
    pygame.draw.rect(screen, (230, 90, 90), enemy)
    pygame.display.flip()

pygame.quit()
