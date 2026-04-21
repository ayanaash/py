import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Shapes")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

#текущий режим 
mode = "square"

start_pos = None  #начальная точка

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # выбор фигуры клавишами
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "square"
            if event.key == pygame.K_2:
                mode = "right_triangle"
            if event.key == pygame.K_3:
                mode = "equilateral_triangle"
            if event.key == pygame.K_4:
                mode = "rhombus"

        #нажали мышь
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        #отпустили мышь - рисуем
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos

            if start_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos

                #square
                if mode == "square":
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    rect = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(screen, BLACK, rect, 2)

                #right triangle
                elif mode == "right_triangle":
                    points = [
                        (x1, y1),
                        (x1, y2),
                        (x2, y2)
                    ]
                    pygame.draw.polygon(screen, BLACK, points, 2)

                #equilateral triangle
                elif mode == "equilateral_triangle":
                    side = abs(x2 - x1)

                    p1 = (x1, y1)
                    p2 = (x1 + side, y1)
                    height = (3 ** 0.5 / 2) * side
                    p3 = (x1 + side // 2, y1 - height)

                    pygame.draw.polygon(screen, BLACK, [p1, p2, p3], 2)

                #rhombus
                elif mode == "rhombus":
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    points = [
                        (cx, y1),   #верх
                        (x2, cy),   #право
                        (cx, y2),   #низ
                        (x1, cy)    #лево
                    ]

                    pygame.draw.polygon(screen, BLACK, points, 2)

                start_pos = None

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()