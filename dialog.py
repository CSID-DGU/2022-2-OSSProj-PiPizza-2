import time
import pygame, sys
from settings import *

class Game:
    def __init__(self):
        #general setup
        pygame.init()  # 초기화 init 호출
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # 디스플레이 뜨게 하기
        pygame.display.set_caption("배달의 민족")  # 게임 이름

        # FPS
        self.clock = pygame.time.Clock()

        self.import_assets() # 이미지 등을 모두 로드해놓고 시작하기


    def import_assets(self):
        self.main_path = 'images/'
        # 메뉴 레이아웃
        self.leading = 50

        # dialog
        self.dialog1_surf = pygame.image.load(f'{self.main_path}Dialog/dialog1.png').convert_alpha()
        self.dialog1_surf = pygame.transform.scale(self.dialog1_surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.dialog1_rect = self.dialog1_surf.get_rect(topleft=(0, 0))

        self.dialog2_surf = pygame.image.load(f'{self.main_path}Dialog/dialog2.png').convert_alpha()
        self.dialog2_rect = self.dialog2_surf.get_rect(topleft=(0, 0))

        self.dialog3_surf = pygame.image.load(f'{self.main_path}Dialog/dialog3.png').convert_alpha()
        self.dialog3_rect = self.dialog3_surf.get_rect(topleft=(0, 0))

    def menu(self): # 맨 처음 시작. 메뉴 화면
        self.intro()
        while True:
            # mouse info
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # 이벤트 체크
            self.click_check()

            #self.fade_in()
            pygame.display.update()


    def intro(self): # 처음 시작화면.
        intro_number = 1
        while True:
            if intro_number == 1:
                self.screen.blit(self.dialog1_surf, self.dialog1_rect)

            elif intro_number == 2:
                self.screen.blit(self.dialog2_surf, self.dialog2_rect)

            elif intro_number == 3:
                self.screen.blit(self.dialog3_surf, self.dialog3_rect)
            else:
                return

            # 엔터키 누르면 다음 화면으로 넘어감. + intro_number == 4 가 되면 intro() 종료하고 메뉴로 넘어감.
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro_number += 1

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.menu()