# Drawing lines.

# Import necessary modules.
import sys, pygame
from pygame.locals import *

# Initialize pygame.
pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
# Second parameter of render() method sets anti-aliasing ON or OFF.
textSurfaceObj = fontObj.render('Hello World!!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()     # set width and height of the text.
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
