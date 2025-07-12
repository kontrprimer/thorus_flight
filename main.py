import pygame
from game.player.player import Player, Enemy
from game.framework import Vector2D
from game.controls import KEY_DIRECTIONS

SCREEN = Vector2D(1920, 1080)
BLACK = (0, 0, 0)


def launch():
    pygame.init()
    screen = pygame.display.set_mode(list(SCREEN))
    clock = pygame.time.Clock()
    # Cap the frame rate
    player = Player(SCREEN * 0.5, SCREEN)
    enemies = [
        Enemy(SCREEN * 0.2, target=player),
        Enemy(SCREEN * 0.8, target=player),
    ]

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        accelerate_units(enemies, keys, player)
        update_units(enemies, player)
        draw_screen(enemies, player, screen)
        pygame.display.flip()
        clock.tick(165)

    pygame.quit()


def draw_screen(enemies, player, screen):
    screen.fill(BLACK)
    for enemy in enemies:
        enemy.draw(screen)
    player.draw(screen)


def update_units(enemies, player):
    player.update()
    for enemy in enemies:
        enemy.update(SCREEN)
        enemy.try_attack()


def accelerate_units(enemies, keys, player):
    acceleration = Vector2D(0, 0)
    for key, step in KEY_DIRECTIONS.items():
        if keys[key]:
            acceleration += step
    acceleration = acceleration.limit(1)
    player.accelerate(acceleration)
    for enemy in enemies:
        enemy.accelerate()


if __name__ == "__main__":
    launch()
