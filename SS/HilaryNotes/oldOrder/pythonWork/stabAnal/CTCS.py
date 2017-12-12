from pylab import *

# plot the magnitude of the amplification factor for CTCS for k Dx = pi/2

c = linspace(-1.5,1.5,31)
A1 = -1j*c + sqrt(complex(1,0)-c**2)
A2 = -1j*c - sqrt(complex(1,0)-c**2)

mag2A1 = A1*conj(A1)
mag2A2 = A2*conj(A2)

ion()
clf()
font = {'size'   : 24}
rc('font', **font)
grid(True, which='both')
plot(c, mag2A1, 'b', label='positive root')
plot(c, mag2A2, 'r', label='negative root')
legend(loc='best')
xlabel('Courant number, $c$')
ylabel('$||A||^2$')

savefig('CTCSA.pdf')

