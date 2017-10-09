import numpy as np
import math
import operator

from functools import reduce


def griewank(*args):
    sumatory = 1.0 / 4000 * np.sum([(x**2) for x in args])
    product = np.prod([np.cos(x / np.sqrt(i+1.0)) for i, x in enumerate(args)])

    return 1 + sumatory - product
