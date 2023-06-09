from Simulator import Simulator 
from os import system

system('cls')

alfa = 1
_lambda = 0.2

for simulationNumber in range(1):
    simulator = Simulator(simulationNumber, _lambda, alfa)
    simulator.mainLoop()