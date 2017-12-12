from pylab import *
import os

f = lambda x:exp(-x)

x = arange(0,6.1,0.2)
y = f(x)

ion()
clf()
grid(True, which='both')
plot(x, y)
plot([x[0], x[-1]], zeros(2), 'k')
axis([x[0], x[-1],-2,4])

font = {'family' : 'times new roman',
        'style' : 'normal',
        'size'   : 24}
rc('font', **font)
xlabel('$t$')
ylabel('y')

plt.savefig('expDecay.pdf', format='pdf')
os.system('pdfcrop expDecay.pdf tmp.pdf')
os.system('mv tmp.pdf expDecay.pdf')
os.system('evince expDecay.pdf &')


dt=0.5
y0=1
t = arange(0, 6.1, dt)
yEF = zeros(len(t))
yEF[0] = y0
for n in range(1, len(t)):
    yEF[n] = yEF[n-1] - dt*yEF[n-1]


yEF

