from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomGenerator import RandomGenerator 

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


  def __init__(self, simulationNumber, _lambda, alfa):
    self.generatorTau = RandomGenerator(52834 + simulationNumber * 100000, _lambda)
    self.generatorV = RandomGenerator(8672 + simulationNumber * 100000, _lambda)
    self.generatorS1 = RandomGenerator(11637 + simulationNumber * 100000, _lambda)
    self.generatorS2 = RandomGenerator(74664 + simulationNumber * 100000, _lambda)

    self.tau = self.generatorTau.randExp()
    self.v =  0.005 + 0.0045 * self.generatorV.rand() # [5,50]m/s
    self.s1 = self.generatorS1.randGauss(0, 4)
    self.s2 = self.generatorS2.randGauss(0, 4)

    self.network = Network(self.x, self.l, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa, self.delta)

  def mainLoop(self):

    clock = 0
    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau, 0, self.t, self.tau))
    
    while clock <= 1000000:

      event = self.eventList.pop()
      clock = event.getSimulationTime()
      event.execute()


      # print("Event list: ")
      # for event in self.eventList:
      #   print(event.eventType())
      # print("------Clock: " + str(clock) + " User length: " + str(len(self.network.userList)))

                  