import pygame, sys
import os
import random
import time
from settings import *
from obstacles import *

class Game:
    def __init__(self):
        pygame.init()
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #디스플레이 설정
        pygame.display.set_caption("배달의 달인") #게임 제목

        #배경음악

        #FPS 초당 프레임
        self.clock = pygame.time.Clock()
        self.level = Level()
        
        #플레이어 기록 설정
        self.user_name = "이름 입력"
        self.game_start_time = None #stage1 시작 시간
        self.game_end_time = None #stage3 클리어 시간
        self.time_score = None #게임 끝났을 때 시간 계산 후 저장

    def run(self):
        self.level = Level()
        self.game_start_time = pygame.time.get_ticks() # 현재 tick 을 받아옴
        while True:
            time = (pygame.time.get_ticks() - self.game_start_time)/1000
            self.level.time = time

            df = self.clock.tick(FPS)
            self.level.run(df)

            if self.level.done:
                break
        
        self.game_end_time = pygame.time.get_ticks()
        self.time_score = (self.game_end_time - self.game_start_time) / 1000

        if self.level.is_clear:
            self.win()
        else:
            self.lose()

    def win(self):
        self.user_name = "이름 입력"

    def lose(self):
        while True:
            
            if self.is_return_key_pressed():
                self.intro_music.play()
                return

    def is_return_key_pressed(self):
        for event in pygame.event.get():
            quit_check(event)

            

isClear = False
total_time = 10 #총 시간


class Level:
    def __init__(self):
        self.stage_changing = False
        self.can_change_stage = True

        self.time = None
        self.is_clear = False
        self.done = False

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Bike()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def win(self):
        print("Game clear")


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
                menu(death_count)

        
        #시간
        timer = font.render("TIMER: "+str(int(elapsed_time)),True,(0,0,0))
        
        SCREEN.blit(timer,(10,10))

        if total_time - elapsed_time <= 0:
            timer = font.render(str(int(total_time-elapsed_time)),True,(0,0,0))
            timerRect = timer.get_rect()
            timerRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            SCREEN.blit(timer, timerRect)


        background()

        cloud.draw(SCREEN)
        cloud.update()

       # score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
            elapsed_time = 0
        elif death_count > 0:
            text = font.render("Press any Key to Continue", True, (0, 0, 0))
            score = font.render("Your Time: " + points), True, (0, 0, 0)
            scoreRect = score.get_rect()
            scoreRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)

pygame.time.delay(100)
pygame.quit()