# Simple Animation with Pygame, Alan Andreoni, 12/8/2021, 7:02 pm v0.2

import pygame, sys, time
from pygame.locals import *

# Setup Pygame
pygame.innit()

# Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caltion('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4