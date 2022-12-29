import logging

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
logging.debug('oeunthoo')


def par(func):
    def wrapper(*args, **kwargs):
        logger.disabled = True
        func(*args, **kwargs)
        logger.disabled = False

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
        # logger.debug('nth')
        count += 1
        logger.debug(f'{count / n * 100:0.2f} %')

    return fact




fac(200000, True)
logger.debug('finished')
