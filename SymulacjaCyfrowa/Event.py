from Network import Network 
from sortedcontainers import SortedList

class Event():
    
    def __init__(self, network, eventList, simulationTime, userID):
        self.network = network
        self.eventList = eventList
        self.simulationTime = simulationTime
        self.userID = userID

    def getSimulationTime(self):
        return self.simulationTime

    def updateTime(self, time):
        self.simulationTime -= time

    def execute(self):
        pass
