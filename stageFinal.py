import random
import pygame
from pygame.locals import *

from settings import *
from level import *
from monsterElv import *
from monsterElv_elecRain import *
from run import *

class StageFinal(MonsterElv):
    def __init__(self, pos, MONSTER_SIZE, groups, sprites_obstacles):
        self.path_sprts = 'images/sprites/'
        self.monElv_surf = pygame.image.load(f'{self.path_sprts}temp_MonsterElv_idleL.png').convert_Alpha()
        self.monElv_surf = pygame.transform.scale(self.monElv_surf, MONSTER_SIZE)

        super(StageFinal, self).__init__(pos, MONSTER_SIZE, groups, sprites_obstacles)
        # self.speed = 6

        # sound

        self.toward = -1

        self.attackBox = pygame.Rect()

    def import_monster_assets(self):
        self.spr = {'idleL':[], 
                    # 'walkL':[], 'walkR':[],
                    # 'attack1L':[], 'attack1R':[],
                    # 'cast_explosionL':[], 'cast_explosionR':[],
                    # 'cast_dazzleL':[], 'cast_dazzleR':[],
                    # 'cast_thunderL':[], 'cast_thunderR':[],
                    # 'deathL':[], 'deathR':[],
                    'hurtL':[], 'hurtR':[]}

        super(MonsterElv, self).import_monster_assets('image/sprites/', MonsterElv_IMG_INFO, 'L')
