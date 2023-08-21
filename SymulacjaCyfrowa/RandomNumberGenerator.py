import numpy as np
import random
import math

class RandomNumberGenerator:

    M = 2147483647.0
    A = 16807
    Q = 127773
    R = 2836
    
    def __init__(self, _lambda, seedUniform): #, seedGauss):
        self.seedUniform = seedUniform
        self._lambda = _lambda

    def randUniform(self):
        h = np.floor(self.seedUniform / self.Q)
        s = self.A * (self.seedUniform - self.Q * h) - self.R * h
        if (s < 0):
            s = s + self.M
        self.seedUniform = s
        return s / self.M
    
    def randExponential(self):
        k = self.randUniform()
        return -(1 / self._lambda) * np.log(k)
    
    def randGauss(self, mean, deviation):
        # Według algorytmu Boxa-Mullera
        u1 = 1.0 - self.randUniform()  # Wartość z przedziału (0, 1)
        u2 = 1.0 - self.randUniform()  # Wartość z przedziału (0, 1)
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        return mean + z0 * deviation
    
    
    

# import numpy as np
# import random
# import math

# class RandomNumberGenerator:

#     M = 2147483647.0
#     A = 16807
#     Q = 127773
#     R = 2836
    
#     def __init__(self, _lambda):
#         self._lambda = _lambda

#     def randUniform(self, seed):
#         s = seed
#         h = np.floor(s / self.Q)
#         s = self.A * (s - self.Q * h) - self.R * h
#         if (s < 0):
#             s = s + self.M
#         return s / self.M
    
#     def randExponential(self, seed):
#         k = self.randUniform(seed)
#         return -(1 / self._lambda) * np.log(k)
    
#     def randGauss(self, mean, deviation):
#         # Według algorytmu Boxa-Mullera
#         u1 = 1.0 - random.random()  # Wartość z przedziału (0, 1)
#         u2 = 1.0 - random.random()  # Wartość z przedziału (0, 1)
#         z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
#         return mean + z0 * deviation
    
    
