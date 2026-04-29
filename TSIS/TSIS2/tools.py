import pygame
from collections import deque  #deque for flood fil

#pencil
def draw_pencil(surface, color, start_pos, end_pos, size):
    pygame.draw.line(surface, color, start_pos, end_pos, size)


#line
def draw_line(surface, color, start_pos, end_pos, size):
    pygame.draw.line(surface, color, start_pos, end_pos, size)


#retangular
def draw_rect(surface, color, start_pos, end_pos, size):
    rect = pygame.Rect(start_pos, (end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
    rect.normalize()
    pygame.draw.rect(surface, color, rect, size)


#circle
def draw_circle(surface, color, start_pos, end_pos, size):
    radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)  #аракаш формула
    pygame.draw.circle(surface, color, start_pos, radius, size)


#flood fill
def flood_fill(surface, start_pos, fill_color):
    width, height = surface.get_size()
    target_color = surface.get_at(start_pos)  #выбор цвета

    if target_color == fill_color:
        return

    queue = deque([start_pos])   #по пикселям

    while queue:
        x, y = queue.popleft()

        if x < 0 or x >= width or y < 0 or y >= height:  #защита от выхода за экран
            continue

        if surface.get_at((x, y)) != target_color:  #проверка грнаиц по цвету
            continue

        surface.set_at((x, y), fill_color)

        queue.append((x+1, y))  #up
        queue.append((x-1, y))  #down
        queue.append((x, y+1))  #left
        queue.append((x, y-1))  #right   заливка с центра