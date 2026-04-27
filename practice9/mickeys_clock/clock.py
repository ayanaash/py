import pygame
import sys
import os
from datetime import datetime
from pygame.math import Vector2


class MickeyClock:
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 1400, 1050
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Mickey Clock")

        self.clock = pygame.time.Clock()

        self.WHITE = (255, 255, 255)

        base_path = os.path.dirname(__file__)

        self.mickey = pygame.image.load(os.path.join(base_path, "images", "mickeybody.png")).convert_alpha()   #загружаем микки
        self.right_hand = pygame.image.load(os.path.join(base_path, "images", "right_hand.png")).convert_alpha() #conv alpha - сохраняет прозрачность
        self.left_hand = pygame.image.load(os.path.join(base_path, "images", "left_hand.png")).convert_alpha()

        self.center = Vector2(self.WIDTH // 2, self.HEIGHT // 2)

        
        self.offset = Vector2(0, -150)   #расстояние от центра до рук

    def rotate_hand(self, image, angle, pivot, offset):
        rotated_image = pygame.transform.rotate(image, -angle)
        rotated_offset = offset.rotate(angle)
        rect = rotated_image.get_rect(center=pivot + rotated_offset) #pivot-центр часов offset-плечо
        return rotated_image, rect

    def run(self):
        running = True

        while running:
            self.clock.tick(1)  #обновление раз в секунду

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            now = datetime.now()
            minutes = now.minute
            seconds = now.second

            #углы
            minute_angle = minutes * 6   #6dg per minute
            second_angle = seconds * 6
            
            rotated_right, rect_right = self.rotate_hand(   #правая рука = минуты
                self.right_hand, minute_angle, self.center, self.offset
            )

            rotated_left, rect_left = self.rotate_hand(   #левая рука = секунды
                self.left_hand, second_angle, self.center, self.offset
            )

            self.screen.fill(self.WHITE)
            self.screen.blit(self.mickey, self.mickey.get_rect(center=self.center))  #микки по центру
            self.screen.blit(rotated_right, rect_right) #руки
            self.screen.blit(rotated_left, rect_left) 

            pygame.display.flip()  #обновление экрана

        pygame.quit()
        sys.exit()