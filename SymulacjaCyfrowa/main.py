from Simulator import Simulator 
from os import system
from RandomGenerator import RandomGenerator 

system('cls')
seed = 44
simulator = Simulator(seed)
simulator.mainLoop()