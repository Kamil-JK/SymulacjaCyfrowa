from Simulator import Simulator 
from os import system
import math
import matplotlib.pyplot as plt
import numpy as np

system('cls')

alfa = 3
#_lambda = [0.0010, 0.0011, 0.0012, 0.0013, 0.0014]
_lambda = [1.5]
simulations = 1 # 10
maxUsersNumber = 300
# x = np.zeros(simulations)
# y = np.zeros(simulations)

for k in range(len(_lambda)):

    usersInSystem = []
    userSum = np.zeros(maxUsersNumber) #Pomocnicza do stworzenia średniej
    userAvg = np.zeros(maxUsersNumber) #Średnia liczba użytkowników w systemie

    for simulationNumber in range(0, simulations):
        simulator = Simulator(simulationNumber * (k + 1), _lambda[k], alfa, maxUsersNumber)
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





