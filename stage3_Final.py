import pygame
from pygame.locals import *
import sys
import random
import time
from tkinter import filedialog
from tkinter import *

from settings import *
from level import *
# from stage2 import *
from description import *

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
          
class LightAttack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player = Player()
        self.direction = player.direction
        if self.direction == "RIGHT":
            self.image = pygame.image.load("images/sprites/LightAttack.png")
        else:
            self.image = pygame.image.load("images/sprites/LightAttack_L.png")           
        self.rect = self.image.get_rect(center = player.pos)
        self.rect.x = player.pos.x
        self.rect.y = player.pos.y - 40
    
    def light(self):
        player = Player()
        player.magic_cooldown = 0
        # Runs while the fireball is still within the screen w/ extra margin
        if -10 < self.rect.x < 900:
            if self.direction == "RIGHT":
                  self.image = pygame.image.load("images/sprites/LightAttack.png")
                  displaysurface.blit(self.image, self.rect)
            else:
                  self.image = pygame.image.load("images/sprites/LightAttack_L.png")
                  displaysurface.blit(self.image, self.rect)
                   
            if self.direction == "RIGHT":
                  self.rect.move_ip(12, 0)
            else:
                  self.rect.move_ip(-12, 0)   
        else:
            self.kill()
            player.magic_cooldown = 1
            player.attacking = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 

        # 플레이어 움직임
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.move_frame = 0

        self.bike_run = True
        self.bike_jump = False
        
        self.imgP = run_ani_R[0]
        # self.imgP = pygame.image.load("images/sprites/Bike1.png")
        self.imgP = pygame.transform.scale(self.imgP, PLAYER_SIZE)
        #"images/sprites", "Bike1.png"
        self.rect = self.imgP.get_rect()

        # 공격할 때
        # self.imgPA = pygame.transform.scale(self.imgPA, )
        self.attacking = False
        self.cooldown = False
        self.magic_cooldown = 1
        self.experiance = 0
        self.mana = 0
        # 목숨 일단 6개
        self.health = 6

        self.vx = 0
        self.pos = PLAYER_COOR_ini
        self.vel = PLAYER_VELOCITY
        self.acc = PLAYER_ACCELERATION
        self.direction = "RIGHT"

        # 라이트 공격 아님
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
        if self.pos[0] > WIDTH:
                self.pos[0] = 0
        if self.pos[0] < 0:
                self.pos[0] = WIDTH
        
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

        # 가만히 있을 때 기본 프레임으로 설정
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
        self.rect.x += 5
        ground = Ground()
        # 바닥에 닿았는지 확인하기
        hits = pygame.sprite.spritecollide(self, ground_group, False)

        self.rect.x -= 5

        # 바닥에 닿았고, 점프 중인 상태가 아니면, 점프하게 하기
        if hits and not self.bike_jump:
            self.bike_jump = True
            self.vel.y = -17.5

    # def jumpAndRun(self):
    #     self.rect.x += 1

    #     # 바닥에 닿았는지 확인하기
    #     hits = pygame.sprite.spritecollide(self, ground_group, False)

    #     self.rect.x -= 1

    #     # 바닥에 닿았고, 점프 중인 상태가 아니면, 점프하게 하기
    #     if hits and not self.bike_jump:
    #         self.bike_jump = True
    #         self.vel.y = -15
    #         if self.direction == "RIGHT":
    #             self.vel.x = 20
    #         else:
    #             self.vel.x = -20

    # # 최종 스테이지 숙이기 기능 없음
    # def duck(self):
    #     super.duck()

    def gravity_check(self):
      hits = pygame.sprite.spritecollide(player, ground_group, False)
      if self.vel.y > 0:
          if hits:
              lowest = hits[0]
              if self.pos[1] < lowest.rect.bottom:
                  self.pos[1] = lowest.rect.top + 1
                  self.vel.y = 0
                  self.bike_jump = False

    # 대시 기능 - 쿨타임 미적용
    def dash(self):
        hits = pygame.sprite.spritecollide(player, ground_group, False)
        # if hits and not self.bike_jump:
        if hits:
            if self.direction == "RIGHT":
                self.vel.x = 13
            if self.direction == "LEFT":
                self.vel.x = -13

    def player_hit(self):
        if self.cooldown == False:
            self.cooldown = True #cooldown 가능하게 함
            pygame.time.set_timer(hit_cooldown, 1000)

            self.health = self.health - 1

            HEALTH_ANI = [pygame.image.load("images/sprites/life0.png"), pygame.image.load("images/sprites/life1.png"), pygame.image.load("images/sprites/life2.png")
                        ,pygame.image.load("images/sprites/life3.png"), pygame.image.load("images/sprites/life4.png"),
                        pygame.image.load("images/sprites/life5.png"), pygame.image.load("images/sprites/life6.png")]
            health.image = HEALTH_ANI[self.health]

            if self.health <= 0:
                self.kill()
                pygame.display.update()

            print("피격")
            print(self.health)
            pygame.display.update()
    



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imgM = pygame.image.load("images/sprites/monsterElv.png")
        self.imgM = pygame.transform.scale(self.imgM, MONSTER_SIZE)
        self.rect = self.imgM.get_rect()
        self.vel = MonsterElv_VELOCITY
        self.pos = MonsterElv_POSITION

        self.direction = random.randint(0,1) # 0: 오른쪽 향함   1: 왼쪽 향함
        self.vel.x = 4.5 # 보스 속도 고정
        self.mana = 6 # 플레이어가 공격하면 마나를 준다 -무효

        if self.direction == 0:
            self.pos = MonsterElv_COOR_ini_R
            self.imgM = pygame.image.load("images/sprites/monsterElv_R.png")
            self.imgM = pygame.transform.scale(self.imgM, MONSTER_SIZE)
        if self.direction == 1:
            self.pos = MonsterElv_COOR_ini
            self.imgM = pygame.image.load("images/sprites/monsterElv.png")
            self.imgM = pygame.transform.scale(self.imgM, MONSTER_SIZE)

    def move(self):
        # Causes the enemy to change directions upon reaching the end of screen    
        if self.pos.x >= (WIDTH-125):
                self.direction = 1
                self.imgM = pygame.image.load("images/sprites/monsterElv.png")
                self.imgM = pygame.transform.scale(self.imgM, MONSTER_SIZE)
        elif self.pos.x <= 0:
                self.direction = 0
                self.imgM = pygame.image.load("images/sprites/monsterElv_R.png")
                self.imgM = pygame.transform.scale(self.imgM, MONSTER_SIZE)
        # 이동하기
        if self.direction == 0: # 왼쪽 향할 때
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
        
        self.rect.center = self.pos # Updates rect

    def update(self):
         # 플레이어와의 충돌
        hits = pygame.sprite.spritecollide(self, Playergroup, False)

         # 플레이어의 라이트공격과의 충돌
        l_hits = pygame.sprite.spritecollide(self, LightAttacks, False)
 
         # 공격 불리언 태그
        if hits and player.attacking == True or l_hits:
            self.kill()
            if player.mana < 100: player.mana += self.mana # 무효
            player.experiance += 1  # 무효
            #print("Enemy killed")
        elif hits and player.attacking == False:
            player.player_hit()
 
        # If collision has occured and player not attacking, call "hit" function            
        elif hits and player.attacking == False:
            player.player_hit()

    def render(self):
        # 그리기
        displaysurface.blit(self.imgM, self.pos)

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/sprites/life6.png")

    def render(self):
        displaysurface.blit(self.image, (10,10))

