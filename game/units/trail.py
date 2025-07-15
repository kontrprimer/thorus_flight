import pygame.draw
from .unit_base import Unit
from game.framework.vector2d import Vector2D


class UnitTrail(Unit):
    def __init__(
        self, pos: Vector2D, screen_size: Vector2D, decay_speed: float, **kwargs
    ):
        super().__init__(pos, screen_size, **kwargs)
        self.remained_size = self.size
        self.decay_speed = decay_speed

    def update(self, keys):
        cur_pos = self.pos
        cur_size = self.size
        super().update(keys)
        self.remained_size = max(0.0, self.remained_size - self.decay_speed)
        new_pos = self.pos
        new_size = self.size
        if cur_pos != new_pos:
            print(cur_pos, new_pos, cur_size, new_size)

    def draw(self, screen):
        intensity = self.remained_size / self.size
        pygame.draw.circle(
            screen,
            (180 + 75 * intensity, 100 + 155 * intensity, 255),
            list(self.pos),
            self.remained_size * 0.3,
        )

    @property
    def exists(self):
        return self.remained_size > 0
