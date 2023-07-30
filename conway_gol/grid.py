import numpy as np
from conway_gol.transition import step

class GridOfLife:
    def __init__(self, m: int, n: int, starting_pattern: np.ndarray = None):
        assert (m > 3 and n > 3)
        self.m = m
        self.n = n
        self.states = [np.full((m, n), 0, dtype=np.int8), np.empty((m, n), dtype=np.int8)]
        self.active_state_idx = 0

        if starting_pattern is not None:
            assert (starting_pattern.shape[0] <= m and starting_pattern.shape[1] <= n)
            self.__insert_pattern(starting_pattern)
        
        self.history = [self.states[0]]
    
    def __insert_pattern(self, pattern: np.ndarray) -> None:
        height, width = pattern.shape
        r, c = self.m // 2 - height // 2, self.n // 2 - width // 2
        for i in range(height):
            for j in range(width):
                self.states[0][r + i, c + j] = np.int8(pattern[i, j])

    def get_grid(self) -> np.ndarray:
        return self.states[self.active_state_idx]
    
    def step_forward(self) -> None:
        step(self.states[self.active_state_idx], self.states[1 - self.active_state_idx], self.m, self.n)
        self.active_state_idx = 1 - self.active_state_idx
        self.history.append(self.states[self.active_state_idx])
    
    def step_backward(self) -> None:
        self.history.pop()
        if len(self.history) > 1:
            self.states[self.active_state_idx] = self.history[-1]
            self.states[1 - self.active_state_idx] = self.history[-2]
            return
        
        self.active_state_idx = 1 - self.active_state_idx
        self.states[1] = np.empty((self.m, self.n), dtype=np.int8)
        self.states[0] = np.full((self.m, self.n), 0, dtype=np.int8) if not self.history else self.history[-1]

    def clear_game(self) -> None:
        self.states = [np.full((self.m, self.n), 0, dtype=np.int8), np.empty((self.m, self.n), dtype=np.int8)]
        self.active_state_idx = 0
        self.history = [self.states[0]]
    
    def toggle_cell(self, r: int, c: int) -> None:
        self.states[self.active_state_idx][r, c] = 1 - self.states[self.active_state_idx][r, c]
        self.history[-1] = self.states[self.active_state_idx]

    def get_generation_count(self) -> int:
        return len(self.history)

    def get_current_pattern(self) -> np.ndarray:
        top_r, bot_r, left_c, right_c = -1, -1, -1, -1
        for r in range(self.m):
            for c in range(self.n):
                if self.states[self.active_state_idx][r, c]:
                    if top_r == -1:
                        top_r = r
                    if left_c == -1 or c < left_c:
                        left_c = c
                    bot_r = r
                    right_c = c if c > right_c else right_c
        grid = []
        for r in range(top_r, bot_r + 1):
            grid.append([])
            for c in range(left_c, right_c + 1):
                grid[-1].append(self.states[self.active_state_idx][r, c])
        return np.array(grid, dtype=np.int8)