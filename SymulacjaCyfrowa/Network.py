import queue
from User import User

class Network:

    userList = []
    
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
        self.newUserNumber = -1
        self.userBuffer = 0
        self.servedUsers = 0

    def createUser(self, userID, isFromBuffer):

        v  = self.v[self.newUserNumber]
        s1 = self.s1[self.newUserNumber]
        s2 = self.s2[self.newUserNumber]
        self.userList.append(User(v, s1, s2, self.x, self.l, userID, self.ttt, self.alfa, self.delta))
        if isFromBuffer:
            self.userBuffer = self.userBuffer - 1
        
    def userToBuffer(self):
        self.userBuffer = self.userBuffer + 1
        return False
            
    def reportUser(self, userID):
        #Report user with userID
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                return self.userList[i].report(self.t)
    
    def destroyUser(self, userID):
        for i in range(len(self.userList) - 1):
            if self.userList[i].userID == userID:
                self.userList.pop(i)
                self.servedUsers = self.servedUsers + 1

    def planNewUser(self):
        self.newUserNumber = self.newUserNumber + 1
        return self.newUserNumber
    
    def getUserListSize(self):
        return len(self.userList)
    
    def getBufferSize(self):
        return self.userBuffer
    
    def getServedUsers(self):
        return self.servedUsers
    
    def getNewUserNumber(self):
        return self.newUserNumber



        

        