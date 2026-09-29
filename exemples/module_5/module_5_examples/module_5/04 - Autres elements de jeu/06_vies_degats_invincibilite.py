"""
Exemple 6 — Vies, dégâts et invincibilité temporaire

Après une collision, le joueur devient invincible brièvement
pour éviter de perdre toutes ses vies instantanément.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60
INVINCIBLE_TIME = 2.0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vies et invincibilité")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

player = pygame.Rect(100, 220, 45, 45)
enemy = pygame.Rect(400, 210, 70, 70)
lives = 3
invincible = False
invincible_timer = 0
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

    if invincible:
        invincible_timer -= dt
        if invincible_timer <= 0:
            invincible = False

    if player.colliderect(enemy) and not invincible:
        lives -= 1
        invincible = True
        invincible_timer = INVINCIBLE_TIME

    screen.fill((22, 24, 34))
    pygame.draw.rect(screen, (230, 80, 80), enemy)
    if not invincible or int(invincible_timer * 10) % 2 == 0:
        pygame.draw.rect(screen, (80, 180, 255), player)
    text = font.render(f"Vies : {lives} | Invincible : {invincible}", True, (240, 240, 240))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()
