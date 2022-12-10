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
        self.imgGround_rect = self.imgGround.get_rect(center = (500, 430))

    def render(self):
        displaysurface.blit(self.imgGround, (self.imgGround_rect.x, self.imgGround_rect.y))     
          

class Player(pygame.sprite.Sprite, Bike):
    def __init__(self):
        super().__init__() 

        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.bike_duck = False
        self.bike_run = True
        self.bike_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        
        self.imgP = self.run_img[0]
        self.imgPrect = self.imgP.get_rect()

        self.vx = 0
        self.pos = PLAYER_COOR_ini
        self.vel = PLAYER_VELOCITY
        self.acc = PLAYER_ACCELERATION
        self.direction = "RIGHT"


    def move(self):
        # Keep a constant acceleration of 0.5 in the downwards direction (gravity)
        #self.acc = vec(0,0.5)
    
        # Will set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
                self.running = True
        else:
                self.running = False
    
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
        
        self.imgPrect.midbottom = self.pos  # Update rect with new pos 

     
    
    def update(self, userInput):
        super.update(userInput)

    def attack(self):
        pass

    def jump(self):
        super.jump()

    def duck(self):
        super.duck()
    

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
 
      
    
player = Player()
background = Background()
ground = Ground()

while True:
      
    for event in pygame.event.get():
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
    player.move()
    displaysurface.blit(player.imgP, player.imgPrect)
 
    pygame.display.update() 

    FPS_CLOCK.tick(FPS)