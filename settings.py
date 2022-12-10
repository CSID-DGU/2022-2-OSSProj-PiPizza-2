
import pygame, sys
from pygame.locals import *
import os
pygame.init()

#화면 크기
SCREEN_SIZE = WIDTH, HEIGHT = (900, 450)
FPS = 60

# 게임 단계
GAME_STATES = [ 'stage1', 'stage2', 'stageFinal']

pygame.init()
# 화면 크기 조정
ScreenResized = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
# screen 변수에 크기옵션 집어넣어 앞으로 그릴 내용 담음
screen = ScreenResized.copy()
pygame.display.set_caption("배달의 달인")

ScreenResized_centerpos = (0,0)
rWIDTH = ScreenResized.get_width()
rHEIGHT = ScreenResized.get_height()
# button_offset = 0.18 뭔지 모름

def checkscrsize(wEvent, hEvent):
    if (wEvent < WIDTH and hEvent < HEIGHT) or wEvent < WIDTH or hEvent < HEIGHT: #최소해상도
        ScreenResized = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
    else:
        if hEvent/wEvent != WIDTH/HEIGHT: #고정화면비
            heightAdjusted = int(wEvent/(rWIDTH/rHEIGHT))
            ScreenResized = pygame.display.set_mode((wEvent,heightAdjusted), RESIZABLE)

def resize(name, w, h):
        global WIDTH, HEIGHT, ScreenResized
        print("ScreenResized: (",ScreenResized.get_width(),",",ScreenResized.get_height(),")")
        return (name, w*ScreenResized.get_width()//WIDTH, h*ScreenResized.get_height()//HEIGHT)

# 메뉴화면 버튼 크기
btn_menu_w = int(rWIDTH/6.8)
btn_menu_h = int(rHEIGHT/8)
btn_gameSetting_w = int(btn_menu_w/2)

# 색상
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

# 캐릭터 HP 정보
PLAYER_HP   = 99
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
BG = pygame.image.load("images/obstacles/Track2.png")

RUNNING = [pygame.image.load("images/sprites/Bike1.png"),
           pygame.image.load("images/sprites/Bike2.png")]
JUMPING = pygame.image.load("images/sprites/Bike2.png")
DUCKING = [pygame.image.load("images/sprites/BikeDuck1.png"),
           pygame.image.load("images/sprites/BikeDuck1.png")]


Traffic_Light = [pygame.image.load("images/obstacles/Traffic1.png"),
                pygame.image.load(
                    "images/obstacles/Traffic3.png"),
                pygame.image.load("images/obstacles/Traffic4.png")]
Traffic_Cone = [pygame.image.load("images/obstacles/RoadBlock.png"),
                pygame.image.load(
                    "images/obstacles/TrafficCone.png"),
                pygame.image.load("images/obstacles/TrafficCone2.png")]

DUST = [pygame.image.load("images/obstacles/Dust1.png"),
        pygame.image.load("images/obstacles/Dust2.png")]

CLOUD = pygame.image.load("images/obstacles/Cloud.png")


#사운드 설정
bgm_on=True
on_pushtime=0
off_pushtime=0

#효과음
jump_sound = pygame.mixer.Sound('sound/jump.wav')
die_sound = pygame.mixer.Sound('sound/die.wav')
clear_sound = pygame.mixer.Sound('sound/rewards.wav')

#bgm
background_m=pygame.mixer.Sound("sound/opening_bgm.mp3")
ingame_m =pygame.mixer.Sound("sound/t-rex_bgm1.mp3")

