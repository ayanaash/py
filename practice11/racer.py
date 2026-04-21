import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)


player_width = 50
player_height = 80
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5


enemy_width = 50
enemy_height = 80
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -100
enemy_speed = 4


coins = []  #список монет
coin_spawn_delay = 40  #задержка появления  0.6sec
coin_timer = 0

score = 0  

#уровень ускорения
LEVEL_UP_COINS = 5  #каждые 5 монет ускорение

font = pygame.font.SysFont("Arial", 24)

#созданиe монеты
def spawn_coin():
    x = random.randint(20, WIDTH - 20)
    y = -20

    #случайный вес монеты
    weight = random.choice([1, 2, 3])

    return {"x": x, "y": y, "weight": weight}

running = True
while running:
    screen.fill(WHITE)

    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    #движение врага
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - enemy_width)

    #появление монет
    coin_timer += 1
    if coin_timer >= coin_spawn_delay:
        coins.append(spawn_coin())
        coin_timer = 0

    #движение монет
    for coin in coins:
        coin["y"] += 5

    #проверка столкновений с монетами
    for coin in coins[:]:
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        coin_rect = pygame.Rect(coin["x"], coin["y"], 20, 20)

        if player_rect.colliderect(coin_rect):
            score += coin["weight"]  # добавляем очки
            coins.remove(coin)

            #увеличение скорости врага
            if score % LEVEL_UP_COINS == 0:
                enemy_speed += 1

    #проверка столкновения с врагом
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    #игрок
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    #враг
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    #монеты
    for coin in coins:
        #цвет зависит от веса
        if coin["weight"] == 1:
            color = YELLOW
        elif coin["weight"] == 2:
            color = (255, 165, 0)  #оранжевый
        else:
            color = (255, 0, 255)  #фиолетовый

        pygame.draw.circle(screen, color, (coin["x"], coin["y"]), 10)

    #отображаем счёт
    score_text = font.render(f"Coins: {score}", True, BLACK)
    speed_text = font.render(f"Speed: {enemy_speed}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 40))

    pygame.display.update()
    clock.tick(60)

pygame.quit()