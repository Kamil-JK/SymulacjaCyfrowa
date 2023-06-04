from Event import Event
from GenerateEvent import GenerateEvent
from GenerateEvent import ReportEvent
from Network import Network 
import numpy as np
from sortedcontainers import SortedList

#    M2 Planowanie zdarzeń
#l – stała równa 5000 m
#x – stała równa 2000 m
#v - zmienna losowa o rozkładzie jednostajnym na przedziale [5, 50] m/s
#t – stała równa 20 ms
#s – zmienna losowa o rozkładzie Gaussa ze średnia równą 0 i odchyleniem standardowym równym 4 dB
#Δ – stała równa 8 dB
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

  def mainLoop(self):

    executionTime = 3 + 20 * np.random.uniform()
    self.eventList.add(GenerateEvent(self.network, self.eventList, executionTime, self.firstUserID))

    while self.clock <= 150:
      #wrzuć nowy even do listy (zaplanuj)
      print("Clock: " + str(self.clock) + " User length: " + str(self.network.userListLength()))
      self.clock = self.clock + 1

      #execute eventu z najmniejszym czasem i wywal go w pętli aż nie będzie ujemnych
      while self.eventList[-1].getExecutionTime() < 0:
        self.eventList.pop().execute()

        print("Event list: ")
        for event in self.eventList:
          print(event.eventType())
                  

      #czas--
      for event in self.eventList:
        event.updateTime(1)