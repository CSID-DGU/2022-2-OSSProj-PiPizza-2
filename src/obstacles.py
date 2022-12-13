import pygame
import random
from settings import *

class Bike:
    X_POS = WIDTH/5 #90
    Y_POS = HEIGHT*0.66 #310
    Y_POS_DUCK = HEIGHT*0.75
    JUMP_VEL = HEIGHT/52.5

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
        self.x = WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WIDTH

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
        self.rect.y = HEIGHT*2/3

class TrafficCone(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = HEIGHT*0.78

class Dust(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = HEIGHT*0.50
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1