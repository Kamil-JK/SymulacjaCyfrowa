from Simulator import Simulator 
from os import system
from RandomGenerator import RandomGenerator 

system('cls')

# generator = RandomGenerator(10000, 0.1)
# print(generator.randExp())
# generator = RandomGenerator(5245245, 0.2)
# print(generator.randExp())
# generator = RandomGenerator(234234, 0.3)
# print(generator.randExp())
# generator = RandomGenerator(64362, 0.4)
# print(generator.randExp())
# generator = RandomGenerator(2345, 0.5)
# print(generator.randExp())
# generator = RandomGenerator(64363, 0.6)
# print(generator.randExp())
# generator = RandomGenerator(64363, 0.6)
# print(generator.randGauss(0, 4))


for simulationNumber in range(1):
    simulator = Simulator(simulationNumber, 0.2)
    simulator.mainLoop()