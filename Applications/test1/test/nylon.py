import threading
import pygame
import importlib
processing = []

class processor:
    def __init__(self):
        self.cores = 32
        self.line = [None for i in range(32)]

    def import_module(self,module):
        print(module)
        return importlib.import_module(module)

    def boot(self):
        '''
        one = threading.Thread(target=importlib.import_module,args=('one',))
        one.start()

        two = threading.Thread(target=importlib.import_module('two'))
        two.start()
        '''
        import one
        threading.Thread(target=one.run,args=()).start()
        import two
        #threading.Thread(target=two.run,args=()).start()
        #one = threading.Thread(target=processor.import_module('one')).start()


class EVENT:
    def __init__(self):
        pass

    def get(self):
        return pygame.event.get()
processor = processor()

processor.boot()