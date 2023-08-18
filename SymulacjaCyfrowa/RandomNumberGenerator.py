import numpy as np
import random
import math

class RandomNumberGenerator:

    M = 2147483647.0
    A = 16807
    Q = 127773
    R = 2836
    
    def __init__(self, _lambda):
        self._lambda = _lambda

    def rand(self, seed):
        s = seed
        h = np.floor(s / self.Q)
        s = self.A * (s - self.Q * h) - self.R * h
        if (s < 0):
            s = s + self.M
        return s / self.M
    
    def randExp(self, seed):
        k = self.rand(seed)
        return -(1 / self._lambda) * np.log(k)
    
    def randGauss(self, mean, deviation):
        # Według algorytmu Boxa-Mullera
        u1 = 1.0 - random.random()  # Wartość z przedziału (0, 1)
        u2 = 1.0 - random.random()  # Wartość z przedziału (0, 1)
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        return mean + z0 * deviation
    

    def randExp2(self, seed):
        h = np.floor(seed / self.Q)
        xx = (self.A * (seed - (self.Q * h))) - (self.R * h)
        if xx < 0:
            xx = xx + self.M
        self.seedEXP = xx

        # Generowanie liczby o rozkładzie wykładniczym
        result = -1 * (1/self._lambda) * np.log(xx / self.M)  

        return result
    
    # def GenerateNormal(self):
    #     u1, newSeed = self.UniformGeneratorForNormal(self.seedNOR)
    #     u2, self.seedNOR = self.UniformGeneratorForNormal(newSeed)
    #     r = np.sqrt(-2 * np.log(u1))
    #     theta = 2 * np.pi * u2
    #     z1 = r * np.cos(theta)
    #     z2 = r * np.sin(theta)
    #     x = 4 * z1  # Odchylenie standardowe = 4
    #     y = 4 * z2  # Odchylenie standardowe = 4
    #     return x, y

        