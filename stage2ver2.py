import pygame
import os
import sys
import random

# setting ----------------------------------------------
# 게임 초기화
pygame.init()

#게임창 크기
scr_size = (width, height) = (900, 450)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
full_screen=False

FPS = 60
gravity=0.65
font = pygame.font.Font('DungGeunMo.ttf', 32)
# 현재 그래픽 너비, 높이 환경 정보 받아와 모니터 사이즈 설정
monitor_size = (monitor_width, monitor_height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

#위 2-1 로 게임창 크기 적용
resized_screen = pygame.display.set_mode((scr_size), pygame.RESIZABLE)
# screen 변수에 크기옵션 집어넣어 앞으로 그릴 내용 담음
screen = resized_screen.copy()

#resizing?
resized_screen_centerpos = (0,0)
rwidth = resized_screen.get_width()
rheight = resized_screen.get_height()
button_offset = 0.18

# 화면 타이틀 설정
pygame.display.set_caption("배달의 달인")

# 3. 게임 내 필요한 설정
# 3-1. 시계 생성(향후 FPS 생성시 활용)
clock = pygame.time.Clock()

dino_size = [44, 47]
object_size = [40, 40]
ptera_size = [46, 40]
collision_immune_time = 500
shield_time = 2000
speed_up_limit_count = 700


def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('sprites', name)
    # 이미지 불러옴
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

# 투명한 이미지 불러오기
def alpha_image(name, sizex=-1, sizey=-1,color_key=None):
    full_name = os.path.join('sprites', name)
    #ubuntu ver : full_name = os.path.join('/home/q202-14/2022-1-OSSProj-JiwooKids-5/sprites', name)
    img = pygame.image.load(full_name)
    if color_key is not None:
        if color_key == -1:
            color_key = img.get_at((0, 0))
        img.set_colorkey(color_key, pygame.RLEACCEL)
    if sizex != -1 or sizey != -1:
        img = pygame.transform.scale(img, (sizex, sizey))
    img.convert_alpha()
    return (img, img.get_rect())


def load_sprite_sheet(
        sheetname,
        nx,
        ny,
        scalex = -1,
        scaley = -1,
        colorkey = None,
        ):
    fullname = os.path.join('sprites', sheetname)
    # sheet = pygame.image.load(fullname)
    # sheet = sheet.convert()
    sheet, sheet_rect = alpha_image(sheetname, -1, -1, -1)

    sheet_rect = sheet.get_rect()

    sprites = []

    sizex = sheet_rect.width/nx
    sizey = sheet_rect.height/ny

    for i in range(0,ny):
        for j in range(0,nx):
            rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
            image = pygame.Surface(rect.size)
            image = image.convert()
            #이미지 어느 위치에 넣을지
            image.blit(sheet,(0,0),rect)

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey,pygame.RLEACCEL)

            if scalex != -1 or scaley != -1:
                image = pygame.transform.scale(image,(scalex,scaley))

            sprites.append(image)

    sprite_rect = sprites[0].get_rect()

    return sprites, sprite_rect


def checkscrsize(eventw, eventh):
    if (eventw < width and eventh < height) or eventw < width or eventh < height: #최소해상도
        resized_screen = pygame.display.set_mode((scr_size), pygame.BLEND_MINRESIZABLE)
    else:
        if eventw/eventh!=width/height: #고정화면비
            adjusted_height=int(eventw/(width/height))
            resizedreen = pygame.display.set_mode((eventw,adjusted_height), pygame.RESIZABLE)


def full_screen_issue():
    global scr_size
    resized_screen = pygame.display.set_mode((scr_size), pygame.RESIZABLE)
    resized_screen = pygame.display.set_mode((scr_size), pygame.RESIZABLE)


