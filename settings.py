import pygame, sys
import os
pygame.init()

#화면 크기
SCRREEN_SIZE = WIDTH, HEIGHT = (900, 450)
FPS = 60

#게임 장면 이름
GAME_STATES = ['stage1', 'stage2', 'stage3']

# 메뉴화면 버튼 크기
btn_menu_w = int(WIDTH/6.8)
btn_menu_h = int(HEIGHT/8)
btn_gameSetting_w = int(btn_menu_w/2)

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


def quit_check(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()