import EA
size = 10

board = EA.erzeuge_individuum(size)
assert len(board.flat) == size**2