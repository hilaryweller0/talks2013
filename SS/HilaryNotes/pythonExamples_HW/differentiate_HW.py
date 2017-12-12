# Code to numerically differentiate the geostrphic wind relation to 
# calculate u for a given function of space (y) and pressure (p)

from pylab import *

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
y = linspace(ymin, ymax, N+1)
p = p0 + pp*cos(y*pi/L)                 # cosine variation of pressure with y
uexact = pp*pi/(rho*f*L)*sin(y*pi/L) # exact geostrophic wind
u2pt = zeros(N+1)                    # empty array for the approximate wind
u2nd = zeros(N+1)                    # empty array for the 2nd order wind

# 2nd order, uncentred, finite difference approximations for dpdy at end
# points and consequently wind at the end points
# pressure gradient and u at y=ymin
dpdy = (p[1] - p[0])/dy
u2pt[0] = gradToWind*dpdy
dpdy = (-3*p[0] + 4*p[1] - p[2])/(2*dy)
u2nd[0] = gradToWind*dpdy
# and at y=ymax
dpdy = (p[N] - p[N-1])/dy
u2pt[N] = gradToWind*dpdy
dpdy = (p[N-2] - 4*p[N-1] + 3*p[N])/(2*dy)
u2nd[N] = gradToWind*dpdy

# centred approximation for the gradient at the mid-points
for j in xrange(1,N):
    dpdy = (p[j+1] - p[j-1])/(2*dy)
    u2pt[j] = gradToWind*dpdy
    u2nd[j] = u2pt[j]

# y and u at the mid-points between pressure points
ymid = arange(ymin+0.5*dy, ymax, dy)
umexact = pp*pi/(rho*f*L)*sin(ymid*pi/L)
umapprox = zeros(N)

for j in xrange(0,N):
    umapprox[j] = gradToWind*(p[j+1] - p[j])/dy


# plot the exact and approximate winds and their errors
# plot options
ion()
figure(1)
clf()
plot(y/1000., uexact, 'k-', label='Exact')
plot(y/1000., u2pt, '*k:', label='2-point differences', \
        ms=12,markeredgewidth=1.5, markerfacecolor='none')
plot(y/1000., u2nd, 'ok:', label='2nd order end-points', \
        ms=12,markeredgewidth=1.5, markerfacecolor='none')
plot(ymid/1000., umapprox, '+k:', label='mid-point differences', \
                  ms=12,markeredgewidth=1.5, markerfacecolor='none')
legend(loc='best')
xlabel('y (km)')
ylabel('u (m/s)')
savefig('geoWind.pdf')

# plot the errors
figure(2)
clf()
plot(y/1000., zeros_like(y), 'k-')
plot(y/1000., u2pt - uexact, '*k:', label='2-point differences', \
                  ms=12,markeredgewidth=1.5, markerfacecolor='none')
plot(y/1000., u2nd - uexact, 'ok:', label='2nd order end-points', \
                  ms=12,markeredgewidth=1.5, markerfacecolor='none')
plot(ymid/1000., umapprox-umexact, '+k:', label='mid-point differences', \
                  ms=12,markeredgewidth=1.5, markerfacecolor='none')
legend(loc='best')
xlabel('y (km)')
ylabel('u error (m/s)')
savefig('geoWindErrors.pdf')

