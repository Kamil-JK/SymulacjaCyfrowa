from GenerateEvent import GenerateEvent
from Network import Network 
from sortedcontainers import SortedList
from RandomGenerator import RandomGenerator 

#    M2 Planowanie zdarzeń
#l – stała równa 5000 m
#x – stała równa 2000 m
#v - zmienna losowa o rozkładzie jednostajnym na przedziale [5, 50] m/s
#t – stała równa 20 ms
#s – zmienna losowa o rozkładzie Gaussa ze średnia równą 0 i odchyleniem standardowym równym 4 dB
#Δ – stała równa 20 dB
#τ - zmienna losowa o rozkładzie wykładniczym o intensywności λ
#𝑡𝑡𝑡 = 100 𝑚𝑠. 
#n = 60
#𝛼 - najmniejsza różnica mocy potrzebna do zmiany stacji bazowej 


class Simulator:

  eventList = SortedList(key=lambda x: -x.getSimulationTime())
  l = 5000
  x = 2000
  t = 20
  delta = 20
  ttt = 100
  n = 4
  t = 20


  def __init__(self, simulationNumber, _lambda, alfa):
    self.generatorTau = RandomGenerator(52834 + simulationNumber * 100000, _lambda)
    self.generatorV = RandomGenerator(8672 + simulationNumber * 100000, _lambda)
    self.generatorS1 = RandomGenerator(11637 + simulationNumber * 100000, _lambda)
    self.generatorS2 = RandomGenerator(74664 + simulationNumber * 100000, _lambda)

    self.tau = self.generatorTau.randExp()
    self.v = self.generatorV.rand()
    self.s1 = self.generatorS1.randGauss(0, 4)
    self.s2 = self.generatorS2.randGauss(0, 4)


    self.network = Network(self.x, self.v, self.s1, self.s2, self.t, self.n, self.ttt, alfa)


  def mainLoop(self):

    clock = 0
    self.eventList.add(GenerateEvent(self.network, self.eventList, self.tau, 0, self.t, self.tau))
    
    while clock <= 30:

      event = self.eventList.pop()
      clock = event.getSimulationTime()
      print("------Clock: " + str(clock) + " User length: " + str(len(self.network.userList)))
      event.execute()


      print("Event list: ")
      for event in self.eventList:
        print(event.eventType())

                  