import pygame, sys
import os
import random
import time
from settings import *
from obstacles import *

# Global Constants

# 화면 타이틀 설정
pygame.display.set_caption("배달의 달인")


fullscreen = False

global isClear
isClear = False
paused = False
start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

total_time = 30  # 총 시간

elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000

def timeReset():
    elapsed_time = 0

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

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN_SIZE.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN_SIZE.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN_SIZE.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.key == pygame.K_ESCAPE:
                paused = not paused
                paused = pausing()

        SCREEN_SIZE.fill((255, 255 , 255))        
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN_SIZE)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(TrafficLight(Traffic_Light))
            elif random.randint(0, 2) == 1:
                obstacles.append(TrafficCone(Traffic_Cone))
            elif random.randint(0, 2) == 2:
                obstacles.append(Dust(DUST))


        for obstacle in obstacles:
            obstacle.draw(SCREEN_SIZE)
            obstacle.update()
            if player.bike_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                elapsed_time = 0
                death_count += 1
                stageOne(death_count)
   
        
        #시간
        elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
        timer = font.render("TIMER: "+str(int(elapsed_time)),True,(0,0,0))
        SCREEN_SIZE.blit(timer,(10,10))

        if total_time - elapsed_time <= 0:
            print("Game Clear")
            timer = font.render(str(int(total_time-elapsed_time)),True,(0,0,0))
            timerRect = timer.get_rect()
            timerRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            SCREEN_SIZE.blit(timer, timerRect)
            death_count = -1
            run=False
            stageOne(death_count)
            #run=False # 다이얼로그로 넘어가야 함


        background()

        cloud.draw(SCREEN_SIZE)
        cloud.update()

       # score()
        clock.tick(30)
        pygame.display.update()




def clear(self):  # True를 반환하면 다시 시작
    pass

def fail(self):
    pass

def stageOne(death_count):
    global points
    run = True
    isClear=False
    while run:
        fullscreen = False
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

        #시작
        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        #Fail
        elif death_count > 0:
            text = font.render("GAME OVER!", True, (0, 0, 0))
            timeReset()
            #score = font.render("Your Score: " + str(points), Trpygame.image.load(os.path.joinue, (0, 0, 0))
            #scoreRect = score.get_rect()
            #scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            #SCREEN.blit(score, scoreRect)
        #클리어
        elif death_count < 0:
            text=font.render("Stage 1 Clear!", True, (0, 0, 0))
            isClear=True
            #stage 3로 넘어가는 코드
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
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