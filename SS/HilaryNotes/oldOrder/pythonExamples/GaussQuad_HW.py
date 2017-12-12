# Calculate the approximate integral of sin(x) between a and b
# using 1-point Gaussiaun quadrature using n intervals

# First import all functions from the Numerical Python library
from numpy import *

# Set integration limits and number of intervals
a = 0.0
b = pi
n = 4000000
m = 1
# from these calculate the interval length
dx = (b - a)/n
# Initialise the integral
I = 0.0

# Sum contribution from each interval (end of loop at end of indentation)
for i in xrange(0,n):
    x = a + (i+0.5)*dx
    I += sin(m*x)

I *= dx

exact = (-cos(m*b)+cos(m*a))/m
print 'Gaussian quadrature integral = ', I, \
    '\nExact integral = ', exact, \
    ' dx = ', dx, ', error = ', I - exact, \
    ' % error = ', 100*(I - exact)/exact

