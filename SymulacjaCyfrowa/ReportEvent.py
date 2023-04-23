from Event import Event

class ReportEvent(Event):
    
    def execute(self):
        print("Report event")
        self.network.reportUser()

    def eventType(self):
        return "ReportEvent"