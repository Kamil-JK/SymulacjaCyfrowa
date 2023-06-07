from GenerateEvent import GenerateEvent
from Network import Network 
import numpy as np
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
#Optymalizacji podlega parametr 𝛼


class Simulator:

  #eventList = SortedList(key=lambda x: -x.getExecutionTime())
  eventList = SortedList(key=lambda x: -x.getExecutionTime())
  clock = 0
  firstUserID = 0
  network = Network()


  def __init__(self, simulationNumber, _lambda):
    self.generatorTau = RandomGenerator(52834 + simulationNumber * 100000, _lambda)
    self.generatorV = RandomGenerator(8672 + simulationNumber * 100000, _lambda)
    self.generatorS1 = RandomGenerator(11637 + simulationNumber * 100000, _lambda)
    self.generatorS2 = RandomGenerator(74664 + simulationNumber * 100000, _lambda)

    self.tau = self.generatorTau.randExp()
    self.v = self.generatorV.rand()
    self.s1 = self.generatorS1.randGauss(0, 4)
    self.s2 = self.generatorS2.randGauss(0, 4)


  def mainLoop(self):

    executionTime = 3 + 20 * np.random.uniform()
    self.eventList.add(GenerateEvent(self.network, self.eventList, executionTime, self.firstUserID))

    
    while self.clock <= 50:
      #wrzuć nowy even do listy (zaplanuj)
      print("Clock: " + str(self.clock) + " User length: " + str(self.network.userListLength()))

      #execute eventu z najmniejszym czasem i wywal go w pętli aż nie będzie ujemnych

      event = self.eventList.pop()
      event.execute()
      self.clock = event.getExecutionTime()

      print("Event list: ")
      for event in self.eventList:
        print(event.eventType())
                  

