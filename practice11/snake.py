import pygame
import random
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Advanced")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


BLOCK = 20
snake = [(100, 100)]
dx, dy = BLOCK, 0


foods = []  # список еды
FOOD_LIFETIME = 300  #5 секунд

score = 0

font = pygame.font.SysFont("Arial", 24)


def spawn_food():
    x = random.randrange(0, WIDTH, BLOCK)
    y = random.randrange(0, HEIGHT, BLOCK)

    weight = random.choice([1, 2, 3])  #разный вес
    lifetime = FOOD_LIFETIME

    return {"x": x, "y": y, "weight": weight, "time": lifetime}

running = True
spawn_timer = 0

while running:
    screen.fill(WHITE)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -BLOCK
    if keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, BLOCK
    if keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -BLOCK, 0
    if keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = BLOCK, 0

    #движение змейки
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    #проверка выхода за границы
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    #генерация еды
    spawn_timer += 1
    if spawn_timer > 50:
        foods.append(spawn_food())
        spawn_timer = 0

    #проверка съедания еды
    for food in foods[:]:
        if new_head[0] == food["x"] and new_head[1] == food["y"]:
            score += food["weight"]  #добавляем очки
            foods.remove(food)
            break
    else:
        snake.pop()  #если не съели - хвост уменьшается

    #обновление таймера еды
    for food in foods[:]:
        food["time"] -= 1
        if food["time"] <= 0:
            foods.remove(food)  #исчезает

    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))

    
    for food in foods:
        if food["weight"] == 1:
            color = RED
        elif food["weight"] == 2:
            color = (255, 165, 0)
        else:
            color = (255, 0, 255)

        pygame.draw.rect(screen, color, (food["x"], food["y"], BLOCK, BLOCK))

    #счёт
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()