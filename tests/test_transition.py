import pytest
import numpy as np
from conway_gol.transition import step


@pytest.fixture
def get_living_state():
	return np.array([
		[False,	False,	True,	False],
		[False,	True,	False,	False],
		[False,	True,	True,	False],
		[False,	False,	False,	False],
	])


@pytest.fixture
def get_dying_state():
	return np.array([
		[True,  True,   False,  True],
		[True,  True,   False,  True],
		[True,  True,   False,  True],
		[True,  True,   False,  True],
	])


def test_living_step(get_living_state):
	successor = np.empty(shape=(4, 4), dtype=np.bool_)
	state = get_living_state
	step(state, successor, 4, 4)
	assert (successor == np.array([
		[False,	False,	False,	False],
		[False,	True,	False,	False],
		[False,	True,	True,	False],
		[False,	True,	True,	False],
	])).all()


def test_dying_step(get_dying_state):
	successor = np.empty(shape=(4, 4), dtype=np.bool_)
	state = get_dying_state
	step(state, successor, 4, 4)
	step(successor, state, 4, 4)
	assert (successor == np.array([
		[False,	False,	False,	False],
		[False,	False,	False,	False],
		[False,	False,	False,	False],
		[False,	False,	False,	False],
	])).all()
	assert (state == successor).all()
