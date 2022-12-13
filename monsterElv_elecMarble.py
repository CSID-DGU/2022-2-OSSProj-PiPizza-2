import pygame
from pygame.locals import *
import os

from rpg import *

class monsterElv_elecMarble:
    def __init__(self):
        super().__init__()
        self.direction = player.direction
        if self.direction == "RIGHT":
            self.image = pygame.image.load("")