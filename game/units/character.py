import datetime

from game.framework.vector2d import Vector2D
from game.units.unit_base import Unit
from game.units.trail import UnitTrail


class Character(Unit):
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        max_speed: float = 50,
        hp: float = 100,
    ):
        super().__init__(position, screen_size)
        self.max_speed = max_speed
        self.max_hp = hp
        self.current_hp = hp
        self.__trails: list[UnitTrail] = []

    @property
    def exists(self):
        return self.current_hp > 0

    def update(self, keys):
        self.update_trails(keys)
        super().update(keys)

    def update_trails(self, keys):
        for trail in self.__trails:
            trail.update(keys)
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(
            UnitTrail(self.pos, self.screen_size, size=12, decay_speed=0.2)
        )

    def take_damage(self, damage: float):
        self.current_hp = max(self.current_hp - damage, 0)
        print(
            datetime.datetime.now(),
            f"Unit {type(self).__name__} got hit for {damage} damage. New hp: {self.current_hp}",
        )

    def draw(self, screen):
        self.draw_trails(screen)
        self.draw_character(screen)

    def draw_character(self, screen):
        raise NotImplementedError

    def draw_trails(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
