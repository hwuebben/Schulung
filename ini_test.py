from EA import *
size = 10

board = erzeuge_individuum(size)
assert len(board.flat) == size**2

assert berechne_fitness(board) > 0
assert type(berechne_fitness(board)) == 'numpy.float64'