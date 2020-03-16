import EA
size = 10

board = EA.erzeuge_individuum(size)
assert len(board.flat) == size**2

assert EA.berechne_fitness(board) > 0
assert type(EA.berechne_fitness(board)) == 'float'