import pygame
from racer import Game
from ui import MainMenu, LeaderboardScreen, SettingsScreen, GameOverScreen
from persistence import load_settings

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game")

clock = pygame.time.Clock()

settings = load_settings()

state = "menu"
game = None
menu = MainMenu(screen)
leaderboard = LeaderboardScreen(screen)
settings_screen = SettingsScreen(screen, settings)
game_over_screen = GameOverScreen(screen)

username = "Player"

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            action = menu.handle_event(event)
            if action == "play":
                username = menu.username
                game = Game(screen, settings, username)
                state = "game"
            elif action == "leaderboard":
                state = "leaderboard"
            elif action == "settings":
                state = "settings"
            elif action == "quit":
                running = False

        elif state == "settings":
            if settings_screen.handle_event(event) == "back":
                state = "menu"

        elif state == "leaderboard":
            if leaderboard.handle_event(event) == "back":
                state = "menu"

        elif state == "game":
            result = game.handle_event(event)
            if result == "game_over":
                game_over_screen.set_data(game)
                state = "game_over"

        elif state == "game_over":
            action = game_over_screen.handle_event(event)
            if action == "retry":
                game = Game(screen, settings, username)
                state = "game"
            elif action == "menu":
                state = "menu"

    if state == "menu":
        menu.draw()
    elif state == "settings":
        settings_screen.draw()
    elif state == "leaderboard":
        leaderboard.draw()
    elif state == "game":
        game.update()
        game.draw()
    elif state == "game_over":
        game_over_screen.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()