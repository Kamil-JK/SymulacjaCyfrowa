from SimulatorV import Simulator 
from os import system
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t
import pandas

system('cls')

v = [5, 20, 35, 50]
_lambda = 1.16
alfa = 1
simulations = 10 # liczba symulacji dla jednej wartości lambda
maxUsersNumber = 400 # maksymalna liczba obsłużonych użytkowników wchodzących do wykresu
initialPhase = 100 # faza początkowa
firstSeed = 12345 # pierwsze ziarno generatora
averageDisconnectedList = []
disconnectedIntervals = []
averageSwitchList = []
switchedIntervals = []
averagePositionList = []
positionIntervals = []


plt.figure(1)

for k in range(len(v)):

    print("v = " + str(v[k]))
    disconnectedUsers = []
    switchedUsers = []
    avgSwitchPosition = []

    for i in range(1, simulations + 1):
        simulator = Simulator(i + k * simulations, _lambda, alfa, maxUsersNumber, firstSeed, v[k])
        simulator.mainLoop()
        disconnected = simulator.disconnectedUsers
        switched = simulator.switchedUsers
        switchPosition = simulator.avgSwitchPosition
        disconnectedUsers.append(disconnected)
        switchedUsers.append(switched)
        avgSwitchPosition.append(switchPosition)


    #Przedziały ufności
    average = np.mean(disconnectedUsers)
    averageDisconnectedList.append(average)
    standardDeviation = np.std(disconnectedUsers)
    dof = len(disconnectedUsers) - 1  # Stopnie swobody
    confFactor = 0.05  # Współczynnik ufności
    criticalValue = t.ppf(1 - confFactor/2, df=dof)  # Wartość krytyczna dla danego współczynnika ufności i stopni swobody
    disconnectedMargin = criticalValue * standardDeviation / np.sqrt(len(disconnectedUsers))# Margines błędu
    disconnectedIntervals.append((average - disconnectedMargin, average + disconnectedMargin))

    average = np.mean(switchedUsers)
    averageSwitchList.append(average)
    standardDeviation = np.std(switchedUsers)
    dof = len(switchedUsers) - 1  # Stopnie swobody
    confFactor = 0.05  # Współczynnik ufności
    criticalValue = t.ppf(1 - confFactor/2, df=dof)  # Wartość krytyczna dla danego współczynnika ufności i stopni swobody
    switchedMargin = criticalValue * standardDeviation / np.sqrt(len(switchedUsers))# Margines błędu
    switchedIntervals.append((average - switchedMargin, average + switchedMargin))

    average = np.mean(avgSwitchPosition)
    averagePositionList.append(average)
    standardDeviation = np.std(avgSwitchPosition)
    dof = len(avgSwitchPosition) - 1  # Stopnie swobody
    confFactor = 0.05  # Współczynnik ufności
    criticalValue = t.ppf(1 - confFactor/2, df=dof)  # Wartość krytyczna dla danego współczynnika ufności i stopni swobody
    positionMargin = criticalValue * standardDeviation / np.sqrt(len(avgSwitchPosition))# Margines błędu
    positionIntervals.append((average - positionMargin, average + positionMargin))



x = v

y = averageDisconnectedList
intervals = [interval[1] - interval[0] for interval in disconnectedIntervals]
plt.figure(1)
plt.errorbar(x, y, yerr=intervals, fmt='o', capsize=5)
plt.xlabel("Prędkość użytkowników")
plt.ylabel("Średnia liczba rozłączonych użytkowników")
plt.xticks(x)
plt.grid(True)

y = averageSwitchList
intervals = [interval[1] - interval[0] for interval in switchedIntervals]
plt.figure(2)
plt.errorbar(x, y, yerr=intervals, fmt='o', capsize=5)
plt.xlabel("Prędkość użytkowników")
plt.ylabel("Średnia liczba przełączeń użytkowników")
plt.xticks(x)
plt.grid(True)

y = averagePositionList
intervals = [interval[1] - interval[0] for interval in positionIntervals]
plt.figure(3)
plt.errorbar(x, y, yerr=intervals, fmt='o', capsize=5)
plt.xlabel("Prędkość użytkowników")
plt.ylabel("Średnia odległość przełączenia")
plt.xticks(x)
plt.grid(True)

plt.show() 

#     x = range(maxUsersNumber)[initialPhase:] #bez fazy początkowej
#     y = userAvg[initialPhase:]
#     plt.plot(x, y, label = str(_lambda[k]))

#     # wykres z przedziałami ufności
#     averageUsers = userAvg[initialPhase:]
#     average = np.mean(averageUsers)
#     averageArray.append(average)
#     standardDeviation = np.std(averageUsers)
#     dof = len(averageUsers) - 1  # Stopnie swobody
#     confFactor = 0.05  # Współczynnik ufności
#     criticalValue = t.ppf(1 - confFactor/2, df=dof)  # Wartość krytyczna dla danego współczynnika ufności i stopni swobody
#     margin = criticalValue * standardDeviation / np.sqrt(len(averageUsers))# Margines błędu
#     confidenceInterval.append((average - margin, average + margin))


# plt.xlabel("Liczba obsłużonych użytkowników")
# plt.ylabel("Średnia liczba użytkowników w systemie")
# plt.legend(title = "Lambda")


# plt.figure(2)
# x = _lambda
# y = averageArray
# intervals = [interval[1] - interval[0] for interval in confidenceInterval]

# plt.errorbar(x, y, yerr=intervals, fmt='o', capsize=5)
# plt.xlabel("Lambda")
# plt.ylabel("Średnia liczba użytkowników w systemie")
# plt.xticks(x)
# plt.grid(True)
# plt.show() 
