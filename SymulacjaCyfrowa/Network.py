import queue
import numpy as np
from Event import Event
from GenerateEvent import GenerateEvent
from ReportEvent import ReportEvent

class Network:

    maxUserNumber = 60
    distanceBS = 5000
    userStartPosition = 2000
    userList = []
    userBuffer = queue.Queue()
    eventList = []
    
    def __init__(self):
        print("Network created")
        
    def createUser():
        v = np.random.uniform()
        print("User created with speed v")
    
    def destroyUser():
        print("Destroy user")
        
    def mainLoop():
        print("Loop")
        #po kolei execute tych eventów
        