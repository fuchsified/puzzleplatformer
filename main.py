# Python puzzle platformer
import pygame
from time import sleep

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_x = 100
player_y = 100
player_speed = 15

gravity = 1
velocity_y = 0
jump_strength = -18
on_ground = False

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

    if keys[pygame.K_s]:
        player_y += player_speed

    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        if on_ground:
            velocity_y = jump_strength
            on_ground = False

    velocity_y += gravity
    player_y += velocity_y

    if player_y > 570:
        player_y = 570
        velocity_y = 0
        on_ground = True


    pygame.draw.rect(screen, (0, 200, 0), (0, 620, 1280, 720))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()