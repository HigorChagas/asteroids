import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            new_angle = random.uniform(20, 50)

            small_one = pygame.math.Vector2.rotate(self.velocity, new_angle)
            small_two = pygame.math.Vector2.rotate(self.velocity, -new_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = small_one * 1.2

            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_two.velocity = small_two * 1.2
