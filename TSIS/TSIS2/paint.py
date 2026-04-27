import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

#settings
color = (0, 0, 0)

brush_sizes = {
    1: 2,
    2: 5,
    3: 10
}
brush_size = brush_sizes[2]

tool = "pencil"

drawing = False
start_pos = None
last_pos = None

#text tool
font = pygame.font.SysFont("Arial", 24)
typing = False
text_input = ""
text_pos = (0, 0)

#main loop
while True:
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #keyboard
        if event.type == pygame.KEYDOWN:

            #brush size
            if event.key == pygame.K_1:
                brush_size = brush_sizes[1]
            if event.key == pygame.K_2:
                brush_size = brush_sizes[2]
            if event.key == pygame.K_3:
                brush_size = brush_sizes[3]

            #tools
            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_f:
                tool = "fill"
            if event.key == pygame.K_t:
                tool = "text"

            #save
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            #text input
            if typing:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, color)
                    canvas.blit(text_surface, text_pos)
                    typing = False
                    text_input = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        #mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            last_pos = event.pos
            drawing = True

            if tool == "fill":
                flood_fill(canvas, event.pos, color)

            if tool == "text":
                typing = True
                text_pos = event.pos
                text_input = ""

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if tool == "line":
                draw_line(canvas, color, start_pos, end_pos, brush_size)

            if tool == "rect":
                draw_rect(canvas, color, start_pos, end_pos, brush_size)

            if tool == "circle":
                draw_circle(canvas, color, start_pos, end_pos, brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "pencil":
                draw_pencil(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

    #text preview
    if typing:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)

    pygame.display.flip()
    clock.tick(60)