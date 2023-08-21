from User import User

class Network:
    
    def __init__(self, x, l, v, s1, s2, t, n, ttt, alfa, delta):
        self.userList = []
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
        self.switchedUsers = 0
        self.disconnectedUsers = 0

    def createUser(self, isFromBuffer):
        self.newUserNumber = self.newUserNumber + 1
        
        v  = self.v[self.newUserNumber]
        s1 = self.s1[self.newUserNumber]
        s2 = self.s2[self.newUserNumber]
        self.userList.append(User(v, s1, s2, self.x, self.l, self.newUserNumber, self.ttt, self.alfa, self.delta))
        if isFromBuffer:
            self.userBuffer = self.userBuffer - 1
        #     print("from buffer user, buffer size = " + str(self.userBuffer))
            # print("create from buffer user " + str(self.newUserNumber) + " and buffer size = " + str(self.userBuffer))
        # else:
            # print("create " + str(self.newUserNumber))
        return self.newUserNumber
        
    def userToBuffer(self):
        #print("user to buffer ")
        self.userBuffer = self.userBuffer + 1
        # print("user to buffer, buffer size = " + str(self.userBuffer))
        return False
            
    def reportUser(self, userID):
        #Report user with userID
        for i in range(len(self.userList)):
            if self.userList[i].userID == userID:
                self.userList[i].report(self.t)
                userState = self.userList[i].getUserState()
                # if userState == "Active":
                #     return userState
                if userState == "Switching":
                    self.switchedUsers = self.switchedUsers + 1 
                    # return userState
                elif userState == "Disconnected":
                    self.disconnectedUsers = self.disconnectedUsers + 1 
                    # return userState
                elif userState == "Served":
                    self.servedUsers = self.servedUsers + 1 
                return userState
    
    def destroyUser(self, userID):
        for i in range(len(self.userList)):# - 1):
            if self.userList[i].userID == userID:
                self.userList.pop(i)
                # self.servedUsers = self.servedUsers + 1   
                # print("delete user " + str(user.getUserID()))
                break
    
    def getUserListSize(self):
        return len(self.userList)
    
    def getBufferSize(self):
        return self.userBuffer
    
    def getServedUsers(self):
        return self.servedUsers
    
    def getDisconnectedUsers(self):
        return self.disconnectedUsers / self.servedUsers
    
    def getSwitchedUsers(self):
        return self.switchedUsers / self.servedUsers
    
    def getNewUserNumber(self):
        return self.newUserNumber
    

        

        