import importlib

import pygame
from pygame import*
operating_system = None
print('Hi')

console = None
scale_rate = (1,1)'''Meaning that the scale is 1x horizontal, 1x vertical'''

class display:
    def init(self):
        return False

    def __init__(self):
        self.screen = [[0,0],[0,0]]

    def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
        self.screen = [[0,0],[size[0],size[1]]]
        self.screensize = (size[0],size[1])

    def flip(self):
        pygame.display.update(rectangle=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1]))

    def update(self,rectangle=None):
        '''

        :param rectangle: pygame.Rect(x1,y1,x2,y2)
        if rectangle == None
        :rectangle=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1])

        if rectangle has parameters:
        scales: if a window is (1000,1000) and the secondary window is (500,500)
        the scale rate is: 2x, 2x
        which means every component in the window should have a scale of 2x
        component A is at (50,50), it then should be at (100,100) on main window
        then blitting area should be [x*scale(2x)][y*scale(2x)]
        if original rectangle update area
        :return:
        '''
        if rectangle == None:
            pygame.display.update(rectangle=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1]))
        else:
            pygame.display.update
        pass


def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
    global operating_system
    operating_system = pygame.display.set_mode(size, flags, depth, display, vsync)


class universal:
    def __init__(self):
        pass

    class display:
        def set_mode(self,start=(0,0),end=(0,0)):
            global console
            console = pygame.display.set_mode(start, end)


class movie:
    def __init__(self):
        pass

class event:
    def __init__(self):
        pass

    def get(self):
        return pygame.event.get()




class screen:
    def __init__(self):
        pass
    def init(self):
        pass

    def update(self):
        pass

    def blit(self,target=None,position=None):
        '''
        Again here in blitting, it couldn't just let pygame
        blit away the stuff.

        Blit has two parameters: target and position
        :param target: the picture or sprite that you want to
        move
        :param position: the destination point of the target
        after the move

        Getting the target picture, we need to resize it
        so that it fits inside the secondary window
        We already know the scale rate from the display:
        picture height=1 at first
        we need to change the scale of it(or smoothscale)
        pygame.transform.smoothscale(target,(target.get_width()*scale_rate[0],target.get_height()*scale_rate[1]))
        Okay. So now we got the resized picture and we are going
        to blit it onto the screen.
        screen.blit(\'''the previous line things\''', ...)

        moreover, the destination is actually just the same process
        as the one of update() used in the display class
        -->
        if rectangle has parameters:
        scales: if a window is (1000,1000) and the secondary window is (500,500)
        the scale rate is: 2x, 2x
        which means every component in the window should have a scale of 2x
        component A is at (50,50), it then should be at (100,100) on main window
        then blitting area should be [x*scale(2x)][y*scale(2x)]
        if original rectangle update area
        -->

        Here we can use
        screen.blit(..., (position[0]*scale_rate[0],position[1]*scale_rate[1]))



        :return: None
        '''
        constant = pygame.transform.smoothscale(target,(target.get_width()*scale_rate[0],target.get_height()*scale_rate[1]))
        screen.blit(constant, (position[0]*scale_rate[0],position[1]*scale_rate[1]))



display = display()
universal = universal()
screen = screen()
event = event()


set_mode((200,200))
display.flip()




pygame.transform.smoothscale()