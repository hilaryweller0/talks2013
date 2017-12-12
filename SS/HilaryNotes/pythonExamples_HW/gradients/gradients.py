from numpy import *
from math import *

# estimate of ddx(sin x) at x=0 for various dx

f = lambda x:sin(x)
dfdx = lambda x:cos(x)

x0 = 0.
for dx in [0.4, 0.2, 0.1]:
    ddx = (f(x0+dx) - f(x0-dx))/(2*dx)
    print dx, ' & ', ddx, ' & ', ddx-dfdx(x0), '\\\\'


# make log paper

from pylab import *
import os
ion()

clf()
grid(True, which='both')
loglog([0.1,0.1], [0.1, 0.1])
axis([0.01,1,0.001,0.1])

font = {'family' : 'times new roman',
        'style' : 'normal',
        'size'   : 24}
rc('font', **font)
xlabel('$\Delta x$')
ylabel('|error|')

plt.savefig('logPaper.pdf', format='pdf')
os.system('pdfcrop logPaper.pdf tmp.pdf')
os.system('mv tmp.pdf logPaper.pdf')
os.system('evince logPaper.pdf &')

