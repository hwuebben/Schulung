
import numpy as np
#dasdad

def create_random_array(n):

    'Erzeugt zufälliges Array mit nxn Feldern mit zufällig erzeugten True einträgen'

    ret = np.zeros(n*n)

    while np.count_nonzero(ret) < (len(ret)/n):
        ind = np.random.randint(0, n**2)
        ret[ind] = 1

    ret = ret == 1
    ret = np.reshape(ret, (n, n))

    return ret

def checkSolution(array):
    'Nimm Array entgegen und überprüfe of es sich um eine Lösung handelt'

    shape = np.shape(array)
    columns = shape[0]#Zeilen
    rows    = shape[1]#Spalten

    for i in range(columns):
        if np.count_nonzero(array[i]) > 1:
            return False
    for i in range(rows):
        if np.count_nonzero(array[:, i]) > 1:
            return False

    return True

def checkSolution_returnvalue(array):
    'Nimm Array entgegen und überprüfe of es sich um eine Lösung handelt'

    shape = np.shape(array)
    columns = shape[0]#Zeilen
    rows    = shape[1]#Spalten


    for i in range(columns):
        if np.count_nonzero(array[i]):
            return False
    for i in range(rows):
        if np.count_nonzero(array[:, i]) > 1:
            return False

    return True


def generateSolution_random(fieldsize):

    random_array = create_random_array(fieldsize)


    while checkSolution(random_array) == False:
        random_array = create_random_array(fieldsize)

        if not np.count_nonzero(random_array) == fieldsize:
            print("Error checksol/createField")
    return random_array

def generateSolution_genetic(fieldsize, popsize):

    'create Population'

    population = createPopulation(popsize)
    fitness = calcFitness(population)

    parents = []

    amountselect = 20

    'select best'
    for i in range(amountselect):
        bestindex = fitness.index(min(fitness))
        parents.append(population[bestindex])
        del fitness[bestindex]
        del population[bestindex]

    newpop = combine(parents)



    while checkSolution(random_array) == False:
        random_array = create_random_array(fieldsize)

        if not np.count_nonzero(random_array) == fieldsize:
            print("Error checksol/createField")
    return random_array


def combine(parents):
    'erhält zwei Kombinationen und kombiniert sie'

    father = parents[0]
    mother = parents[1]

    size = len(father)
    #TODO tatata

    ands = np.bitwise_and(father, mother)
    xors = np.bitwise_xor(father, mother)
    xorsts = np.count_nonzero(xors)
    andsts = np.count_nonzero(ands)

    missing = size - andsts

    pick = 0
    while pick < andsts:
        pass





def combine_muster(ind0, ind1):
    pass


def createPopulation(popsize=100):
    'erstellt eine Population und gibt sie als Liste zurück'
    liste = []
    for i in range(popsize):

        liste.append(create_random_array(fieldsize))

    population = liste
    return population



def calcFitness(population):
    'berechnet die Fitness und gibt sie als Liste zurück'
    liste = []

    shape = np.shape(population[0])
    columns = shape[0]  # Zeilen
    rows = shape[1]  # Spalten
    fieldlen = len(population)**0.5

    for j in range(len(population)):

        zeilen_summen = np.sum(population[j], axis=0)
        spalten_summen = np.sum(population[j], axis=1)

        add =  1 / (np.var(zeilen_summen) + np.var(spalten_summen))
        liste.append(add)
    popfitness = liste
    return popfitness



if __name__ == '__main__':

    fieldsize = 5
    popsize = 100

    combine(createPopulation(2))

    #print(random_array_solution)


#random_array_solution = generateSolution_random(fieldsize)
#print(random_array_solution)




