
import pygame, sys
from pygame.locals import *
import os
# from run import *

pygame.init()
vec = pygame.math.Vector2

#화면 크기 및 FPS
SCREEN_SIZE = WIDTH, HEIGHT = (900, 450)
FPS = 60

# 게임 단계
GAME_STATES = [ 'stage1', 'stage2', 'stageFinal']

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
                pygame.image.load(
                    "images/obstacles/Traffic3.png"),
                pygame.image.load("images/obstacles/Traffic4.png")]
Traffic_Cone = [pygame.image.load("images/obstacles/RoadBlock.png"),
                pygame.image.load(
                    "images/obstacles/TrafficCone.png"),
                pygame.image.load("images/obstacles/TrafficCone2.png")]

DUST = [pygame.image.load("images/obstacles/Dust1.png"),
        pygame.image.load("images/obstacles/Dust2.png")]


# 최종 스테이지 
ACC = 0.3
FRIC = -0.10

# HP 정보
PLAYER_HP   = 100
MONSTER_HP  = 100

CLOUD = pygame.image.load("images/obstacles/Cloud.png")


'''
def pausing():
    global gameOver
    global gameQuit
    global resized_screen
    global paused
    gameQuit = False
    pause_pic, pause_pic_rect = pygame.image.load(os.path.join("images/Dialog",'paused.png', 360, 75, -1))
    pause_pic_rect.centerx = WIDTH * 0.5
    pause_pic_rect.centery = HEIGHT * 0.2

    # BUTTON IMG LOAD
    retbutton_image, retbutton_rect = pygame.image.load(os.path.join("images/Button",'home.png', 70, 62, -1))
    resume_image, resume_rect = pygame.image.load(os.path.join("images/Button",'back.png', 70, 62, -1))

    resized_retbutton_image, resized_retbutton_rect = pygame.image.load(os.path.join("images/Button",'home.png', 70, 62, -1))
    resized_resume_image, resized_resume_rect = pygame.image.load(os.path.join("images/Button",'back.png', 70, 62, -1))

    # BUTTONPOS
    retbutton_rect.centerx = WIDTH * 0.4
    retbutton_rect.top = HEIGHT * 0.52
    resume_rect.centerx = WIDTH * 0.6
    resume_rect.top = HEIGHT * 0.52

    resized_retbutton_rect.centerx = resized_screen.get_width() * 0.4
    resized_retbutton_rect.top = resized_screen.get_height() * 0.52
    resized_resume_rect.centerx = resized_screen.get_width() * 0.6
    resized_resume_rect.top = resized_screen.get_height() * 0.52

    while not gameQuit:
        if pygame.display.get_surface() is None:
            print("Couldn't load display surface")
            gameQuit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameQuit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.unpause()  # pausing상태에서 다시 esc누르면 배경음악 일시정지 해제
                        #첫번째 return 값은 pause상태, 두번째는 introFlag
                        return False, introFlag

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        x, y = event.pos
                        if resized_retbutton_rect.collidepoint(x, y):
                            introFlag = True
                            gameQuit = True
                            return None, introFlag

                        if resized_resume_rect.collidepoint(x, y):
                            pygame.mixer.music.unpause()  # pausing상태에서 오른쪽의 아이콘 클릭하면 배경음악 일시정지 해제
                            return False, introFlag

                if event.type == pygame.VIDEORESIZE:
                    checkscrsize(event.w, event.h)

            screen.fill(255,255,255)
            screen.blit(pause_pic, pause_pic_rect)
            screen.blit(retbutton_image, retbutton_rect)
            screen.blit(resume_image, resume_rect)
            pygame.display.update()


    pygame.quit()
    quit()
'''

# 캐릭터 사이즈
PLAYER_SIZE     = (HEIGHT/4, HEIGHT/4)
MONSTER_SIZE    = (140,136)

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


