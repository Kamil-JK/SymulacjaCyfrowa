import math

class User:

    def __init__(self, v, s1, s2, x, userID, ttt, alfa):
        self.v = v
        self.s1 = s1
        self.s2 = s2
        self.x = x
        self.userID = userID
        self.ttt = ttt
        self.alfa = alfa
        self.currentBS = 0
        self.adjacentBS = 1
        self.current_ttt = 0
        self.l = 5000

    def report(self, t):
        self.x = self.x + self.v * t
        powerBS = [0, 0]
        powerBS[0] = 4.56 - 22 * math.log10(self.x) + self.s1
        powerBS[1] = 4.56 - 22 * math.log10(self.l - self.x) + self.s2
        if powerBS[0] - powerBS[1] >= self.alfa:
            self.currentBS = 0
            self.adjacentBS = 1
        elif powerBS[1] - powerBS[0] >= self.alfa:
            self.currentBS = 1
            self.adjacentBS = 0


