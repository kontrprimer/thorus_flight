import time

from game.framework.draw_image import draw_image
from .character import Character


class Enemy(Character):
    def __init__(self, target: Character, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.__last_attack_time = 0.0

    def accelerate(self):
        pos_delta = self.target.pos - self.pos
        speed_delta = self.target.speed - self.speed
        speed_correction = speed_delta - speed_delta.project_on(pos_delta)
        if time.time() - self.__last_attack_time < 0.5:
            pos_delta = pos_delta * -1
        if speed_correction.length > 0.04:
            acceleration = speed_correction
        else:
            acceleration = pos_delta + speed_correction
        self.speed = self.speed + acceleration.set_length(0.05) / self.mass

    def try_attack(self):
        pass

    def draw_character(self, screen):
        draw_image(
            screen,
            image_path="data/ship_1_a.png",
            pos=self.pos,
            scale_k=self.size / 128 * 1.3,
            rotation_deg=self.speed.angle(degrees=True) + 90,
        )
