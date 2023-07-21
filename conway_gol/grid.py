import numpy as np
from transition import step

class GridOfLife:
    def __init__(self, m: int, n: int, starting_pattern: np.ndarray = None):
        assert (m > 3 and n > 3)
        self.m = m
        self.n = n
        self.grid = np.full((m, n), False)
        if np.ndarray is not None:
            assert (starting_pattern.shape[0] <= m and starting_pattern.shape[1] <= n)
            self.__insert_pattern(starting_pattern)
    
    def __insert_pattern(self, pattern: np.ndarray):
        height, width = pattern.shape
        r, c = self.m // 2 - height // 2, self.n // 2 - width // 2
        for i in range(height):
            for j in range(width):
                self.grid[r + i, c + j] = pattern[i, j]
