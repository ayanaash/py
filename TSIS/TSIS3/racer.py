import pygame
import random
import time
from persistence import save_score

WIDTH, HEIGHT = 600, 800

LANES = [150, 300, 450]

class Player:
    def __init__(self, color):
        self.lane = 1
        self.y = 650
        self.color = color
        self.speed = 5
        self.shield = False

    def move(self, direction):
        self.lane = max(0, min(2, self.lane + direction))  #сохр границ

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (LANES[self.lane]-25, self.y, 50, 80))


class Obstacle:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.y = -100
        self.type = random.choice(["barrier", "oil", "pothole"])
        self.speed = 5

    def update(self):
        self.y += self.speed  #вниз

    def draw(self, screen):
        color = (200, 0, 0) if self.type == "barrier" else (0, 0, 0)
        pygame.draw.rect(screen, color,
                         (LANES[self.lane]-25, self.y, 50, 50))


class TrafficCar:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.y = -100
        self.speed = random.randint(4, 7)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0),
                         (LANES[self.lane]-25, self.y, 50, 80))


class PowerUp:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.y = -100
        self.type = random.choice(["nitro", "shield", "repair"])
        self.spawn_time = time.time()

    def update(self):
        self.y += 4

    def draw(self, screen):   #голуб                зеленый               фиол
        colors = {"nitro": (0,255,255) , "shield": (0,255,0), "repair": (255,0,255)}
        pygame.draw.circle(screen, colors[self.type],
                           (LANES[self.lane], int(self.y)), 20)


class Game:
    def __init__(self, screen, settings, username):
        self.screen = screen
        self.player = Player(settings["car_color"])
        self.obstacles = []
        self.traffic = []
        self.powerups = []

        self.score = 0
        self.distance = 0
        self.coins = 0

        self.active_power = None
        self.power_timer = 0

        self.spawn_timer = 0
        self.username = username

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.move(-1)
            elif event.key == pygame.K_RIGHT:
                self.player.move(1)
        return None

    def spawn_logic(self):
        self.spawn_timer += 1

        if self.spawn_timer % 60 == 0:
            self.obstacles.append(Obstacle())

        if self.spawn_timer % 90 == 0:
            self.traffic.append(TrafficCar())

        if self.spawn_timer % 200 == 0:
            self.powerups.append(PowerUp())

    def collision(self, obj):
        return obj.lane == self.player.lane and abs(obj.y - self.player.y) < 50

    def update(self):
        self.spawn_logic()

        self.distance += 1
        self.score += 1

        # difficulty scaling
        if self.distance % 500 == 0:
            for t in self.traffic:
                t.speed += 1

        for obj in self.obstacles:
            obj.update()
            if self.collision(obj):
                if self.player.shield:
                    self.player.shield = False
                else:
                    self.game_over()

        for car in self.traffic:
            car.update()
            if self.collision(car):
                if self.player.shield:
                    self.player.shield = False
                else:
                    self.game_over()

        for p in self.powerups:
            p.update()

            if time.time() - p.spawn_time > 5:
                self.powerups.remove(p)
                continue

            if self.collision(p):
                self.activate_power(p.type)
                self.powerups.remove(p)

        if self.active_power == "nitro":
            self.player.speed = 10
            if time.time() > self.power_timer:
                self.player.speed = 5
                self.active_power = None

    def activate_power(self, type_):
        if self.active_power:
            return

        self.active_power = type_

        if type_ == "nitro":
            self.power_timer = time.time() + 4

        elif type_ == "shield":
            self.player.shield = True

        elif type_ == "repair":
            self.score += 100

    def game_over(self):
        save_score(self.username, self.score, self.distance)
        raise Exception("game_over")

    def draw(self):
        self.screen.fill((50, 50, 50))

        self.player.draw(self.screen)

        for obj in self.obstacles:
            obj.draw(self.screen)

        for car in self.traffic:
            car.draw(self.screen)

        for p in self.powerups:
            p.draw(self.screen)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(text, (10, 10))