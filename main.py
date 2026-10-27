# Python puzzle platformer
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

PLAYER_SIZE = 50

player_x = 100
player_y = 100
player_speed = 15

gravity = 1
velocity_y = 0
jump_strength = -18
on_ground = False

platforms = [
    pygame.Rect(0, 620, 1300, 100),
    pygame.Rect(250, 500, 250, 40),
    pygame.Rect(500, 400, 250, 40),
    pygame.Rect(75, 200, 100, 20)
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    keys = pygame.key.get_pressed()

    prev_bottom = player_y + PLAYER_SIZE

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        if on_ground:
            velocity_y = jump_strength
            on_ground = False

    velocity_y += gravity
    player_y += velocity_y

    on_ground = False
    for plat in platforms:
        if (velocity_y >= 0
                and player_x + PLAYER_SIZE > plat.left
                and player_x < plat.right
                and player_y + PLAYER_SIZE >= plat.top
                and prev_bottom <= plat.top):
            player_y = plat.top - PLAYER_SIZE
            velocity_y = 0
            on_ground = True

    if player_x <= 0:
        player_x = 1230
    if player_x >= 1280:
        player_x = 0

    for plat in platforms:
        color = (255, 0, 0) if plat.y == 620 else (0, 255, 0)
        pygame.draw.rect(screen, color, plat)
    pygame.draw.rect(screen, (0, 0, 0), (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()