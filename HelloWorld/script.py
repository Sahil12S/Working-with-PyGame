# Printing "Hello World" on screen.

# Importing required libraries.
import pygame, sys
from pygame.locals import *

# Initialize PyGame modules.
pygame.init()

# Set display window size.
# set_mode() takes 2 item sequence and not int.
# @return - Surface object
DISPLAYSURF = pygame.display.set_mode((400, 300))
# Set Title of window.
pygame.display.set_caption('Hello World!')

while True:     # Main game loop.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
