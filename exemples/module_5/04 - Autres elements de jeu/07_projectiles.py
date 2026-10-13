"""
Exemple 7 — Projectiles

Un projectile est un sprite qui avance puis se supprime avec kill()
quand il quitte l'écran.
"""

import pygame

WIDTH, HEIGHT = 800, 500
FPS = 60


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((16, 6))
        self.image.fill((255, 230, 80))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 600

    def update(self, dt):
        self.rect.x += self.speed * dt
        if self.rect.left > WIDTH:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectiles")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

player = pygame.Rect(80, 230, 40, 40)
projectiles = pygame.sprite.Group()
running = True

while running:
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            projectiles.add(Projectile(player.right, player.centery))

    projectiles.update(dt)

    screen.fill((20, 22, 35))
    pygame.draw.rect(screen, (80, 180, 255), player)
    projectiles.draw(screen)
    text = font.render("ESPACE pour tirer", True, (240, 240, 240))
    screen.blit(text, (20, 20))
    pygame.display.flip()

pygame.quit()
