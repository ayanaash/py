import pygame
import sys
from game import SnakeGame
from db import init_db, save_score, get_top_scores, get_personal_best

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.Font(None, 36)

init_db()

def draw_text(text, y):
    surf = font.render(text, True, (255, 255, 255))
    screen.blit(surf, (200, y))

def main():
    # ⚠ лучше временно заменить input на фиксированное имя
    username = "player1"

    game = SnakeGame(username)

    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        screen.fill((0, 0, 0))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.dx, game.dy = 0, -20
                elif e.key == pygame.K_DOWN:
                    game.dx, game.dy = 0, 20
                elif e.key == pygame.K_LEFT:
                    game.dx, game.dy = -20, 0
                elif e.key == pygame.K_RIGHT:
                    game.dx, game.dy = 20, 0

        if not game_over:
            alive = game.update()

            if not alive:
                game_over = True
                save_score(username, game.score, game.level)

            game.draw(screen)

            draw_text(f"Score: {game.score}", 10)

        else:
            draw_text("GAME OVER", 200)

            y = 250
            for row in get_top_scores():
                draw_text(str(row), y)
                y += 30

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

main()