import dis
from random import seed
from math import sin
import time
from mod import a
from mod2 import a

print(a) # Overriden from mod2

def f_2():
    seed()

print('\nCall stack\n---------------')
dis.dis(f_2)

def tight_loop_fast(iterations):
    """
    >>> %timeit tight_loop_fast(10000000)
    1 loops, best of 3: 2.56 s per loop
    """
    start = time.perf_counter()
    result = 0
    for i in range(iterations):
        # this call to sin only requires only one lookup
        result += sin(i)
    end = time.perf_counter()
    print(f"Time: {end - start:0.4f} seconds")

tight_loop_fast(20000000)

