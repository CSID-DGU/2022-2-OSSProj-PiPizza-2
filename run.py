import pygame, sys
from pygame.locals import *
from settings import *
from level import *

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
        self.btn_start_pos = (WIDTH - int(3*btn_menu_w), int(2.5* btn_menu_h))
        self.btn_exit_pos = (WIDTH - int(3.2*btn_menu_w), int(4* btn_menu_h))
        self.btn_gameSetting_pos = (WIDTH - int(3.4*btn_menu_w), int(5.5* btn_menu_h))
        
        self.btn_soundOn_pos = (WIDTH - int(4.2*btn_menu_w), int(3* btn_menu_h))
        self.btn_soundOff_pos = (WIDTH - int(3.2*btn_menu_w), int(3* btn_menu_h))

        self.btn_backToMenu_pos = (WIDTH - int(3*btn_menu_w), int(6* btn_menu_h))

        self.import_assets() # 이미지 로드


    def import_assets(self):
        # 이미지 폴더 경로
        self.path_images = 'images/'
        # 메뉴 레이아웃? 어디서 쓰이는지 모르겠음
        self.leading = 50

        # 메뉴화면 배경
        self.background_surf = pygame.image.load(f'{self.path_images}temp_menu_background.png').convert_alpha()
        self.background_surf = pygame.transform.scale(self.background_surf, (WIDTH, HEIGHT))
        self.background_rect = self.background_surf.get_rect(topleft=(0, 0))

        # 종료 버튼 -> 게임 종료, 화면 닫음
        # self.exit_button_surf = pygame.image.load(f'{self.main_path}menu_exit.png').convert_alpha()
        # self.exit_button = self.exit_button_surf.get_rect(center=self.exit_button_pos)
        
        # 메뉴화면 버튼들
        self.btn_start_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_start = self.btn_start_surf.get_rect(center=self.btn_start_pos)
        self.btn_exit_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_exit = self.btn_exit_surf.get_rect(center=self.btn_exit_pos)
        self.btn_gameSetting_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_gameSetting = self.btn_gameSetting_surf.get_rect(center=self.btn_gameSetting_pos)
        # 환경설정화면 버튼들
        self.btn_soundOn_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_soundOff_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_backToMenu_surf = pygame.image.load(f'{self.path_images}temp_btn_menu.png').convert_alpha()
        self.btn_soundOn = self.btn_soundOn_surf.get_rect(center=self.btn_soundOn_pos)
        self.btn_soundOff = self.btn_soundOff_surf.get_rect(center=self.btn_soundOff_pos)
        self.btn_backToMenu = self.btn_backToMenu_surf.get_rect(center=self.btn_backToMenu_pos)
    
    
    # 메인 메뉴화면
    def menu(self):
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
                elif self.btn_set.collidepoint(mouse_x, mouse_y):
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


    # 메인 게임 시작
    def run(self):
        self.level = Level()
        while True:
            for event in pygame.event.get():
                quit(event)

            # delta time 잘 모르겠음
            df = self.clock.tick(FPS)
            self.level.run(df)          
            pygame.display.update()
    
    def check_click(self):
        self.is_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.is_clicked = True
            quit(event)

    # 환경설정
    def gameSetting(self):
        
        # 사운드 슬라이더로 배경음악&효과음 볼륨 조절 가능하도록 구현
        # 이 아니라 소리 끄고 켜기로 수정함

        while True:
            self.screen.blit(self.background_surf, self.background_rect)
            
            mouse_x, mouse_y = pygame.mouse.get_pos()

             # 버튼 클릭 시
            if self.is_clicked:
                if self.btn_soundOn.collidepoint(mouse_x, mouse_y):
                    self.soundOn()
                elif self.btn_soundOff.collidepoint(mouse_x, mouse_y):
                    self.soundOff()
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

    def soundOn(self):
        pass

    def soundOff(self):
        pass

    def quit(event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

         
# checking if we are in the run file
# 게임 실행 (실행 시 시작화면은 메인 메뉴)
# 실행 안 되는 문제를 해결했는데, 원래 코드 '__run__'을 run 대신 main으로 바꾸(고 변수와 조건문을 일부 주석처리하)니 해결됨 이유는 모르겠다.
if __name__ == '__main__':
    game = Game()
    game.menu()

