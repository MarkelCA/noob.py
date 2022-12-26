import random
import time
import math
import dis 

def f_1():
    random.seed()

print('\nCall stack\n---------------')
dis.dis(f_1)


def tight_loop_slow(iterations):
    """
    >>> %timeit tight_loop_slow(10000000)
    1 loops, best of 3: 3.2 s per loop
    """
    result = 0
    start = time.perf_counter()
    for i in range(iterations):
        # this call to sin requires two dictionary lookups
        result += math.sin(i)

    end = time.perf_counter()
    print(f"Time: {end - start:0.4f} seconds")

tight_loop_slow(20000000)

