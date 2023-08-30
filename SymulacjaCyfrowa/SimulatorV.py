from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomNumberGenerator import RandomNumberGenerator 
import matplotlib.pyplot as plt
import numpy as np

# M2 Planowanie zdarzeń
# A1 Optymalizacja parametru alfa
#
# Parametry:
#
# l       dystans między stacjami bazowymi równy 5000 m
# x       pozycja użytkownika równa na początku 2000 m
# v       prędkość użytkownika równy zmiennej losowej o rozkładzie jednostajnym na przedziale [5, 50] m/s
# t       okres raportowania użytkownika równy 20 ms
# s       zmienna losowa o rozkładzie Gaussa ze średnia równą 0 i odchyleniem standardowym równym 4 dB
# delta   różnica mocy stanowiąca próg usunięcia użytkownika równy 20 dB
# tau     okres pojawiania się użytkowników w systemie równy zmiennej losowa o rozkładzie wykładniczym o intensywności λ
# 𝑡𝑡𝑡      czas histerezy zmiany stacji bazowej równy 100 𝑚𝑠. 
# n       maks. liczba użytkowników w systemie równa 60
# alfa    najmniejsza różnica mocy potrzebna do zmiany stacji bazowej - podlega optymalizacji


class Simulator:

  def __init__(self, simulationNumber, _lambda, alfa, maxUsersNumber, firstSeed, v):

    self.maxUsersNumber = maxUsersNumber
    self.firstSeed = firstSeed

    self.eventList = SortedList(key=lambda x: -x.getSimulationTime())
    self.l = 5000
    self.x = 2000
    self.delta = 20
    self.ttt = 0.1
    self.n = 60
    self.t = 0.02
    self.tau = []
    self.v = []
    self.s1 = []
    self.s2 = []
    self.usersServed = 0
    self.eventNumber = 0
    self.usersServedResult = []
    self.usersInSystem = []
    self.disconnectedUsers = 0
    self.switchedUsers = 0
    self.avgSwitchPosition = 0

    seed = self.firstSeed + (simulationNumber + 1) * 100000
    self.generator = RandomNumberGenerator(_lambda, seed)

    for i in range(self.maxUsersNumber + 100): #+100 - z powodu spadku na końcu wykresu
      self.tau.append(self.generator.randExponential())
      self.v.append(v) # [5,50]m/s
      self.s1.append(self.generator.randGauss(0, 4))
      self.s2.append(self.generator.randGauss(0, 4))

    self.network = Network(self.x, self.l, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa, self.delta)

  def mainLoop(self):

    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau[0], self.t, self.maxUsersNumber + 100, self.eventNumber, self.tau, self.n)) #self.maxUsersNumber + self.n
    while self.usersServed < self.maxUsersNumber:

      event = self.eventList.pop()

      if event.execute():
        self.usersServed = self.usersServed + 1
        self.usersServedResult.append(self.usersServed)
        self.usersInSystem.append(self.network.getUserListSize() + self.network.getBufferSize())

    self.disconnectedUsers = self.network.getDisconnectedUsers()
    self.switchedUsers = self.network.getSwitchedUsers()
    self.avgSwitchPosition = self.network.getMeanSwitchingPosition()

      

                  