def resize(name, w, h, color):
        global width, height, resized_screen
        print("resized_screen: (",resized_screen.get_width(),",",resized_screen.get_height(),")")
        return (name, w*resized_screen.get_width()//width, h*resized_screen.get_height()//height, color)

def textsize(size):
    font = pygame.font.Font('DungGeunMo.ttf', size)
    return font


#obstacles -----------------

class Traffic_Light(pygame.sprite.Sprite): #장애물 1.신호등
    def __init__(self, speed=5, sizex=-1, sizey=-1):
        pygame.sprite.Sprite.__init__(self,self.containers) #Sprite를 사용하면 이미지, 위치, 충돌 처리를 통합해서 처리
        self.images, self.rect = load_sprite_sheet('Traffic1.png', 3, 1, sizex, sizey, -1)
        self.rect.bottom = int(0.9*height)
        self.rect.left = width + self.rect.width
        self.image = self.images[random.randrange(0,3)] #0과 3 사이의 난수를 반환
        self.movement = [-1*speed, 0] #캐릭터에게 speed의 속도로 다가옴

    def draw(self): #self.image와 rect를 screen에 삽입
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()

RUNNING = [pygame.image.load(os.path.join(("images/sprites", "Bike1.png")),
           pygame.image.load(os.path.join("images/sprites", "Bike2.png")))]
JUMPING = pygame.image.load(os.path.join("images/sprites", "Bike2.png"))
DUCKING = [pygame.image.load(os.path.join("images/sprites", "BikeDuck1.png")),
           pygame.image.load(os.path.join("images/sprites", "BikeDuck1.png"))]


Traffic_Light = [pygame.image.load(os.path.join("images/obstacles", "Traffic1.png")),
                pygame.image.load(os.path.join(
                    "images/obstacles", "Traffic3.png")),
                pygame.image.load(os.path.join("images/obstacles", "Traffic4.png"))]
Traffic_Cone = [pygame.image.load(os.path.join("images/obstacles", "RoadBlock.png")),
                pygame.image.load(os.path.join(
                    "images/obstacles", "TrafficCone.png")),
                pygame.image.load(os.path.join("images/obstacles", "TrafficCone2.png"))]

DUST = [pygame.image.load(os.path.join("images/obstacles", "Dust1.png")),
        pygame.image.load(os.path.join("images/obstacles", "Dust2.png"))]

CLOUD = pygame.image.load(os.path.join("images/obstacles", "Cloud.png"))

BG = pygame.image.load(os.path.join("images/obstacles", "Track.png"))

class Dino():
    def __init__(self, sizex=-1, sizey=-1,type = None):
        
        # 디노의 타입을 결정합니다. 
        self.type = type

        # 해당하는 디노의 스킨을 가져와서 적용
        if type == 'ORIGINAL':
            self.images, self.rect = load_sprite_sheet('dino_arrange.png', 14, 1, sizex, sizey, -1)
            # self.images, self.rect = load_sprite_sheet('pinkdino.png', 6, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png', 8, 1, 59, sizey, -1)
            # self.images1, self.rect1 = load_sprite_sheet('pinkdino_ducking.png', 2, 1, 59, sizey, -1)
        elif type == 'PINK':
            self.images, self.rect = load_sprite_sheet('dino_pink.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_pink_ducking.png', 8, 1, 59, sizey, -1)
        elif type == 'RED':
            self.images, self.rect = load_sprite_sheet('dino_red.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_red_ducking.png', 8, 1, 59, sizey, -1)    
        elif type == 'ORANGE':
            self.images, self.rect = load_sprite_sheet('dino_orange.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_orange_ducking.png', 8, 1, 59, sizey, -1) 
        elif type == 'YELLOW':
            self.images, self.rect = load_sprite_sheet('dino_yellow.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_yellow_ducking.png', 8, 1, 59, sizey, -1)
        elif type == 'GREEN':
            self.images, self.rect = load_sprite_sheet('dino_green.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_green_ducking.png', 8, 1, 59, sizey, -1)
        elif type == 'PURPLE':
            self.images, self.rect = load_sprite_sheet('dino_purple.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_purple_ducking.png', 8, 1, 59, sizey, -1)  
        elif type == 'BLACK':
            self.images, self.rect = load_sprite_sheet('dino_black.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_black_ducking.png', 8, 1, 59, sizey, -1)    
        else: 
            self.images, self.rect = load_sprite_sheet('dino_arrange.png', 14, 1, sizex, sizey, -1)
            self.images1, self.rect1 = load_sprite_sheet('dino_ducking.png', 8, 1, 59, sizey, -1)

        self.rect.bottom = int(0.9*height)
        self.rect.left = width/15
        self.image = self.images[0]
        self.index = 0
        self.counter = 0
        self.score = 0
        self.score2 = 0
        self.item_time = 0
        self.isJumping = False
        self.isDead = False
        self.isDucking = False
        self.isBlinking = False
        self.movement = [0, 0]
        self.jumpSpeed = 11.5
        self.superJumpSpeed = self.jumpSpeed * 1.3
        self.collision_immune = False
        self.isSuper = False

        # 아이템 사용 상태
        self.Superglass = False
        self.Sovel = False
        self.Mask = False

        self.stand_pos_width = self.rect.width
        self.duck_pos_width = self.rect1.width

    def draw(self):
        screen.blit(self.image, self.rect)

    def checkbounds(self):
        if self.rect.bottom > int(0.9*height):
            self.rect.bottom = int(0.9*height)
            self.isJumping = False

    def update(self):
        # 1. movement y값 변경
        if self.isJumping: 
            self.movement[1] = self.movement[1] + gravity # 움직임의 y값에 gravity값을 더해 점프 높이를 적용

        # 2. Dino의 상황별 모션 구현
        if self.Superglass: # 안경쓰고 있을 때
            if self.isJumping: self.index = 5 # 뛰고있을 때
            # 걸어갈 때
            if self.isDucking: # 숙이고있으면
                if self.counter % 5 == 0: 
                    if self.index==2: self.index=3
                    elif self.index==3: self.index=2
                    else: self.index=2
            else: # 서있으면
                if self.counter % 5 == 0: 
                    if self.index == 6: self.index=7
                    elif self.index == 7: self.index=6
                    else: self.index = 6

        elif self.Sovel: # 삽들고 있을 때
            if self.isJumping: self.index = 8 # 뛰고있을 때
            # 걸어갈 때
            if not self.isDucking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==9: self.index=10
                    elif self.index==10: self.index=9
                    else: self.index=9
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==4: self.index=5
                    elif self.index==5: self.index=4
                    else: self.index=4

        elif self.Mask: # 마스크 쓰고 있을 때
            if self.isJumping: self.index = 11 # 뛰고있을 때
            # 걸어갈 때
            if not self.isDucking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==12: self.index=13
                    elif self.index==13: self.index=12
                    else: self.index=12
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==6: self.index=7
                    elif self.index==7: self.index=6
                    else: self.index=6

        # elif self.isBlinking: # 눈 깜빡이기
        #     if self.index == 0:
        #         if self.counter % 400 == 399:
        #             self.index = 2
        #     else:
        #         if self.counter % 20 == 19:
        #             self.index = 2

        else: # 아무것도 안입고 있을 때
            if self.isJumping: self.index = 0 # 뛰고있을 때
             # 걸어갈 때
            if not self.isDucking: # 서있으면
                if self.counter % 5 == 0:
                    if self.index==2: self.index=3
                    elif self.index==3: self.index=2
                    else: self.index=2
            else: # 숙이고있으면
                if self.counter % 5 == 0:
                    if self.index==0: self.index=1
                    elif self.index==1: self.index=0
                    else: self.index=0

        if self.isDead: # 죽었을 경우
            self.index = 4

        if self.collision_immune:
            if self.counter % 10 == 0: self.index = 2

        # 숙이고 있는 모션 구현
        if not self.isDucking:
            if self.counter % 5 == 0:
                self.image = self.images[self.index]
            self.rect.width = self.stand_pos_width
        else:
            if self.counter % 5 == 0: 
                self.image = self.images1[self.index]
            if self.collision_immune is True:
                if self.counter % 5 == 0:
                    self.image = self.images[5]
            self.rect.width = self.duck_pos_width

        self.rect = self.rect.move(self.movement)
        self.checkbounds()

        if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
            self.score += 1
            self.score2 += 1
            self.item_time += 1
            if self.score % 100 == 0 and self.score != 0:
                if pygame.mixer.get_init() != None:
                    checkPoint_sound.play()

        self.counter = (self.counter + 1)


## 시작 화면 ##
def introscreen():
    # pygame.mixer.music.play(-1)  # 배경음악 실행
    global resized_screen

    # temp_dino를 전역변수로 설정합니다.
    global temp_dino
    global type_idx
    global dino_type
    dino_type = ['ORIGINAL','RED','ORANGE','YELLOW','GREEN','PURPLE','BLACK','PINK']
    type_idx = 0
    ALPHA_MOVE = 20
    click_count = 0
    #
    temp_dino = Dino(dino_size[0], dino_size[1])
    temp_dino.isBlinking = True
    gameStart = False

    ###이미지 로드###
    # 배경 이미지
    alpha_back, alpha_back_rect = alpha_image('intro_bg.png', width + ALPHA_MOVE, height)
    alpha_back_rect.left = -ALPHA_MOVE
    # 버튼 이미지
    r_btn_gamestart, r_btn_gamestart_rect = load_image(*resize('btn_start.png', 150, 50, -1))
    btn_gamestart, btn_gamestart_rect = load_image('btn_start.png', 150, 50, -1)
    r_btn_board, r_btn_board_rect = load_image(*resize('btn_board.png', 150, 50, -1))
    btn_board, btn_board_rect = load_image('btn_board.png', 150, 50, -1)
    r_btn_option, r_btn_option_rect = load_image(*resize('btn_option.png', 150, 50, -1))
    btn_option, btn_option_rect = load_image('btn_option.png', 150, 50, -1)
    # DINO IMAGE