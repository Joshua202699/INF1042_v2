"""
Exemple 7 — Collisions avec Rect

colliderect() permet de savoir si deux rectangles se touchent.
"""

import random
import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collisions et score")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

player = pygame.Rect(100, 100, 45, 45)
coin = pygame.Rect(350, 220, 30, 30)
score = 0
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

    if player.colliderect(coin):
        score += 1
        coin.topleft = (random.randint(20, WIDTH - 50), random.randint(60, HEIGHT - 50))

    screen.fill((20, 25, 35))
    pygame.draw.rect(screen, (80, 180, 255), player)
    pygame.draw.rect(screen, (255, 220, 80), coin, border_radius=6)
    texte = font.render(f"Score : {score}", True, (240, 240, 240))
    screen.blit(texte, (20, 20))
    pygame.display.flip()

pygame.quit()
