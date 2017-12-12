from pylab import *

rgh = 1.0
c = 0.4
kdx = linspace(0,pi,100)
exact = kdx*rgh;
Agrid = 2*arcsin(0.5*c*sin(kdx))/c
Cgrid = 2*arcsin(c*sin(0.5*kdx))/c

clf()
ion()
plot(kdx/pi, exact, 'k', label='exact')
plot(kdx/pi, Agrid, 'r', label='A-grid')
legend(loc='best')

xlabel(r'$k\Delta x/\pi$')
ylabel(r'wave frequency, $\omega$')

savefig('A_dispersion.pdf')

plot(kdx/pi, Cgrid, 'b', label='C-grid')
legend(loc='best')
savefig('AC_dispersion.pdf')

