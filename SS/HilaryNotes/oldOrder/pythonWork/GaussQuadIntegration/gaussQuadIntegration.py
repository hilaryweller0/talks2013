from numpy import *

def trapezoidal_rule(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the composite trapezoidal rule, using n subintervals"""
    h = (b - a) / n
    s = f(a) + f(b)
    for i in xrange(1, n):
        s += 2 * f(a + i * h)
    return s * h / 2

def Gauss1Int(f, a, b, n):
    """Approximates the definite integral of f from a to b by
    the 1-point Gaussian quadrature, using n subintervals"""
    dx = (b - a) / n
    sum = 0
    for i in xrange(1, n):
        sum += f((i-0.5)*dx)
    return sum * dx

print trapezoidal_rule(lambda x:sin(x), 0.0, 10.0, 100000)

print Gauss1Int(lambda x:sin(x), 0.0, 10.0, 100000)



import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
plt.ion()

x = np.arange(0,1,0.01);

dx=0.1
xn = np.arange(0,1,dx);
xmid = xn + 0.5*dx;

plt.clf()
font = {'family' : 'Times',
        'weight' : 'normal',
        'size'   : 22}
plt.rc('font', **font)
plt.plot(x, np.sin(x*np.pi))
pl.bar(xn, np.sin(xmid*np.pi), width=dx, facecolor='none', edgecolor='black')
plt.xlabel('x')
plt.ylabel('f')

plt.savefig('GaussQuad.pdf', format='pdf')
plt.savefig('GaussQuad.eps', format='eps')

