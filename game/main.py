import pygame


def launch():
    pygame.init()
    pygame.display.set_mode((800, 600))

    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
    # ---Закрытие всех модулей Pygame---
    pygame.quit()


if __name__ == "__main__":
    print(launch())
