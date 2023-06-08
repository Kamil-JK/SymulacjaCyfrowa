import queue
from User import User

class Network:

    distanceBS = 5000
    userStartPosition = 2000
    userList = []
    userBuffer = queue.Queue()
    
    
    def __init__(self, v, s1, s2, t, n):
        self.v = v
        self.s1 = s1
        self.s2 = s2
        self.t = t
        self.n = n

    def userListLength(self):
        return len(self.userList)

    def createUser(self, userID):
        if len(self.userList) < self.n:
            self.userList.append(User(self.v, self.s1, self.s2, self.userStartPosition, userID))
            return True
        else:
            self.userBuffer.put(User(self.v, self.s1, self.s2, self.userStartPosition, userID))
            print("Buffer size: " + str(self.userBuffer.qsize()))
            return False
            
    
    def reportUser(self, userID):
        #Report user with userID
        self.userList[userID].report(self.t)
    
    def destroyUser(self):
        print("I should now check the queue")
        if self.userBuffer.empty() == False:
            print("Create report event and user Może w report evencie to się zrobi jakiś może return true czy coś")

        

        