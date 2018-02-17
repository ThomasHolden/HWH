
import numpy as np
import datetime
from contextlib import contextmanager

@contextmanager
def stopwatch(message):
    t0 = datetime.datetime.now()
    try:
        yield
    finally:
        print(message,datetime.datetime.now() - t0)


def add2(x):
    return x + 2

N = 10000000

np.random.seed(42)
r = np.random.normal(0,1,N)

### List comprehension version
with stopwatch('List comprehension version took:'):
    r2 = [add2(x) for x in r if x >1]

### Loop version
with stopwatch('Loop version took:'):
    r3 = []
    for x in r:
        if x>1:
            val = add2(x)
            r3.append(val)

print(r3 == r2)



