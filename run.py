import pygame, sys
from pygame.locals import *
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("배달의 달인")
        self.clock = pygame.time.Clock()
        self.level = Level()

        # 메뉴 버튼 위치(center)
        btn_start_pos = (WIDTH - int(3*menu_btn_w), int(2.5* menu_btn_h))
        btn_quit_pos = (WIDTH - int(3.2*menu_btn_w), int(4* menu_btn_h))
        btn_game_setting_pos = (WIDTH - int(3.4*menu_btn_w), int(5.5* menu_btn_h))

        # 메뉴 버튼들
        self.btn_start
        self.btn_quit
        self.btn_game_setting
    
    
    # 메인 메뉴
    def menu(self):
        # 마우스 위치
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # 버튼 클릭
        if self.is_clicked:
            # 게임 시작
            if self.btn_start.collidepoint(mouse_x, mouse_y):
                self.run()
            # 게임 종료
            elif self.btn_quit.collidepoint(mouse_x, mouse_y):
                pygame.quit()
                sys.exit()
            # 환경설정
            elif self.btn_set.collidepoint(mouse_x, mouse_y):
                self.game_setting()
            else:
                pass

    # 메인 게임 시작
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # delta time 잘 모르겠음
            dt = self.clock.tick() / 1000
            self.level.run(dt)          
            pygame.display.update()
    
    # 환경설정
    def game_setting(self):
        pass
        # 사운드 슬라이더로 배경음악&효과음 볼륨 조절 가능하도록 구현
        


# checking if we are in the run file
# 게임 실행 (실행 시 시작화면은 메인 메뉴)
if __name__ == '__run__':
    game = Game()
    game.menu()

