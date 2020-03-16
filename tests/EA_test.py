import numpy as np

from EA import erzeuge_individuum

def test_erzeuge_individuum():
    for n in range(10):
        x = erzeuge_individuum(n)
        assert x.shape == (n,n)
        assert x.dtype == np.int
        assert np.count_nonzero(x[:]) == n

def test_berechne_fitness():
    pass