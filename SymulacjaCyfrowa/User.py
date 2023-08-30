import math
import logging

logging.basicConfig(filename='logs.txt', level=logging.DEBUG, filemode='w')
# consoleLogger=logging.StreamHandler()
# consoleLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
# logging.getLogger().addHandler(consoleLogger)

class User:

    def __init__(self, v, s1, s2, x, l, userID, ttt, alfa, delta):
        self.v = v
        self.s1 = s1
        self.s2 = s2
        self.x = x
        self.x0 = x
        self.l = l
        self.userID = userID
        self.ttt = ttt
        self.alfa = alfa
        self.delta = delta
        self.currentBS = 1
        self.ttt_1_2 = 0
        self.ttt_2_1 = 0
        self.state = "Active"
        logging.debug("Create user " + str(self.userID))

    def getUserID(self):
        return self.userID
    
    def getUserState(self):
        return self.state
    
    def getUserPosition(self):
        return self.x

    def report(self, t):
        self.state = "Active"
        self.x = self.x + self.v * t
        powerBS1 = 4.56 - 22 * math.log10(self.x) + self.s1
        powerBS2 = 4.56 - 22 * math.log10(self.l - self.x) + self.s2

        if self.x >= self.l - self.x0:
            logging.debug("Delete user " + str(self.userID)+ " - reached destination in " + str(self.x) + "m")
            self.state = "Served"

        elif self.currentBS == 2:
            if powerBS2 - powerBS1 >= self.delta:
                logging.debug("Delete user" + str(self.userID)+ " - delta condition in " + str(self.x) + "m")
                self.state = "Disconnected"
            elif powerBS1 - powerBS2 >= self.alfa:
                self.ttt_1_2 = 0
                self.ttt_2_1 = self.ttt_2_1 + t            
                if(self.ttt_2_1 >= self.ttt):
                    logging.debug("Switch to BS1")
                    self.state = "Switching"
                    self.currentBS = 1
                    self.ttt_1_2 = 0
            else:
                self.ttt_1_2 = 0
                self.ttt_2_1 = 0          

        elif self.currentBS == 1:
            if powerBS1 - powerBS2 >= self.delta:
                logging.debug("Delete user" + str(self.userID)+ " - delta condition in " + str(self.x) + "m")
                self.state = "Disconnected"     
            elif powerBS2 - powerBS1 >= self.alfa:
                self.ttt_1_2 = 0
                self.ttt_2_1 = self.ttt_2_1 + t            
                if(self.ttt_2_1 >= self.ttt):
                    logging.debug("Switch to BS2 user" + str(self.userID)+ " in " + str(self.x) + "m")
                    self.state = "Switching"
                    self.currentBS = 2
                    self.ttt_2_1 = 0
            else:
                self.ttt_1_2 = 0
                self.ttt_2_1 = 0
