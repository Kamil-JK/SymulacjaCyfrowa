class Event():
    
    def __init__(self, network, eventList, simulationTime, t, maxUsersNumber):
        self.network = network
        self.eventList = eventList
        self.simulationTime = simulationTime
        self.t = t
        self.maxUsersNumber = maxUsersNumber

    def getSimulationTime(self):
        return self.simulationTime

    def updateTime(self, time):
        self.simulationTime -= time

    def execute(self):
        pass
