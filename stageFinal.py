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

    def lose(self):
        pass
    def win(self):
        pass
