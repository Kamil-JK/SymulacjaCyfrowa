import math

class User:

    def __init__(self, speed, s1, s2, position, userID):
        self.speed = speed
        self.s1 = s1
        self.s2 = s2
        self.position = position
        self.userID = userID

    def report(self, t):
        self.position = self.position + self.speed * t
        self.powerBS1 = 4.56 - 22 * math.log10(self.position) + self.s1
        self.powerBS2 = 4.56 - 22 * math.log10(5000 - self.position) + self.s2
        if self.powerBS1 > self.powerBS2:
            self.connectedTo = "BS1"
        else:
            self.connectedTo = "BS2"



