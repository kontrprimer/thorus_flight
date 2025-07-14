from game.framework.vector2d import Vector2D


class Unit:
    def __init__(
        self,
        position: Vector2D,
        screen_size: Vector2D,
        mass: float = 1,
        size: float = 10,
    ):
        self.pos = position
        self.speed = Vector2D(0.0, 0.0)
        self.screen_size = screen_size

        self.size = size
        self.screen_margin_size = Vector2D(size + 1, size + 1)
        self.space_size = screen_size + self.screen_margin_size * 2

        self.mass = mass

    def update(self, keys):
        self.pos = (
            self.pos + self.screen_margin_size + self.speed
        ) % self.space_size - self.screen_margin_size

    def draw(self, screen):
        raise NotImplementedError

    @property
    def exists(self):
        raise NotImplementedError

    def take_damage(self, damage: float):
        raise NotImplementedError


def collide(unit_1: Unit, unit_2: Unit):
    collision_direction = unit_1.pos - unit_2.pos
    unit_1_collision_speed = unit_1.speed.project_on(collision_direction)
    unit_2_collision_speed = unit_2.speed.project_on(collision_direction)
    collision_speed = unit_1_collision_speed + unit_2_collision_speed
    collision_impulse = collision_speed * (unit_1.mass + unit_2.mass)
    collision_damage = collision_impulse.length
    unit_1.take_damage(collision_damage)
    unit_2.take_damage(collision_damage)
    unit_1.speed -= unit_1_collision_speed * 2 - collision_speed
    unit_2.speed -= unit_2_collision_speed * 2 - collision_speed
