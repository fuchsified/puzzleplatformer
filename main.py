# Python puzzle platformer
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_x = 100
player_y = 100
player_speed = 15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))



    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

    if keys[pygame.K_w]:
        player_y -= player_speed

    if keys[pygame.K_s]:
        player_y += player_speed

    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 150, 150))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()