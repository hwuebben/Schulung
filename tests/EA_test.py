import numpy as np

from EA import *

def test_erzeuge_individuum():
    for n in range(10):
        x = erzeuge_individuum(n)
        assert x.shape == (n,n)
        assert x.dtype == np.int
        assert np.count_nonzero(x[:]) == n

def test_berechne_fitness():
    for n in range(1,10):
        xn = berechne_fitness(erzeuge_individuum(n))
        assert xn >= 0. 
        assert xn <= 1.
        assert xn.dtype == np.float