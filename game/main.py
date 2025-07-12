import pygame

from game.player.player import Player
from game.framework import Vector2D
from game.controls import KEY_DIRECTIONS

SCREEN = Vector2D(1920, 1080)
BLACK = (0, 0, 0)


def launch():
    pygame.init()
    screen = pygame.display.set_mode(list(SCREEN))
    clock = pygame.time.Clock()
    player = Player(Vector2D(100, 100))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        acceleration = Vector2D(0, 0)
        for key, step in KEY_DIRECTIONS.items():
            if keys[key]:
                acceleration += step
        acceleration = acceleration.limit(1)
        player.accelerate(acceleration)
        player.move(SCREEN)
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()

    # Cap the frame rate
    clock.tick(60)


if __name__ == "__main__":
    print(launch())
