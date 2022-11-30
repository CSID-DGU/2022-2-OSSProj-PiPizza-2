
import pygame, sys
from pygame.locals import *
import os
pygame.init()

#화면 크기
SCREEN_SIZE = WIDTH, HEIGHT = (900, 450)
FPS = 60

# 메뉴화면 버튼 크기

btn_menu_w = int(WIDTH/6.8)
btn_menu_h = int(HEIGHT/8)
btn_gameSetting_w = int(btn_menu_w/2)

GAME_STATES = [ 'stage1', 'stage2', 'stageFinal']

# 화면 크기 조정
#위 2-1 로 게임창 크기 적용
ScreenResized = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
# screen 변수에 크기옵션 집어넣어 앞으로 그릴 내용 담음
screen = ScreenResized.copy()


ScreenResized_centerpos = (0,0)
rWidth = ScreenResized.get_width()
rHeight = ScreenResized.get_height()
# button_offset = 0.18 뭔지 모름

# 색상
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

# 캐릭터 HP 정보
PLAYER_HP   = 100
MONSTER_HP    = 100


# 캐릭터 사이즈
PLAYER_SIZE     = (120, 120)
MONSTER_SIZE    = (300, 300)

# player settings
PLAYER_SPELL1_MP = 10
PLAYER_SPELL2_MP = 20
PLAYER_SPELL1_CASTTIME = 3.0
PLAYER_SPELL2_CASTTIME = 5.0
PLAYER_COOR_ini = (100, 420) # 플레이어 초기 위치
PLAYER_IMG_INFO = {'idle': {'idx': 11, 'size': PLAYER_SIZE}, 'idleL': {'idx': 11, 'size': PLAYER_SIZE},
                     'run': {'idx': 8, 'size': PLAYER_SIZE}, 'runL': {'idx': 8, 'size': PLAYER_SIZE},
                     'jump': {'idx': 3, 'size': PLAYER_SIZE}, 'jumpL': {'idx': 3, 'size': PLAYER_SIZE},
                     'fall': {'idx': 3, 'size': PLAYER_SIZE}, 'fallL': {'idx': 3, 'size': PLAYER_SIZE},
                     'death': {'idx': 11, 'size': PLAYER_SIZE}, 'deathL': {'idx': 11, 'size': PLAYER_SIZE},
                     'hitted': {'idx': 4, 'size': PLAYER_SIZE}, 'hittedL': {'idx': 4, 'size': PLAYER_SIZE},
                     'attack1': {'idx': 7, 'size': PLAYER_SIZE}, 'attack1L': {'idx': 7, 'size': PLAYER_SIZE},
                     'attack2': {'idx': 7, 'size': PLAYER_SIZE}, 'attack2L': {'idx': 7, 'size': PLAYER_SIZE},
                     'cast1': {'idx': 11, 'size': PLAYER_SIZE}, 'cast1L':{'idx':11, 'size': PLAYER_SIZE},
                     'cast2': {'idx': 11, 'size': PLAYER_SIZE}, 'cast2L': {'idx': 11, 'size': PLAYER_SIZE}
                     }

# MonsterElv 설정
MonsterElv_POWER = 30
MonsterElv_COOR_ini = (1000, 125) # 몬스터3(Devil) 초기 위치
MonsterElv_IMG_INFO = {'idleL': {'idx': 8, 'size': MONSTER_SIZE}, 
                        #'idleR': {'idx': 8, 'size': DEVIL_SIZE},
                    # 'walkL': {'idx': 8, 'size': DEVIL_SIZE}, 'walkR': {'idx': 8, 'size': DEVIL_SIZE},
                    # 'attack1L': {'idx': 8, 'size': DEVIL_SIZE}, 'attack1R': {'idx': 8, 'size': DEVIL_SIZE},
                    # 'cast_explosionL':{'idx': 8, 'size': DEVIL_SIZE}, 'cast_explosionR':{'idx': 8, 'size': DEVIL_SIZE}, 
                    # 'cast_dazzleL':{'idx': 8, 'size': DEVIL_SIZE}, 'cast_dazzleR':{'idx': 8, 'size': DEVIL_SIZE}, 
                    # 'cast_thunderL':{'idx': 8, 'size': DEVIL_SIZE}, 'cast_thunderR':{'idx': 8, 'size': DEVIL_SIZE}, 
                    # 'deathL': {'idx': 7, 'size': DEVIL_SIZE}, 'deathR': {'idx': 7, 'size': DEVIL_SIZE},
                    # 'hurtL': {'idx': 3, 'size': DEVIL_SIZE}, 'hurtR': {'idx': 3, 'size': DEVIL_SIZE}
                    }


# MonsterElv 스킬 설정
# MonsterElv_ELECMARBLE_SIZE = (560, 372)
# MonsterElv_ELECMARBLE_INFO = {'darkbolt': {'idx': 11, 'size': DEVIL_DARKBOLT_SIZE}}
# MonsterElv_ELECRAIN_SIZE = (560, 372)
# MonsterElv_ELECRAIN_INFO = {'firebomb': {'idx': 14, 'size': DEVIL_FIREBOMB_SIZE}}
# MonsterElv_SHOCKWAVE_SIZE = 
# MonsterElv_SHOCKWAVE_INFO = 
# MonsterElv_TORNADO_SIZE = 
# MonsterElv_TORNADO_INFO = 


#이미지 설정
RUNNING = [pygame.image.load(os.path.join("images/sprites", "Bike1.png")),
           pygame.image.load(os.path.join("images/sprites", "Bike2.png"))]
JUMPING = pygame.image.load(os.path.join("images/sprites", "Bike2.png"))
DUCKING = [pygame.image.load(os.path.join("images/sprites", "BikeDuck1.png")),
           pygame.image.load(os.path.join("images/sprites", "BikeDuck1.png"))]

Traffic_Light = [pygame.image.load(os.path.join("images/obstacles", "Traffic1.png")),
                pygame.image.load(os.path.join("images/obstacles", "Traffic3.png")),
                pygame.image.load(os.path.join("images/obstacles", "Traffic4.png"))]
Traffic_Cone = [pygame.image.load(os.path.join("images/obstacles", "RoadBlock.png")),
                pygame.image.load(os.path.join("images/obstacles", "TrafficCone.png")),
                pygame.image.load(os.path.join("images/obstacles", "TrafficCone2.png"))]

DUST = [pygame.image.load(os.path.join("images/obstacles", "Dust1.png")),
        pygame.image.load(os.path.join("images/obstacles", "Dust2.png"))]

CLOUD = pygame.image.load(os.path.join("images/obstacles", "Cloud.png"))

BG = pygame.image.load(os.path.join("images/obstacles", "Track.png"))



