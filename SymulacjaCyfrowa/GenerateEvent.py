from Event import Event

class GenerateEvent(Event):    

    def __init__(self, network, eventList, simulationTime, userID, t, tau):
        super().__init__(network, eventList, simulationTime, userID, t)
        self.tau = tau
        print("Generate event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
    
    def execute(self):
        print("Generate event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))

        userInSystem = self.network.createUser(self.userID)
        if (userInSystem):
            reportTime = self.t  + self.simulationTime
            self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID, self.t))


        #Nowy generateEvent po losowym czasie
        generateTime = self.tau + self.simulationTime
        self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.userID + 1, self.t, self.tau))

    def eventType(self):
        return "GenerateEvent, userID: " + str(self.userID) + ", time: " + str(self.simulationTime)
    

class ReportEvent(Event):
    
    def __init__(self, network, eventList, simulationTime, userID, t):
        super().__init__(network, eventList, simulationTime, userID, t)
        print("Report event created, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))

    def execute(self):
        print("Report event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        self.network.reportUser(self.userID)
        reportTime = self.t  + self.simulationTime
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID, self.t))
        
    def eventType(self):
        return "ReportEvent, userID: " + str(self.userID) + ", time: " + str(self.simulationTime)
