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
#nygame.init()
print(nygame.event.get())
screen = nygame.display.set_mode((200, 200))
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
        print('1')
        for event in nygame.event.get():
            # check for closing window
            if event.type == nygame.QUIT:
                running = False
        print('2')

        #Detect closure mode
        '''
        if nygame.processor.status == 0:
            exit(1)
        '''

        # Update
        print('one')
        # Draw / render
        screen.fill(RED)

        # *after* drawing everything, flip the display
        nygame.display.flip()

    nygame.quit()

def off():
    exit(1)