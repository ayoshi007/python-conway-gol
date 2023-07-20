import numpy as np

ALIVE_SUM = 3
NO_CHANGE_SUM = 4

def step(state: np.ndarray, successor: np.ndarray, m: int, n: int) -> None:
    field_sum = 0
    for r in range(m):
        for c in range(n):
            field_sum = get_field_sum(state, get_neighborhood(r, c, m, n))
            successor[r, c] = field_sum == ALIVE_SUM
            if field_sum == NO_CHANGE_SUM:
                successor[r, c] = state[r, c]


def get_field_sum(grid: np.ndarray, neighborhood: list[int]) -> int:
    return sum([grid[r, c] for r, c in neighborhood])

def get_neighborhood(row: int, col: int, m: int, n: int) -> list[int]:
    arr = []
    arr.append(
        [row - 1,   col - 1],   [row - 1,   col],   [row - 1,   col + 1],
        [row,       col - 1],   [row,       col],   [row,       col + 1],
        [row + 1,   col - 1],   [row + 1,   col],   [row + 1,   col + 1]
    )
    arr = [
        [m - 1 if r < 0 else (0 if r == m else r), n - 1 if c < 0 else (0 if c == n else c)]
        for [r, c] in arr
    ]

    return arr
