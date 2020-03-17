import concurrent.futures
import time
import random

def test(tMax = 5):
    t = random.random() * tMax
    time.sleep(t)
    print(t)
    return t

def mp1(n=10):
    with concurrent.futures.ThreadPoolExecutor(n) as ex:
        fs = [ex.submit(test, _+1) for _ in range(n)]#

        print("Started")
        
    concurrent.futures.wait(fs)
    print("Summe: ", sum([f.result() for f in fs]))
    print("Finished")

mp1(5)