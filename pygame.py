import importlib
importlib.import_module('pygame')
import pygame
operating_system = None
print('Hi')


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
    pass

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

display = display()
universal = universal()
screen = screen()
event = event()


set_mode((200,200))
display.flip()





