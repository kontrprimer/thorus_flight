import time

from game.framework.vector2d import Vector2D
from game.framework.draw_image import draw_image
from .character import Character


class Enemy(Character):
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        target: Character,
        hp: float = 100,
    ):
        super().__init__(position, screen_size, hp)
        self.target = target
        self.__last_attack_time = 0.0

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed = self.speed + direction.set_length(0.04)

    def try_attack(self):
        if time.time() - self.__last_attack_time < 1:
            return
        from_target_vector = self.pos - self.target.pos
        if from_target_vector.length < 50:
            self.target.take_damage(10)
            self.speed = from_target_vector.set_length(10)
            self.__last_attack_time = time.time()

    def draw_character(self, screen):
        draw_image(
            screen,
            image_path="data/ship_1_a.png",
            pos=self.pos,
            scale_k=0.3,
            rotation_deg=self.speed.angle,
        )
