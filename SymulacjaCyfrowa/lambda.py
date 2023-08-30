from Simulator import Simulator 
from os import system
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

system('cls')

alfa = 3
_lambda = [1.14, 1.16, 1.18, 1.2, 1.22]
simulations = 20 # liczba symulacji dla jednej wartości lambda
maxUsersNumber = 400 # maksymalna liczba obsłużonych użytkowników wchodzących do wykresu
initialPhase = 100 # faza początkowa
firstSeed = 12345 # pierwsze ziarno generatora
averageArray = []
standardDeviationArray = []
confidenceInterval = []

plt.figure(1)

for k in range(len(_lambda)):

    usersInSystem = []
    userSum = np.zeros(maxUsersNumber) #Pomocnicza do stworzenia średniej
    userAvg = np.zeros(maxUsersNumber) #Średnia liczba użytkowników w systemie

    for simulationNumber in range(1, simulations + 1):
        simulator = Simulator(simulationNumber + k * simulations, _lambda[k], alfa, maxUsersNumber, firstSeed)
        simulator.mainLoop()
        print("Simulation " + str(k*simulations + simulationNumber))
        usersInSystem.append(simulator.usersInSystem)

    for j in range(len(usersInSystem[0])):
        for i in range(len(usersInSystem)):
            userSum[j] = userSum[j] + usersInSystem[i][j]

    for i in range(len(userAvg)):
        userAvg[i] = userSum[i] / simulations

    x = range(maxUsersNumber)[initialPhase:] #bez fazy początkowej
    y = userAvg[initialPhase:]
    plt.plot(x, y, label = str(_lambda[k]))

    # wykres z przedziałami ufności
    averageUsers = userAvg[initialPhase:]
    average = np.mean(averageUsers)
    averageArray.append(average)
    standardDeviation = np.std(averageUsers)
    dof = len(averageUsers) - 1  # Stopnie swobody
    confFactor = 0.05  # Współczynnik ufności
    criticalValue = t.ppf(1 - confFactor/2, df=dof)  # Wartość krytyczna dla danego współczynnika ufności i stopni swobody
    margin = criticalValue * standardDeviation / np.sqrt(len(averageUsers))# Margines błędu
    confidenceInterval.append((average - margin, average + margin))


plt.xlabel("Liczba obsłużonych użytkowników")
plt.ylabel("Średnia liczba użytkowników w systemie")
plt.legend(title = "Lambda")


plt.figure(2)
x = _lambda
y = averageArray
intervals = [interval[1] - interval[0] for interval in confidenceInterval]

plt.errorbar(x, y, yerr=intervals, fmt='o', capsize=5)
plt.xlabel("Lambda")
plt.ylabel("Średnia liczba użytkowników w systemie")
plt.xticks(x)
plt.grid(True)
plt.show() 
