import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, PLAYER_SIZE, groups, obstacle_sprites):
        super().__init__()
        self.path_sprts = 'images/sprites/'
        self.img_player_pos = (())
        self.img_player_surf = pygame.image.load(f"{self.path_sprts}Bike1").convert_alpha()
        self.img_player = self.img_player_surf.get_rect(center=self.img_player_pos)
        