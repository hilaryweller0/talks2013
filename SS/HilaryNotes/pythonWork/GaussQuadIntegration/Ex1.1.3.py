# Calculate the approximate integral of sin(x) between a and b
# using 1-point Gaussiaun quadrature using n intervals

# First import all funcitons from the Numerical Python libaray
from numpy import *

# Set integration limits and number of intervals
a = 0.0
b = pi
n = 70
m = 10
# from these calculate the interval length
dx = (b - a)/n
# Initialise the integral
I = 0

# Sum contribution from each interval
# (end of loop set by end of indentation)
for i in xrange(1,n):
    I += sin(m*(i-0.5)*dx)

I *= dx

print 'Gaussian quadrature integral with ', n, ' intervals = ', I, \
    '\nExact integral = ', (-cos(m*b)+cos(m*a))/m, \
    ', error = ', I + (cos(m*b)-cos(m*a))/m


# Error as a function of dx for integrating 1/x^p between 1 and 101
# using Gaussian quadrature
from numpy import *
import matplotlib.pyplot as plt
plt.ion()

a = 0.1
b = 11
n = 10**arange(4,9)
nn = size(n)
p = 8
Iexact = 1./(p-1.)*(a**(1-p) - b**(1-p))
dxs = zeros(nn)
error = zeros(nn)
for i in xrange(0,nn):
    n[i]
    I = 0
    dx = (b-a)/float(n[i])
    dxs[i] = dx
    for ix in xrange(0,n[i]):
        x = a+(ix+0.5)*dx
        I += x**(-p)
    I *= dx
    error[i] = abs(I - Iexact)

plt.clf()
plt.loglog(dxs, error)

