# Simple program to see working of PyGame

# Import necessary modules
import sys, pygame

# Initialize PyGame
pygame.init()

size = width, height = 1280, 720        # Set window size
speed = [2, 2]          # Set movement speed
black = 0, 0, 0

screen = pygame.display.set_mode(size)      # Create graphical window

ball = pygame.image.load("intro_ball.gif")      # Load image
ballrect = ball.get_rect()          # For storing rectangular coordinates.

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)         # move ball with set speed
    # If ball goes outside the screen, we reverse the speed in that direction.
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)              # Fill screen with black color.
    screen.blit(ball, ballrect)     # Draw image onto screen.   
    pygame.display.flip()           # Make everything visible.
