import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game") #название окна сверху

clock = pygame.time.Clock()

#создание шара
ball = Ball(WIDTH // 2, HEIGHT // 2, screen_width=WIDTH, screen_height=HEIGHT)

running = True
while running:
    screen.fill((255, 255, 255)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #управление стрелками
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        ball.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(1, 0)
    if keys[pygame.K_UP]:
        ball.move(0, -1)
    if keys[pygame.K_DOWN]:
        ball.move(0, 1)

   
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
sys.exit()