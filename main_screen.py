import pygame
from pygame.locals import *

size = width, height = (800, 800)


pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("배달의 달인")
screen.fill((60, 220, 0))

# draw graphics
pygame.draw.rect(
    screen,
    (50, 50, 50),
    (width/2, height/2, int(width/3), int(height/3))
)

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()