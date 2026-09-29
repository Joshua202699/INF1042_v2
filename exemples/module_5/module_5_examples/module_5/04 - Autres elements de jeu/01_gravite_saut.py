"""
Exemple 1 — Gravité et saut

La gravité augmente la vitesse verticale vers le bas.
Le saut applique une vitesse négative vers le haut.
on_ground empêche le double saut infini.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60
FLOOR_Y = 430
GRAVITY = 1800
JUMP_SPEED = -650
MOVE_SPEED = 260

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravité et saut")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

player = pygame.Rect(100, FLOOR_Y - 50, 50, 50)
pos_y = float(player.y)
velocity_y = 0
on_ground = True
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                velocity_y = JUMP_SPEED
                on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= MOVE_SPEED * dt
    if keys[pygame.K_RIGHT]: player.x += MOVE_SPEED * dt

    velocity_y += GRAVITY * dt
    pos_y += velocity_y * dt
    player.y = round(pos_y)

    if player.bottom >= FLOOR_Y:
        player.bottom = FLOOR_Y
        pos_y = float(player.y)
        velocity_y = 0
        on_ground = True

    screen.fill((22, 24, 34))
    pygame.draw.line(screen, (120, 220, 120), (0, FLOOR_Y), (WIDTH, FLOOR_Y), 4)
    pygame.draw.rect(screen, (80, 180, 255), player)
    text = font.render("ESPACE pour sauter | ← → pour bouger", True, (240, 240, 240))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()
