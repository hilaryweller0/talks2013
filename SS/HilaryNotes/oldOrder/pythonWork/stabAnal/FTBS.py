from pylab import *

# plot the magnitude of the amplification factor for FTBS for k Dx = pi

c = linspace(-0.5,1.5,21)
magA2 = 1 - 4*c*(1-c)


ion()
clf()
font = {'size'   : 24}
rc('font', **font)
grid(True, which='both')
plot(c, magA2, 'k')
xlabel('Courant number, $c$')
ylabel('$||A||^2$')

savefig('FTBSA.pdf')

