# Pygame template - skeleton for a new pygame project

from Applications import nygame

FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialize pygame and create window

nygame.init()
screen = nygame.display.set_mode((500, 500))
nygame.display.set_caption("My Game")


print(screen,'andncnsn')

# Game loop
running = True
count = 0


def run():
    running=True
    while running:
        # keep loop running at the right speed
        # Process input (events)
        #print(pygame.event.get())

        for event in nygame.event.get():
            # check for closing window
            if event.type == nygame.QUIT:
                running = False



        # Update
        print('two')
        # Draw / render
        screen.fill(GREEN)

        # *after* drawing everything, flip the display
        nygame.display.flip()

    nygame.quit()

