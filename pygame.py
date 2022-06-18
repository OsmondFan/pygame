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

    def flip(self):
        pygame.display.update(rectangle=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1]))

    def update(self,rectangle=None):
        '''

        :param rectangle: pygame.Rect(x1,y1,x2,y2)
        :return:
        '''
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





