import pygame.draw


class UnitTrail:
    def __init__(self, pos, size, decay_speed):
        self.pos = pos
        self.size = size
        self.original_size = size
        self.decay_speed = decay_speed

    def update(self):
        self.size = max(0, self.size - self.decay_speed)

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
