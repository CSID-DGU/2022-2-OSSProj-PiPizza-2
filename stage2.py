# 변수 명 바꿔야 함

import pygame, sys
import os
import random
pygame.init()

# Global Constants

# 화면 타이틀 설정
pygame.display.set_caption("배달의 달인")


fullscreen = False

global isClear
isClear = False
start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

total_time = 30  # 총 시간

elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

SCREEN_HEIGHT = 450
SCREEN_WIDTH = 900
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# def resize(name, w, h, color):
#     global width, height, resized_screen
#     print("resized_screen: (",resized_screen.get_width(),",",resized_screen.get_height(),")")
#     return (name, w*resized_screen.get_width()//width, h*resized_screen.get_height()//height, color)

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

BG = pygame.image.load("images/obstacles/Track.png")





class Bike:
    X_POS = SCREEN_WIDTH/5 #90
    Y_POS = SCREEN_HEIGHT*0.66 #310
    Y_POS_DUCK = SCREEN_HEIGHT*0.75
    JUMP_VEL = SCREEN_HEIGHT/52.5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.bike_duck = False
        self.bike_run = True
        self.bike_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.bike_rect = self.image.get_rect()
        self.bike_rect.x = self.X_POS
        self.bike_rect.y = self.Y_POS


    def update(self, userInput):
        if self.bike_duck:
            self.duck()
        if self.bike_run:
            self.run()
        if self.bike_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0


        if userInput[pygame.K_UP] and not self.bike_jump:
            self.bike_duck = False
            self.bike_run = False
            self.bike_jump = True
        elif userInput[pygame.K_DOWN] and not self.bike_jump:
            self.bike_duck = True
            self.bike_run = False
            self.bike_jump = False
        elif not (self.bike_jump or userInput[pygame.K_DOWN]):
            self.bike_duck = False
            self.bike_run = True
            self.bike_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.bike_rect = self.image.get_rect()
        self.bike_rect.x = self.X_POS
        self.bike_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.bike_rect = self.image.get_rect()
        self.bike_rect.x = self.X_POS
        self.bike_rect.y = self.Y_POS
        self.step_index += 1


    def jump(self):
        self.image = self.jump_img
        if self.bike_jump:
            self.bike_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.bike_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.bike_rect.x, self.bike_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class TrafficLight(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = SCREEN_HEIGHT*2/3


class TrafficCone(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = SCREEN_HEIGHT*0.78


 
class Dust(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = SCREEN_HEIGHT*0.50
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1



def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Bike()
    cloud = Cloud()
    game_speed = 22.5
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    # def score():
    #     global points, game_speed
    #     points += 1
    #     if points % 100 == 0:
    #         game_speed += 1

    #     text = font.render("Points: " + str(points), True, (0, 0, 0))
    #     textRect = text.get_rect()
    #     textRect.center = (1000, 40)
    #     SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #SCREEN.fill((247, 155 , 96))
        SCREEN.fill((255, 255 , 255))        
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(TrafficLight(Traffic_Light))
            elif random.randint(0, 2) == 1:
                obstacles.append(TrafficCone(Traffic_Cone))
            elif random.randint(0, 2) == 2:
                obstacles.append(Dust(DUST))


        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.bike_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                elapsed_time = 0
                death_count += 1
                stageTwo(death_count)
   
        
        #시간
        elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
        timer = font.render("TIMER: "+str(int(elapsed_time)),True,(0,0,0))
        SCREEN.blit(timer,(10,10))

        if total_time - elapsed_time <= 0:
            print("Game Clear")
            timer = font.render(str(int(total_time-elapsed_time)),True,(0,0,0))
            timerRect = timer.get_rect()
            timerRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(timer, timerRect)
            death_count = -1
            run=False
            stageTwo(death_count)
            #run=False # 다이얼로그로 넘어가야 함


        background()

        cloud.draw(SCREEN)
        cloud.update()

       # score()
        clock.tick(30)
        pygame.display.update()




def clear(self):  # True를 반환하면 다시 시작
    pass

def fail(self):
    pass

def stageTwo(death_count):
    global points
    run = True
    while run:
        fullscreen = False
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

        #시작
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            elapsed_time = 0
        #Fail
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            total_time = 0
            #score = font.render("Your Score: " + str(points), Trpygame.image.load(os.path.joinue, (0, 0, 0))
            #scoreRect = score.get_rect()
            #scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            #SCREEN.blit(score, scoreRect)
        #클리어
        elif death_count < 0:
            text=font.render("Stage 2 Clear!", True, (0, 0, 0))
            isClear=True
            #stage 3로 넘어가는 코드
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                main()
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        SCREEN = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                    else:
                        SCREEN = pygame.display.set_mode((SCREEN.get_width(), SCREEN.get_height()), pygame.FULLSCREEN)

            # 스크린 리사이즈
            if event.type == pygame.VIDEORESIZE:
                if not fullscreen:
                    SCREEN = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)




# pygame.time.delay(100)
# stageTwo(death_count=0)
# pygame.quit()