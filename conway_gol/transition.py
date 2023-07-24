import numpy as np

ALIVE_SUM = 3
NO_CHANGE_SUM = 4


def step(state: np.ndarray, successor: np.ndarray, m: int, n: int) -> None:
    field_sum = 0
    for r in range(m):
        for c in range(n):
            field_sum = _get_field_sum(state, _get_neighborhood(r, c, m, n))
            successor[r, c] = field_sum == ALIVE_SUM
            if field_sum == NO_CHANGE_SUM:
                successor[r, c] = state[r, c]


def _get_field_sum(grid: np.ndarray, neighborhood: list[int]) -> int:
    return sum([grid[r, c] for r, c in neighborhood])


def _get_neighborhood(row: int, col: int, m: int, n: int) -> list[int]:
    arr = []
    arr.extend([
        [row - 1,   col - 1],   [row - 1,   col],   [row - 1,   col + 1],
        [row,       col - 1],   [row,       col],   [row,       col + 1],
        [row + 1,   col - 1],   [row + 1,   col],   [row + 1,   col + 1]
    ])
    arr = map(
        lambda rc:
        [
            m - 1 if rc[0] < 0 else (0 if rc[0] == m else rc[0]),
            n - 1 if rc[1] < 0 else (0 if rc[1] == n else rc[1])
        ],
        arr
    )

    return arr
