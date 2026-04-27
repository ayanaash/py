import pygame
from persistence import load_scores, save_settings

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.username = ""

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "play"
            elif event.key == pygame.K_l:
                return "leaderboard"
            elif event.key == pygame.K_s:
                return "settings"
            elif event.key == pygame.K_q:
                return "quit"
            else:
                self.username += event.unicode

    def draw(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Press Enter to Play", True, (255,255,255))
        self.screen.blit(text, (100, 300))


class LeaderboardScreen:
    def __init__(self, screen):
        self.screen = screen
        self.scores = load_scores()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            return "back"

    def draw(self):
        font = pygame.font.Font(None, 36)
        for i, s in enumerate(self.scores[:10]):
            txt = font.render(f"{i+1}. {s['name']} - {s['score']}", True, (255,255,255))
            self.screen.blit(txt, (100, 100 + i*40))


class SettingsScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                save_settings(self.settings)
                return "back"

    def draw(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Press B to go back", True, (255,255,255))
        self.screen.blit(text, (100, 300))


class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.data = None

    def set_data(self, game):
        self.data = game

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return "retry"
            elif event.key == pygame.K_m:
                return "menu"

    def draw(self):
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over", True, (255,0,0))
        self.screen.blit(text, (200, 300))