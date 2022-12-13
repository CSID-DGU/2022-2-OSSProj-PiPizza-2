import pygame
from pygame.locals import *
from settings import *

class Sound:
    def __init__(self):
        pass
    
    # 메뉴화면 환경설정 함수
    def set_soundOn(self):
        print("소리 켜기 버튼 눌림")

        global bgm_on
        
        if not bgm_on:
            bgm_on = True
            background_m.play(-1)

        if ingame:
            background_m.stop()
            ingame_m.play(-1)
            

    # 메뉴화면 환경설정 함수
    def set_soundOff(self):
        print("소리 끄기 버튼 눌림")

        global bgm_on

        if bgm_on:
            bgm_on = False
            background_m.stop()
            ingame_m.stop()
            
