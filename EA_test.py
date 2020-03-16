from EA import erzeuge_individuum, berechne_fitness
import numpy as np

def test_erzeuge_individuum():

    for i in range(999):
        test1 = erzeuge_individuum(i)
        assert test1.shape[0] == test1.shape[1]
        assert np.sum(test1) == i



def test_berechne_fitness():

        eins = [0,1,0]
        zwei = [1,1,1]
        drei = [0,1,1]

        i = np.array([eins, zwei, drei])
        test2 = berechne_fitness(i)
        assert np.dtype(test2) == np.float #oder dtype
