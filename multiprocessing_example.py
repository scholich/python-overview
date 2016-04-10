"""Example for multiprocessing.

"""
import time
from multiprocessing import Pool

def wait(i):
    time.sleep(.5)
    return i

if __name__ == "__main__":
    po = Pool(8)
    pool = Pool(processes=8)              # start 8 worker processes
    # result = pool.apply_async(f, range(8))
    # print result.get(timeout=1)           # prints "100" unless your computer is *very* slow
    currtime = time.time()
    print pool.map(wait, range(10))          # prints "[0, 1, 4,..., 81]"
    print 'time elapsed:', time.time() - currtime