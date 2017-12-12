import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import os

plt.ion()

x = np.arange(0,1,0.01);

f = lambda x: np.exp(x) - 2

plt.clf()
font = {'family' : 'times new roman' ,
        'style' : 'normal',
        'size'   : 24}
plt.rc('font', **font)
plt.plot(x, f(x), 'k', x, pl.zeros(pl.size(x)), 'k:')
plt.xlabel('x')
plt.ylabel('f')

plt.savefig('curve.pdf', format='pdf')
os.system('evince curve.pdf &')
os.system('pdfcrop curve.pdf tmp.pdf')
os.system('mv tmp.pdf curve.pdf')

