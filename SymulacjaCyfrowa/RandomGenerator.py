import numpy as np

class RandomGenerator:

    kM = 2147483647.0
    kA = 16807
    kQ = 127773
    kR = 2836
    _lambda = 1
    
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        h = self.seed / self.kQ
        self.seed = self.kA * (self.seed - self.kQ * h) - self.kR * h
        if (self.seed < 0):
            self.seed = self.seed + self.kM
        return self.seed / self.kM
    
    def randExp(self):
        h = self.seed / self.kQ
        self.seed = self.kA * (self.seed - self.kQ * h) - self.kR * h
        if (self.seed < 0):
            self.seed = self.seed + self.kM
        k = self.seed / self.kM
        return -(1 / self._lambda) * np.log(k)
        