import threading

processing = []
def  process(action,args=None):
    threading.Thread(target=action,args=args).start()


