import random

import pygame

from settings import (
    COIN_GREEN,
    COIN_LIFETIME,
    COIN_ORANGE,
    COIN_ORANGE_TIME,
    COIN_RED,
    COIN_RED_TIME,
    COIN_SIZE,
    HEIGHT,
    WIDTH,
)


class Coin:
    """A timed coin that changes colour as it gets closer to disappearing."""

    def __init__(self, rect):
        self.rect = rect
        self.age = 0.0

    @classmethod
    def create_random(cls):
        """Create one coin at a random position on the screen."""
        rect = pygame.Rect(
            random.randint(40, WIDTH - 80),
            random.randint(40, HEIGHT - 80),
            COIN_SIZE,
            COIN_SIZE,
        )
        return cls(rect)

    def update(self, dt):
        """Increase the coin age."""
        self.age += dt

    def is_expired(self):
        """Return True when the coin has been on screen too long."""
        return self.age >= COIN_LIFETIME

    def colour(self):
        """Choose the colour based on the age of the coin."""
        if self.age >= COIN_RED_TIME:
            return COIN_RED

        if self.age >= COIN_ORANGE_TIME:
            return COIN_ORANGE

        return COIN_GREEN

    def draw(self, screen):
        """Draw the coin."""
        pygame.draw.rect(screen, self.colour(), self.rect, border_radius=8)

    def draw_hitbox(self, screen):
        """Draw the collision box for debugging."""
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)

    def current_points(self,COIN_COLLECT_POINTS):
        if self.age >= COIN_RED_TIME:
            return COIN_COLLECT_POINTS[2]

        if self.age >= COIN_ORANGE_TIME:
            return COIN_COLLECT_POINTS[1]

        return COIN_COLLECT_POINTS[0]

