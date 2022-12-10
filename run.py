import pygame, sys
import os
from pygame.locals import *
from settings import *

from level import *
from sound import *
from description import *
from stage2 import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("배달의 달인")
        
        self.clock = pygame.time.Clock()
        self.level = Level()

        # 클릭 이벤트 (종료(quit))
        self.is_clicked = False

        # 버튼 위치(center)
        self.btn_start_pos = (WIDTH - int(2.2*btn_menu_w), int(2.5* btn_menu_h))
        self.btn_exit_pos = (WIDTH - int(2.4*btn_menu_w), int(4* btn_menu_h))
        self.btn_gameSetting_pos = (WIDTH - int(2.6*btn_menu_w), int(5.5* btn_menu_h))
        
        self.btn_soundOn_pos = (WIDTH - int(8.3*btn_gameSetting_w), int(4* btn_menu_h))
        self.btn_soundOff_pos = (WIDTH - int(6.3*btn_gameSetting_w), int(4* btn_menu_h))
        self.btn_backToMenu_pos = (WIDTH - int(3.6*btn_menu_w), int(6* btn_menu_h))

        self.import_assets() # 이미지 로드

        # 디스크립션(다이얼로그)
        self.dial = Description()


    def import_assets(self):
        
        # 이미지 폴더 경로
        self.path_images = 'images/'
        self.path_btn = 'images/Button/'
        self.path_bg = 'images/background/'
        # self.path_dial = 'images/Dialog/'
        # self.path_obstcls = 'images/obstacles/'
        # self.path_sprts = 'images/sprites/'
        
        # 메뉴 레이아웃? 어디서 쓰이는지 모르겠음
        # self.leading = 50

        # 메뉴화면 배경
        self.background_surf = pygame.image.load(f'{self.path_bg}menu_background.png').convert_alpha()
        self.background_set_surf = pygame.image.load(f'{self.path_bg}menu_background_set_b.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (WIDTH, HEIGHT))
        self.background_set_surf = pygame.transform.scale(self.background_set_surf, (WIDTH, HEIGHT))
        self.background_rect = self.background_surf.get_rect(topleft=(0, 0))
        self.background_set_rect = self.background_set_surf.get_rect(topleft=(0, 0))
        
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

        # 다이얼로그

        
    
    
    # 메인 메뉴화면
    def menu(self):

        if bgm_on:
            pass
        background_m.play(-1) # 배경음악 실행

        while True:
            self.screen.blit(self.background_surf, self.background_rect)
        
            # 마우스 위치
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

    def checkClear(self):
        if stageTwo().isClear == True:
            self.level.isOneClear = True

    # 메인 게임 시작
    def run(self):
        
        if bgm_on:
            background_m.stop()
            ingame_m.play(-1) 

        # dial1
        self.dial.dial1()
        #self.dial.clear1_dial2()
        
        while True:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = not paused
                        paused_value, return_home_value = pausing()
                        if paused_value != None:
                            paused = paused_value
                        else:
                            introFlag = return_home_value
                            gameQuit = True
                            return introFlag

            stageTwo(death_count=0)

            # delta frame으로 수정
            df = self.clock.tick(FPS)
            self.level.run(df)          
            pygame.display.update()

            

            # 게임 클리어 플래그 (while문 탈출 및 시간 저장)
            if self.level.isOneClear or self.level.isTwoClear or self.level.isFinalClear:
                break 
        
        # 클리어 시간 저장
        #


        # 게임 클리어 시 (단계별 클리어 시 설명화면)
        if self.level.isOneClear:
            self.dial.clear1_dial2()
        elif self.level.isTwoClear:
            self.dial.clear2_dial3()
        elif self.level.isFinalClear:
            self.dial.clear3()
            #
        else:
            pass

            
    
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
        
        # 사운드 슬라이더로 배경음악&효과음 볼륨 조절 가능하도록 구현
        # 이 아니라 소리 끄고 켜기로 수정함
        
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

    # def quit(event):
    #     if event.type == QUIT:
    #         pygame.quit()
    #         sys.exit()

         
# checking if we are in the run file?
# 게임 실행 (실행 시 시작화면은 메인 메뉴)
# 실행 안 되는 문제를 해결했는데, 원래 코드 '__run__'을 run 대신 main으로 바꿈
if __name__ == '__main__':
    game = Game()
    game.menu()