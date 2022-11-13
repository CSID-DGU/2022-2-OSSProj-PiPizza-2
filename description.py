import pygame, sys
from pygame.locals import *
from settings import *
pygame.init()

class Description:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.path_dial = 'images/Dialog/'

        # 디스크립션 이미지
        self.dial1_surf = pygame.image.load(f'{self.path_dial}temp_dialog1.png').convert_alpha()
        self.dial1_rect = self.dial1_surf.get_rect(topleft=(0, 0))
        self.clear1_surf = pygame.image.load(f'{self.path_dial}description1.png').convert_alpha()
        self.clear1_rect = self.clear1_surf.get_rect(topleft=(0, 0))
        self.dial2_surf = pygame.image.load(f'{self.path_dial}dialog2.png').convert_alpha()
        self.dial2_rect = self.dial2_surf.get_rect(topleft=(0, 0))
        self.clear2_surf = pygame.image.load(f'{self.path_dial}description2.png').convert_alpha()
        self.clear2_rect = self.clear2_surf.get_rect(topleft=(0, 0))
        self.dial3_surf = pygame.image.load(f'{self.path_dial}dialog3.png').convert_alpha()
        self.dial3_rect = self.dial3_surf.get_rect(topleft=(0, 0))
        # self.clear3_surf

    def dial1(self):
        self.num = 0
        while True:
            if self.num == 0:
                self.screen.blit(self.dial1_surf, self.dial1_rect)
                pygame.display.update()
            else:
                return

            if self.is_returnKey_pressed():
                self.num += 1

    def clear1(self):
        while True:
            self.screen.blit(self.clear1_surf, self.clear1_rect)
            pygame.display.update()

    def dial2(self):
        while True:
            self.screen.blit(self.dial2_surf, self.dial2_rect)
            pygame.display.update()        

    def clear2(self):
        while True:
            self.screen.blit(self.clear2_surf, self.clear2_rect)
            pygame.display.update()

    def dial3(self):
        while True:
            self.screen.blit(self.dial3_surf, self.dial3_rect)
            pygame.display.update()    

    def is_returnKey_pressed(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    return True
        return False            