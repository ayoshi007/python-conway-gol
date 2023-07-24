import numpy as np
from transition import step

class GridOfLife:
    def __init__(self, m: int, n: int, starting_pattern: np.ndarray = None):
        assert (m > 3 and n > 3)
        self.m = m
        self.n = n
        self.states = [np.full((m, n), np.False_), np.empty((m, n), dtype=np.bool_)]
        self.active_state_idx = np.False_

        if np.ndarray:
            assert (starting_pattern.shape[0] <= m and starting_pattern.shape[1] <= n)
            self.__insert_pattern(starting_pattern)
        
        self.history = [self.grid]
    
    def __insert_pattern(self, pattern: np.ndarray) -> None:
        height, width = pattern.shape
        r, c = self.m // 2 - height // 2, self.n // 2 - width // 2
        for i in range(height):
            for j in range(width):
                self.states[0][r + i, c + j] = pattern[i, j]

    def get_grid(self) -> np.ndarray:
        return self.states[self.active_state_idx]
    
    def step_forward(self) -> None:
        step(self.states[self.active_state_idx], self.states[~self.active_state_idx], self.m, self.n)
        self.active_state_idx = ~self.active_state_idx
        self.history.append(self.states[self.active_state_idx])
    
    def step_backward(self) -> None:
        self.history.pop()
        if len(self.history) > 1:
            self.states[self.active_state_idx] = self.history[-1]
            self.states[~self.active_state_idx] = self.history[-2]
            return
        
        self.active_state_idx = np.False_
        self.states[1] = np.empty((self.m, self.n), dtype=np.bool_)
        self.states[0] = np.full((self.m, self.n), False) if not self.history else self.history[-1]

    def clear_game(self) -> None:
        self.states = [np.full((self.m, self.n), False), np.empty((self.m, self.n), dtype=np.bool_)]
        self.active_state_idx = np.False_
        self.history = [self.states[0]]
    
    def toggle_cell(self, r: int, c: int) -> None:
        self.states[self.active_state_idx][r, c] = ~self.states[self.active_state_idx][r, c]

    def get_generation_count(self):
        return len(self.history)
