import numpy as np
from EA import *
size = 10

board = erzeuge_individuum(size)
assert len(board.flat) == size**2