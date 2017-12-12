# Outer code for setting up the linear advection problem and calling the
# function to perform the linear advection
import pylab as pl

# all the linear advection schemes, diagnostics and initial conditions
execfile("advectionSchemes.py")
execfile("initialConditions.py")
execfile("moreAdvectionSchemes.py")

# input variables
xmax = 1.0              # limits of the geometry
xmin = 0.0              # (must be real numbers, not integers)
nx = 100                 # number of intervals to divide the geometry
nt = 50                 # number of time steps
c = 0.2                 # Courant number for the advection
dx = (xmax - xmin)/nx   # spatial resolution
u = 1.0                 # wind speed
dt = c*dx/u             # time step

# spatial points for plotting and for defining initial conditions
x = pl.linspace(xmin, xmax, nx+1)

# initial conditions
phiOld = mixed(x)

# Exact solution is the same as the initial conditions but moved around
# the cyclic domain
phiExact = mixed((x - u*nt*dt)%(xmax - xmin))

# Call function for advecting the profile using FTBS and CTCS for nt time steps
phiFTBS = FTBS(phiOld.copy(), c, nt)
phiCTCS = CTCS(phiOld.copy(), c, nt)
#phiLinearSL = linearSL(phiOld.copy(), c, nt)
#phiQuick = quick(phiOld.copy(), c, nt)
#phiVanLeer = vanLeer(phiOld.copy(), c, nt)

# plot options
font = {'size'   : 14}
pl.rc('font', **font)

# plot the results versus the analytic solution
pl.ion()
pl.clf()
#pl.plot(x, phiOld,      'k--', label='Initial')
pl.plot(x, phiExact,    'k', label='Exact')
pl.plot(x, phiFTBS,     'r', label='FTBS')
pl.plot(x, phiCTCS,     'b', label='CTCS')
#pl.plot(x, phiLinearSL, 'g--', label='linear SL')
#pl.plot(x, phiQuick,    'grey', label='QUICK')
#pl.plot(x, phiVanLeer,  'yellow', label='van Leer')
pl.legend(loc='best')
pl.xlabel('x')
pl.ylabel('$\phi$')
#pl.savefig('phi.pdf')

