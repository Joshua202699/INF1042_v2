from pathlib import Path

import pygame

from settings import PLAYER_SIZE, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    """A simple animated player controlled with WASD."""

    def __init__(self, start_pos, image_folder):
        super().__init__()
        self.image_folder = Path(image_folder)
        self.speed = PLAYER_SPEED
        self.pos = pygame.math.Vector2(start_pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.facing = "right"
        self.frame_index = 0
        self.animation_timer = 0.0
        self.animation_speed = 0.14  # seconds per animation frame

        self.idle_image = self._load_image("player_idle.png")
        self.run_right_frames = [
            self._load_image("player_run_right_1.png"),
            self._load_image("player_run_right_2.png"),
        ]
        self.run_left_frames = [pygame.transform.flip(frame, True, False) for frame in self.run_right_frames]

        self.image = self.idle_image
        self.rect = self.image.get_rect(center=self.pos)

    def _load_image(self, filename):
        """Load a transparent PNG and scale it to the player size."""
        path = self.image_folder / filename
        image = pygame.image.load(str(path)).convert_alpha()
        return pygame.transform.smoothscale(image, (PLAYER_SIZE, PLAYER_SIZE))

    def update(self, keys, dt, screen_rect):
        """Read WASD input, move the player, and update animation."""
        direction = pygame.math.Vector2(0, 0)

        if keys[pygame.K_a]:
            direction.x -= 1
            self.facing = "left"
        if keys[pygame.K_d]:
            direction.x += 1
            self.facing = "right"
        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_s]:
            direction.y += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.velocity = direction * self.speed
        self.pos += self.velocity * dt

        self.rect.center = (round(self.pos.x), round(self.pos.y))
        self.rect.clamp_ip(screen_rect)
        self.pos.update(self.rect.center)

        self._animate(dt)

    def _animate(self, dt):
        """Switch between walking frames while moving."""
        moving = self.velocity.length_squared() > 0

        if not moving:
            self.image = self.idle_image
            self.frame_index = 0
            self.animation_timer = 0.0
            return

        frames = self.run_left_frames if self.facing == "left" else self.run_right_frames
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0.0
            self.frame_index = (self.frame_index + 1) % len(frames)

        self.image = frames[self.frame_index]

    def draw_hitbox(self, surface):
        """Optional debug helper."""
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 1)
