"""
Exemple 9 — Plateforme mobile

La plateforme avance entre deux limites, puis inverse sa vitesse.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plateforme mobile")
clock = pygame.time.Clock()

platform = pygame.Rect(200, 320, 180, 24)
platform_speed = 180
min_x = 120
max_x = 680
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    platform.x += platform_speed * dt
    if platform.left < min_x or platform.right > max_x:
        platform_speed *= -1

    screen.fill((22, 24, 34))
    pygame.draw.line(screen, (80, 80, 100), (min_x, 360), (max_x, 360), 2)
    pygame.draw.rect(screen, (120, 220, 120), platform)
    pygame.display.flip()

pygame.quit()
