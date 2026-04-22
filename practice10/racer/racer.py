import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")


clock = pygame.time.Clock()
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
RED = (200, 0, 0)

#машина
player_width = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - 100, player_width, 80)
player_speed = 6

#монеты
coin_size = 20
coins = []  # список всех монет на экране
coin_spawn_timer = 0


score = 0
font = pygame.font.SysFont("Arial", 24)


def spawn_coin():
    #cоздание монеты в случайной позиции сверху
    x = random.randint(50, WIDTH - 50)  #random posistion
    coin = pygame.Rect(x, -20, coin_size, coin_size)  #монета появляется сверху
    coins.append(coin)


def draw_coins():
    #рисовка монет
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin.center, coin_size // 2)


def move_coins():
    #движение монет вниз
    global coins
    for coin in coins:
        coin.y += 5

    #удаление монет которые ушли за экран (создаем новый список)
    coins = [
    c for c in coins   
    if c.y < HEIGHT] # только если она на экране



running = True
while running:
    clock.tick(FPS)
    screen.fill((40, 40, 40))  #фон дороги

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    #появление монет
    coin_spawn_timer += 1
    if coin_spawn_timer > 40:  #каждые ~0.6 сек 
        spawn_coin()
        coin_spawn_timer = 0

    move_coins()

    #сбор монет
    for coin in coins[:]:
        if player.colliderect(coin):  #если машина касается монеты
            coins.remove(coin)
            score += 1

    pygame.draw.rect(screen, RED, player)  #машина
    draw_coins()

    #счёт
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 130, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()