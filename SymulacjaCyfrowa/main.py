from Simulator import Simulator 
from os import system

system('cls')

for simulationNumber in range(1):
    simulator = Simulator(simulationNumber, 0.2)
    simulator.mainLoop()