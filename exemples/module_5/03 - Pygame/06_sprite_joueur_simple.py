"""
Exemple 6 — Sprite simple

Un sprite regroupe :
- une image ou surface à dessiner
- un rect pour la position et les collisions
- une méthode update() pour la logique
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60
PLAYER_SPEED = 260


class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.image.fill((70, 170, 255))
        self.rect = self.image.get_rect(center=start_pos)
        self.pos = pygame.Vector2(self.rect.center)

    def update(self, keys, dt):
        direction = pygame.Vector2(0, 0)
        if keys[pygame.K_a]: direction.x -= 1
        if keys[pygame.K_d]: direction.x += 1
        if keys[pygame.K_w]: direction.y -= 1
        if keys[pygame.K_s]: direction.y += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.pos += direction * PLAYER_SPEED * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite joueur")
clock = pygame.time.Clock()

player = Player((WIDTH // 2, HEIGHT // 2))
all_sprites = pygame.sprite.Group(player)
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    all_sprites.update(keys, dt)

    screen.fill((25, 25, 35))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
