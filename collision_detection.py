#Pygame Collision Dection Practice, Alan Andreoni, 1/7/22 6:06 pm, v0.2

import pygame, sys, random
from pygame.locals import *
from simple_animation import WINDOWHEIGHT, WINDOWWIDTH

# Setup PyGame
pygame.init()
mainClock = pygame.time.Clock()

# Setup the PyGame Window
WINDOWWIDTH= 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 32)
pygame.display.set_caption('Collision Detection 2022')