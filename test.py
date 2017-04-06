# coding: utf-8
from scipy import stats
from scipy.stats import norm
import numpy
import pylab

a = numpy.random.normal(loc=0.0, scale=1.0, size=100)
print a


class InitTest:
    l = 10
    map = [[1 for i in range(l)] for j in range(l/2)]

    def __init__(self):
        pass

    def show(self):
        print self.map

t = InitTest()
t.show()
if isinstance(t, InitTest):
    print 2333
else:
    print 21111, type(t)
