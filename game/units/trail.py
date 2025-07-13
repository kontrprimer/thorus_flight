import pygame.draw
from .unit_base import Unit
from game.framework.vector2d import Vector2D


class UnitTrail(Unit):
    def __init__(
        self,
        pos: Vector2D,
        screen_size: Vector2D,
        size: float,
        decay_speed: float,
    ):
        super().__init__(pos, screen_size)
        self.size = size
        self.original_size = size
        self.decay_speed = decay_speed

    def update(self, keys):
        super().update(keys)
        self.size = max(0.0, self.size - self.decay_speed)

    def draw(self, screen):
        intensity = self.size / self.original_size
        pygame.draw.circle(
            screen,
            (180 + 75 * intensity, 100 + 155 * intensity, 255),
            list(self.pos),
            self.size,
        )

    @property
    def exists(self):
        return self.size > 0
