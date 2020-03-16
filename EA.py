# Created by HEW at 04.03.2020
import numpy as np
import sys

"""
Diese Datei implementiert einen evolutionaeren Algorithmus 
zur Loesung des Turm Problems
"""


def erzeuge_individuum(n, choice_func=np.random.choice):
    """
    erzeuge ein Individuum
    bestehend aus einem boolean array der shape (n,n)
    mit n zufällig verteilten True/1 Einträgen
    :param n:
    :return: individuum
    """
    board = np.zeros((n, n), dtype=int)
    rand_inds = choice_func(np.arange(n**2), size=n, replace=False)
    board.flat[rand_inds] = 1
    return board


def berechne_fitness(ind):
    """
    berechne Fitness fuer ein gegebenes Individuum
    :param ind:
    :return: Fitness
    """
    zeilen_summen = np.sum(ind, axis=0)
    spalten_summen = np.sum(ind, axis=1)

    return 1 / (np.var(zeilen_summen) + np.var(spalten_summen) + 1)


def mutiere_individuum(ind, choice_func=np.random.choice):
    """
    mutiere (leichte Veraenderung) ein gegebenes individuum
    :param choice_func:
    :param ind:
    """
    besetzt = np.flatnonzero(ind)
    frei = np.flatnonzero(ind == 0)

    rand_queen_index = choice_func(besetzt)

    rand_free_index = choice_func(frei)

    ind.flat[rand_free_index] = 1
    ind.flat[rand_queen_index] = 0


def mutiere_individuum_2(ind):
    """
    mutiere (leichte Veraenderung) ein gegebenes individuum
    :param ind:
    """
    besetzt = []
    frei = []
    for i in range(ind.shape[0]):
        for j in range(ind.shape[1]):
            if ind[i, j] == 1:
               besetzt.append([i, j])
            else:
               frei.append([i, j])

    frei_tausch = frei[np.random.randint(0, len(frei))]
    besetzt_tausch = besetzt[np.random.randint(0, len(besetzt))]

    ind[frei_tausch[0], frei_tausch[1]] = 1
    ind[besetzt_tausch[0], besetzt_tausch[1]] = 0


def rekombiniere(ind0, ind1):
    """
    erzeuge ein "Kind"-Individuum durch Rekombination
    2er gegebener "Eltern"-Individuen ind0 und ind1.
    das Kind Individuum enthaelt die Eltern-Eintraege
    an Stellen an denen sich die ELtern gleichen.
    An den Stellen an denen sich die Eltern unterscheiden enthaelt das Kind
    zur einen Haelfte die Eintraege von ind0 und zur anderen die von ind1
    :param ind0:
    :param ind1:
    :return: das durch Rekombination erzeugte Individuum
    """
    xor_ind = np.logical_xor(ind0, ind1)
    and_ind = np.logical_and(ind0, ind1)

    xor_nonzeros = np.flatnonzero(xor_ind)
    chosen = np.random.choice(xor_nonzeros, size=xor_nonzeros.size // 2, replace=False)

    and_ind.flat[chosen] = 1
    return and_ind*1


def erzeuge_pop(pop_size, n):
    """
    erzeuge eine zufaellig initialisierte Population spezifizierter Groeße.
    :param pop_size: Groeße der Population
    :param n: Problemgroeße
    :return:
    """
    pop = []
    for _ in range(pop_size):
        pop.append(erzeuge_individuum(n))
    return pop


def selektiere_rekombination(pop, pop_fit):
    """
    waehle 2 Individuen zur Rekombination aus der Population aus.
    Die Auswahlwahrscheinlichkeit ist proportional zur Fitness der Individuen.
    :param pop:
    :param pop_fit:
    :return: die selektierten Individuen
    """
    i0, i1 = np.random.choice(np.arange(len(pop)),
                              size=2,
                              replace=False,
                              p=pop_fit / np.sum(pop_fit))
    return pop[i0], pop[i1]


def berechne_pop_fitness(pop):
    """
    berechne Fitness für die gesamte uebergebene Population
    :param pop:
    :return: Liste mit Fitnesswerten
    """
    pop_fit = []
    for ind in pop:
        pop_fit.append(berechne_fitness(ind))
    return pop_fit


def erzeuge_neue_generation(pop, pop_fit):
    """
    erzeuge naechste Population/Generation aus der aktuellen
    :param pop:
    :param pop_fit:
    :return: die neue Population, mit Fitness
    """
    """erzeuge neue Individuen"""
    new_pop = []
    for _ in range(pop_size):
        ind_0, ind_1 = selektiere_rekombination(pop, pop_fit)
        new_ind = rekombiniere(ind_0, ind_1)
        mutiere_individuum(new_ind)
        new_pop.append(new_ind)

    """ waehle die besten Individuen aus pop und new pop fuer die naechste Generation aus"""
    new_pop_fit = berechne_pop_fitness(new_pop)
    fit_combine = pop_fit + new_pop_fit
    pop_combine = pop + new_pop

    best_indices = np.argsort(fit_combine)[-pop_size::]
    final_pop = [pop_combine[i] for i in best_indices]# list comprehension
    final_pop_fit = [fit_combine[i] for i in best_indices]# list comprehension
    # die oben benutzte "List comprehension" ist eine Kurzschreibweise fuer:
    # pop_fit = []
    # for i in best_indices:
    #     pop_fit.append(fit_combine[i])
    return final_pop, final_pop_fit

if __name__ == "__main__":
    "initialisiere Parameter"
    pop_size = int(sys.argv[1])
    problem_size = int(sys.argv[2])
    max_gen = int(sys.argv[3])

    "erzeuge initiale Population"
    pop = erzeuge_pop(pop_size, problem_size)
    pop_fit = berechne_pop_fitness(pop)

    "starte Generationen Schleife"
    for _ in range(max_gen):
        "entnehme bestes Individuum"
        best_index = np.argmax(pop_fit)

        "Ueberpruefe Abbruchbedingung (optimales Ergebnis gefunden?)"
        if pop_fit[best_index] == 1:
            break

        "erzeuge naechste Population"
        pop, pop_fit = erzeuge_neue_generation(pop, pop_fit)

    print("Generationen Schleife beendet")
    print("beste Fitness: ", pop_fit[best_index])
    print("bestes Individuum:\n", pop[best_index])
