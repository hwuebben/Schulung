from EA import *

def choice_func(x, size, replace):
    return x[0:size]

def test_inid():
    for n in range(1,10):
        board = erzeuge_individuum(n, choice_func)
        assert len(board.flat) == n**2

test_inid()