import numpy as np
from EA import *
size = 10

board = erzeuge_individuum(size)
assert len(board.flat) == size**2

assert berechne_fitness(board) > 0

value = berechne_fitness(board)

print(type(value))

assert type(value) is np.float64