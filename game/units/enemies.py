import time

from game.framework import Vector2D, draw_svg
from game.units.player import Player
from game.units.trail import UnitTrail


class Enemy:
    def __init__(self, position: Vector2D, target: Player):
        self.pos = position
        self.target = target
        self.speed = Vector2D(0.1, 0.1)
        self.max_speed = 6
        self.__trails: list[UnitTrail] = []
        self.__last_attack_time = 0.0

    def update(self, clip: Vector2D):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(UnitTrail(self.pos, size=12, decay_speed=0.2))
        self.pos = (self.pos + self.speed) % clip

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed = self.speed.set_length(
            self.speed.length - 0.02
        ) + direction.set_length(0.07)
        self.speed = self.speed.limit(self.max_speed)

    def try_attack(self):
        if time.time() - self.__last_attack_time < 1:
            return
        from_target_vector = self.pos - self.target.pos
        if from_target_vector.length < 50:
            self.target.get_damage(10)
            self.speed = from_target_vector.set_length(self.max_speed)
            self.__last_attack_time = time.time()

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
