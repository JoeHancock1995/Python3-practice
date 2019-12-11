import pygame, sys

from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, BLACK, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.rect(DISPLAYSURF, WHITE, (0, 80 , 200, 20))
pygame.draw.circle(DISPLAYSURF, BLACK, (300, 50), 20, 0)
pygame.draw.rect(DISPLAYSURF, WHITE, (200, 150, 100, 20))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
