"""
Exemple 10 — Collectibles avec spritecollide

spritecollide(player, coins, True) retourne les pièces touchées
et les supprime du groupe parce que le troisième argument vaut True.
"""

import random
import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 220, 70), (12, 12), 12)
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH - 40), random.randint(70, HEIGHT - 40)))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collectibles")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

player = pygame.sprite.Sprite()
player.image = pygame.Surface((42, 42))
player.image.fill((80, 180, 255))
player.rect = player.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

coins = pygame.sprite.Group(Coin() for _ in range(10))
score = 0
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    speed = 260
    if keys[pygame.K_LEFT]: player.rect.x -= speed * dt
    if keys[pygame.K_RIGHT]: player.rect.x += speed * dt
    if keys[pygame.K_UP]: player.rect.y -= speed * dt
    if keys[pygame.K_DOWN]: player.rect.y += speed * dt

    hits = pygame.sprite.spritecollide(player, coins, True)
    for coin in hits:
        score += 10

    screen.fill((20, 22, 35))
    coins.draw(screen)
    screen.blit(player.image, player.rect)
    text = font.render(f"Score : {score}", True, (240, 240, 240))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()
