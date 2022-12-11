import importlib

import pygame as Pygame

import sys  # 导入sys模块
sys.setrecursionlimit(100000000)  # 将默认的递归深度修改为100000000



#import moviepy

#import threading
from Applications.test1.test import nylon

nylon.event = nylon.EVENT()

operating_system = None
print('Hi')


scale_rate = (1,1)#Meaning that the scale is 1x horizontal, 1x vertical

class DISPLAY:
    def init(self):
        return False

    def __init__(self):
        self.screen = [[0,0],[0,0]]

    def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
        self.screen = [[0,0],[size[0],size[1]]]
        self.screensize = (size[0],size[1])
        print(console)
        return console


    def flip(self):
        #a = threading.Thread(target=Pygame.display.update,args=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1])).start()
        Pygame.display.update(self.screen[0][0], self.screen[0][1], self.screen[1][0], self.screen[1][1])

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
            Pygame.display.update(rectangle=(self.screen[0][0],self.screen[0][1],self.screen[1][0],self.screen[1][1]))
        else:
            Pygame.display.update(rectangle=())

    def move_window(self,x,y):
        self.screen = [[0+x,0+y],[size[0]+x,size[1]+y]]
        return True

    def set_caption(self,name):
        pass

def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
    global operating_system
    operating_system = Pygame.display.set_mode(size, flags, depth, display, vsync)

def init():
    pass

class UNIVERSAL:
    def __init__(self):
        pass

    class display:
        def set_mode(self,window=(0,0)):
            global console

            print(window[0],window[1],type(window[0]),type(window[1]))
            console = Pygame.display.set_mode((window[0],window[1]))
            return console

        def set_caption(self,name):
            Pygame.display.set_caption(str(name))


class movie:
    def __init__(self):
        pass

    def show(self):
        moviepy.show()



class EVENT:
    def __init__(self):
        self.event = []

    def get(self):
        print('2r')
        self.event = nylon.event.get()
        print('3')
        return self.event

    '''
    error: Event reacheed maxium recursion depth
    fix: because the name is also called pygame.
    it continues to do the same line for many times.
    Also, the "event" name cannot be used as a 
    variable.
    
    Pygame.init()
    
    event = EVENT()
    
    print(event.get())
    '''

class SCREEN:
    def __init__(self):
        pass

    def init(self):
        pass

    def update(self):
        pass

    def fill(self,color=(0,0,0)):
        Pygame.console.fill(color)



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
        console.blit(..., (position[0]*scale_rate[0],position[1]*scale_rate[1]))



        :return: None

        constant = pygame.transform.smoothscale(target,(target.get_width()*scale_rate[0],target.get_height()*scale_rate[1]))
        console.blit(constant, (position[0]*scale_rate[0],position[1]*scale_rate[1]))
        '''


class MIXER:
    def __init__(self):
        pass

    def init(self):
        pass


class time:
    def Clock():
        def __init__():
            pass

fonts = []
class FONT:
    def Font(self,name="Times New Roman",size=12):
        fonts.append(Pygame.font.Font(name,size))
        return Pygame.font.Font(name,size)




class IMPORTS:
    def __init__(self):
        self.imported = []

    def imports(self,modulename):
        self.imported.append(importlib.import_module(modulename))


class PROCESSOR:
    def __init__(self):
        self.status = 1



Pygame.init()

#universal.display()


UNIVERSAL.display().set_mode((500,500))
'''
print(console)
pygame.init()
running = 1
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    console.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(console, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
'''

