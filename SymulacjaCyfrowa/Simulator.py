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

  def __init__(self, simulationNumber, _lambda, alfa, maxUsersNumber):

    self.eventList = SortedList(key=lambda x: -x.getSimulationTime())
    self.l = 5000
    self.x = 2000
    self.t = 20
    self.delta = 20
    self.ttt = 100
    self.n = 60
    self.t = 20
    self.tau = []
    self.v = []
    self.s1 = []
    self.s2 = []
    self.usersServed = 0
    self.maxUsersNumber = maxUsersNumber
    self.eventNumber = 0

    self.usersServedResult = []
    self.usersInSystem = []

    self.generator = RandomNumberGenerator(_lambda)

    seed = (simulationNumber + 1) * 100000 * maxUsersNumber

    for i in range(self.maxUsersNumber + self.n):
      self.tau.append(self.generator.randExp(seed))
      seed = seed + 50000
      self.v.append(0.005 + 0.045 * self.generator.rand(seed)) # [5,50]m/s
      seed = seed + 50000
      self.s1.append(self.generator.randGauss(0, 4))
      self.s2.append(self.generator.randGauss(0, 4))

    self.network = Network(self.x, self.l, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa, self.delta)

  def mainLoop(self):

    clock = 0
    x = []
    y = []
    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau[0], self.t, self.maxUsersNumber + self.n, self.eventNumber, self.tau, self.n))
    while self.usersServed < self.maxUsersNumber:

      event = self.eventList.pop()
      clock = event.getSimulationTime()/1000
      y.append(self.network.getUserListSize() + self.network.getBufferSize())
      x.append(clock)
      if event.execute():
        self.usersServed = self.usersServed + 1
        self.usersServedResult.append(self.usersServed)
        self.usersInSystem.append(self.network.getUserListSize())

       
    plt.xlabel("Czas symulacji [s]")
    plt.ylabel("Liczba użytkowników w systemie i kolejce")
    plt.plot(x, y)
    plt.show()
      

                  