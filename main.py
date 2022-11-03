import pygame
from src import game
from sys import exit

WIDTH = 800
HEIGHT = 600
BG_COLOR = "black"
CLOCK = pygame.time.Clock()
FPS = 50


game = game.Game(WIDTH, HEIGHT, BG_COLOR)
paused = False

pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        if pygame.mouse.get_pressed()[0]:
            mouse_position = pygame.mouse.get_pos()
            game.create_random_object(mouse_position)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

            if event.key == pygame.K_RIGHT:
                game.force[0] += 0.25
            if event.key == pygame.K_LEFT:
                game.force[0] -= 0.25
            if event.key == pygame.K_UP:
                game.force[1] += 0.25
            if event.key == pygame.K_DOWN:
                game.force[1] -= 0.25

    
    if not paused:
        game.draw()
        game.update()

        pygame.display.update()
    
    CLOCK.tick(FPS)