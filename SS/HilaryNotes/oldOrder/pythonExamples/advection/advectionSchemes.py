import pylab as pl
import time

def CTCS(phiOld, c, nt, epsilon=0., alpha=1.):
    "Linear advection of profile in phiOld using CTCS"
    "(FTCS for 1st time step)"
    "with RAW filter with coefficients epsilon and alpha"
    
    # add wrap-around point for cyclic boundaries
    phiOld = pl.append(phiOld, [phiOld[0]])
    
    # mid and new time-step arrays for phi
    phi = pl.zeros_like(phiOld)
    phiNew = pl.zeros_like(phiOld)
    
    # FTCS for first time step
    for i in xrange(1,len(phi)-1):
        phi[i] = phiOld[i] - 0.5*c*(phiOld[i+1] - phiOld[i-1])
    # cyclic BCs
    phi[0] = phi[-2]
    phi[-1] = phi[1]
    
    # CTCS for remaining time steps
    for it in xrange(2,nt+1):
        for i in xrange(1,len(phi)-1):
            phiNew[i] = phiOld[i] - c*(phi[i+1] - phi[i-1])
        
        # cyclic BCs
        phiNew[0] = phiNew[-2]
        phiNew[-1] = phiNew[1]
        
        # RAW filter
        d = epsilon*(phiNew - 2*phi + phiOld)
        phi += alpha*d
        phiNew += (alpha - 1.)*d
        
        # update arrays
        phiOld = phi.copy()
        phi = phiNew.copy()

    # return phiNew (without the cyclic wrap-around point)
    return phiNew[0:len(phi)-1]

def FTBS(phiOld, c, nt):
    "Linear advection of profile in phiOld using FTBS"
    
    # add wrap-around point for cyclic boundaries
    phiOld = pl.append(phiOld, [phiOld[0]])
    
    # new time-step array for phi
    phi = pl.zeros_like(phiOld)
    
    # FTBS
    for it in xrange(1,nt+1):
        for i in xrange(1,len(phi)):
            phi[i] = phiOld[i] - c*(phiOld[i] - phiOld[i-1])
        # cyclic BCs
        phi[0] = phi[-2]
        
        # update arrays
        phiOld = phi.copy()

    # return phi (without the cyclic wrap-around point)
    return phi[0:len(phi)-1]


