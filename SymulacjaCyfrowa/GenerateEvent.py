from Event import Event

class GenerateEvent(Event):    

    def execute(self):
        print("Generate event")
        self.network.createUser()

    def eventType(self):
        return "GenerateEvent"