from Network import Network 

class Event():

    def __init__(self, network, executionTime):
        self.network = network
        self.executionTime = executionTime

    def getExecutionTime(self):
        return self.executionTime

    def updateTime(self, time):
        self.executionTime -= time

    def execute(self):
        pass

    def eventType(self):
        pass