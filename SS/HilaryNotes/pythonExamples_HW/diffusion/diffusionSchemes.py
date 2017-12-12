import pylab as pl
import scipy as Sci
import scipy.linalg

def FTCS(phiOld, k, nt):
    "Diffusion of profile in phiOld using FTCS using non-dimensional"
    "diffusion coefficient, k"
    
    # new time-step array for phi
    phi = pl.zeros_like(phiOld)
    
    # FTCS
    for it in xrange(nt):
        for i in xrange(1,len(phi)-1):
            phi[i] = phiOld[i] \
                   + k*(phiOld[i+1] - 2*phiOld[i] + phiOld[i-1])
        
        # update arrays
        phiOld = phi.copy()

    return phi


def BTCS(phi, k, nt):
    "Diffusion of profile in phi using BTCS using non-dimensional"
    "diffusion coefficient, k"
    
    N = len(phi)
    
    # array representing BTCS
    M = pl.zeros([N,N])
    M[0,0] = 1.
    M[-1,-1] = 1.
    for i in xrange(1,N-1):
        M[i-1,i] = -k
        M[i,i] = 1+2*k
        M[i+1,i] = -k
        
    # BTCS
    for it in xrange(nt):
        phi = scipy.linalg.solve(M,phi)

    return phi


