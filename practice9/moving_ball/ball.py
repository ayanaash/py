import pygame

class Ball:
    def __init__(self, x, y, radius=25, speed=20, screen_width=600, screen_height=400):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = (255, 0, 0)

    def move(self, dx, dy):
        new_x = self.x + dx * self.speed   #dx - left/right
        new_y = self.y + dy * self.speed   #dy - up/down

        # проверка границ (чтобы шар не выходил за экран)
        if self.radius <= new_x <= self.screen_width - self.radius:
            self.x = new_x

        if self.radius <= new_y <= self.screen_height - self.radius:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)