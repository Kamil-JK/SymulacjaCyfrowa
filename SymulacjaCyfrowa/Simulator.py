from Event import Event
from GenerateEvent import GenerateEvent
from ReportEvent import ReportEvent
from Network import Network 
import numpy as np


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

  eventList = []
  clock = 0
  network = Network()

  def mainLoop(self):

    executionTime = 5 + 30 * np.random.uniform() #np.random.exponential() potem
    self.eventList.append(GenerateEvent(self.network, executionTime))

    while self.clock <= 20:
      #wrzuć nowy even do listy (zaplanuj)
      print("Clock: " + str(self.clock) + " User length: " + str(self.network.userListLength()))
      self.clock = self.clock + 1

      #execute eventu z najmniejszym czasem i wywal go w pętli aż nie będzie ujemnych
      while self.eventList[-1].getExecutionTime() < 0:
        if self.eventList[-1].eventType() == "GenerateEvent":
          self.eventList[-1].execute()
          reportExecutionTime = self.eventList[-1].getExecutionTime() + 20
          self.eventList.pop(-1)
          self.eventList.append(ReportEvent(self.network, reportExecutionTime))
          
          #Nowy generateEvent
          executionTime = 5 + 30 * np.random.uniform() #np.random.exponential() potem
          self.eventList.append(GenerateEvent(self.network, executionTime))
          self.eventList.sort(reverse=True, key = Event.getExecutionTime)

        #Czy ten report ma być powtarzany dla każdego usera co 20s?
        elif self.eventList[-1].eventType() == "ReportEvent":
          self.eventList[-1].execute()
          reportExecutionTime = self.eventList[-1].getExecutionTime() + 20
          self.eventList.pop(-1)
          self.eventList.append(ReportEvent(self.network, reportExecutionTime))
          self.eventList.sort(reverse=True, key = Event.getExecutionTime)
          
          


      #czas--
      for event in self.eventList:
        event.updateTime(3)