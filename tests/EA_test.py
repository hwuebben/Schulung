import numpy as np

def test_erzeuge_individuum():
    from EA import erzeuge_individuum
    choice_func=lambda x, size, replace: x[:size]

    for n in range(10):
        x = erzeuge_individuum(n, choice_func)
        assert x.shape == (n,n)
        assert x.dtype == np.int
        assert np.count_nonzero(x[:]) == n

def test_berechne_fitness():
    from EA import berechne_fitness
    for n in range(1,10):
        an = np.random.randint(0, 2, (n,n))
        xn = berechne_fitness(an)
        assert xn >= 0. 
        assert xn <= 1.
        assert xn.dtype == np.float


def test_mutiere_individuum():
    from EA import mutiere_individuum
    choice_func=lambda x, size=None, replace=None: x

    for n in range(1,10):
        x = np.random.randint(0, 2, (n,n))
        y = x.copy()
        mutiere_individuum(y, choice_func)

        assert x.shape == (n,n)
        assert x.dtype == np.int
        assert np.any(x != y)

test_mutiere_individuum()