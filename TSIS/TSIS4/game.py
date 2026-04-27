import pygame
import random
import json

WIDTH, HEIGHT = 600, 600
CELL = 20

class SnakeGame:
    def __init__(self, username):
        self.username = username
        self.reset()
        self.load_settings()

    def load_settings(self):
        with open("settings.json", "r") as f:
            s = json.load(f)
        self.snake_color = tuple(s["snake_color"])
        self.grid = s["grid"]

    def reset(self):
        self.snake = [(100, 100)]
        self.dx, self.dy = CELL, 0
        self.food = self.spawn_food()
        self.poison = self.spawn_food()
        self.score = 0
        self.level = 1
        self.speed = 10

        self.power_up = None
        self.power_spawn_time = 0
        self.active_power = None
        self.power_end_time = 0

        self.obstacles = []

    def spawn_food(self):
        return (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))

    def spawn_power(self):
        types = ["speed", "slow", "shield"]
        return (self.spawn_food(), random.choice(types))

    def generate_obstacles(self):
        self.obstacles = []
        for _ in range(self.level * 3):
            pos = self.spawn_food()
            if pos not in self.snake:
                self.obstacles.append(pos)

    def update(self):
        head = (self.snake[0][0] + self.dx, self.snake[0][1] + self.dy)

        # collisions
        if head in self.snake or head in self.obstacles:
            if self.active_power == "shield":
                self.active_power = None
            else:
                return False

        self.snake.insert(0, head)

        # normal food
        if head == self.food:
            self.score += 10
            self.food = self.spawn_food()

            if self.score % 50 == 0:
                self.level += 1
                self.generate_obstacles()
        else:
            self.snake.pop()

        # poison
        if head == self.poison:
            for _ in range(2):
                if len(self.snake) > 1:
                    self.snake.pop()
            if len(self.snake) <= 1:
                return False
            self.poison = self.spawn_food()

        # power spawn
        now = pygame.time.get_ticks()
        if not self.power_up and now - self.power_spawn_time > 8000:
            self.power_up = self.spawn_power()
            self.power_spawn_time = now

        # collect power
        if self.power_up and head == self.power_up[0]:
            self.active_power = self.power_up[1]
            self.power_end_time = now + 5000
            self.power_up = None

        # expire power
        if self.active_power and now > self.power_end_time:
            self.active_power = None

        return True

    def draw(self, screen):
        for segment in self.snake:
            pygame.draw.rect(screen, self.snake_color, (*segment, CELL, CELL))

        pygame.draw.rect(screen, (255,0,0), (*self.food, CELL, CELL))
        pygame.draw.rect(screen, (139,0,0), (*self.poison, CELL, CELL))

        for ob in self.obstacles:
            pygame.draw.rect(screen, (100,100,100), (*ob, CELL, CELL))

        if self.power_up:
            color = (0,0,255) if self.power_up[1]=="speed" else (255,255,0)
            pygame.draw.rect(screen, color, (*self.power_up[0], CELL, CELL))