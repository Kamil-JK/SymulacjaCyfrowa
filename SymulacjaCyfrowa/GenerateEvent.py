from Event import Event

class GenerateEvent(Event):    

    def __init__(self, network, eventList, simulationTime, t, maxUsersNumber, tau):
        super().__init__(network, eventList, simulationTime, t, maxUsersNumber)
        self.tau = tau
        # print("Generate event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
    
    def execute(self):
        # print("Generate event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        if self.network.getNewUserNumber() + 1 < self.maxUsersNumber:
            newUserID = self.network.planNewUser()
            if self.network.getUserListSize() < 60:
                self.network.createUser(newUserID, False)
                reportTime = self.t  + self.simulationTime
                self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, newUserID))
                generateTime = self.tau[newUserID] + self.simulationTime
                self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.t, self.maxUsersNumber, self.tau))
            else:
                self.network.userToBuffer()
                generateTime = self.tau[newUserID] + self.simulationTime
                self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.t, self.maxUsersNumber, self.tau))
        return False
    

class ReportEvent(Event):
    
    def __init__(self, network, eventList, simulationTime, t, maxUsersNumber, userID):
        super().__init__(network, eventList, simulationTime, t, maxUsersNumber)
        self.userID = userID
        #print("Report event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))

    def execute(self):
        #print("Report event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        reportTime = self.t  + self.simulationTime
        report = self.network.reportUser(self.userID)
        if report:                 # if user in system
            self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, self.userID))
        elif report == False:      # if user deleted
            self.network.destroyUser(self.userID)
            if self.network.getBufferSize() >= 1 and self.network.getUserListSize() < 60 and self.network.getNewUserNumber() + 1 <= self.maxUsersNumber:
                newUserID = self.network.planNewUser()
                self.network.createUser(newUserID, True)
                self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.t, self.maxUsersNumber, newUserID))
                               
            return True
        return False

