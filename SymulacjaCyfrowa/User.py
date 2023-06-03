import math

class User:

    def __init__(self, speed, position, userID):
        print("User created with id: " + str(userID))
        self.speed = speed
        self.position = position
        self.userID = userID

    def report(self, time):
        self.position = self.position + self.speed * time
        s = 0 #zmienna losowa o rozkładzie Gaussa ze średnią zero i odchyleniem standardowym 4 dB
        self.powerBS1 = 1#4.56 - 22 * math.log10(self.position) + s
        self.powerBS2 = 2#4.56 - 22 * math.log10(5000 - self.position) + s
        if self.powerBS1 > self.powerBS2:
            self.connectedTo = "BS1"
        else:
            self.connectedTo = "BS2"



