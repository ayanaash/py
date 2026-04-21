import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 28)

player = MusicPlayer("music")

clock = pygame.time.Clock()

def draw():  #обновление экрана
    screen.fill((30, 30, 30))

    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))   #название
    time_text = font.render(f"Time: {player.get_position()} sec", True, (200, 200, 200))  #сколько секунд

    controls_text = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (150, 150, 150))

    screen.blit(track_text, (50, 80))  #позиция названия
    screen.blit(time_text, (50, 130))
    screen.blit(controls_text, (50, 200))

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next()

            elif event.key == pygame.K_b:
                player.previous()

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    draw()
    clock.tick(60)