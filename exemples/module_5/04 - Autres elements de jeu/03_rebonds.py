"""
Exemple 3 — Rebonds

Quand l'objet touche un bord, on inverse la vitesse sur l'axe concerné.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rebonds")
clock = pygame.time.Clock()

ball = pygame.Rect(100, 100, 35, 35)
vx = 260
vy = 180
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.x += vx * dt
    ball.y += vy * dt

    if ball.left <= 0 or ball.right >= WIDTH:
        vx *= -1
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        vy *= -1

    screen.fill((20, 22, 35))
    pygame.draw.ellipse(screen, (255, 190, 80), ball)
    pygame.display.flip()

pygame.quit()
