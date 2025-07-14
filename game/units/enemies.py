import time

from game.framework.draw_image import draw_image
from .character import Character


class Enemy(Character):
    def __init__(self, target: Character, **kwargs):
        super().__init__(**kwargs)
        self.target = target
        self.__last_attack_time = 0.0

    def accelerate(self):
        direction = self.target.pos - self.pos
        self.speed = self.speed + direction.set_length(0.04) / self.mass

    def try_attack(self):
        if time.time() - self.__last_attack_time < 1:
            return
        from_target_vector = self.pos - self.target.pos
        if from_target_vector.length <= self.size + self.target.size:
            damage_factor = 1.75
            collision_vector = self.speed.project_on(from_target_vector)
            collision_impulse_vector = collision_vector * self.mass
            self.target.take_damage(collision_impulse_vector.length * damage_factor)
            self.speed -= collision_vector * 2
            self.__last_attack_time = time.time()

    def draw_character(self, screen):
        draw_image(
            screen,
            image_path="data/ship_1_a.png",
            pos=self.pos,
            scale_k=0.3,
            rotation_deg=self.speed.angle,
        )
