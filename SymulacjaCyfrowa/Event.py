class Event():
    
    def __init__(self, network, eventList, simulationTime, userID, t):
        self.network = network
        self.eventList = eventList
        self.simulationTime = simulationTime
        self.userID = userID
        self.t = t

    def getSimulationTime(self):
        return self.simulationTime

    def updateTime(self, time):
        self.simulationTime -= time

    def execute(self):
        pass
