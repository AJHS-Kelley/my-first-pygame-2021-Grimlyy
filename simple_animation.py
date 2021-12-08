# Simple Animation with Pygame, Alan Andreoni, 12/8/2021, 6:58 pm v0.1

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.innit()

# Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caltion('Animation Example!')
