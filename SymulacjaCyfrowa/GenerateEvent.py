from Event import Event
from ReportEvent import ReportEvent
from sortedcontainers import SortedList
import numpy as np

class GenerateEvent(Event):    

    def __init__(self, network, eventList, executionTime, userID):
        
    
    def execute(self):
        print("Generate event")
        self.network.createUser(self.userID)
        #Nowy reportEvent po czase 20
        reportTime = 20
        self.eventList.add(ReportEvent(self.network, self.eventList, reportTime, self.userID))
        #Nowy generateEvent po losowym czasie
        generateTime = 5 + 30 * np.random.uniform()
        self.eventList.add(GenerateEvent(self.network, self.eventList, generateTime, self.userID + 1))

    def eventType(self):
        return "GenerateEvent"