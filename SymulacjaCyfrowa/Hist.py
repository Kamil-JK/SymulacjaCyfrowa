from RandomGenerator import RandomGenerator 
from RandomNumberGenerator import RandomNumberGenerator 
import matplotlib.pyplot as plt

uniform = []
exponential = []
gauss = []

# for i in range(1, 10000):
#     generator = RandomGenerator(i * 10000, 0.2)
#     uniform.append(generator.rand())
#     exponential.append(generator.randExp())
#     gauss.append(generator.randGauss(0, 4))

generator = RandomNumberGenerator(0.2)
for i in range(1, 10000):
    uniform.append(generator.randUniform(i))
    exponential.append(generator.randExponential(i))
    gauss.append(generator.randGauss(0, 4))

plt.figure(1)
plt.hist(uniform, bins=550)
plt.title("Rozkład równomierny")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")

plt.figure(2)
plt.hist(exponential, bins=50)
plt.title("Rozkład wykładniczy")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")

plt.figure(3)
plt.hist(gauss, bins=50)
plt.title("Rozkład Gaussa")
plt.xlabel("Wartość")
plt.ylabel("Liczba wystąpień")


plt.show() 