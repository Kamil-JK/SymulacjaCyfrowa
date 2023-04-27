import queue
import numpy as np
from User import User

class Network:

    maxUserNumber = 60
    distanceBS = 5000
    userStartPosition = 2000
    userList = {}
    userBuffer = queue.Queue()
    
    
    def __init__(self):
        print("Network created")

    def userListLength(self):
        return len(self.userList)

    def createUser(self, userID):
        v = 5 + 45 * np.random.uniform()
        self.userList.append(User(v, self.userStartPosition, userID))
    
    def reportUser(self, userID):
        #Report user with userID
        self.userList[userID].report(20)
    
    def destroyUser(self):
        print("Destroy user")
        

        