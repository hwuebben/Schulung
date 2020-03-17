import EA as ea

numero = 10

def ind_test():
    board = ea.erzeuge_individuum(numero)
    assert len(board.flat) == numero*numero

# main
ind_test()
