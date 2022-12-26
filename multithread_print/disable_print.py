import io
import sys

class NullWriter(object):
    def write(self, arg):
        pass

def par(func):
    def wrapper(*args, **kwargs):
        try:
            text_trap = NullWriter()
            sys.stdout = text_trap

            func(*args, **kwargs)
        finally:
            sys.stdout = sys.__stdout__

    return wrapper

@par
def fac(n: int, out: bool = False) -> int:
    count = 0

    # Normal behavior
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    # End Normal behavior

        if out:
            print(fact)

        count += 1
        print(str(count / n * 100) + '%')

    return fact





fac(3000, True)
    
