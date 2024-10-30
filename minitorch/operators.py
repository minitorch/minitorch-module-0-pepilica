"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


def mul(a, b):
    return a * b


def id(a):
    return a


def add(a, b):
    return a + b


def neg(a):
    return -a


def lt(a, b):
    return a < b


def eq(a, b):
    return a == b


def max(a, b):
    if lt(a, b):
        return b
    return a


def is_close(a, b):
    return abs(a - b) < 1e-2


def sigmoid(x):
    return (1. / (1. + math.exp(-x))) if x >= 0 else (math.exp(x) / (1. + math.exp(x)))


def relu(x):
    return 0 if x < 0 else x


def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def inv(x):
    return 1. / x


def log_back(x, c=1):
    return c / x


def inv_back(x, c=1):
    return -c / x ** 2


def relu_back(x, c=1):
    return c if x >= 0 else 0


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(iter, func):
    for i in iter:
        yield func(i)


def zipWith(iter1, iter2):
    iter2_iterator = iter(iter2)
    i2 = None
    is_second_exhausted = False
    for i1 in iter1:
        try:
            i2 = next(iter2_iterator)
        except StopIteration:
            is_second_exhausted = True
        if is_second_exhausted:
            break
        yield (i1, i2)


def reduce(iter, func, init_value=0):
    cur_value = init_value
    for i in iter:
        cur_value = func(cur_value, i)
    return cur_value


def negList(arr):
    return list(map(arr, lambda x: -x))


def addLists(arr1, arr2):
    a = zipWith(arr1, arr2)
    b = map(a, lambda x: x[0] + x[1])
    return list(b)


def sum(arr):
    return reduce(arr, lambda a, b: a + b, 0)


def prod(arr):
    return reduce(arr, lambda a, b: a * b, 1)

