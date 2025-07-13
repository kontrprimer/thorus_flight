import time

from game.framework import Vector2D, draw_svg
from .character import Character


class Enemy(Character):
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        target: Character,
        max_speed: float = 6,
        hp: float = 100,
    ):
        super().__init__(position, screen_size, max_speed, hp)
        self.target = target
        self.__last_attack_time = 0.0

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed = self.speed.set_length(
            self.speed.length - 0.02
        ) + direction.set_length(0.07)
        self.speed = self.speed.limit(max(self.max_speed, self.speed.length))

    def try_attack(self):
        if time.time() - self.__last_attack_time < 1:
            return
        from_target_vector = self.pos - self.target.pos
        if from_target_vector.length < 50:
            self.target.take_damage(10)
            self.speed = from_target_vector.set_length(self.max_speed)
            self.__last_attack_time = time.time()

    def draw_character(self, screen):
        draw_svg(
            screen,
            svg_path="data/ship_1_a.svg",
            pos=self.pos,
            scale_k=0.15,
            rotation_deg=self.speed.angle,
        )
