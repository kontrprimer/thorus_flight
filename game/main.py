import pygame


def launch(true=True):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    texture = pygame.image.load("texture_player3.jpg")
    texture_potato = pygame.image.load("potato.jpg")
    player_position = pygame.Rect(150, 250, 50, 50)
    potato_position = pygame.Rect(250, 350, 50, 50)
    r = pygame.Rect(350, 250, 100, 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    run = true
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            elif e.type == pygame.KEYDOWN:
                pygame.draw.rect(screen, BLACK, player_position)
                last_move = act(e.key)
                player_position = new_position(player_position, last_move)
                eat_potato(player_position, potato_position, last_move)

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, r)

        for x in range(
            potato_position.left, potato_position.right, texture.get_width()
        ):
            for y in range(
                potato_position.top, potato_position.bottom, texture.get_height()
            ):
                screen.blit(texture_potato, (x, y))

        for x in range(
            player_position.left, player_position.right, texture.get_width()
        ):
            for y in range(
                player_position.top, player_position.bottom, texture.get_height()
            ):
                screen.blit(texture, (x, y))
        pygame.display.flip()
    pygame.quit()


def eat_potato(player_position, potato_position, last_move):
    if player_position == potato_position:
    if player_position == potato_position:
        new_position(potato_position, last_move)


def new_position(position, command):
    if command == "up":
        if position.y > 0:
            position.move_ip(0, -50)
    elif command == "down":
        if position.y < 550:
            position.move_ip(0, 50)
    elif command == "left":
        if position.x > 0:
            position.move_ip(-50, 0)
    elif command == "right":
        if position.x < 750:
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
