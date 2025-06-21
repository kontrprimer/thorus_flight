import pygame


def launch(true=True):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    player_position = pygame.Rect(150, 250, 50, 50)
    r = pygame.Rect(350, 250, 100, 100)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    run = true
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.KEYDOWN:
                pygame.draw.rect(screen, BLACK, player_position)
                act(e.key)
                player_position = new_position(player_position, act(e.key))
                print(player_position)
        pygame.draw.rect(screen, WHITE, r)
        pygame.draw.rect(screen, RED, player_position)
        pygame.display.flip()
    pygame.quit()


def new_position(position, command):
    if command == "up":
        position.move_ip(0, -50)
    elif command == "down":
        position.move_ip(0, 50)
    elif command == "left":
        position.move_ip(-50, 0)
    elif command == "right":
        position.move_ip(50, 0)
    return position


def act(key):
    if key == pygame.K_UP:
        print("up")
        return "up"
    elif key == pygame.K_DOWN:
        print("down")
        return "down"
    elif key == pygame.K_LEFT:
        print("left")
        return "left"
    elif key == pygame.K_RIGHT:
        print("right")
        return "right"
    elif key == pygame.K_ESCAPE:
        exit(0)
    return None


if __name__ == "__main__":
    print(launch())
