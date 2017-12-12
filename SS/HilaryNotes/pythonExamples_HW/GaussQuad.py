# Calculate the approximate integral of sin(x) between a and b
# using 1-point Gaussiaun quadrature using N intervals

# First import all functions from the Numerical Python library
import numpy as np

# Set integration limits and number of intervals
a = 0.0              # a is real, not integer, so dont write a = 0
b = np.pi            # pi is from numpy library so prefix with np.
N = 40               # N is an integer
# from these calculate the interval length
dx = (b - a)/N       # since a and b are real, dx is real
# Initialise the integral
I = 0.0

# Sum contribution from each interval (end of loop at end of indentation)
for i in xrange(0,N):    # : at the beginning of a loop
    x = a + (i+0.5)*dx
    I += np.sin(x)       # sin is in the numpy library so prefix with np.

I *= dx

print 'Gaussian quadrature integral = ', I, \
    '\nExact integral = ', -np.cos(b)+np.cos(a), \
    ' dx = ', dx, ', error = ', I + np.cos(b)-np.cos(a)

