from Simulator import Simulator 
from os import system
import math
import matplotlib.pyplot as plt
import numpy as np

system('cls')

alfa = 3
_lambda = [1.14, 1.16, 1.18, 1.2, 1.22]
# _lambda = [1.16, 1.17, 1.18, 1.19, 1.20] #, 1.2, 1.22, 1.24]
# _lambda = [0.32, 0.34, 0.36, 0.38, 0.4]
# _lambda = [1.18, 1.2, 1.22, 1.24, 1.26]
simulations = 20 # 10
maxUsersNumber = 400
# x = np.zeros(simulations)
# y = np.zeros(simulations)

for k in range(len(_lambda)):

    usersInSystem = []
    userSum = np.zeros(maxUsersNumber) #Pomocnicza do stworzenia średniej
    userAvg = np.zeros(maxUsersNumber) #Średnia liczba użytkowników w systemie

    for simulationNumber in range(1, simulations + 1):
        simulator = Simulator(simulationNumber + k * simulations, _lambda[k], alfa, maxUsersNumber)
        simulator.mainLoop()
        #print(simulator.usersInSystem)
        print("sim" + str(k*simulations + simulationNumber) + " over")
        usersInSystem.append(simulator.usersInSystem)

    # print(usersInSystem[0]) 
    # print(usersInSystem[0][2]) 

    for j in range(len(usersInSystem[0])):
        for i in range(len(usersInSystem)):
            userSum[j] = userSum[j] + usersInSystem[i][j]

    #print(userSum)

    for i in range(len(userAvg)):
        userAvg[i] = userSum[i] / simulations

    x = range(maxUsersNumber)
    y = userAvg 
    # print(x)
    # print(y)
    plt.plot(x, y, label = str(_lambda[k]))

plt.xlabel("Liczba obsłużonych użytkowników")
plt.ylabel("Średnia liczba użytkowników w systemie")
plt.legend(title = "Lambda")
plt.show() 





