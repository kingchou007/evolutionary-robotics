import random
import numpy as np

class SOLUTION:

    def __init__(self):
        # a 3-row x 2-column matrix of random values
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
