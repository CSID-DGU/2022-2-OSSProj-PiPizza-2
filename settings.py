import pygame, sys
from pygame.locals import *
import os

# from run import *


pygame.init()

#화면 크기 및 FPS
SCREEN_SIZE = WIDTH, HEIGHT = (900, 450)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

vec = pygame.math.Vector2

# 게임 단계
GAME_STATES = [ 'stage1', 'stage2', 'stageFinal']
ingame = False

# pygame.init()
# # 화면 크기 조정
# ScreenResized = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
# # screen 변수에 크기옵션 집어넣어 앞으로 그릴 내용 담음
# global screen
# screen = ScreenResized.copy()
# pygame.display.set_caption("배달의 달인")

# ScreenResized_centerpos = (0,0)
# rWIDTH = ScreenResized.get_width()
# rHEIGHT = ScreenResized.get_height()
# button_offset = 0.18 뭔지 모름

# def checkscrsize(wEvent, hEvent):
#     if (wEvent < WIDTH and hEvent < HEIGHT) or wEvent < WIDTH or hEvent < HEIGHT: #최소해상도
#         ScreenResized = pygame.display.set_mode((SCREEN_SIZE), RESIZABLE)
#     else:
#         if hEvent/wEvent != WIDTH/HEIGHT: #고정화면비
#             heightAdjusted = int(wEvent/(rWIDTH/rHEIGHT))
#             ScreenResized = pygame.display.set_mode((wEvent,heightAdjusted), RESIZABLE)

# def resize(name, w, h):
#         global WIDTH, HEIGHT, ScreenResized
#         print("ScreenResized: (",ScreenResized.get_width(),",",ScreenResized.get_height(),")")
#         return (name, w*ScreenResized.get_width()//WIDTH, h*ScreenResized.get_height()//HEIGHT)

# g = Game()


# 메뉴화면 버튼 크기
btn_menu_w = int(WIDTH/6.8)
btn_menu_h = int(HEIGHT/8)
btn_gameSetting_w = int(btn_menu_w/2)

# for event in pygame.event.get():
#     if event.type == pygame.VIDEORESIZE:
#         checkscrsize(event.w, event.h)
#         btn_menu_w = int(g.ScreenResized.get_width()/6.8)
#         btn_menu_h = int(g.ScreenResized.get_height()/8)

# 색상
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

# 캐릭터 HP 정보
PLAYER_HP   = 99
MONSTER_HP    = 100



#스테이지1,2 (최종 스테이지 상속)
#이미지 설정
BG = pygame.image.load("images/obstacles/Track2.png")

stage1_bg =  pygame.image.load('images/background/stage1_bg.png')
stage2_bg =  pygame.image.load('images/background/stage2_bg.png')


RUNNING = [pygame.image.load("images/sprites/Bike1.png"),
           pygame.image.load("images/sprites/Bike2.png")]
JUMPING = pygame.image.load("images/sprites/Bike2.png")
DUCKING = [pygame.image.load("images/sprites/BikeDuck1.png"),
           pygame.image.load("images/sprites/BikeDuck1.png")]


Traffic_Light = [pygame.image.load("images/obstacles/Traffic1.png"),
                pygame.image.load("images/obstacles/Traffic3.png"),
                pygame.image.load("images/obstacles/Traffic4.png")]
Traffic_Cone = [pygame.image.load("images/obstacles/RoadBlock.png"),
                pygame.image.load("images/obstacles/TrafficCone.png"),
                pygame.image.load("images/obstacles/TrafficCone2.png")]

DUST = [pygame.image.load("images/obstacles/Dust1.png"),
        pygame.image.load("images/obstacles/Dust2.png")]

BIRD = [pygame.image.load("images/obstacles/Bird1.png"),
        pygame.image.load("images/obstacles/Bird2.png")]

CAR = [pygame.image.load("images/obstacles/Car1.png"),
        pygame.image.load("images/obstacles/Car2.png")]


# 최종 스테이지 
ACC = 0.3
FRIC = -0.10

# HP 정보
PLAYER_HP   = 100
MONSTER_HP  = 100

CLOUD = pygame.image.load("images/obstacles/Cloud.png")


def pausing():
    global gameOver
    global gameQuit
    global paused
    gameOver = False
    gameQuit = False
    paused = False

    pygame.mixer.music.pause()

    pause_pic_surf = pygame.image.load("images/dialog/paused.png").convert_alpha()
    pause_pic_pos = (WIDTH - int(3.5*btn_menu_w), int(btn_menu_h))
    pause_btn = pause_pic_surf.get_rect(center=pause_pic_pos)

    # BUTTON IMG LOAD & POS
    home_img_surf = pygame.image.load("images/button/home.png").convert_alpha()
    home_pos = (WIDTH - int(8.8*btn_gameSetting_w), int(5* btn_menu_h))
    home_btn = home_img_surf.get_rect(center=home_pos)

    resume_img_surf = pygame.image.load("images/button/back.png").convert_alpha()
    resume_pos = (WIDTH - int(4.6*btn_gameSetting_w), int(5* btn_menu_h))
    resume_btn = resume_img_surf.get_rect(center=resume_pos)

    while not gameQuit:
        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            gameQuit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameQuit = True
                    gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()  # pausing상태에서 다시 esc누르면 배경음악 일시정지 해제
                        return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        x, y = event.pos
                        if home_btn.collidepoint(x, y):
                            gameOver = False
                            gameQuit = True
                            

                        if resume_btn.collidepoint(x, y):
                            pygame.mixer.music.unpause()  # pausing상태에서 오른쪽의 아이콘 클릭하면 배경음악 일시정지 해제
                            return False

            SCREEN.fill((255,255,255))
            SCREEN.blit(pause_pic_surf, pause_btn)
            SCREEN.blit(home_img_surf, home_btn)
            SCREEN.blit(resume_img_surf, resume_btn)
            pygame.display.update()

    pygame.quit()
    quit()


