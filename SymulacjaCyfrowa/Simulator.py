from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomNumberGenerator import RandomNumberGenerator 

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

  eventList = SortedList(key=lambda x: -x.getSimulationTime())
  l = 5000
  x = 2000
  t = 20
  delta = 20
  ttt = 100
  n = 60
  t = 20
  tau = []
  v = []
  s1 = []
  s2 = []
  usersServed = 0


  def __init__(self, simulationNumber, _lambda, alfa):
    self.generator = RandomNumberGenerator(_lambda)

    seed = simulationNumber * 10000000000

    for i in range(100000):
      self.tau.append(self.generator.randExp(seed))
      seed = seed + 50000
      self.v.append(0.005 + 0.045 * self.generator.rand(seed)) # [5,50]m/s
      seed = seed + 50000
      self.s1.append(self.generator.randGauss(0, 4))
      self.s2.append(self.generator.randGauss(0, 4))

    self.network = Network(self.x, self.l, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa, self.delta)

  def mainLoop(self):

    clock = 0
    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau[0], 0, self.t, self.tau))
    
    while self.usersServed <= 100:

      event = self.eventList.pop()
      clock = event.getSimulationTime()
      if event.execute():
        self.usersServed = self.usersServed + 1


      # print("Event list: ")
      # for event in self.eventList:
      #   print(event.eventType())
      # print("------Clock: " + str(clock) + " User length: " + str(len(self.network.userList)))

                  