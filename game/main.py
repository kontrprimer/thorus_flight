import pygame


def launch():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    r = pygame.Rect(350, 250, 100, 100)
    WHITE = (255, 255, 255)

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
        pygame.draw.rect(screen, WHITE, r)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    print(launch())
