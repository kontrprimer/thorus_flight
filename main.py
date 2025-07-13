import pygame

from game.units.player import Player
from game.framework.vector2d import Vector2D
from game.scene import Battle01
import time

SCREEN = Vector2D(1920, 1080)


def launch():
    pygame.init()
    screen = pygame.display.set_mode(list(SCREEN))
    clock = pygame.time.Clock()
    player = Player(SCREEN * 0.5, SCREEN)
    scene = Battle01(player, SCREEN)
    frame_start = time.time()
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        scene.update()
        scene.draw(screen)
        if scene.finished():
            scene = scene.exit_scene()

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
