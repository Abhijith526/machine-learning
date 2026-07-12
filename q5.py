import random
import numpy
from scipy import stats


def gen_eration():
    num = []
    for i in range(25):
        num.append(random.randint(1, 10))
    return num


def mean(ls):
    return numpy.mean(ls)


def median(ls):
    return numpy.median(ls)


def mode(ls):
    return stats.mode(ls).mode


ls1 = gen_eration()

print("Generated List:", ls1)
print("Mean:", mean(ls1))
print("Median:", median(ls1))
print("Mode:", mode(ls1))