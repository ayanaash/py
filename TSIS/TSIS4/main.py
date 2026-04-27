import pygame
import sys
from game import SnakeGame
from db import init_db, save_score, get_top_scores, get_personal_best

pygame.init()
screen = pygame.display.set_mode((600,600))
font = pygame.font.Font(None, 36)

init_db()

def draw_text(text, y):
    surf = font.render(text, True, (255,255,255))
    screen.blit(surf, (200, y))

def main():
    username = input("Enter username: ")
    game = SnakeGame(username)
    best = get_personal_best(username)

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((0,0,0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.dx, game.dy = 0, -20
                if e.key == pygame.K_DOWN:
                    game.dx, game.dy = 0, 20
                if e.key == pygame.K_LEFT:
                    game.dx, game.dy = -20, 0
                if e.key == pygame.K_RIGHT:
                    game.dx, game.dy = 20, 0

        alive = game.update()
        game.draw(screen)

        draw_text(f"Score: {game.score}", 10)
        draw_text(f"Best: {best}", 40)

        if not alive:
            save_score(username, game.score, game.level)
            print("GAME OVER")
            print("TOP 10:")
            for row in get_top_scores():
                print(row)
            pygame.quit()
            break

        pygame.display.flip()
        clock.tick(10)

main()