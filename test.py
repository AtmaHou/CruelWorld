# coding: utf-8
from scipy import stats
from scipy.stats import norm
import numpy
import pylab

X = norm()
Y = norm(loc=1.0,scale=2.0)
t = numpy.arange(-10, 10, 0.01)
pylab.plot(t,X.pdf(t),label="$X$",color="red"))
pylab.plot(t,Y.pdf(t),"b--",label="$Y$")