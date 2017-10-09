import math
import operator

from functools import reduce


def griewank(*args):
    sumatory = 1.0 / 4000 * sum([(args[i]**2) for i in range(len(args))])
    product = (math.cos(args[i] / math.sqrt(i+1.0)) for i in range(len(args)))
    product = reduce(operator.mul, product, 1)

    return 1 + sumatory - product
