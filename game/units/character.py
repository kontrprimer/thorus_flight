from game.framework import Vector2D
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

    def update(self):
        self.update_trails()
        super().update()

    def update_trails(self):
        for trail in self.__trails:
            trail.update()
        self.__trails = [trail for trail in self.__trails if trail.exists]
        self.__trails.append(
            UnitTrail(self.pos, self.screen_size, size=12, decay_speed=0.2)
        )

    def take_damage(self, damage: float):
        self.current_hp = max(self.current_hp - damage, 0)

    def draw(self, screen):
        self.draw_trails(screen)
        self.draw_character(screen)

    def draw_character(self, screen):
        raise NotImplementedError

    def draw_trails(self, screen):
        for trail in self.__trails:
            trail.draw(screen)
