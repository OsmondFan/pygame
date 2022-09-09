# Pygame template - skeleton for a new pygame project
import time
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


# Game loop
running = True
count = 0
start = time.time()

while running:
    # keep loop running at the right speed
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    count+=1
    now = time.time()
    fps = count/(now-start)
    fpsImage = myfont.render(str(fps), True, WHITE)
    # Draw / render
    screen.fill(BLACK)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

