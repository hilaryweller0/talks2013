# Outer code for setting up the diffusion problem and calling the
# function to diffusion. Boundary conditions are fixed value
import pylab as pl

# all the diffusion schemes and initial conditions
execfile("diffusionSchemes.py")
execfile("initialConditions.py")

# input variables
xmax = 1.0              # limits of the geometry
xmin = 0.0              # (must be real numbers, not integers)
nx = 100                # number of intervals to divide the geometry
nt = 50                 # number of time steps
K = 1.                  # Diffusion coefficient
dx = (xmax - xmin)/nx   # spatial resolution
dt = 2e-5               # time step
Kdtbydx2 = K*dt/dx**2   # Non-dimensional diffusion coeffient

# spatial points for plotting and for defining initial conditions
x = pl.linspace(xmin, xmax, nx+1)

# initial conditions
phiOld = topHat(x)

# Diffusion using FTCS and BTCS
phiFTCS = FTCS(phiOld.copy(), Kdtbydx2, nt)
phiBTCS = BTCS(phiOld.copy(), Kdtbydx2, nt)

# plot options
font = {'size'   : 14}
pl.rc('font', **font)

# plot the results in comparison to the initial conditions
pl.ion()
pl.clf()
pl.plot(x, phiOld,     'k', label='Initial conditions')
pl.plot(x, phiFTCS,     'r', label='FTCS')
pl.plot(x, phiBTCS,     'b', label='BTCS')
pl.legend(loc='best')
pl.xlabel('x')
pl.ylabel('$\phi$')
#pl.savefig('phi.pdf')

