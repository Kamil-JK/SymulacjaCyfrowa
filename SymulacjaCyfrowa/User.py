import math

class User:

    def __init__(self, v, s1, s2, x, l, userID, ttt, alfa, delta):
        self.v = v
        self.s1 = s1
        self.s2 = s2
        self.x = x
        self.l = l
        self.userID = userID
        self.ttt = ttt
        self.alfa = alfa
        self.delta = delta
        self.currentBS = 1
        self.ttt_1_2 = 0
        self.ttt_2_1 = 0

    def report(self, t):
        self.x = self.x + self.v * t
        powerBS1 = 4.56 - 22 * math.log10(self.x) + self.s1
        powerBS2 = 4.56 - 22 * math.log10(self.l - self.x) + self.s2

        if self.x == self.l - self.x:
            print("Destroy user distance")
            return False

        elif self.currentBS == 2:
            if powerBS2 - powerBS1 >= self.delta:
                print("Destroy user delta")
                return False
            elif powerBS1 - powerBS2 >= self.alfa:
                self.ttt_1_2 = 0
                self.ttt_2_1 = self.ttt_2_1 + t            
                if(self.ttt_2_1 == 100):
                    print("Switch to BS1")
                    self.currentBS = 1
                    self.ttt_2_1 = 0
            else:
                self.ttt_1_2 = 0
                self.ttt_2_1 = 0          

        elif self.currentBS == 1:
            if powerBS1 - powerBS2 >= self.delta:
                print("Destroy user delta")
                return False      
            elif powerBS2 - powerBS1 >= self.alfa:
                self.ttt_1_2 = 0
                self.ttt_2_1 = self.ttt_2_1 + t            
                if(self.ttt_2_1 == 100):
                    print("Switch to BS2")
                    self.currentBS = 1
                    self.ttt_2_1 = 0
            else:
                self.ttt_1_2 = 0
                self.ttt_2_1 = 0
        return True