enemy = Enemy()
player = Player()
# player.direction = "RIGHT"
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
health = HealthBar()

LightAttacks = pygame.sprite.Group()
hit_cooldown = pygame.USEREVENT + 1
font = pygame.font.Font('freesansbold.ttf', 20)

class Stage3:
    def __init__(self):
        # self.enemy = Enemy()
        # self.player = Player()
        # # player.direction = "RIGHT"
        # self.Playergroup = pygame.sprite.Group()
        # self.Playergroup.add(self.player)

        # self.background = Background()
        # self.ground = Ground()
        # self.ground_group = pygame.sprite.Group()
        # self.ground_group.add(self.ground)
        # self.health = HealthBar()

        # self.LightAttacks = pygame.sprite.Group()
        # self.hit_cooldown = pygame.USEREVENT + 1
        self.hp = player.health
        

    def timeReset():
        global elapsed_time
        elapsed_time = 0
        

        # elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

    def run3(self):
        # 게임 실행
        
        while True:
            start_ticks = pygame.time.get_ticks()
            player.gravity_check()   
            # press any key
            userInput = pygame.key.get_pressed()

            # 시간
            total_time = 60  # 총 시간
            elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

            timer = font.render("TIMER: "+str(int(elapsed_time)), True, (0,0,0))
            displaysurface.blit(timer, (10,10))

            if total_time - elapsed_time <= 0:
                print("Game Clear")
                timer = font.render(str(int(total_time - elapsed_time)), True, (0,0,0))
                timerRect = timer.get_rect()
                timerRect.center = (WIDTH//2, HEIGHT//2+50)
                displaysurface.blit(timer, timerRect)
                player.health = -1
                run = False
                dial = Description()
                dial.clear3()

            if player.health == 0:
                stage3.run3()
            for event in pygame.event.get():
                if event.type == hit_cooldown:
                    player.cooldown = False
                    pygame.time.set_timer(hit_cooldown, 0)
                # Event handling for a range of different key presses    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.jump()
                    # if event.key == pygame.K_UP and (pygame.K_LEFT or pygame.K_RIGHT):
                    #     player.jumpAndRun()
                    if event.key == pygame.K_p:
                        if player.attacking == False:
                            player.attack()
                    if event.key == pygame.K_a and player.magic_cooldown == 1:     # a 키 누르면 공격
                    # if event.key == pygame.K_a:     # a 키 누르면 공격
                        if player.mana >= 6:
                            player.mana -= 6
                            player.attacking = True
                            lightAttack = LightAttack()
                            LightAttacks.add(lightAttack)

                    if event.key == pygame.K_d:
                            player.dash()
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

            if player.health > 0:
                displaysurface.blit(player.imgP, player.rect)
            health.render()

            for attack in LightAttacks:
                attack.light()

            enemy.render()
            enemy.move()
            enemy.update()

            pygame.display.update() 

            FPS_CLOCK.tick(FPS)
            # print(enemy.vel.x)

    def stageThree(Self):
        stage3 = Stage3()
        run = True
        while run:
        # SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        # #게임 시작 시 나오는 이미지
        # background_img =  pygame.image.load('images/background/stage2_bg.png')

        # #self.background_img_rect = self.background_img.get_rect()
        # #self.background_img_rect.x = self.X_POS
        # #self.background_img_rect.y = self.Y_POS
        # SCREEN.blit(background_img, (0,0))
            bgimage = pygame.image.load("images/background/stage3_bg.png")
            bgimage_rect = bgimage.get_rect(topleft=(0, 0))
            displaysurface.blit(bgimage, (bgimage_rect.x, bgimage_rect.y))
                
            font = pygame.font.Font('freesansbold.ttf', 30)

            #시작
            if player.health > 0:
                text = font.render("Press any Key to Start", True, (0, 0, 0))
                #timeReset()
        
            #Fail
            if player.health == 0:
                text = font.render("Continue?", True, (0, 0, 0))
                # scoreRect = score.get_rect()
                # scoreRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
                # displaysurface.blit(score, scoreRect)

                # stage3.run3()

            #클리어
            elif player.health < 0:
                text=font.render("Stage 3 Clear!", True, (0, 0, 0))
                dial = Description()
                dial.clear3()

            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            displaysurface.blit(text, textRect)
            displaysurface.blit(RUNNING[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    # sys.exit()
                if event.type == pygame.KEYDOWN:
                    stage3.stageThree()
                    # if event.key == pygame.K_f:
                    #     fullscreen = not fullscreen
                    #     if fullscreen:
                    #         SCREEN = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                    #     else:
                    #         SCREEN = pygame.display.set_mode((SCREEN.get_width(), SCREEN.get_height()), pygame.FULLSCREEN)

                # # 스크린 리사이즈
                # if event.type == pygame.VIDEORESIZE:
                #     if not fullscreen:
                #         SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)              



if __name__ == '__main__':
    stage3 = Stage3()
    stage3.stageThree()