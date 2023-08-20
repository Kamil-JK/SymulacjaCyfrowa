from Simulator import Simulator 
from os import system
import math
import matplotlib.pyplot as plt
import numpy as np

system('cls')

alfa = 3
_lambda = [1.14, 1.16, 1.18, 1.2, 1.22]
# _lambda = [1.16, 1.17, 1.18, 1.19, 1.20] #, 1.2, 1.22, 1.24]
simulations = 3 # liczba symulacji dla jednej wartości lambda
maxUsersNumber = 400 # maksymalna liczba obsłużonych użytkowników wchodzących do wykresu
initialPhase = 100 # faza początkowa
firstSeed = 12345 # pierwsze ziarno generatora

for k in range(len(_lambda)):

    usersInSystem = []
    userSum = np.zeros(maxUsersNumber) #Pomocnicza do stworzenia średniej
    userAvg = np.zeros(maxUsersNumber) #Średnia liczba użytkowników w systemie

    for simulationNumber in range(1, simulations + 1):
        simulator = Simulator(simulationNumber + k * simulations, _lambda[k], alfa, maxUsersNumber, firstSeed)
        simulator.mainLoop()
        print("sim" + str(k*simulations + simulationNumber) + " over")
        usersInSystem.append(simulator.usersInSystem)

    for j in range(len(usersInSystem[0])):
        for i in range(len(usersInSystem)):
            userSum[j] = userSum[j] + usersInSystem[i][j]

    for i in range(len(userAvg)):
        userAvg[i] = userSum[i] / simulations

    x = range(maxUsersNumber)[initialPhase:] #bez fazy początkowej
    y = userAvg[initialPhase:]
    plt.plot(x, y, label = str(_lambda[k]))

plt.xlabel("Liczba obsłużonych użytkowników")
plt.ylabel("Średnia liczba użytkowników w systemie")
plt.legend(title = "Lambda")
plt.show() 





