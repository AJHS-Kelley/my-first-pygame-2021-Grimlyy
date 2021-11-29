# Pygame Practice, Alan Andreoni, 11/29/2021 8:35 am, v0.3

import pygame, sys
from pygame.locals import *

# start pygame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, World!')

# Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

#Setup Text
text = basicFont.render('Hello, World!', True, WHITE, BLUE)

