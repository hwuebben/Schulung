# Created by HEW at 17.03.2020
import threading
import concurrent.futures
import multiprocessing
import time


def test_func():
    time.sleep(1)
    print("done")

def threads_old():
    threads = []
    for _ in range(20):
        t = threading.Thread(target=test_func)
        t.start()
        threads.append(t)

    print("programm geht weiter1")

    for t in threads:
        t.join()

    print("programm geht weiter2")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        processes = [executor.submit(test_func) for _ in range(20)]
        print("programm geht weiter3")

        # for process in processes:
        for f in concurrent.futures.as_completed(processes):
            print(f.result())
        print("programm geht weiter4")


def mp_old():
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=test_func)
        process.start()
        processes.append(process)

    print("pos 1")
    for p in processes:
        p.join()
    print("pos 2")

if __name__ == "__main__":
    mp_old()



