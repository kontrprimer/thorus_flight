import pygame
from game.units.player import Player
from game.units.enemies import Enemy
from game.framework import Vector2D
from game.controls import KEY_DIRECTIONS
import time

SCREEN = Vector2D(1920, 1080)
BLACK = (0, 0, 0)


def launch():
    pygame.init()
    screen = pygame.display.set_mode(list(SCREEN))
    clock = pygame.time.Clock()
    # Cap the frame rate
    player = Player(SCREEN * 0.5, SCREEN)
    enemies = [
        Enemy(Vector2D(-70, -70), target=player, screen_size=SCREEN),
        Enemy(SCREEN + Vector2D(60, 60), target=player, screen_size=SCREEN),
    ]
    frame_start = time.time()
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        accelerate_units(enemies, keys, player)
        update_units(enemies, player)
        draw_screen(enemies, player, screen)

        frame_end = time.time()
        draw_debug_text(
            screen,
            f"Estimated FPS: {round(1 / (frame_end - frame_start))}",
            list(SCREEN),
        )
        pygame.display.flip()
        clock.tick(165)
        frame_start = frame_end

    pygame.quit()


def draw_screen(enemies, player, screen):
    screen.fill(BLACK)
    for enemy in enemies:
        enemy.draw(screen)
    player.draw(screen)


def update_units(enemies, player):
    player.update()
    for enemy in enemies:
        enemy.update()
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


def draw_debug_text(
    screen, text, screen_size, font_size=24, color=(255, 255, 255), margin=10
):
    font = pygame.font.Font(None, font_size)
    rendered_text = font.render(text, True, color)

    # Place text in top-right area but align left edge
    x = screen_size[0] - 200  # Fixed distance from the right edge
    y = margin

    # Optional: Draw background box behind the text for visibility
    text_rect = rendered_text.get_rect(topleft=(x, y))
    bg_rect = text_rect.inflate(6, 4)
    pygame.draw.rect(screen, (30, 30, 30), bg_rect)

    screen.blit(rendered_text, text_rect)


if __name__ == "__main__":
    launch()