# 캐릭터 사이즈
PLAYER_SIZE     = (HEIGHT/4, HEIGHT/4)
MONSTER_SIZE    = (132,126)

# 공격 사이즈
LIGHT_SIZE = PLAYER_SIZE
MARBLE_SIZE = (WIDTH/23, WIDTH/23)
RAIN_SIZE = (WIDTH/23, HEIGHT/9)

# 플레이어(player) 설정
PLAYER_SPELL1_MP = 10
PLAYER_SPELL2_MP = 20
PLAYER_SPELL1_CASTTIME = 3.0
PLAYER_SPELL2_CASTTIME = 5.0
PLAYER_COOR_ini = vec(220, 350) # 플레이어 초기 위치
PLAYER_VELOCITY = vec(2,0)
PLAYER_VELOCITY_DASH = vec(0,0) # 대시 기능
PLAYER_ACCELERATION = vec(6,0)

HEALTH_ANI = [ pygame.image.load("images/sprites/life1.png"), pygame.image.load("images/sprites/life2.png")
            ,pygame.image.load("images/sprites/life3.png"), pygame.image.load("images/sprites/life4.png"),
            pygame.image.load("images/sprites/life5.png"), pygame.image.load("images/sprites/life6.png")]

running_l1 = pygame.image.load(os.path.join("images/sprites", "Bike1_L.png"))
running_l1 = pygame.transform.scale(running_l1, PLAYER_SIZE)
running_l2 = pygame.image.load(os.path.join("images/sprites", "Bike2_L.png"))
running_l2 = pygame.transform.scale(running_l2, PLAYER_SIZE)

running_R1 = pygame.image.load(os.path.join("images/sprites", "Bike1.png"))
running_R1 = pygame.transform.scale(running_R1, PLAYER_SIZE)
running_R2 = pygame.image.load(os.path.join("images/sprites", "Bike2.png"))
running_R2 = pygame.transform.scale(running_R2, PLAYER_SIZE)
DUCKING_L = [pygame.image.load(os.path.join("images/sprites", "BikeDuck1_L.png"))]
# RUNNING_L = pygame.transform.scale(RUNNING_L, PLAYER_SIZE)
# DUCKING_L = pygame.transform.scale(DUCKING_L, PLAYER_SIZE)

run_ani_L = [running_l2, running_l2]
run_ani_R = [running_R1, running_R2]

# 보스(MonsterElv) 설정
MonsterElv_POWER = 20
MonsterElv_POSITION = vec(0,0)
MonsterElv_COOR_ini = vec(680, 270) # 보스 초기 위치(왼쪽 향할 때)
MonsterElv_COOR_ini_R = vec(WIDTH - 680, 270) # 보스 초기 위치(오른쪽 향할 때)
MonsterElv_VELOCITY = vec(0,0)
MonsterElv_IMG_INFO = {'idleL': {'idx': 8, 'size': MONSTER_SIZE}, 
                        #'idleR': {'idx': 8, 'size': DEVIL_SIZE},
                    # 'attack1L': {'idx': 8, 'size': DEVIL_SIZE}, 'attack1R': {'idx': 8, 'size': DEVIL_SIZE},
                    # 'cast_thunderL':{'idx': 8, 'size': DEVIL_SIZE}, 'cast_thunderR':{'idx': 8, 'size': DEVIL_SIZE}, 
                    # 'deathL': {'idx': 7, 'size': DEVIL_SIZE}, 'deathR': {'idx': 7, 'size': DEVIL_SIZE},
                    # 'hurtL': {'idx': 3, 'size': DEVIL_SIZE}, 'hurtR': {'idx': 3, 'size': DEVIL_SIZE}
                    }

# 보스 스킬 설정
MonsterElv_ELECMARBLE_SIZE = (40,40)
MonsterElv_ELECMARBLE_INFO = {'elecmarble': {'idx': 11, 'size': MonsterElv_ELECMARBLE_SIZE}}
MonsterElv_ELECRAIN_SIZE = (40, 50)
MonsterElv_ELECRAIN_INFO = {'elecrain': {'idx': 14, 'size': MonsterElv_ELECRAIN_SIZE}}
MonsterElv_DAZZLE_TIME = 3.0


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
ingame_m =pygame.mixer.Sound("sound/MP_Dancing_piano.mp3")


