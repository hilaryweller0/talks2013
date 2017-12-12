import pylab as pl
import time

def linearSL(phiOld, c, nt):
    "Semi-Lagrangian advection of profile in phiOld using"
    "linear interpolation"
    
    # add wrap-around point for cyclic boundaries
    phiOld = pl.append(phiOld, [phiOld[0]])
    
    # new time-step arrays for phi
    phi = pl.zeros_like(phiOld)
    
    # loop over the time steps
    for it in xrange(1,nt+1):
        # loop over the grid-points
        for j in xrange(1,len(phi)-1):
            # The index of the point to the left of the departure point
            k = int(j-c)
            # the location of the departure point within interval k->k+1
            beta = j-k-c
            
            # Linear interpolation onto the departure point
            phi[j] = (1-beta)*phiOld[k] + beta*phiOld[k+1]
        
        # cyclic BCs
        phi[0] = phi[-2]
        phi[-1] = phi[1]
        
        # update arrays
        phiOld = phi.copy()
        
    # return phi (without the cyclic wrap-around point)
    return phi[0:len(phi)-1]


def quick(phiOld, c, nt):
    "advection for nt time steps with a Courant number of c using QUICK"
    "(quadratic upwind)"
    
    # add two wrap-around points for cyclic boundaries
    phiOld = pl.append(phiOld, [phiOld[0:2]])
    
    # new time-step arrays for phi
    phi = phiOld.copy()
    
    # QUICK for all the time steps
    for it in xrange(nt):
    
        phiMid = (3*phi[2:] + 6*phi[1:-1] - phi[0:-2])/8.
        phi[2:-1] = phiOld[2:-1] - c*(phiMid[1:] - phiMid[:-1])
        
        # cyclic BCs
        phi[0] = phi[-3]
        phi[1] = phi[-2]
        phi[-1] = phi[2]
        
        # update arrays
        phiOld = phi.copy()
        
    # return phiNew (without the cyclic wrap-around points)
    return phi[0:len(phi)-2]


def vanLeer(phiOld, c, nt):
    "advection for nt time steps with a Courant number of c using centred"
    "and upwind combined with van-Leer limiter"
    
    # add two wrap-around points for cyclic boundaries
    phiOld = pl.append(phiOld, [phiOld[0:2]])
    
    # new time-step arrays for phi
    phi = phiOld.copy()
    
    # all the time steps
    for it in xrange(nt):

        #low and high order fluxes
        phiL = phi[1:-1]
        phiH = 0.5*(phi[2:] + phi[1:-1])
            
        denom = pl.where(\
            (abs(phi[2:] - phi[1:-1])<pl.finfo(pl.double).resolution),\
            pl.finfo(pl.double).resolution, phi[2:] - phi[1:-1])
    
        r = (phi[1:-1] - phi[0:-2])/denom
        limiter = (r + abs(r))/(1 + abs(r))
            
        # limited flux at the mid-points
        phiMid = limiter*phiH + (1-limiter)*phiL

        phi[2:-1] = phiOld[2:-1] - c*(phiMid[1:] - phiMid[:-1])
        
        # cyclic BCs
        phi[0] = phi[-3]
        phi[1] = phi[-2]
        phi[-1] = phi[2]
        
        # update arrays
        phiOld = phi.copy()
        
    # return phiNew (without the cyclic wrap-around points)
    return phi[0:len(phi)-2]

