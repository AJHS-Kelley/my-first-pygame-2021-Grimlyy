# Pygame Practice, Alan Andreoni, 11/29/2021 8:35 am, v0.8

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

NAVYBLUE = (51, 17, 95)

# Setup Fonts
basicFont = pygame.font.SysFont(None, 48)

# Setup Text
text = basicFont.render('Hello, World!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw background onto window surface
windowSurface.fill(NAVYBLUE)

#draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw blue lines on the windowSurface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# Draw a circle
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw an ellipse
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw text background
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Get a pixel array
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# run the game loop.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()