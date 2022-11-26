import pygame
from pygame.locals import *
from settings import *
from run import *

class MonsterElv(pygame.sprite.Sprite):
    def __init__(self, pos, MONSTER_SIZE, groups, sprites_obstacle):
        super().__init__()
        # self.path_sprts = 'images/sprites/'
        # self.monElv_surf = pygame.image.load(f'{self.path_sprts}temp_MonsterElv_idleL.png').convert_Alpha()
        # self.monElv_surf = pygame.transform.scale(self.monElv_surf, MONSTER_SIZE)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,0)
        self.scale = MONSTER_SIZE
        self.display_surface = pygame.display.get_surface()


        # graphic setup
        self.import_assetsMonster()
        self.status = 'idleL'    # 시작은 왼쪽 방향을 보고 서 있기
        self.status_prev = ''

        self.direction = -1
        self.speed = 4
        self.space_number = 0
        
        self.sprites_obstacle = sprites_obstacle
    
    def import_assetsMonster(self, path, MonsterInfo, reverse_key):

        for spr_name in self.spr.keys():
            # self.spr[spr_name] = import_sprites_image(path, spr_name +'.png' )
            pass