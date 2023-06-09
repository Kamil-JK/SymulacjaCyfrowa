import queue
from User import User

class Network:

    userList = []
    userBuffer = queue.Queue()
    
    def __init__(self, x, l, v, s1, s2, t, n, ttt, alfa, delta):
        self.x = x
        self.l = l 
        self.v = v
        self.s1 = s1
        self.s2 = s2
        self.t = t
        self.n = n
        self.ttt = ttt
        self.alfa = alfa
        self.delta = delta

    def createUser(self, userID):
        if len(self.userList) < self.n:
            self.userList.append(User(self.v, self.s1, self.s2, self.x, self.l, userID, self.ttt, self.alfa, self.delta))
            return True
        else:
            self.userBuffer.put(User(self.v, self.s1, self.s2, self.x, self.l, userID, self.ttt, self.alfa, self.delta))
            print("Buffer size: " + str(self.userBuffer.qsize()))
            return False
            
    
    def reportUser(self, userID):
        #Report user with userID
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                return self.userList[userID].report(self.t)
    
    def destroyUser(self, userID):
        print("I should now check the queue")
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                self.userList.remove(userID)

    def checkQueue(self):
        if self.userBuffer.empty() == False and len(self.userList) < self.n :
            print("Create report event and user Może w report evencie to się zrobi jakiś może return true czy coś")

        

        