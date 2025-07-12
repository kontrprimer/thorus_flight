import pygame.draw

from game.framework import Vector2D, draw_svg


class Player:
    def __init__(self, position: Vector2D):
        self.pos = position
        self.speed = Vector2D(0.1, 5.1)
        self.max_speed = 50
        self.__trails: list[UnitTrail] = []

    def update(self, clip: Vector2D):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self, direction: Vector2D):
        self.speed += direction * 0.08
        self.speed = self.speed.limit(self.max_speed)

    def draw(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
        draw_svg(
            screen,
            svg_path="data/ship_2_a.svg",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,  # Rotation angle in degrees
        )


class Enemy:
    def __init__(self, position: Vector2D, target: Player):
        self.pos = position
        self.target = target
        self.speed = Vector2D(0.1, 0.1)
        self.max_speed = 10
        self.__trails: list[UnitTrail] = []

    def update(self, clip: Vector2D):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed += direction.set_length(0.5)
        self.speed = self.speed.limit(self.max_speed)

    def draw(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
        draw_svg(
            screen,
            svg_path="data/ship_1_a.svg",  # Replace with your SVG file path
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,  # Rotation angle in degrees
        )


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
