from Network import Network 
from sortedcontainers import SortedList

class Event():
    
    def __init__(self, network, eventList, executionTime, userID):
        self.network = network
        self.eventList = eventList
        self.executionTime = executionTime
        self.userID = userID

    def getExecutionTime(self):
        return self.executionTime

    def updateTime(self, time):
        self.executionTime -= time

    def execute(self):
        pass
