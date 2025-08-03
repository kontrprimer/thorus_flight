from game.units.unit_base import Unit


def process_collisions(units: list[Unit]):
    for unit_1 in units:
        for unit_2 in units:
            if unit_1 is unit_2:
                continue
            if unit_1.size + unit_2.size >= (unit_2.pos - unit_1.pos).length:
                collide(unit_1, unit_2)


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

    center = (unit_1.pos + unit_2.pos) * 0.5
    min_distance_from_center = (unit_1.size + unit_2.size) * 0.5 + 0.001

    unit_1.pos = center + (unit_1.pos - center).set_length(min_distance_from_center)
    unit_2.pos = center + (unit_2.pos - center).set_length(min_distance_from_center)
