import logging

logging.debug('oeunthoo')
# logger = logging.getLogger()
# logger.setLevel(level=logging.DEBUG)


def par(func):
    def wrapper(*args, **kwargs):
        logger.debug('oeunth')
        func(*args, **kwargs)

    return wrapper

@par
def fac(n: int, out: bool = False) -> int:
    count = 0

    # Normal behavior
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    # End Normal behavior

        # if out:
            # print(fact)

        count += 1
        # print(str(count / n * 100) + '%')

    return fact



# logger.debug('oeuntth')


# fac(3000, True)
    
