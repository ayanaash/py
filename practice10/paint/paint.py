import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK


mode = "draw"  # draw / rect / circle / erase


brush_size = 5

drawing = False
start_pos = None  #точка где начали рисовать


screen.fill(WHITE)

def draw_ui():
    #панель цветов
    for i, color in enumerate(colors):       #x
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))  #рисуем палитрy

    #режим
    font = pygame.font.SysFont(None, 24)

    modes = ["draw", "rect", "circle", "erase"]
    for i, m in enumerate(modes):
        text = font.render(m, True, BLACK)
        screen.blit(text, (10 + i*80, 50))


running = True
while running:
    draw_ui()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #нажали мышь
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

            x, y = event.pos

            #выбор цвета
            for i, color in enumerate(colors):
                if 10 + i*40 < x < 40 + i*40 and 10 < y < 40:   #проверka попали ли в цветной квадрат
                    current_color = color

            #выбор режима
            modes = ["draw", "rect", "circle", "erase"]
            for i, m in enumerate(modes):
                if 10 + i*80 < x < 70 + i*80 and 50 < y < 80:
                    mode = m

        #отпустили мышь
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))  #создаём прямоугольник из двух точек
                pygame.draw.rect(screen, current_color, rect, 2)

            if mode == "circle":
                end_pos = event.pos
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)  #считаем радиус по формуле расстояния
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)

        #движение мыши
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)  #рисуем маленькие кружки - получается линия

            if mode == "erase":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size * 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()