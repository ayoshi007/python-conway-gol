import pytest
import numpy as np
from conway_gol.grid import GridOfLife


@pytest.fixture
def get_still_life_grid() -> GridOfLife:
    grid = GridOfLife(
        m=10, n=10,
        starting_pattern=np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ])
    )
    return grid


@pytest.fixture
def get_glider_grid() -> GridOfLife:
    grid = GridOfLife(
        m=10, n=10,
        starting_pattern=np.array([
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
        ])
    )
    return grid


@pytest.fixture
def get_copperhead() -> GridOfLife:
    grid = GridOfLife(
        m=30, n=30,
        starting_pattern=np.array([
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        ])
    )
    return grid


def test_still_life(get_still_life_grid):
    grid: GridOfLife = get_still_life_grid
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ])).all()
    grid.clear_game()
    assert (grid.get_current_pattern() == []).all()


def test_glider_gun(get_glider_grid):
    grid: GridOfLife = get_glider_grid
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0],
    ])).all()
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
    ])).all()
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [1, 0, 0],
        [0, 1, 1],
        [1, 1, 0],
    ])).all()
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ])).all()


def test_copperhead(get_copperhead):
    grid: GridOfLife = get_copperhead
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
    ])).all()
    grid.step_backward()
    assert (grid.get_current_pattern() == np.array([
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    ])).all()
    grid.step_forward()
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ])).all()


def test_toggle_cell(get_glider_grid):
    grid: GridOfLife = get_glider_grid
    grid.toggle_cell(4, 6)
    assert (grid.get_current_pattern() == np.array([
        [0, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
    ])).all()
    grid.step_forward()
    assert (grid.get_current_pattern() == np.array([
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
    ])).all()
    assert (grid.get_grid() == np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])).all()

def test_overflow(get_glider_grid):
    grid: GridOfLife = get_glider_grid
    for i in range(12):
        grid.step_forward()
    grid.step_forward()
    assert (grid.get_grid() == np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    ])).all()
    grid.step_backward()
    assert (grid.get_grid() == np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    ])).all()
    grid.step_forward()
    grid.step_forward()
    assert (grid.get_grid() == np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    ])).all()
