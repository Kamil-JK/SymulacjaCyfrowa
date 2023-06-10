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
        self.totalUserNumber = 0

    def createUser(self, userID):
        v  = self.v[self.totalUserNumber]
        s1 = self.s1[self.totalUserNumber]
        s2 = self.s2[self.totalUserNumber]
        if len(self.userList) < self.n:
            self.userList.append(User(v, s1, s2, self.x, self.l, userID, self.ttt, self.alfa, self.delta))
            self.totalUserNumber = self.totalUserNumber + 1
            return True
        else:
            self.userBuffer.put(User(v, s1, s2, self.x, self.l, userID, self.ttt, self.alfa, self.delta))
            # print("Buffer size: " + str(self.userBuffer.qsize()))
            self.totalUserNumber = self.totalUserNumber + 1
            return False
            
    
    def reportUser(self, userID):
        #Report user with userID
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                return self.userList[userID].report(self.t)
    
    def destroyUser(self, userID):
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                self.userList.remove(userID)

    def bufferEmpty(self):
        return self.userBuffer.empty()

    def userFromBuffer(self):
        user = self.userBuffer.get()
        self.userList.append(user)
        return user.getUserID()

        

        