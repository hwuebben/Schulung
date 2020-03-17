
def ui(x=1):
    return x+1


class Testclass():

    def __init__(self):
        self.test = 0

testobk = Testclass

testobk.neu = lambda a : a + 10
testobk.nsd = ui()

print(testobk.neu)
print(testobk.nsd)