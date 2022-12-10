
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
MonsterElv_IMG_INFO = {'idleL': {'idx': 8, 'size': MONSTER_SIZE} }


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

CLOUD = pygame.image.load("images/obstacles/Cloud.png")


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
