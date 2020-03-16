# Created by HEW at 04.03.2020
import numpy as np
"""
Diese Datei implementiert eine einfache trial and error Loesung fuer das
Turm Problem
"""


def create_random_array(n):
    """
    erzeuge boolean array der shape (n,n)
    mit n zufällig verteilten True/1 Einträgen
    """
    board = np.zeros((n,n))
    rand_inds = np.random.choice(np.arange(n**2), size = n, replace=False)
    board.flat[rand_inds] = 1
    return board


def create_random_array_2(n):
    """
    erzeuge boolean array der shape (n,n)
    mit n zufällig verteilten True/1 Einträgen
    """
    board = np.zeros((n,n))
    nr_queens = 0
    while nr_queens < n:
        rand_ind_x = np.random.randint(n)
        rand_ind_y = np.random.randint(n)
        if board[rand_ind_x, rand_ind_y] == 0:
            board[rand_ind_x, rand_ind_y] = 1
            nr_queens += 1
    return board


def create_random_array_3(n):
    """
    erzeuge boolean array der shape (n,n)
    mit n zufällig verteilten True/1 Einträgen
    """
    board = np.zeros(n**2)
    board[0:n] = 1
    np.random.shuffle(board)
    board = board.reshape((n,n))
    return board


def check_array(a):
    """
    nehme array a entgegen und überprüfe ob 1/True-Einträge
    in gleicher Zeile oder Spalte vorhanden
    :param a:
    :return: False falls dies der Fall ist sonst True
    """
    zeilen = []
    spalten = []
    for zeile in range(a.shape[0]):
        for spalte in range(a.shape[1]):
            if a[zeile, spalte] == 0:
                continue
            if zeile in zeilen or spalte in spalten:
                return False
            zeilen.append(zeile)
            spalten.append(spalte)
    return True


def check_array_2(a):
    """
    nehme array a entgegen und überprüfe ob 1/True-Einträge
    in gleicher Zeile oder Spalte vorhanden
    :param a:
    :return: False falls dies der Fall ist sonst True
    """
    zeilen_summen = np.sum(a, axis=0)
    spalten_summen = np.sum(a, axis=1)
    for zeilen_summe in zeilen_summen:
        if not zeilen_summe == 1:
            return False
    for spalten_summe in spalten_summen:
        if not spalten_summe == 1:
            return False
    return True


def check_array_3(a):
    """
    nehme array a entgegen und überprüfe ob 1/True-Einträge
    in gleicher Zeile oder Spalte vorhanden
    :param a:
    :return: False falls dies der Fall ist sonst True
    """
    zeilen_summen = np.sum(a, axis=0)
    spalten_summen = np.sum(a, axis=1)
    return np.all(zeilen_summen == 1) and np.all(spalten_summen == 1)


def check_array_4(a):
    """
    nehme array a entgegen und überprüfe ob 1/True-Einträge
    in gleicher Zeile oder Spalte vorhanden
    :param a:
    :return: False falls dies der Fall ist sonst True
    """
    x,y = np.nonzero(a)
    x_set = set(x)
    y_set = set(y)
    return x.size == len(x_set) and y.size == len(y_set)

if __name__ == "__main__":
    n = 5
    while True:
        a = create_random_array_3(n)
        if check_array_3(a):
            print(a)
            break
