from Event import Event

class GenerateEvent(Event):    

    def __init__(self, network, eventList, simulationTime, userID, tau):
        super().__init__(network, eventList, simulationTime, userID)
        self.tau = tau
    
    def execute(self):
        print("GenerateEvent executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        self.network.createUser(self.userID)
        #Nowy reportEvent po czase 20
        reportTime = 20  + self.simulationTime
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID))
        #Nowy generateEvent po losowym czasie
        generateTime = self.tau + self.simulationTime
        self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.userID + 1, self.tau))

    def eventType(self):
        return "GenerateEvent, userID: " + str(self.userID) + ", time: " + str(self.simulationTime)
    

class ReportEvent(Event):
    
    def __init__(self, network, eventList, simulationTime, userID):
        super().__init__(network, eventList, simulationTime, userID)

    def execute(self):
        print("Report event executing, userID: " + str(self.userID) + ", time: " + str(self.simulationTime))
        self.network.reportUser(self.userID)
        #Nowy reportEvent po czase 20
        reportTime = 10  + self.simulationTime
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID))
        
    def eventType(self):
        return "ReportEvent, userID: " + str(self.userID) + ", time: " + str(self.simulationTime)
