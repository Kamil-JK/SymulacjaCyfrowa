from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomNumberGenerator import RandomNumberGenerator 
from RandomGenerator import RandomGenerator 
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
    # self.delta = 20
    self.delta = 20
    self.ttt = 0.1
    self.n = 60
    self.t = 0.02
    self.tau = []
    self.v = []
    self.s1 = []
    self.s2 = []
    self.usersServed = 0
    self.maxUsersNumber = maxUsersNumber
    self.eventNumber = 0

    self.usersServedResult = []
    self.usersInSystem = []

    seed = 12345 + (simulationNumber + 1) * 100000
    self.generator = RandomNumberGenerator(_lambda, seed)

    for i in range(self.maxUsersNumber + 100): #+100 - z powodu spadku na końcu wykresu
      self.tau.append(self.generator.randExponential())
      self.v.append(5 + 45 * self.generator.randUniform()) # [5,50]m/s
      self.s1.append(self.generator.randGauss(0, 4))
      self.s2.append(self.generator.randGauss(0, 4))
    
    # for i in range(1, self.maxUsersNumber + self.n):
    #     generator2 = RandomGenerator(i * 10000, 0.2)
    #     self.tau.append(generator2.rand())
    #     generator2 = RandomGenerator(i * 10000, 0.2)
    #     self.v.append(generator2.randExp())
    #     generator2 = RandomGenerator(i * 10000, 0.2)
    #     self.s1.append(generator2.randGauss(0, 4))


    # for i in range(self.maxUsersNumber + self.n):
    #   self.tau.append(self.generator.randExponential())
    #   seed = seed + 50000
    #   self.v.append(5 + 45 * self.generator.randUniform()) # [5,50]m/s
    #   seed = seed + 50000
    #   self.s1.append(self.generator.randGauss(0, 4))
    #   self.s2.append(self.generator.randGauss(0, 4))


    # plt.figure(1)
    # plt.hist(self.v, bins=50)
    # plt.title("Rozkład równomierny")
    # plt.xlabel("Wartość")
    # plt.ylabel("Liczba wystąpień")

    # plt.figure(2)
    # plt.hist(self.tau, bins=50)
    # plt.title("Rozkład wykładniczy")
    # plt.xlabel("Wartość")
    # plt.ylabel("Liczba wystąpień")

    # plt.figure(3)
    # plt.hist(self.s1, bins=50)
    # plt.title("Rozkład Gaussa")
    # plt.xlabel("Wartość")
    # plt.ylabel("Liczba wystąpień")
    # plt.show()

    self.network = Network(self.x, self.l, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa, self.delta)

  def mainLoop(self):

    # clock = 0
    # x = []
    # y1 = []
    # y2 = []
    # y3 = []

    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau[0], self.t, self.maxUsersNumber + 100, self.eventNumber, self.tau, self.n)) #self.maxUsersNumber + self.n
    while self.usersServed < self.maxUsersNumber:

      event = self.eventList.pop()
      # clock = event.getSimulationTime()/1000
      # y1.append(self.network.getUserListSize())
      # y2.append(self.network.getBufferSize())
      # y3.append(self.network.getUserListSize() + self.network.getBufferSize())
      # x.append(clock)
      if event.execute():
        self.usersServed = self.usersServed + 1
        self.usersServedResult.append(self.usersServed)
        self.usersInSystem.append(self.network.getUserListSize() + self.network.getBufferSize())

    print(str(self.network.getNewUserNumber()))
    # plt.xlabel("Czas symulacji [s]")
    # plt.ylabel("Liczba użytkowników w systemie i kolejce")
    # plt.plot(x, y1, label = "system")
    # plt.plot(x, y2, label = "kolejka")
    # plt.plot(x, y3, label = "razem")
    # plt.legend()
    # plt.show()
      

                  