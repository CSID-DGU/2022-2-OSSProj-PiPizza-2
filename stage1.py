import pygame, sys
import os
import random
import time
from settings import *
from obstacles import *

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #디스플레이 설정
        pygame.display.set_caption("배달의 달인") #게임 제목

        #FPS 초당 프레임
        self.clock = pygame.time.Clock()
        self.level = Level()

        # 클릭 이벤트 (종료(quit))
        self.is_clicked = False

        # 버튼 위치(center)
        self.btn_start_pos = (WIDTH - int(2*btn_menu_w), int(2.5* btn_menu_h))
        self.btn_exit_pos = (WIDTH - int(2.2*btn_menu_w), int(4* btn_menu_h))
        self.btn_gameSetting_pos = (WIDTH - int(2.4*btn_menu_w), int(5.5* btn_menu_h))
        
        self.btn_soundOn_pos = (WIDTH - int(8.5*btn_gameSetting_w), int(4* btn_menu_h))
        self.btn_soundOff_pos = (WIDTH - int(6.5*btn_gameSetting_w), int(4* btn_menu_h))
        self.btn_backToMenu_pos = (WIDTH - int(3.8*btn_menu_w), int(6* btn_menu_h))

        self.import_assets() # 이미지 로드

    def import_assets(self):
         # 이미지 폴더 경로
        self.path_images = 'images/'
        self.path_btn = 'images/Button/'
        self.path_bg = 'images/background/'

        # 메뉴화면 배경
        self.background_surf = pygame.image.load(f'{self.path_bg}menu_background.png').convert_alpha()
        self.background_set_surf = pygame.image.load(f'{self.path_bg}menu_background_set_b.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (WIDTH, HEIGHT))
        self.background_set_surf = pygame.transform.scale(self.background_set_surf, (WIDTH, HEIGHT))
        self.background_rect = self.background_surf.get_rect(topleft=(0, 0))
        self.background_set_rect = self.background_set_surf.get_rect(topleft=(0, 0))

        #stage1 배경 
        self.stage1_bg_surf = pygame.image.load(f'{self.path_bg}menu_background.png').convert_alpha()
        self.stage1_bg_surf = pygame.transform.scale(self.background_surf, (WIDTH, HEIGHT))
        self.stage1_bg_rect = self.background_surf.get_rect(topleft=(0, 0))
        
        # 메뉴화면 버튼들
        self.btn_start_surf = pygame.image.load(f'{self.path_btn}btn_start_.png').convert_alpha()
        self.btn_start = self.btn_start_surf.get_rect(center=self.btn_start_pos)
        self.btn_exit_surf = pygame.image.load(f'{self.path_btn}btn_exit_.png').convert_alpha()
        self.btn_exit = self.btn_exit_surf.get_rect(center=self.btn_exit_pos)
        self.btn_gameSetting_surf = pygame.image.load(f'{self.path_btn}btn_gameSetting_.png').convert_alpha()
        self.btn_gameSetting = self.btn_gameSetting_surf.get_rect(center=self.btn_gameSetting_pos)

        # 환경설정화면 버튼들
        self.btn_soundOn_surf = pygame.image.load(f'{self.path_btn}btn_soundOn_.png').convert_alpha()
        self.btn_soundOff_surf = pygame.image.load(f'{self.path_btn}btn_soundOff_.png').convert_alpha()
        self.btn_backToMenu_surf = pygame.image.load(f'{self.path_btn}btn_backToMenu_.png').convert_alpha()
        self.btn_soundOn = self.btn_soundOn_surf.get_rect(center=self.btn_soundOn_pos)
        self.btn_soundOff = self.btn_soundOff_surf.get_rect(center=self.btn_soundOff_pos)
        self.btn_backToMenu = self.btn_backToMenu_surf.get_rect(center=self.btn_backToMenu_pos)

    def menu(self):
        self.intro()
        while True:
            self.screen.blit(self.background_surf, self.background_rect)
            #self.SCREEN.fill((255, 255, 255))
            #font = pygame.font.Font('freesansbold.ttf', 30)

            # mouse info
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # 버튼 클릭 시
            if self.is_clicked:
                # 게임 시작
                if self.btn_start.collidepoint(mouse_x, mouse_y):
                    self.run()
                # 게임 종료
                elif self.btn_exit.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    sys.exit()
                # 환경설정
                elif self.btn_gameSetting.collidepoint(mouse_x, mouse_y):
                    self.gameSetting()
                else:
                    pass

            # 마우스 클릭 이벤트 체크
            self.check_click()

            # 화면 업데이트
            self.screen.blit(self.btn_start_surf, self.btn_start)
            self.screen.blit(self.btn_exit_surf, self.btn_exit)
            self.screen.blit(self.btn_gameSetting_surf, self.btn_gameSetting)
           
            pygame.display.update()

    def intro(self):
        intro_number = 1
        while True:
            if intro_number == 1: # 게임 이름 화면
                self.screen.blit(self.background_surf, self.background_rect)

            elif intro_number == 2: # 게임 배경(스토리) 설명 화면
                self.screen.blit(self.stage1_bg_surf, self.stage1_bg_rect)

            else:
                return

            if self.is_return_key_pressed():
                intro_number += 1

            pygame.display.update()

    def run(self):
        self.level = Level()
        self.game_start_time = pygame.time.get_ticks() # 현재 tick 을 받아옴
        while True:
            time = (pygame.time.get_ticks() - self.game_start_time)/1000
            self.level.time = time
            
            for event in pygame.event.get():
                quit_check(event)

            df = self.clock.tick(FPS)
            self.level.run(df)
            pygame.display.update()

            if self.level.done:
                break

        self.game_end_time = pygame.time.get_ticks()
        self.time_score = (self.game_end_time - self.game_start_time) / 1000

        if self.level.is_clear: # 클리어했으면
            pass
        else: # 졌으면
            self.lose()

    def lose(self):
        while True:
            self.screen.blit(self.lose_background_surf, self.lose_background_rect)

            if self.is_return_key_pressed():
                self.intro_music.play()
                return

            # 화면 업데이트
            pygame.display.update()

    # 마우스 클릭 체크
    def check_click(self):
        self.is_clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_clicked = True
        
    # 환경설정
    def gameSetting(self):
        
        while True:
            self.screen.blit(self.background_set_surf, self.background_set_rect)
            # 마우스 위치
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # 클래스 Sound의 sound 인스턴스 생성
            sound = Sound()
            
            # 버튼 클릭 시
            if self.is_clicked:
                # 소리 켜기
                if self.btn_soundOn.collidepoint(mouse_x, mouse_y):
                    sound.set_soundOn()
                # 소리 끄기
                elif self.btn_soundOff.collidepoint(mouse_x, mouse_y):
                    sound.set_soundOff()
                # 메뉴로 돌아가기
                elif self.btn_backToMenu.collidepoint(mouse_x, mouse_y):
                    self.menu()
                else:
                    pass
            
            # 마우스 클릭 이벤트 체크
            self.check_click()

            # 화면 업데이트
            self.screen.blit(self.btn_soundOn_surf, self.btn_soundOn)
            self.screen.blit(self.btn_soundOff_surf, self.btn_soundOff)
            self.screen.blit(self.btn_backToMenu_surf, self.btn_backToMenu)
            
            pygame.display.update()
    
    def is_return_key_pressed(self):
        for event in pygame.event.get():
            quit_check(event)


class Level:
    def __init__(self):
        self.scene_num = 0
        self.game_state = GAME_STATES[self.scene_num]
        self.stage_changing = False
        self.can_change_stage = True
        self.time = None

        self.display_surface = pygame.display.get_surface()
        self.main()

        self.is_clear = False
        self.done = False

    def main(self):
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
        total_time = 10

        def background():
            global x_pos_bg, y_pos_bg
            image_width = BG.get_width()
            self.SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
            self.SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width:
                self.SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
                x_pos_bg = 0
            x_pos_bg -= game_speed

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.SCREEN.fill((255, 255 , 255))        
            userInput = pygame.key.get_pressed()

            self.player.draw(self.SCREEN)
            self.player.update(userInput)

            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(TrafficLight(Traffic_Light))
                elif random.randint(0, 2) == 1:
                    obstacles.append(TrafficCone(Traffic_Cone))
                elif random.randint(0, 2) == 2:
                    obstacles.append(Dust(DUST))
       

            for obstacle in obstacles:
                obstacle.draw(self.SCREEN)
                obstacle.update()
                if player.bike_rect.colliderect(obstacle.rect):
                    pygame.time.delay(2000)
                    elapsed_time = 0
                    death_count += 1
                    death(death_count)

        
                #시간
            timer = font.render("TIMER: "+str(int(elapsed_time)),True,(0,0,0))
            self.SCREEN.blit(timer,(10,10))

            if total_time - elapsed_time <= 0:
                timer = font.render(str(int(total_time-elapsed_time)),True,(0,0,0))
                timerRect = timer.get_rect()
                timerRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
                self.SCREEN.blit(timer, timerRect)

            cloud.draw(self.SCREEN)
            cloud.update()

            # score()
            pygame.display.update()

    def death(self, death_count):
        global points
        run = True
        while run:
            self.SCREEN.fill((255, 255, 255))
            font = pygame.font.Font('freesansbold.ttf', 30)

            if death_count == 0:
                text = font.render("Press any Key to Start", True, (0, 0, 0))
                elapsed_time = 0
            elif death_count > 0:
                text = font.render("Press any Key to Continue", True, (0, 0, 0))
                score = font.render("Your Time: " + points), True, (0, 0, 0)
                scoreRect = score.get_rect()
                scoreRect.center = (WIDTH // 2, HEIGHT // 2 + 50)
                self.SCREEN.blit(score, scoreRect)
            
                textRect = text.get_rect()
                textRect.center = (WIDTH // 2, HEIGHT // 2)
                self.SCREEN.blit(text, textRect)
                self.SCREEN.blit(RUNNING[0], (WIDTH // 2 - 20, HEIGHT // 2 - 140))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                    if event.type == pygame.KEYDOWN:
                        run()


    def run(self, df):
        self.scene.updata(df, self.time)
        self.scene_manager(self.scene)

    def scene_manager(self, scene):
        scene_change = False
        for event in pygame.event.get():
            quit_check(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                scene.fade_out()
                scene_change = True

        if scene_change:
            if self.scene_num < len(GAME_STATES) - 1:
                self.scene_num += 1
            else:
                self.scene_num = 0
                self.is_clear = True
                self.done = True

            self.game_state = GAME_STATES[self.scene_num]

            #씬 받기
            self.player.scene_num = self.scene_num

    

class Sound:
    def __init__(self):
        pass
    
    # 메뉴화면 환경설정 함수
    def set_soundOn(self):
        print("소리 켜기 버튼 눌림")
    # 메뉴화면 환경설정 함수
    def set_soundOff(self):
        print("소리 끄기 버튼 눌림")

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,PLAYER_SIZE, groups, obstacle_sprites):
        pygame.sprite.Sprite.__init__(self, groups)
        self.scene_num = 0



if __name__ == '__main__':
    game = Game()
    game.menu()