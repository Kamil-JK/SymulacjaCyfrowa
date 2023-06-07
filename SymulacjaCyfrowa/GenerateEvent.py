from Event import Event
import numpy as np

class GenerateEvent(Event):    

    def __init__(self, network, eventList, executionTime, userID):
        super().__init__(network, eventList, executionTime, userID)
    
    def execute(self):
        print("GenerateEvent executing, userID: " + str(self.userID) + ", time: " + str(self.executionTime))
        self.network.createUser(self.userID)
        #Nowy reportEvent po czase 20
        reportTime = 20  + self.executionTime
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID))
        #Nowy generateEvent po losowym czasie
        generateTime = 3 + 10 * np.random.uniform() + self.executionTime
        self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.userID + 1))

    def eventType(self):
        return "GenerateEvent, userID: " + str(self.userID) + ", time: " + str(self.executionTime)
    

class ReportEvent(Event):
    
    def __init__(self, network, eventList, executionTime, userID):
        super().__init__(network, eventList, executionTime, userID)

    def execute(self):
        print("Report event executing, userID: " + str(self.userID) + ", time: " + str(self.executionTime))
        self.network.reportUser(self.userID)
        #Nowy reportEvent po czase 20
        reportTime = 20  + self.executionTime
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID))
        
    def eventType(self):
        return "ReportEvent, userID: " + str(self.userID) + ", time: " + str(self.executionTime)
