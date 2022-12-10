import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *

from settings import *
from level import *
from stage2 import *

pygame.init()  # pygame 시작
vec = pygame.math.Vector2
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# 디스플레이 가져오기
displaysurface = pygame.display.get_surface()
pygame.display.set_caption("배달의 달인")

# 색상
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 
  
# 글꼴
headingfont = pygame.font.SysFont("Verdana", 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 
text = regularfont.render('LOAD' , True , color_light)
 



class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("images/background/stage3_bg.png")
            self.bgimage_rect = self.bgimage.get_rect(topleft=(0, 0))
      def render(self):
            displaysurface.blit(self.bgimage, (self.bgimage_rect.x, self.bgimage_rect.y))
            

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgGround = pygame.image.load("images/background/ground_3.png")
        self.rect = self.imgGround.get_rect(center = (500, 430))

    def render(self):
        displaysurface.blit(self.imgGround, (self.rect.x, self.rect.y))     
          

class Player(pygame.sprite.Sprite, Bike):
    def __init__(self):
        super().__init__() 

        # 플레이어 움직임
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.move_frame = 0

        self.bike_duck = False
        self.bike_run = True
        self.bike_jump = False
        
        self.imgP = run_ani_R[0]
        # self.imgP = pygame.image.load("images/sprites/Bike1.png")
        self.imgP = pygame.transform.scale(self.imgP, PLAYER_SIZE)
        #"images/sprites", "Bike1.png"
        self.rect = self.imgP.get_rect()

        # 공격할 때
        # self.imgPA = pygame.transform.scale(self.imgPA, )

        self.vx = 0
        self.pos = PLAYER_COOR_ini
        self.vel = PLAYER_VELOCITY
        self.acc = PLAYER_ACCELERATION
        self.direction = "RIGHT"

        # 라이트 공격
        self.attacking = False
        self.attack_frame = pygame.image.load("images/sprites/LightEffect.png")
        self.attack_frame = pygame.transform.scale(self.attack_frame, LIGHT_SIZE)
        self.attack_frame_L = pygame.image.load("images/sprites/LightEffect_L.png")
        self.attack_frame_L = pygame.transform.scale(self.attack_frame, LIGHT_SIZE)


    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        self.acc = vec(0,0.5)
    
        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
                self.bike_run = True
        else:
                self.bike_run = False
    
        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()
    
        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
                self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
                self.acc.x = ACC 
    
        # Formulas to calculate velocity while accounting for friction
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values
    
        # This causes character warping from one point of the screen to the other
        if self.pos.x > WIDTH:
                self.pos.x = 0
        if self.pos.x < 0:
                self.pos.x = WIDTH
        
        self.rect.midbottom = self.pos  # Update rect with new pos 

     
    
    def update(self):
        # 움직임 마지막에는 기본 프레임 반환
        if self.move_frame > 1:
            self.move_frame = 0
            return

        # 조건 충족 시 다음 프레임으로 바꿈
        if self.bike_run == True:  
            if self.vel.x > 0:
                    self.imgP = run_ani_R[self.move_frame]
                    self.direction = "RIGHT"
            else:
                    self.imgP = run_ani_L[self.move_frame]
                    self.direction = "LEFT"
            self.move_frame += 1

        # Returns to base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                    self.imgP = run_ani_R[self.move_frame]
            elif self.direction == "LEFT":
                    self.imgP = run_ani_L[self.move_frame]
                
    def attack(self):
        if self.direction == "RIGHT":
            self.imgP = self.attack_frame
        elif self.direction == "LEFT":
            self.imgP = self.attack_frame_L

    def jump(self):
        self.rect.x += 1

        # 바닥에 닿았는지 확인하기
        hits = pygame.sprite.spritecollide(self, ground_group, False)

        self.rect.x -= 1

        # 바닥에 닿았고, 점프 중인 상태가 아니면, 점프하게 하기
        if hits and not self.bike_jump:
            self.bike_jump = True
            self.vel.y = -12

    def duck(self):
        super.duck()

    def gravity_check(self):
      hits = pygame.sprite.spritecollide(player, ground_group, False)
      if self.vel.y > 0:
          if hits:
              lowest = hits[0]
              if self.pos.y < lowest.rect.bottom:
                  self.pos.y = lowest.rect.top + 1
                  self.vel.y = 0
                  self.bike_jump = False
    

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
 
      
    
player = Player()
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

# 게임 실행
while True:
    player.gravity_check()   
    for event in pygame.event.get():
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                  player.jump()
            if event.key == pygame.K_a:     # a 키 누르면 공격
                if player.attacking == False:
                    player.attack()
                    player.attacking = True
        # Will run when the close window button is clicked    
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
            
        # For events that occur upon clicking the mouse (left click) 
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass


        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
              pass

    # 불러오기(그리기) ------
    background.render() 
    ground.render()
    player.update()
    if player.attacking == True:
        player.attack() 
    player.move()
    displaysurface.blit(player.imgP, player.rect)
 
    pygame.display.update() 

    FPS_CLOCK.tick(FPS)