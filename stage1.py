import pygame
import os

#https://www.youtube.com/watch?v=KbKMqxVw8x0 - 점수판, 배경

#pygame 초기화
pygame.init()

#전역 변수
SCREEN_HEIGHT = 600 #화면 높이 설정
SCREEN_WIDTH = 1100 #화면 넓이 설정
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#화면 타이틀 설정
pygame.display.set_caption("PiPizza")

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"sprites")

RUNNING = [pygame.image.load(os.path.join(image_path,"delivery.png"))]
DUNKING = [pygame.image.load(os.path.join(image_path,"delivery_lying.png"))]
JUMPING = [pygame.image.load(os.path.join(image_path,"delivery.png"))]

class Delivery:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.duck_img = DUNKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.deli_duck = False
        self.deli_run = True
        self.deli_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.deli_rect = self.image.get_rect()
        self.deli_rect.x = self.X_POS
        self.deli_rect.y = self.Y_POS

    def update(self, userInput):
        if self.deli_duck:
            self.duck()
        if self.deli_run:
            self.run()
        if self.deli_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.deli_jump:
            self.deli_duck = False
            self.deli_run = False
            self.deli_jump = True
        elif userInput[pygame.K_DOWN] and not self.deli_jump:
            self.deli_duck = True
            self.deli_run = False
            self.deli_jump = False
        elif not (self.deli_jump or userInput[pygame.K_DOWN]):
            self.deli_duck = False
            self.deli_run = True
            self.deli_jump = False

    def duck(self):
        self.image = self.run_img[self.step_index // 5]
        self.deli_rect = self.image.get_rect()
        self.deli_rect_x = self.X_POS
        self.deli_rect_y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.deli_rect = self.image.get_rect()
        self.deli_rect_x = self.X_POS
        self.deli_rect_y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.deli_jump:
            self.deli_rect_y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.deli_jump = False
            self.jump_vel = self.JUMP_VEL


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.deli_rect_x, self.deli_rect_y))

'''      
class Bird:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50,100)
        self.image = Bird
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed


    def draw(self, SCREEN):
'''



def main():
    global game_speed
    run = True
    clock = pygame.time.Clock()
    player = Delivery()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()


if __name__ == "__main__":
    main()