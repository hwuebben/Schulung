import numpy as np
from EA import *

def choice_func(x, size, replace):
    return x[0:size]

def test_inid():
    for n in range(1,10):
        board = erzeuge_individuum(n, choice_func)
        assert len(board.flat) == n**2

def test_mutate():
    board = np.zeros((3, 3))
    original = board
    mutiere_individuum(board)

    assert board == original

test_inid()
test_mutate()