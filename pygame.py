import importlib
importlib.import_module('pygame')

screen = None
print('Hi')


class display:
    def __init__(self):
        self.screen = [[0,0],[0,0]]

    def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
        self.screen = [[0,0],[size[0],size[1]]]

    def flip(self):
        pg.screen.flip()

class universal:
    def set_mode(self,size=(0,0),flags=0,depth=0,display=0,vsync=0):
        global screen
        screen = display.set_mode(size, flags, depth, display, vsync)


class screen:
    def __init__(self):
        pass
    def init(self):
        pass

    def update(self):
        pass



