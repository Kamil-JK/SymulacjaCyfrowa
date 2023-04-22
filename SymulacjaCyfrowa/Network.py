import queue
import numpy as np
from User import User

class Network:

    maxUserNumber = 60
    distanceBS = 5000
    userStartPosition = 2000
    userList = []
    userBuffer = queue.Queue()
    
    def __init__(self):
        print("Network created")
        
    def createUser():
        speed = np.random.uniform(5,50) #m/s             
        Network.userList.append(User(speed))
        print("Number of users in the system: "+ str(len(Network.userList)))
    
    def destroyUser():
        print("")