import pygame


def launch():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    r = pygame.Rect(50, 50, 100, 200)
    pygame.draw.rect(screen, (255, 0, 0), r, 5)

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
    # ---Закрытие всех модулей Pygame---
    pygame.quit()


if __name__ == "__main__":
    print(launch())
