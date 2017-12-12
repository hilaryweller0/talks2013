# Initial conditions for linear advection
import pylab as pl

def topHat(x):
    "Function defining a top hat as a function of position, x"
    #chooses 1 where condition is true, else chooses zeros
    phi = pl.where((x<0.75) & (x>=0.25), 1., 0.)
    return phi

