import pygame
from pygame.locals import *

size = width, height = (900, 400)
btn_start_w = int(width/6.8)
btn_start_h = int(height/9)

pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("배달의 달인")
screen.fill((60, 220, 0))

# draw graphics
pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width - int(3*btn_start_w), int(2.5* btn_start_h), btn_start_w, btn_start_h)
)

pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width - int(3.2*btn_start_w), int(4* btn_start_h), btn_start_w, btn_start_h)
)

pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width - int(3.4*btn_start_w), int(5.5* btn_start_h), btn_start_w, btn_start_h)
)

pygame.display.update()

flower = pygame.image.load("img.jpg")
flower = pygame.transform.scale(flower, (120, 133))
flower_loc = flower.get_rect()
flower_loc.center = 60, height/2

while running:
    flower_loc[1] += 1
    if flower_loc[1] > height:
        flower_loc[1] = -200

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]:
                flower_loc = flower_loc.move([-120,-133])
            if event.key in [K_RIGHT, K_d]:
                flower_loc = flower_loc.move([120, 133])


    screen.blit(flower, flower_loc)
    pygame.display.update()

pygame.quit()