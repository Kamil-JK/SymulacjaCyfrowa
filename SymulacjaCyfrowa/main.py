from Simulator import Simulator 
from os import system
import math

system('cls')

alfa = 1
_lambda = 0.2

x=2999
l=5000

powerBS1 = 4.56 - 22 * math.log10(x)
powerBS2 = 4.56 - 22 * math.log10(l - x)

print(powerBS1)
print(powerBS2)
print(math.log10(x))
print(math.log10(l - x))
print(powerBS2 - powerBS1)

powerBS1 = 4.56 - 22 * math.log10(x) - 8.5
powerBS2 = 4.56 - 22 * math.log10(l - x) + 8.5

print(powerBS1)
print(powerBS2)
print(powerBS2 - powerBS1)


for simulationNumber in range(1,2):
    simulator = Simulator(simulationNumber, _lambda, alfa)
    simulator.mainLoop()

