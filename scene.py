import pygame
from pygame.locals import *

import random
import time

from settings import *
from player import *
from monsterElv import *
from stageFinal import *

pygame.init()

class Scene:
    def __init__(self, player, monsterElv, sceneNum, gameState, visible_sprites):
        self.display_surface = pygame.display.get_surface()
        self.gameState = gameState
        self.sceneNum = sceneNum
        self.sceneChange = False
        
        self.player = player
        self.monsterElv = monsterElv
        self.player.set_state_ini()

        self.visible_sprites = visible_sprites
        self.visible_sprites.background_Setting(self.gameState)

        # fade in/out
        self.fade_surf = pygame.Surface((WIDTH, HEIGHT))
        self.fade_sufr.fill((0,0,0))
        self.alpha = 255
        self.fade_surf.set_alpha(self.alpha)

    def update(self, df, time):
        
        self.visibile_sprites.custom_draw(self.player, self.gameState, self.monster)

        self.monster.setTargetPos(self.player.hitbox.centerx)  # 플레이어 hitbox x 값 monster targetpos 로 넘겨주기.
        self.monster.update(df)

        self.player.setTargetPos(self.monster.getHitBox()[0])  # 몬스터 hitbox x 값 player targetpos 로 넘겨주기.
        self.player.update(df)

        self.fade_in()
        pygame.display.update()

    def fade_in(self):
        # alpha 값 조절해서 fade in 효과 내기
        # scene 생성 후 alpha 값이 차츰 작아지다가 0 보다 작아지면 alpha 는 계속 0을 유지한다.
        # scene 삭제 시 fade_out 함수를 호출하면 alpha 값이 다시 차츰 높아지게 한다.
        self.alpha -= 30 if self.alpha > 0 else 0
        self.fade_surf.set_alpha(self.alpha)
        self.display_surface.blit(self.fade_surf, (0, 0))

    def fade_out(self): # 장면 전환시, 다음 장면 생성 전에 이 함수를 호출하자
        for alpha in range(0, 300):
            self.fade_surf.set_alpha(alpha)
            self.display_surface.blit(self.fade_surf, (0, 0))
            pygame.display.update()

    def draw(self, player, gameState, monsterElv):
        if gameState == 'stageFinal':
            self.display_surface.blit("images/temp_menu_background.png")
            # self.display_surface.blit("")

            self.drawBar(player, monsterElv)
            self.setCircle()

            pygame.draw.rect(self.display_surface, (255,0,0))
