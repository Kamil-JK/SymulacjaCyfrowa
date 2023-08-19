from Event import Event

class GenerateEvent(Event):    

    def __init__(self, network, eventList, simulationTime, t, maxUsersNumber, eventNumber, tau, n):
        super().__init__(network, eventList, simulationTime, t, maxUsersNumber)
        self.tau = tau
        self.eventNumber = eventNumber
        self.n = n
        # print("Generate event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
    
    def execute(self):
        # print("Generate event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        if self.eventNumber < self.maxUsersNumber:
            generateTime = self.tau[self.eventNumber] + self.simulationTime
            if self.network.getUserListSize() < self.n:
                newUserID = self.network.createUser(False)
                reportTime = self.t  + self.simulationTime
                self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, newUserID, self.n))
                self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.t, self.maxUsersNumber, self.eventNumber + 1, self.tau, self.n))
            else:
                self.network.userToBuffer() #buffer size?
                self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.t, self.maxUsersNumber, self.eventNumber + 1, self.tau, self.n))
        return False
    

class ReportEvent(Event):
    
    def __init__(self, network, eventList, simulationTime, t, maxUsersNumber, userID, n):
        super().__init__(network, eventList, simulationTime, t, maxUsersNumber)
        self.userID = userID
        self.n = n
        #print("Report event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))

    def execute(self):
        #print("Report event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        reportTime = self.t  + self.simulationTime
        userIsActive = self.network.reportUser(self.userID)
        if userIsActive:                 # if user in system
            self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, self.userID, self.n))
        elif userIsActive == False:      # if user deleted
            self.network.destroyUser(self.userID)
            if self.network.getBufferSize() >= 1 and self.network.getUserListSize() < self.n and self.network.getNewUserNumber() + 1 <= self.maxUsersNumber:
                newUserID = self.network.createUser(True)
                self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, newUserID, self.n))
                               
            return True
        return False

