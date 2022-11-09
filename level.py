import pygame
from settings import *

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface() 

        # sprite groups 스프라이트 그리(draw)고 업데이트하기
        self.all_sprites = pygame.sprite.Group()

    def run(self, dt):
        self.display_surface.fill('black')          # 이전 프레임을 가린다
        self.all_sprites.draw(self.display_surface) # 디스플레이 서피스 위에 그린다
        self.all_sprites.update()                   # 스프라이트를 업데이트한다
        # print('게임 실행')