import pygame
from pygame.locals import *
from settings import *
from player import *
from monsterElv import *
from run import *

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface() 

        # sprite groups 스프라이트 그리(draw)고 업데이트하기
        self.all_sprites = pygame.sprite.Group()

        self.isOneClear = False
        self.isTwoClear = False
        self.isFinalClear = False
        
        self.sceneNum = 2
        self.gameState = GAME_STATES[self.sceneNum]
        self.stateChanging = False
        self.canChangeState = True

        self.create_map()

    def create_map(self):
        # player 생성
        self.player = Player(PLAYER_COOR_ini, PLAYER_SIZE, [self.visible_sprites], self.sprites_obstacles)
        # monster 생성
        self.monster = MonsterElv(MonsterElv_COOR_ini, MONSTER_SIZE, [self.visible_sprites], self.sprites_obstacle)
        # scene 생성
        #self.scene = Scene(self.player, self.monster, self.scene_num, self.game_state, self.visible_sprites) #시작은 game_state = 'intro'임

    def run(self, df):
        self.display_surface.fill('black')          # 이전 프레임을 가린다
        self.all_sprites.draw(self.display_surface) # 디스플레이 서피스 위에 그린다
        self.all_sprites.update()                   # 스프라이트를 업데이트한다
        # print('게임 실행')

    def monster_create(self, game_state):
        if game_state == 'level3': # boss 생성 후 바꿔야함
            pass
            #return StageFinal(MonsterElv_COOR_ini, MONSTER_SIZE, [self.visible_sprites], self.obstacle_sprites)

    def scene_manager(self):
        
        # if self.isOneClear or self.isTwoClear or self.isFinalClear:
        #     # sceneNum 증가시켜서 gameState 바꾸기
        #     if self.sceneNum < len(GAME_STATES) -1:
        #         self.sceneNum += 1

            self.gameState = GAME_STATES[self.sceneNum]

            #self.scene = Scene(self.player, self.monster, self.scene_num, self.game_state, self.visible_sprites)