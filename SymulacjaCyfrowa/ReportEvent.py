from Event import Event
from GenerateEvent import GenerateEvent
from sortedcontainers import SortedList

class ReportEvent(Event):
    
    def execute(self):
        print("Report event")
        self.network.reportUser()
        #Nowy reportEvent po czase 20
        reportTime = 20
        self.eventList.add(GenerateEvent(self.network, self.eventList, reportTime, self.userID))
        
    def eventType(self):
        return "ReportEvent"