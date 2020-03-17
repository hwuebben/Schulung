from EA import erzeuge_individuum, berechne_fitness, mutiere_individuum
import numpy as np

def test_erzeuge_individuum():

    for i in range(999):
        def choicefunc(x, size, replace):   #depend injection
            return x[0:size]
        test1 = erzeuge_individuum(n=i, inj_func=choicefunc)
        assert test1.shape[0] == test1.shape[1]
        assert np.sum(test1) == i


def test_berechne_fitness():

        eins = [0,1,0]
        zwei = [1,1,1]
        drei = [0,1,1]

        i = np.array([eins, zwei, drei])
        test2 = berechne_fitness(i)
        assert np.dtype(test2) == np.float #oder dtype


def test_mutiere_individuum():
    # Arrange
    eins = [0, 1, 0]
    zwei = [1, 1, 1]
    drei = [0, 1, 1]


    ind = np.array([eins, zwei, drei])
    indc = np.copy(ind)

    size = np.size(ind)
    def choicefunc(x, size, replace):  # depend injection
        return x[0:size]
    # Act
    mutiere_individuum(ind)
    # Assert
    assert np.any(ind == indc)
