# Code to numerically differentiate the geostrphic wind relation to 
# calculate u for a given function of space (y) and pressure (p)

import pylab as pl

# Constants describing the problem
p0 = 1e5             # the mean pressure
pp = 200.            # the magnitude of the pressure variations
f = 1e-4             # the Coriolis parameter
rho = 1.2            # density
L = 2.4e6            # the length scale of the pressure variations
ymin = 0.0           # the minimum space dimension
ymax = 1e6           # the maximum space dimension
N = 8                # the number of intervals to divide space into
dy = (ymax - ymin)/N # the length of the spacing
gradToWind = -1./(rho*f)  # constant scaling between pressure gradient and wind

# arrays for space (y), pressure (p), approximate wind (u2pt) and uexact
y = pl.linspace(ymin, ymax, N+1)     # array of N+1 elements from ymin to ymax
p = p0 + pp*pl.cos(y*pl.pi/L)        # cosine variation of pressure with y
uexact = pp*pl.pi/(rho*f*L)*pl.sin(y*pl.pi/L) # exact geostrophic wind
u2pt = pl.zeros(N+1)                 # empty array for the 2 point approx wind

# 1st order, uncentred, finite difference approximations for dpdy at end
# points and consequently wind at the end points
# pressure gradient and u at y=ymin
dpdy = (p[1] - p[0])/dy            # arrays are indexed from zero
u2pt[0] = gradToWind*dpdy
# and at y=ymax
dpdy = (p[N] - p[N-1])/dy          # p has N+1 elements so the last one is p[N]
u2pt[N] = gradToWind*dpdy

# centred approximation for the gradient at the mid-points
for j in xrange(1,N):         # returns the numbers 1 to N-1 in turn as needed
    dpdy = (p[j+1] - p[j-1])/(2*dy)
    u2pt[j] = gradToWind*dpdy

# plot the exact and approximate winds and their errors
# plot options
pl.ion()
pl.figure(1)
pl.clf()
pl.plot(y/1000., uexact, 'k-', label='Exact')
pl.plot(y/1000., u2pt, '*k:', label='2-point differences', \
           ms=12,markeredgewidth=1.5, markerfacecolor='none')
pl.legend(loc='best')
pl.xlabel('y (km)')
pl.ylabel('u (m/s)')
pl.savefig('geoWind.pdf')

# plot the errors
pl.figure(2)
pl.clf()
# (zeros_like returns an array of zeros of the same size as y)
pl.plot(y/1000., pl.zeros_like(y), 'k-')
pl.plot(y/1000., u2pt - uexact, '*k:', label='2-point differences', \
                     ms=12,markeredgewidth=1.5, markerfacecolor='none')
pl.legend(loc='best')
pl.xlabel('y (km)')
pl.ylabel('u error (m/s)')
pl.savefig('geoWindErrors.pdf')

